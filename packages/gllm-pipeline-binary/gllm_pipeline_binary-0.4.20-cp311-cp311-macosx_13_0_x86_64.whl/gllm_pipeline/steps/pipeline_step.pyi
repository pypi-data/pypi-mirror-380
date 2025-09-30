import abc
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from gllm_core.utils.retry import RetryConfig as RetryConfig
from gllm_datastore.cache.cache import BaseCache as BaseCache
from gllm_pipeline.exclusions import ExclusionSet as ExclusionSet
from gllm_pipeline.pipeline.pipeline import Pipeline as Pipeline
from gllm_pipeline.steps.step_error_handler import RaiseStepErrorHandler as RaiseStepErrorHandler
from gllm_pipeline.steps.step_error_handler.step_error_handler import BaseStepErrorHandler as BaseStepErrorHandler
from gllm_pipeline.utils.error_handling import ErrorContext as ErrorContext
from gllm_pipeline.utils.graph import create_edge as create_edge
from gllm_pipeline.utils.retry_converter import retry_config_to_langgraph_policy as retry_config_to_langgraph_policy
from langchain_core.runnables import RunnableConfig as RunnableConfig
from langgraph.graph import StateGraph as StateGraph
from langgraph.types import RetryPolicy as RetryPolicy
from pydantic import BaseModel as BaseModel
from typing import Any

LANGGRAPH_CONFIG_PREFIX: str

class BasePipelineStep(ABC, metaclass=abc.ABCMeta):
    '''The base class for all pipeline steps.

    A pipeline step represents a single operation or task within a larger processing pipeline.
    Each step must implement:
    1. execute() - to perform the actual operation
    2. add_to_graph() - to integrate with the pipeline structure (optional, default implementation provided)

    The default implementation of add_to_graph is suitable for steps that:
    1. Have a single entry point
    2. Have a single exit point
    3. Connect to all previous endpoints

    For more complex graph structures (e.g., conditional branching), steps should override add_to_graph.

    Examples:
        1. Basic Usage:
            ```python
            step = MyCustomStep("my_step")
            ```

        2. Adding Step Level Caching:
            ```python
            step = MyCustomStep(
                "my_step",
                cache_store=cache_store,
                cache_config={"ttl": 1800}
            )

        3. Retry Configuration:
            ```python
            retry_config = RetryConfig(max_retries=3, backoff_factor=2)
            step = MyCustomStep(
                "my_step",
                retry_config=retry_config
            )
            ```

        4. Error Handling:
            ```python
            step = MyCustomStep(
                "my_step",
                error_handler=error_handler
            )
            ```

    Attributes:
        name (str): A unique identifier for the pipeline step.
        retry_policy (RetryPolicy | None): Configuration for retry behavior using LangGraph\'s RetryPolicy.
        cache_store ("BaseCache" | None): The cache store used for caching step results, if configured.
        is_cache_enabled (bool): Property indicating whether caching is enabled for this step.
    '''
    name: Incomplete
    error_handler: Incomplete
    retry_policy: Incomplete
    cache_store: Incomplete
    def __init__(self, name: str, retry_config: RetryConfig | None = None, error_handler: BaseStepErrorHandler | None = None, cache_store: BaseCache | None = None, cache_config: dict[str, Any] | None = None) -> None:
        '''Initializes a new pipeline step.

        Args:
            name (str): A unique identifier for the pipeline step.
            retry_config (RetryConfig | None, optional): Configuration for retry behavior using
                GLLM Core\'s RetryConfig. Defaults to None, in which case no retry config is applied.
                The RetryConfig is automatically converted to LangGraph\'s RetryPolicy when needed for internal use.
                Note that `timeout` is not supported and will be ignored.
            error_handler (BaseStepErrorHandler | None, optional): Strategy to handle errors during execution.
                Defaults to None, in which case the RaiseStepErrorHandler is used.
            cache_store ("BaseCache" | None, optional): The cache store to use for caching step results.
                Defaults to None. If None, no caching will be used.
            cache_config (dict[str, Any] | None, optional): Configuration for the cache store.
                1. key_func: A function to generate cache keys. If None, the cache instance will use its own key
                    function.
                2. name: The name of the cache. If None, the cache instance will use its own key function.
                3. ttl: The time-to-live for the cache. If None, the cache will not have a TTL.
                4. matching_strategy: The strategy for matching cache keys.
                    If None, the cache instance will use "exact".
                5. matching_config: Configuration for the matching strategy.
                    If None, the cache instance will use its own default matching strategy configuration.

        Caching Mechanism:
            When a cache_store is provided, the step\'s execution method is automatically
            wrapped with a cache decorator. This means:
            1. Before execution, the cache is checked for existing results based on input parameters
            2. If a cached result exists and is valid, it\'s returned immediately
            3. If no cached result exists, the step executes normally and the result is cached
            4. Cache keys are generated from the step\'s input state and configuration
            5. The cache name defaults to "step_{step_name}" if not specified
        '''
    @property
    def is_cache_enabled(self) -> bool:
        """Check if this step has caching enabled.

        Returns:
            bool: True if caching is enabled, False otherwise.
        """
    @property
    def is_excluded(self) -> bool:
        """Whether this step is excluded from execution/graph integration.

        Returns:
            bool: True if the step is excluded, False otherwise.
        """
    @is_excluded.setter
    def is_excluded(self, value: bool) -> None:
        """Set the exclusion state for this step.

        Args:
            value (bool): Exclusion flag.
        """
    def add_to_graph(self, graph: StateGraph, previous_endpoints: list[str], retry_policy: RetryPolicy | None = None) -> list[str]:
        """Integrates this step into the pipeline's internal structure.

        This method is responsible for:
        1. Adding the step's node(s) to the graph if not already present
        2. Creating edges from previous endpoints to this step's entry points
        3. Returning this step's exit points (endpoints)

        This method provides a default implementation suitable for simple steps.
        Steps with more complex graph structures should override this method.

        This method is used by `Pipeline` to manage the pipeline's execution flow.
        It should not be called directly by users.

        Args:
            graph (StateGraph): The internal representation of the pipeline structure.
            previous_endpoints (list[str]): The endpoints from previous steps to connect to.
            retry_policy (RetryPolicy | None): Configuration for retry behavior using LangGraph's RetryPolicy.
                If None, the retry policy of the step is used. If the step is not a retryable step,
                this parameter is ignored.

        Returns:
            list[str]: The exit points (endpoints) of this step.
        """
    @abstractmethod
    async def execute(self, state: dict[str, Any] | BaseModel, config: RunnableConfig) -> dict[str, Any] | None:
        """Executes the operation defined for this pipeline step.

        This method should be implemented by subclasses to perform the actual processing or computation for this step.

        Args:
            state (dict[str, Any] | BaseModel): The current state of the pipeline, containing all data.
            config (RunnableConfig): Runtime configuration for this step's execution.

        Returns:
            dict[str, Any] | None: The update to the pipeline state after this step's operation.
                This should include new or modified data produced by this step, not the entire state.
                Returns None if no state update is needed.

        Raises:
            NotImplementedError: If the subclass does not implement this method.
        """
    async def execute_direct(self, state: dict[str, Any], config: RunnableConfig) -> dict[str, Any] | None:
        """Execute this step directly, bypassing graph-based execution.

        This method is used when a step needs to be executed directly, such as in parallel execution.
        The default implementation calls _execute_with_error_handling for consistent error handling.

        Args:
            state (dict[str, Any]): The current state of the pipeline.
            config (RunnableConfig): Runtime configuration for this step's execution.

        Returns:
            dict[str, Any] | None: Updates to apply to the pipeline state, or None if no updates.
        """
    def apply_exclusions(self, exclusions: ExclusionSet) -> None:
        """Apply exclusions to this step.

        Args:
            exclusions (ExclusionSet): The exclusion set to apply.
        """
    def get_mermaid_diagram(self) -> str:
        """Generates a Mermaid diagram representation of the pipeline step.

        This method provides a default implementation that can be overridden by subclasses
        to provide more detailed or specific diagrams.

        It is recommended to implement this method for subclasses that have multiple connections to other steps.

        Returns:
            str: Empty string.
        """
    def __or__(self, other: BasePipelineStep | Pipeline) -> Pipeline:
        """Combines this step with another step or pipeline.

        This method allows for easy composition of pipeline steps using the | operator.

        Args:
            other (BasePipelineStep | Pipeline): Another step or pipeline to combine with this one.

        Returns:
            Pipeline: A new pipeline containing the combined steps.
        """
    def __lshift__(self, other: BasePipelineStep | Pipeline) -> Pipeline:
        """Combines this step with another step or pipeline using the '<<' operator.

        Args:
            other (BasePipelineStep | Pipeline): The step or pipeline to add after this step.

        Returns:
            Pipeline: A new pipeline with this step followed by the other step or pipeline.
        """
    def __rshift__(self, other: BasePipelineStep | Pipeline) -> Pipeline:
        """Combines this step with another step or pipeline using the '>>' operator.

        Args:
            other (BasePipelineStep | Pipeline): The step or pipeline to include this step in.

        Returns:
            Pipeline: A new pipeline with this step included in the other step or pipeline.
        """
