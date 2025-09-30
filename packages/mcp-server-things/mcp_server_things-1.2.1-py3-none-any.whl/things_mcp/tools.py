"""Simplified hybrid implementation: things.py for reads, AppleScript for writes."""

import asyncio
import logging
from typing import Any, Dict, List, Optional
from datetime import datetime

# Import things.py for direct database access
import things

from .services.applescript_manager import AppleScriptManager
from .pure_applescript_scheduler import PureAppleScriptScheduler
from .operation_queue import get_operation_queue, Priority
from .locale_aware_dates import locale_handler
from .services.validation_service import ValidationService
from .services.tag_service import TagValidationService
from .move_operations import MoveOperationsTools
from .config import ThingsMCPConfig
from .response_optimizer import ResponseOptimizer, FieldOptimizationPolicy

logger = logging.getLogger(__name__)


class ThingsTools:
    """
    Main Things 3 tools implementation with hybrid approach:
    - Read operations via things.py (fast direct database access)
    - Write operations via AppleScript (full control and reliability)
    - Tag validation and policy enforcement
    """
    
    def __init__(self, applescript_manager: AppleScriptManager, config: Optional[ThingsMCPConfig] = None):
        """Initialize with AppleScript manager and optional configuration.
        
        Args:
            applescript_manager: AppleScript manager instance for write operations
            config: Optional configuration for tag validation and policies
        """
        self.applescript = applescript_manager
        self.config = config
        self.reliable_scheduler = PureAppleScriptScheduler(applescript_manager)
        
        # Initialize validation service and advanced move operations for writes
        self.validation_service = ValidationService(applescript_manager)
        self.move_operations = MoveOperationsTools(applescript_manager, self.validation_service)
        
        # Initialize response optimizer
        self.response_optimizer = ResponseOptimizer(FieldOptimizationPolicy.STANDARD)
        
        # Initialize tag validation service if config is provided
        self.tag_validation_service = None
        if config:
            self.tag_validation_service = TagValidationService(applescript_manager, config)
            logger.info("Things tools initialized with tag validation service")
        else:
            logger.info("Things tools initialized without tag validation (backward compatibility mode)")

        logger.info("Things tools initialized - reads via things.py, writes via AppleScript")
    
    # ========== READ OPERATIONS (things.py) ==========
    
    async def get_todos(self, project_uuid: Optional[str] = None, include_items: Optional[bool] = None) -> List[Dict]:
        """Get todos directly from database via things.py."""
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self._get_todos_sync, project_uuid, include_items)
    
    def _get_todos_sync(self, project_uuid: Optional[str] = None, include_items: Optional[bool] = None) -> List[Dict]:
        """Synchronous implementation of get_todos using things.py."""
        try:
            if project_uuid:
                # Get todos for a specific project
                todos_data = things.todos(project=project_uuid)
            else:
                # Get all todos
                todos_data = things.todos()
            
            # Convert to list if it's a generator/iterator
            if hasattr(todos_data, '__iter__') and not isinstance(todos_data, (list, dict)):
                todos_data = list(todos_data)
            
            # Handle case where things.py returns a single dict instead of list
            if isinstance(todos_data, dict):
                todos_data = [todos_data]
            
            return [self._convert_todo(todo) for todo in todos_data]
        except Exception as e:
            logger.error(f"Error getting todos via things.py: {e}")
            return []
    
    async def get_projects(self, include_items: bool = False) -> List[Dict]:
        """Get all projects directly from database."""
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self._get_projects_sync, include_items)
    
    def _get_projects_sync(self, include_items: bool = False) -> List[Dict]:
        """Synchronous implementation using things.py."""
        try:
            projects_data = things.projects()
            
            # Convert to list if needed
            if hasattr(projects_data, '__iter__') and not isinstance(projects_data, (list, dict)):
                projects_data = list(projects_data)
            
            if isinstance(projects_data, dict):
                projects_data = [projects_data]
            
            result = []
            for project in projects_data:
                project_dict = self._convert_project(project)
                
                # Add items if requested
                if include_items:
                    project_items = things.todos(project=project.get('uuid', ''))
                    if hasattr(project_items, '__iter__') and not isinstance(project_items, (list, dict)):
                        project_items = list(project_items)
                    if isinstance(project_items, dict):
                        project_items = [project_items]
                    
                    project_dict['items'] = [self._convert_todo(item) for item in project_items]
                else:
                    # Just count items
                    project_items = things.todos(project=project.get('uuid', ''))
                    if hasattr(project_items, '__iter__') and not isinstance(project_items, (list, dict)):
                        project_items = list(project_items)
                    if isinstance(project_items, dict):
                        project_items = [project_items]
                    project_dict['item_count'] = len(project_items)
                
                result.append(project_dict)
            
            return result
        except Exception as e:
            logger.error(f"Error getting projects via things.py: {e}")
            return []
    
    async def get_areas(self, include_items: bool = False) -> List[Dict]:
        """Get all areas directly from database."""
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self._get_areas_sync, include_items)
    
    def _get_areas_sync(self, include_items: bool = False) -> List[Dict]:
        """Synchronous implementation using things.py."""
        try:
            areas_data = things.areas()
            
            # Convert to list if needed
            if hasattr(areas_data, '__iter__') and not isinstance(areas_data, (list, dict)):
                areas_data = list(areas_data)
            
            if isinstance(areas_data, dict):
                areas_data = [areas_data]
            
            result = []
            for area in areas_data:
                area_dict = self._convert_area(area)
                
                # Add items if requested
                if include_items:
                    # Get projects in this area
                    area_projects = things.projects(area=area.get('uuid', ''))
                    if hasattr(area_projects, '__iter__') and not isinstance(area_projects, (list, dict)):
                        area_projects = list(area_projects)
                    if isinstance(area_projects, dict):
                        area_projects = [area_projects]
                    
                    # Get todos in this area
                    area_todos = things.todos(area=area.get('uuid', ''))
                    if hasattr(area_todos, '__iter__') and not isinstance(area_todos, (list, dict)):
                        area_todos = list(area_todos)
                    if isinstance(area_todos, dict):
                        area_todos = [area_todos]
                    
                    area_dict['projects'] = [self._convert_project(proj) for proj in area_projects]
                    area_dict['todos'] = [self._convert_todo(todo) for todo in area_todos]
                else:
                    # Just count items
                    area_projects = things.projects(area=area.get('uuid', ''))
                    if hasattr(area_projects, '__iter__') and not isinstance(area_projects, (list, dict)):
                        area_projects = list(area_projects)
                    if isinstance(area_projects, dict):
                        area_projects = [area_projects]
                    
                    area_todos = things.todos(area=area.get('uuid', ''))
                    if hasattr(area_todos, '__iter__') and not isinstance(area_todos, (list, dict)):
                        area_todos = list(area_todos)
                    if isinstance(area_todos, dict):
                        area_todos = [area_todos]
                    
                    area_dict['project_count'] = len(area_projects)
                    area_dict['todo_count'] = len(area_todos)
                
                result.append(area_dict)
            
            return result
        except Exception as e:
            logger.error(f"Error getting areas via things.py: {e}")
            return []
    
    async def get_tags(self, include_items: bool = False) -> List[Dict]:
        """Get all tags with counts or items - super fast with things.py."""
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self._get_tags_sync, include_items)
    
    def _get_tags_sync(self, include_items: bool) -> List[Dict]:
        """Synchronous implementation - this should be very fast."""
        try:
            tags_data = things.tags()
            
            # Convert to list if needed
            if hasattr(tags_data, '__iter__') and not isinstance(tags_data, (list, dict)):
                tags_data = list(tags_data)
            
            if isinstance(tags_data, dict):
                tags_data = [tags_data]
            
            result = []
            for tag in tags_data:
                # Start with basic tag structure
                tag_dict = {
                    'name': tag.get('title', '')
                }
                
                # Only add id if it's different from name
                tag_id = tag.get('uuid', '')
                if tag_id and tag_id != tag_dict['name']:
                    tag_dict['id'] = tag_id
                
                if include_items:
                    # Get actual items for this tag
                    tagged_todos = things.todos(tag=tag.get('title', ''))
                    if hasattr(tagged_todos, '__iter__') and not isinstance(tagged_todos, (list, dict)):
                        tagged_todos = list(tagged_todos)
                    if isinstance(tagged_todos, dict):
                        tagged_todos = [tagged_todos]
                    
                    tag_dict['items'] = [self._convert_todo(todo) for todo in tagged_todos]
                else:
                    # Just count - this should be instant with SQL
                    tagged_todos = things.todos(tag=tag.get('title', ''))
                    if hasattr(tagged_todos, '__iter__') and not isinstance(tagged_todos, (list, dict)):
                        tagged_todos = list(tagged_todos)
                    if isinstance(tagged_todos, dict):
                        tagged_todos = [tagged_todos]
                    
                    # Only add count if greater than 0
                    count = len(tagged_todos)
                    if count > 0:
                        tag_dict['item_count'] = count
                
                result.append(tag_dict)
            
            return result
        except Exception as e:
            logger.error(f"Error getting tags via things.py: {e}")
            return []
    
    async def search_todos(self, query: str, limit: Optional[int] = None) -> List[Dict]:
        """Search todos directly in database with optional limit."""
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self._search_sync, query, limit)
    
    def _search_sync(self, query: str, limit: Optional[int] = None) -> List[Dict]:
        """Synchronous search implementation with limit support."""
        try:
            # Use things.py search functionality if available
            if hasattr(things, 'search'):
                results = things.search(query)
            else:
                # Fallback: get all todos and filter manually
                all_todos = things.todos()
                if hasattr(all_todos, '__iter__') and not isinstance(all_todos, (list, dict)):
                    all_todos = list(all_todos)
                if isinstance(all_todos, dict):
                    all_todos = [all_todos]
                
                query_lower = query.lower()
                results = []
                for todo in all_todos:
                    title = todo.get('title', '').lower()
                    notes = todo.get('notes', '').lower()
                    if query_lower in title or query_lower in notes:
                        results.append(todo)
                        # Apply limit during search for efficiency
                        if limit and len(results) >= limit:
                            break
            
            # Convert to list if needed
            if hasattr(results, '__iter__') and not isinstance(results, (list, dict)):
                results = list(results)
            if isinstance(results, dict):
                results = [results]
            
            # Apply limit if not already applied during search
            if limit and len(results) > limit:
                results = results[:limit]
            
            return [self._convert_todo(todo) for todo in results]
        except Exception as e:
            logger.error(f"Error searching todos via things.py: {e}")
            return []
    
    async def get_inbox(self) -> List[Dict]:
        """Get inbox items directly from database."""
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self._get_inbox_sync)
    
    def _get_inbox_sync(self) -> List[Dict]:
        """Synchronous implementation with error handling."""
        try:
            # Get all todos and filter for inbox manually to avoid potential sorting issues
            all_todos = things.todos()
            
            if hasattr(all_todos, '__iter__') and not isinstance(all_todos, (list, dict)):
                all_todos = list(all_todos)
            if isinstance(all_todos, dict):
                all_todos = [all_todos]
            
            # Filter for inbox items (start='Inbox' or no start/area/project)
            inbox_todos = []
            for todo in all_todos:
                start = todo.get('start', '')
                area = todo.get('area', '')
                project = todo.get('project', '')
                
                if (start == 'Inbox' or 
                    (not start and not area and not project)):
                    inbox_todos.append(todo)
            
            return [self._convert_todo(todo) for todo in inbox_todos]
        except Exception as e:
            logger.error(f"Error getting inbox via things.py: {e}")
            return []
    
    async def get_today(self) -> List[Dict]:
        """Get today items directly from database."""
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self._get_today_sync)
    
    def _get_today_sync(self) -> List[Dict]:
        """Synchronous implementation with error handling for None values in sorting."""
        try:
            # Get all todos and filter for today manually to avoid sorting issues
            all_todos = things.todos()
            
            if hasattr(all_todos, '__iter__') and not isinstance(all_todos, (list, dict)):
                all_todos = list(all_todos)
            if isinstance(all_todos, dict):
                all_todos = [all_todos]
            
            # Filter for today items (start='Today' or activation_date=today)
            from datetime import date
            today_str = date.today().strftime('%Y-%m-%d')
            
            today_todos = []
            for todo in all_todos:
                # Check if this is a today item
                start = todo.get('start', '')
                start_date = todo.get('start_date', '')
                
                if (start == 'Today' or 
                    start_date == today_str or
                    (start_date and start_date <= today_str and start != 'Someday')):
                    today_todos.append(todo)
            
            # Sort manually with None-safe comparison
            def safe_sort_key(todo):
                today_index = todo.get('today_index', 0) or 0
                start_date = todo.get('start_date', '') or ''
                return (today_index, start_date)
            
            today_todos.sort(key=safe_sort_key)
            
            return [self._convert_todo(todo) for todo in today_todos]
        except Exception as e:
            logger.error(f"Error getting today via things.py: {e}")
            return []
    
    async def get_upcoming(self) -> List[Dict]:
        """Get upcoming items directly from database."""
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self._get_upcoming_sync)
    
    def _get_upcoming_sync(self) -> List[Dict]:
        """Synchronous implementation."""
        try:
            upcoming_data = things.upcoming()
            
            if hasattr(upcoming_data, '__iter__') and not isinstance(upcoming_data, (list, dict)):
                upcoming_data = list(upcoming_data)
            if isinstance(upcoming_data, dict):
                upcoming_data = [upcoming_data]
            
            return [self._convert_todo(todo) for todo in upcoming_data]
        except Exception as e:
            logger.error(f"Error getting upcoming via things.py: {e}")
            return []
    
    async def get_anytime(self) -> List[Dict]:
        """Get anytime items directly from database."""
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self._get_anytime_sync)
    
    def _get_anytime_sync(self) -> List[Dict]:
        """Synchronous implementation with error handling."""
        try:
            # Get all todos and filter for anytime manually to avoid sorting issues
            all_todos = things.todos()
            
            if hasattr(all_todos, '__iter__') and not isinstance(all_todos, (list, dict)):
                all_todos = list(all_todos)
            if isinstance(all_todos, dict):
                all_todos = [all_todos]
            
            # Filter for anytime items
            anytime_todos = []
            for todo in all_todos:
                start = todo.get('start', '')
                if start == 'Anytime':
                    anytime_todos.append(todo)
            
            return [self._convert_todo(todo) for todo in anytime_todos]
        except Exception as e:
            logger.error(f"Error getting anytime via things.py: {e}")
            return []
    
    async def get_someday(self) -> List[Dict]:
        """Get someday items directly from database."""
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self._get_someday_sync)
    
    def _get_someday_sync(self) -> List[Dict]:
        """Synchronous implementation with error handling."""
        try:
            # Get all todos and filter for someday manually to avoid sorting issues
            all_todos = things.todos()
            
            if hasattr(all_todos, '__iter__') and not isinstance(all_todos, (list, dict)):
                all_todos = list(all_todos)
            if isinstance(all_todos, dict):
                all_todos = [all_todos]
            
            # Filter for someday items
            someday_todos = []
            for todo in all_todos:
                start = todo.get('start', '')
                if start == 'Someday':
                    someday_todos.append(todo)
            
            return [self._convert_todo(todo) for todo in someday_todos]
        except Exception as e:
            logger.error(f"Error getting someday via things.py: {e}")
            return []
    
    async def get_logbook(self, limit: int = 50, period: str = "7d") -> List[Dict]:
        """Get completed items directly from database."""
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self._get_logbook_sync, limit, period)
    
    def _get_logbook_sync(self, limit: int = 50, period: str = "7d") -> List[Dict]:
        """Synchronous implementation."""
        try:
            logbook_data = things.logbook()
            
            if hasattr(logbook_data, '__iter__') and not isinstance(logbook_data, (list, dict)):
                logbook_data = list(logbook_data)
            if isinstance(logbook_data, dict):
                logbook_data = [logbook_data]
            
            # Apply limit
            if limit and len(logbook_data) > limit:
                logbook_data = logbook_data[:limit]
            
            # TODO: Apply period filter based on completion date if available in the data
            
            return [self._convert_todo(todo) for todo in logbook_data]
        except Exception as e:
            logger.error(f"Error getting logbook via things.py: {e}")
            return []
    
    async def get_trash(self) -> List[Dict]:
        """Get trashed items directly from database."""
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self._get_trash_sync)
    
    def _get_trash_sync(self) -> List[Dict]:
        """Synchronous implementation."""
        try:
            trash_data = things.trash()
            
            if hasattr(trash_data, '__iter__') and not isinstance(trash_data, (list, dict)):
                trash_data = list(trash_data)
            if isinstance(trash_data, dict):
                trash_data = [trash_data]
            
            return [self._convert_todo(todo) for todo in trash_data]
        except Exception as e:
            logger.error(f"Error getting trash via things.py: {e}")
            return []
    
    async def get_tagged_items(self, tag: str) -> List[Dict]:
        """Get items with a specific tag directly from database."""
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self._get_tagged_items_sync, tag)
    
    def _get_tagged_items_sync(self, tag: str) -> List[Dict]:
        """Synchronous implementation."""
        try:
            tagged_data = things.todos(tag=tag)
            
            if hasattr(tagged_data, '__iter__') and not isinstance(tagged_data, (list, dict)):
                tagged_data = list(tagged_data)
            if isinstance(tagged_data, dict):
                tagged_data = [tagged_data]
            
            return [self._convert_todo(todo) for todo in tagged_data]
        except Exception as e:
            logger.error(f"Error getting tagged items via things.py: {e}")
            return []
    
    async def get_todo_by_id(self, todo_id: str) -> Dict[str, Any]:
        """Get a specific todo by ID directly from database."""
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self._get_todo_by_id_sync, todo_id)
    
    def _get_todo_by_id_sync(self, todo_id: str) -> Dict[str, Any]:
        """Synchronous implementation."""
        try:
            # Get all todos and find the one with matching ID
            # things.py might not have a direct get-by-id method
            all_todos = things.todos()
            
            if hasattr(all_todos, '__iter__') and not isinstance(all_todos, (list, dict)):
                all_todos = list(all_todos)
            if isinstance(all_todos, dict):
                all_todos = [all_todos]
            
            for todo in all_todos:
                if todo.get('uuid') == todo_id:
                    return self._convert_todo(todo)
            
            # If not found, return error
            return {
                "success": False,
                "error": "TODO_NOT_FOUND",
                "message": f"Todo with ID '{todo_id}' not found"
            }
        except Exception as e:
            logger.error(f"Error getting todo by ID via things.py: {e}")
            return {
                "success": False,
                "error": "DATABASE_ERROR",
                "message": str(e)
            }
    
    # ========== WRITE OPERATIONS (AppleScript) ==========
    # Keep all the existing write operations from the original tools.py
    
    def _escape_applescript_string(self, text: str) -> str:
        """Escape a string for safe use in AppleScript."""
        if not text:
            return '""'
        
        # Escape backslashes first, then quotes
        escaped = text.replace('\\', '\\\\').replace('"', '\\"')
        return f'"{escaped}"'
    
    def _convert_iso_to_applescript_date(self, iso_date: str) -> str:
        """Convert ISO date (YYYY-MM-DD) to AppleScript property-based date construction."""
        try:
            # Use the locale-aware date handler
            return locale_handler.convert_iso_to_applescript(iso_date)
        except Exception as e:
            logger.error(f"Error converting ISO date '{iso_date}': {e}")
            # Fallback to original approach if needed
            try:
                parsed = datetime.strptime(iso_date, '%Y-%m-%d').date()
                return parsed.strftime('%d/%m/%Y')  # DD/MM/YYYY for European locale
            except ValueError:
                return iso_date
    
    async def _validate_tags_with_policy(self, tags: List[str]) -> Dict[str, List[str]]:
        """Validate tags using policy-aware service if available."""
        if self.tag_validation_service:
            # Use the correct method name
            result = await self.tag_validation_service.validate_and_filter_tags(tags)
            # Convert TagValidationResult to dict format expected by callers
            return {
                'created': result.created_tags,
                'existing': result.valid_tags,
                'filtered': result.filtered_tags,
                'warnings': result.warnings
            }
        else:
            # Fallback to simple validation - assume all tags are valid
            return {
                'created': [],
                'existing': tags,
                'filtered': [],
                'warnings': []
            }
    
    async def add_todo(self, title: str, **kwargs) -> Dict[str, Any]:
        """Add a new todo using AppleScript (write operation)."""
        try:
            # Handle tag validation BEFORE creating the todo
            tags = kwargs.get('tags', [])
            tag_validation = None
            if tags and self.tag_validation_service:
                tag_validation = await self._validate_tags_with_policy(tags)

                # Check if there are any errors that should block creation
                if tag_validation.get('errors'):
                    return {
                        "success": False,
                        "error": "; ".join(tag_validation['errors']),
                        "message": "Tag validation failed",
                        "tag_info": tag_validation
                    }

                # Update kwargs with only the valid tags (removes filtered tags)
                valid_tags = tag_validation.get('existing', []) + tag_validation.get('created', [])
                if valid_tags != tags:
                    kwargs = dict(kwargs)  # Make a copy
                    kwargs['tags'] = valid_tags

            # Use the reliable scheduler for adding todos
            result = await self.reliable_scheduler.add_todo(title=title, **kwargs)

            # Add tag validation info to result if available
            if tag_validation:
                result['tag_info'] = tag_validation

            return result
        except Exception as e:
            logger.error(f"Error adding todo: {e}")
            return {
                "success": False,
                "error": str(e),
                "message": "Failed to add todo"
            }
    
    async def update_todo(self, todo_id: str, **kwargs) -> Dict[str, Any]:
        """Update a todo using AppleScript (write operation)."""
        try:
            # Handle tag validation BEFORE updating the todo
            tags = kwargs.get('tags', [])
            tag_validation = None
            if tags and self.tag_validation_service:
                tag_validation = await self._validate_tags_with_policy(tags)

                # Check if there are any errors that should block update
                if tag_validation.get('errors'):
                    return {
                        "success": False,
                        "error": "; ".join(tag_validation['errors']),
                        "message": "Tag validation failed",
                        "tag_info": tag_validation
                    }

                # Update kwargs with only the valid tags (removes filtered tags)
                valid_tags = tag_validation.get('existing', []) + tag_validation.get('created', [])
                if valid_tags != tags:
                    kwargs = dict(kwargs)  # Make a copy
                    kwargs['tags'] = valid_tags

            # Use the reliable scheduler for updating todos
            result = await self.reliable_scheduler.update_todo(todo_id=todo_id, **kwargs)

            # Add tag validation info to result if available
            if tag_validation:
                result['tag_info'] = tag_validation

            return result
        except Exception as e:
            logger.error(f"Error updating todo: {e}")
            return {
                "success": False,
                "error": str(e),
                "message": "Failed to update todo"
            }
    
    async def delete_todo(self, todo_id: str) -> Dict[str, Any]:
        """Delete a todo using AppleScript (write operation)."""
        try:
            script = f'''
            tell application "Things3"
                set targetTodo to to do id "{todo_id}"
                delete targetTodo
                return "deleted"
            end tell
            '''
            result = await self.applescript.execute_applescript(script)
            return {
                "success": result.get('success', False),
                "message": "Todo deleted successfully" if result.get('success') else result.get('error', 'Failed to delete todo')
            }
        except Exception as e:
            logger.error(f"Error deleting todo: {e}")
            return {
                "success": False,
                "error": str(e),
                "message": "Failed to delete todo"
            }
    
    async def add_project(self, title: str, **kwargs) -> Dict[str, Any]:
        """Add a new project using AppleScript (write operation)."""
        try:
            # Use the reliable scheduler for adding projects
            result = await self.reliable_scheduler.add_project(title=title, **kwargs)
            
            # Handle tag validation if needed
            tags = kwargs.get('tags', [])
            if tags and self.tag_validation_service:
                tag_validation = await self._validate_tags_with_policy(tags)
                result['tag_info'] = tag_validation
            
            return result
        except Exception as e:
            logger.error(f"Error adding project: {e}")
            return {
                "success": False,
                "error": str(e),
                "message": "Failed to add project"
            }
    
    async def update_project(self, project_id: str, **kwargs) -> Dict[str, Any]:
        """Update a project using AppleScript (write operation)."""
        try:
            # Use the reliable scheduler for updating projects
            result = await self.reliable_scheduler.update_project(project_id=project_id, **kwargs)
            
            # Handle tag validation if needed
            tags = kwargs.get('tags', [])
            if tags and self.tag_validation_service:
                tag_validation = await self._validate_tags_with_policy(tags)
                result['tag_info'] = tag_validation
            
            return result
        except Exception as e:
            logger.error(f"Error updating project: {e}")
            return {
                "success": False,
                "error": str(e),
                "message": "Failed to update project"
            }
    
    async def move_record(self, todo_id: str, destination_list: str) -> Dict[str, Any]:
        """Move a todo using AppleScript (write operation)."""
        try:
            return await self.move_operations.move_record(todo_id, destination_list)
        except Exception as e:
            logger.error(f"Error moving record: {e}")
            return {
                "success": False,
                "error": str(e),
                "message": "Failed to move record"
            }
    
    async def add_tags(self, todo_id: str, tags: List[str]) -> Dict[str, Any]:
        """Add tags to a todo using AppleScript (write operation)."""
        try:
            # Validate tags first
            tag_validation = await self._validate_tags_with_policy(tags)
            
            # Use only valid tags
            valid_tags = tag_validation['existing'] + tag_validation['created']
            
            if not valid_tags:
                return {
                    "success": False,
                    "error": "NO_VALID_TAGS",
                    "message": "No valid tags to add",
                    "tag_info": tag_validation
                }
            
            # Build AppleScript to add tags
            script = f'''
            tell application "Things3"
                set targetTodo to to do id "{todo_id}"
            '''
            
            for tag in valid_tags:
                escaped_tag = self._escape_applescript_string(tag).strip('"')
                script += f'\n    set tag names of targetTodo to (tag names of targetTodo) & {{"{escaped_tag}"}}'
            
            script += '''
                return "tags_added"
            end tell
            '''
            
            result = await self.applescript.execute_applescript(script)
            return {
                "success": result.get('success', False),
                "message": f"Added {len(valid_tags)} tags successfully" if result.get('success') else result.get('error', 'Failed to add tags'),
                "tag_info": tag_validation
            }
        except Exception as e:
            logger.error(f"Error adding tags: {e}")
            return {
                "success": False,
                "error": str(e),
                "message": "Failed to add tags"
            }
    
    async def remove_tags(self, todo_id: str, tags: List[str]) -> Dict[str, Any]:
        """Remove tags from a todo using AppleScript (write operation)."""
        try:
            # Build AppleScript to remove tags
            script = f'''
            tell application "Things3"
                set targetTodo to to do id "{todo_id}"
                set currentTags to tag names of targetTodo
            '''

            for tag in tags:
                escaped_tag = self._escape_applescript_string(tag).strip('"')
                script += f'''
                set newTags to {{}}
                repeat with tagName in currentTags
                    if tagName is not equal to "{escaped_tag}" then
                        set newTags to newTags & tagName
                    end if
                end repeat
                set tag names of targetTodo to newTags
                set currentTags to newTags
                '''

            script += '''
                return "tags_removed"
            end tell
            '''

            result = await self.applescript.execute_applescript(script)
            return {
                "success": result.get('success', False),
                "message": f"Removed {len(tags)} tags successfully" if result.get('success') else result.get('error', 'Failed to remove tags')
            }
        except Exception as e:
            logger.error(f"Error removing tags: {e}")
            return {
                "success": False,
                "error": str(e),
                "message": "Failed to remove tags"
            }

    async def bulk_update_todos(self, todo_ids: List[str], **kwargs) -> Dict[str, Any]:
        """
        Update multiple todos with the same changes in a single operation.

        Args:
            todo_ids: List of todo IDs to update
            **kwargs: Update parameters (same as update_todo: completed, canceled, title, notes, when, deadline, tags)

        Returns:
            Dict with success status, count of updated items, and any errors
        """
        try:
            if not todo_ids:
                return {
                    "success": False,
                    "error": "No todo IDs provided",
                    "updated_count": 0
                }

            # Handle tag validation once for all todos if tags are being updated
            tags = kwargs.get('tags', [])
            tag_validation = None
            if tags and self.tag_validation_service:
                tag_validation = await self._validate_tags_with_policy(tags)

                # Check if there are any errors that should block update
                if tag_validation.get('errors'):
                    return {
                        "success": False,
                        "error": "; ".join(tag_validation['errors']),
                        "message": "Tag validation failed",
                        "tag_info": tag_validation,
                        "updated_count": 0
                    }

                # Update kwargs with only the valid tags
                valid_tags = tag_validation.get('existing', []) + tag_validation.get('created', [])
                if valid_tags != tags:
                    kwargs = dict(kwargs)
                    kwargs['tags'] = valid_tags

            # Build a single AppleScript to update all todos
            script = 'tell application "Things3"\n'
            script += '    set successCount to 0\n'
            script += '    set errorMessages to {}\n'

            for todo_id in todo_ids:
                script += f'    try\n'
                script += f'        set targetTodo to to do id "{todo_id}"\n'

                # Add update operations based on kwargs
                if 'completed' in kwargs:
                    completed_val = str(kwargs['completed']).lower()
                    script += f'        set status of targetTodo to {"completed" if completed_val == "true" else "open"}\n'

                if 'canceled' in kwargs:
                    canceled_val = str(kwargs['canceled']).lower()
                    script += f'        set status of targetTodo to {"canceled" if canceled_val == "true" else "open"}\n'

                if 'title' in kwargs:
                    escaped_title = self._escape_applescript_string(kwargs['title']).strip('"')
                    script += f'        set name of targetTodo to "{escaped_title}"\n'

                if 'notes' in kwargs:
                    escaped_notes = self._escape_applescript_string(kwargs['notes']).strip('"')
                    script += f'        set notes of targetTodo to "{escaped_notes}"\n'

                if 'when' in kwargs:
                    when_value = kwargs['when']
                    if when_value:
                        as_date = self._convert_iso_to_applescript_date(when_value)
                        script += f'        set activation date of targetTodo to date "{as_date}"\n'

                if 'deadline' in kwargs:
                    deadline = kwargs['deadline']
                    if deadline:
                        as_date = self._convert_iso_to_applescript_date(deadline)
                        script += f'        set due date of targetTodo to date "{as_date}"\n'

                if 'tags' in kwargs and kwargs['tags']:
                    escaped_tags = [self._escape_applescript_string(t).strip('"') for t in kwargs['tags']]
                    tags_list = ', '.join([f'"{tag}"' for tag in escaped_tags])
                    script += f'        set tag names of targetTodo to {{{tags_list}}}\n'

                script += '        set successCount to successCount + 1\n'
                script += '    on error errMsg\n'
                script += f'        set end of errorMessages to "ID {todo_id}: " & errMsg\n'
                script += '    end try\n'

            script += '    return {successCount:successCount, errors:errorMessages}\n'
            script += 'end tell'

            result = await self.applescript.execute_applescript(script)

            if result.get('success'):
                # Parse the AppleScript result
                # AppleScript returns: {successCount:X, errors:[...]}
                output = result.get('output', '')

                # Try to parse the success count from the output
                success_count = len(todo_ids)  # Default to all if we can't parse
                error_messages = []

                # Simple parsing: look for successCount in the output
                if 'successCount' in output:
                    try:
                        # Extract number after successCount:
                        import re
                        match = re.search(r'successCount[:\s]+(\d+)', output)
                        if match:
                            success_count = int(match.group(1))
                    except Exception as e:
                        logger.warning(f"Could not parse success count from: {output}, error: {e}")

                # Check if there were any errors
                if 'errors' in output and success_count < len(todo_ids):
                    error_messages.append(f"{len(todo_ids) - success_count} todos failed to update")

                return {
                    "success": success_count > 0,
                    "message": f"Bulk update completed: {success_count}/{len(todo_ids)} todos updated" +
                              (f" ({', '.join(error_messages)})" if error_messages else ""),
                    "updated_count": success_count,
                    "failed_count": len(todo_ids) - success_count,
                    "total_requested": len(todo_ids),
                    "tag_info": tag_validation if tag_validation else None
                }
            else:
                return {
                    "success": False,
                    "error": result.get('error', 'Unknown error'),
                    "updated_count": 0,
                    "failed_count": len(todo_ids),
                    "total_requested": len(todo_ids)
                }

        except Exception as e:
            logger.error(f"Error in bulk update: {e}")
            return {
                "success": False,
                "error": str(e),
                "message": "Failed to perform bulk update",
                "updated_count": 0
            }
    
    # Additional write operations that might be needed - delegate to existing methods
    async def get_due_in_days(self, days: int) -> List[Dict[str, Any]]:
        """Get todos due within specified days - use AppleScript for now."""
        try:
            return await self.reliable_scheduler.get_todos_due_in_days(days)
        except Exception as e:
            logger.error(f"Error getting todos due in {days} days: {e}")
            return []
    
    async def get_todos_due_in_days(self, days: int) -> List[Dict[str, Any]]:
        """Get todos due within specified days - use AppleScript for now."""
        try:
            return await self.reliable_scheduler.get_todos_due_in_days(days)
        except Exception as e:
            logger.error(f"Error getting todos due in {days} days: {e}")
            return []
    
    async def get_activating_in_days(self, days: int) -> List[Dict[str, Any]]:
        """Get todos activating within specified days - use AppleScript for now."""
        try:
            return await self.reliable_scheduler.get_todos_activating_in_days(days)
        except Exception as e:
            logger.error(f"Error getting todos activating in {days} days: {e}")
            return []
    
    async def get_todos_activating_in_days(self, days: int) -> List[Dict[str, Any]]:
        """Get todos activating within specified days - use AppleScript for now."""
        try:
            return await self.reliable_scheduler.get_todos_activating_in_days(days)
        except Exception as e:
            logger.error(f"Error getting todos activating in {days} days: {e}")
            return []
    
    async def get_upcoming_in_days(self, days: int) -> List[Dict[str, Any]]:
        """Get todos upcoming within specified days using things.py."""
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self._get_upcoming_in_days_sync, days)
    
    def _get_upcoming_in_days_sync(self, days: int) -> List[Dict[str, Any]]:
        """Synchronous implementation using things.py to find todos due/activating within days."""
        try:
            from datetime import datetime, date, timedelta
            
            today = date.today()
            target_date = today + timedelta(days=days)
            
            logger.info(f"Searching for todos between {today} and {target_date}")
            
            # Get all open todos
            all_todos = things.todos()
            
            # Convert to list if needed
            if hasattr(all_todos, '__iter__') and not isinstance(all_todos, (list, dict)):
                all_todos = list(all_todos)
            if isinstance(all_todos, dict):
                all_todos = [all_todos]
            
            upcoming_todos = []
            seen_ids = set()  # Track unique todos
            
            for todo in all_todos:
                # Skip if already processed (avoid duplicates)
                todo_id = todo.get('uuid', '')
                if todo_id in seen_ids:
                    continue
                
                # Check if todo is open (things.py uses 'incomplete' instead of 'open')
                status = todo.get('status', '')
                if status not in ('open', 'incomplete', ''):
                    continue
                
                # Check deadline
                deadline = todo.get('deadline')
                if deadline:
                    try:
                        # Parse deadline date
                        if isinstance(deadline, str):
                            deadline_date = datetime.strptime(deadline[:10], '%Y-%m-%d').date()
                        else:
                            deadline_date = deadline
                        
                        # Check if within range
                        if today <= deadline_date <= target_date:
                            upcoming_todos.append(todo)
                            seen_ids.add(todo_id)
                            continue
                    except (ValueError, TypeError) as e:
                        logger.debug(f"Could not parse deadline {deadline}: {e}")
                
                # Check activation date (start date)
                start_date = todo.get('start_date')
                if start_date:
                    try:
                        # Parse start date
                        if isinstance(start_date, str):
                            start_date_obj = datetime.strptime(start_date[:10], '%Y-%m-%d').date()
                        else:
                            start_date_obj = start_date
                        
                        # Check if within range
                        if today <= start_date_obj <= target_date:
                            upcoming_todos.append(todo)
                            seen_ids.add(todo_id)
                    except (ValueError, TypeError) as e:
                        logger.debug(f"Could not parse start_date {start_date}: {e}")
            
            logger.info(f"Found {len(upcoming_todos)} todos due/activating in next {days} days")
            
            # Convert to our format
            return [self._convert_todo(todo) for todo in upcoming_todos]
            
        except Exception as e:
            logger.error(f"Error getting upcoming todos in {days} days: {e}", exc_info=True)
            return []
    
    async def get_todos_upcoming_in_days(self, days: int) -> List[Dict[str, Any]]:
        """Alias for get_upcoming_in_days for compatibility."""
        return await self.get_upcoming_in_days(days)
    
    async def search_advanced(self, **filters) -> List[Dict[str, Any]]:
        """Advanced search - delegate to AppleScript scheduler with limit support."""
        try:
            # Convert 'tag' to 'tags' for PureAppleScriptScheduler compatibility
            if 'tag' in filters and filters['tag']:
                filters['tags'] = [filters['tag']]  # Convert single tag to list
                del filters['tag']  # Remove the singular key
            
            return await self.reliable_scheduler.search_advanced(**filters)
        except Exception as e:
            logger.error(f"Error in advanced search: {e}")
            return []
    
    async def get_recent(self, period: str) -> List[Dict[str, Any]]:
        """Get recent items - for now delegate to AppleScript, could be optimized with things.py later."""
        try:
            return await self.reliable_scheduler.get_recent(period)
        except Exception as e:
            logger.error(f"Error getting recent items: {e}")
            return []
    
    # ========== CONVERSION HELPERS ==========
    
    def _convert_todo(self, todo: Dict) -> Dict:
        """Convert things.py todo to our MCP format with optimization."""
        converted = {
            'id': todo.get('uuid', ''),
            'name': todo.get('title', ''),
            'notes': todo.get('notes'),
            'status': todo.get('status', 'open'),
            'tag_names': todo.get('tags', []),
            'created': todo.get('created'),
            'modified': todo.get('modified'),
            'when': todo.get('start_date'),
            'deadline': todo.get('deadline'),
            'completed': todo.get('stop_date'),
            'project': todo.get('project'),
            'area': todo.get('area'),
            'heading': todo.get('heading'),
            'checklist': todo.get('checklist_items', []),
            'has_reminder': bool(todo.get('reminder_time')),
            'reminder_time': todo.get('reminder_time'),
            'activation_date': todo.get('activation_date')
        }
        # Apply optimization to remove duplicates and empty fields
        return self.response_optimizer.optimize_todo(converted)
    
    def _convert_project(self, project: Dict) -> Dict:
        """Convert things.py project to our MCP format with optimization."""
        converted = {
            'id': project.get('uuid', ''),
            'name': project.get('title', ''),
            'notes': project.get('notes'),
            'tag_names': project.get('tags', []),
            'area': project.get('area'),
            'status': project.get('status', 'open'),
            'created': project.get('created'),
            'modified': project.get('modified'),
            'when': project.get('start_date'),
            'deadline': project.get('deadline'),
            'completed': project.get('stop_date')
        }
        # Apply optimization to remove duplicates and empty fields
        return self.response_optimizer.optimize_project(converted)
    
    def _convert_area(self, area: Dict) -> Dict:
        """Convert things.py area to our MCP format with optimization."""
        converted = {
            'id': area.get('uuid', ''),
            'name': area.get('title', ''),
            'tag_names': area.get('tags', []),
            'notes': area.get('notes'),
            'created': area.get('created'),
            'modified': area.get('modified')
        }
        # Apply optimization to remove duplicates and empty fields
        return self.response_optimizer.optimize_area(converted)