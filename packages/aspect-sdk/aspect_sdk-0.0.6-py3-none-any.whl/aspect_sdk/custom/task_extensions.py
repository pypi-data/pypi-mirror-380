import time
from typing import Optional, Callable, Protocol, Dict, Any
from aspect_sdk._generated import TaskGetResponse, FeatureState, FeatureInfo


class WaitForDoneOptions:
    """Options for polling task completion"""
    
    def __init__(
        self,
        interval: float = 5.0,
        callback: Optional[Callable[[TaskGetResponse], None]] = None
    ):
        """
        Args:
            interval: Polling interval in seconds (default: 5.0)
            callback: Callback function called on each poll with the current task state
        """
        self.interval = interval
        self.callback = callback


class TaskExtensions(Protocol):
    """Protocol defining task extension methods"""
    
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
        ...


def are_all_features_done(task: TaskGetResponse) -> bool:
    """
    Checks if all features in a task are in a final state (completed, failed, or cancelled)
    
    Args:
        task: The task schema to check
        
    Returns:
        True if all features are in a final state, False otherwise
    """
    processing_states = {FeatureState.QUEUED, FeatureState.PROCESSING}
    
    # Handle both dict and object attribute access for features
    if hasattr(task, 'features'):
        features = task.features
    else:
        features = getattr(task, 'features', {})
    
    if isinstance(features, dict):
        feature_values = list(features.values())
    else:
        # If features is an object with attributes
        feature_values = [getattr(features, attr) for attr in dir(features) 
                         if not attr.startswith('_') and isinstance(getattr(features, attr), FeatureInfo)]
    
    return all(
        feature_info.state not in processing_states
        for feature_info in feature_values
        if isinstance(feature_info, FeatureInfo)
    )


def delay(seconds: float) -> None:
    """
    Sleeps for the specified number of seconds
    
    Args:
        seconds: Number of seconds to wait
    """
    time.sleep(seconds)
