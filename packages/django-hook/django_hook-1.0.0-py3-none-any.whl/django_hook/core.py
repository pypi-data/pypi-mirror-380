from typing import Any, Callable, List, Optional, Tuple
from .registry import hook_registry


class HookSystem:
    """
    Hook management system for Django
    """

    @classmethod
    def invoke(cls, hook_name: str, *args: Any, **kwargs: Any) -> List[Any]:
        """
        Invoke a hook and aggregate results from all implementers

        Args:
            hook_name: Name of the hook
            *args: Positional arguments
            **kwargs: Keyword arguments

        Returns:
            Dict of {app_name: result}
        """

        results: List[Any] = []

        for _, hook_func in hook_registry.get_hooks(hook_name):
            try:
                result = hook_func(*args, **kwargs)
                results.append(result)
            except Exception as e:
                import logging

                logger = logging.getLogger(__name__)
                logger.error(f"Error executing hook {hook_name}: {e}")

        return results

    @classmethod
    def invoke_aggregate(
        cls,
        hook_name: str,
        aggregator: Callable[[List[Any]], Any],
        *args: Any,
        **kwargs: Any,
    ) -> Any:
        """
        Invoke hook and aggregate results with custom aggregator function

        Args:
            hook_name: Name of the hook
            aggregator: Aggregator function
            *args: Positional arguments
            **kwargs: Keyword arguments

        Returns:
            Aggregated result
        """
        results = cls.invoke(hook_name, *args, **kwargs)
        return aggregator(results)

    @classmethod
    def get_hook_implementations(
        cls, hook_name: str
    ) -> List[Tuple[str, Callable[..., Any]]]:
        """
        Get all implementers of a hook

        Returns:
            List of tuples containing (app_name, hook_function)
        """
        return hook_registry.get_hooks(hook_name)

    @classmethod
    def register_hook(
        cls,
        hook_name: str,
        hook_func: Callable[..., Any],
        app_name: Optional[str] = None,
    ) -> None:
        """
        Manually register a hook

        Args:
            hook_name: Name of the hook
            hook_func: Hook function
            app_name: App name (optional)
        """
        if app_name is None:
            # Use module name if app name not provided
            app_name = hook_func.__module__.split(".")[0]

        hook_registry.register(hook_name, hook_func, app_name)
