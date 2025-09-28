import json
import hashlib
from pathlib import Path
from typing import Optional
from datetime import datetime

from openagent.core.llm import gen_ai_resp_format
from openagent.prompts.execution_planer import ExecutionPlanPrompt
from openagent.models.scheduling import ExecutionPlan


class ExecutionPlanCache:
    """Cache for execution plans to avoid duplicate LLM calls."""

    def __init__(self, base_dir: Optional[Path] = None):
        """Initialize the cache with a directory.

        Args:
            base_dir: Base directory for cache storage. If None, uses default persistence directory.
        """
        if base_dir is None:
            # Use the same directory structure as persistence system
            from openagent.config.config import OpenAgentConfig

            config = OpenAgentConfig()
            base_dir = Path(config.execution_output_folder)

        self.cache_dir = base_dir / "cache" / "plans"
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def _get_cache_key(self, query: str) -> str:
        """Generate cache key from query."""
        return hashlib.sha256(query.encode()).hexdigest()[:16]

    def _get_cache_file(self, cache_key: str) -> Path:
        """Get cache file path for a cache key."""
        return self.cache_dir / f"plan_{cache_key}.json"

    def get_cached_plan(self, query: str) -> Optional[ExecutionPlan]:
        """Get cached execution plan if available."""
        try:
            cache_key = self._get_cache_key(query)
            cache_file = self._get_cache_file(cache_key)

            if not cache_file.exists():
                return None

            with open(cache_file, "r") as f:
                cache_data = json.load(f)

            # Check if cache is still valid (you can add expiration logic here)
            cached_at = datetime.fromisoformat(cache_data["cached_at"])
            age_hours = (datetime.now() - cached_at).total_seconds() / 3600

            # Cache expires after 24 hours (configurable)
            if age_hours > 24:
                cache_file.unlink()  # Remove expired cache
                return None

            # Reconstruct ExecutionPlan from cached data
            plan_data = cache_data["plan"]
            plan = ExecutionPlan(**plan_data)

            # Ensure the plan has the correct query for proper execution_id
            if not plan.query:
                plan.query = query

            return plan

        except Exception:
            # If cache reading fails, just return None to regenerate
            return None

    def cache_plan(self, query: str, plan: ExecutionPlan):
        """Cache an execution plan."""
        try:
            cache_key = self._get_cache_key(query)
            cache_file = self._get_cache_file(cache_key)

            cache_data = {
                "query": query,
                "cached_at": datetime.now().isoformat(),
                "plan": (
                    plan.model_dump() if hasattr(plan, "model_dump") else plan.__dict__
                ),
            }

            with open(cache_file, "w") as f:
                json.dump(cache_data, f, indent=2, default=str)

        except Exception:
            # If caching fails, log but don't crash
            pass

    def clear_cache(self):
        """Clear all cached plans."""
        try:
            for cache_file in self.cache_dir.glob("plan_*.json"):
                cache_file.unlink()
        except Exception:
            pass


# Global cache instance using unified directory structure
_plan_cache = ExecutionPlanCache()


def get_execution_plan(query: str, use_cache: bool = True) -> ExecutionPlan:
    """Generate an execution plan based on the provided query.

    Args:
        query (str): The input query for which to generate the execution plan.
        use_cache (bool): Whether to use cached plans if available.
    Returns:
        ExecutionPlan: The generated execution plan with query-based execution_id.
    """
    # Try to get cached plan first
    if use_cache:
        cached_plan = _plan_cache.get_cached_plan(query)
        if cached_plan:
            return cached_plan

    # Generate new plan using LLM
    prompt = ExecutionPlanPrompt(query)
    response = gen_ai_resp_format(
        messages=prompt.to_message_chain(),
        resp_cast=ExecutionPlan,
    )

    # Ensure the original query is preserved in the ExecutionPlan for hash-based execution_id
    if not response.query:
        # Create new ExecutionPlan with the query to get proper hash-based execution_id
        response = ExecutionPlan(
            entries=response.entries,
            total_entries=response.total_entries,
            query=query,  # This will generate the hash-based execution_id
        )

    # Cache the generated plan
    if use_cache:
        _plan_cache.cache_plan(query, response)

    return response


def clear_plan_cache():
    """Clear all cached execution plans."""
    _plan_cache.clear_cache()


def get_plan_cache_stats() -> dict:
    """Get statistics about the plan cache."""
    cache_files = list(_plan_cache.cache_dir.glob("plan_*.json"))

    # Also get persistence base directory for comparison
    from openagent.config.config import OpenAgentConfig

    config = OpenAgentConfig()
    persistence_base = Path(config.execution_output_folder)

    return {
        "cached_plans": len(cache_files),
        "cache_directory": str(_plan_cache.cache_dir),
        "persistence_base_directory": str(persistence_base),
        "unified_structure": _plan_cache.cache_dir.is_relative_to(persistence_base),
        "cache_files": [f.name for f in cache_files],
    }
