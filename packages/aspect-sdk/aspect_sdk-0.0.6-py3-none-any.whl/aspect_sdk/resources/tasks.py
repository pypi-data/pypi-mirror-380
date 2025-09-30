# Tasks resource - handles all task-related operations
from typing import Optional
from aspect_sdk._generated import (
    TasksApi,
    Configuration,
    TaskCreateRequest,
    TaskCreateResponse,
    TaskGetResponse,
    ApiClient,
)
from aspect_sdk.custom.task_extensions import (
    WaitForDoneOptions,
    TaskExtensions,
    are_all_features_done,
    delay,
)


class Tasks:
    """Task resource class implementing TaskExtensions protocol"""
    
    def __init__(self, config: Configuration):
        api_client = ApiClient(config)
        self._api = TasksApi(api_client)
    
    def create(self, task_data: TaskCreateRequest) -> TaskCreateResponse:
        """
        Create a new task
        
        Args:
            task_data: The task creation request data
            
        Returns:
            The created task response
        """
        return self._api.post_tasks_tasks(task_data)
    
    def get(self, task_id: str) -> TaskGetResponse:
        """
        Get a task
        
        Args:
            task_id: The ID of the task to retrieve
            
        Returns:
            The task schema
        """
        return self._api.get_tasks_tasks_task_id(task_id)
    
    def wait_for_done(
        self,
        task_id: str,
        options: Optional[WaitForDoneOptions] = None
    ) -> TaskGetResponse:
        """
        Polls a task until all features are either completed or failed
        
        Args:
            task_id: The ID of the task to poll
            options: Polling options including interval and callback
            
        Returns:
            The final TaskGetResponse when all features are done
        """
        if options is None:
            options = WaitForDoneOptions()
        
        while True:
            current_task = self.get(task_id)
            
            # Call the callback if provided
            if options.callback:
                options.callback(current_task)
            
            # Check if all features are in a final state
            if are_all_features_done(current_task):
                return current_task
            
            # Wait for the specified interval before polling again
            delay(options.interval)
