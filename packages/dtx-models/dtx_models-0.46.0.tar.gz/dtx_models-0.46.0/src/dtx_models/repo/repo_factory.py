"""
Repository factory for managing all repositories with lazy loading.
"""

from typing import Optional

from .base_repo import BaseRepository
from .behavior_repo import BehaviorRepository
from .converter_repo import ConverterRepository
from .evaluator_repo import EvaluatorRepository
from .prompt_template_repo import PromptTemplateRepository
from .converter_prompt_template_repo import ConverterPromptTemplateRepository
from .attack_strategies_repo import AttackStrategiesRepository
from .attack_recipes_repo import AttackRecipesRepository


class RepositoryFactory:
    """
    Factory class for managing all repositories with lazy initialization.
    """

    def __init__(self, data_dir: Optional[str] = None):
        """
        Initialize the repository factory.
        
        Args:
            data_dir: Optional base directory for all repositories
        """
        self._data_dir = data_dir
        self._behavior_repo: Optional[BehaviorRepository] = None
        self._converter_repo: Optional[ConverterRepository] = None
        self._evaluator_repo: Optional[EvaluatorRepository] = None
        self._template_repo: Optional[PromptTemplateRepository] = None
        self._converter_template_repo: Optional[ConverterPromptTemplateRepository] = None
        self._attack_strategies_repo: Optional[AttackStrategiesRepository] = None
        self._attack_recipes_repo: Optional[AttackRecipesRepository] = None
    
    @property
    def behaviors(self) -> BehaviorRepository:
        """Get the behavior repository (lazy loaded)."""
        if self._behavior_repo is None:
            self._behavior_repo = BehaviorRepository(self._data_dir)
        return self._behavior_repo
    
    @property
    def converters(self) -> ConverterRepository:
        """Get the converter repository (lazy loaded)."""
        if self._converter_repo is None:
            self._converter_repo = ConverterRepository(self._data_dir)
        return self._converter_repo
    
    @property
    def evaluators(self) -> EvaluatorRepository:
        """Get the evaluator repository (lazy loaded)."""
        if self._evaluator_repo is None:
            self._evaluator_repo = EvaluatorRepository(self._data_dir)
        return self._evaluator_repo
    
    @property
    def templates(self) -> PromptTemplateRepository:
        """Get the prompt template repository (lazy loaded)."""
        if self._template_repo is None:
            self._template_repo = PromptTemplateRepository(self._data_dir)
        return self._template_repo
    
    @property
    def converter_templates(self) -> ConverterPromptTemplateRepository:
        """Get the converter prompt template repository (lazy loaded)."""
        if self._converter_template_repo is None:
            self._converter_template_repo = ConverterPromptTemplateRepository(self._data_dir)
        return self._converter_template_repo
    
    @property
    def attack_strategies(self) -> AttackStrategiesRepository:
        """Get the attack strategies repository (lazy loaded)."""
        if self._attack_strategies_repo is None:
            self._attack_strategies_repo = AttackStrategiesRepository(self._data_dir)
        return self._attack_strategies_repo
    
    @property
    def attack_recipes(self) -> AttackRecipesRepository:
        """Get the attack recipes repository (lazy loaded)."""
        if self._attack_recipes_repo is None:
            self._attack_recipes_repo = AttackRecipesRepository(self._data_dir)
        return self._attack_recipes_repo
    
    def reload_all(self) -> None:
        """Reload all repositories."""
        if self._behavior_repo:
            self._behavior_repo.reload()
        if self._converter_repo:
            self._converter_repo.reload()
        if self._evaluator_repo:
            self._evaluator_repo.reload()
        if self._template_repo:
            self._template_repo.reload()
        if self._converter_template_repo:
            self._converter_template_repo.reload()
        if self._attack_strategies_repo:
            self._attack_strategies_repo.reload()
        if self._attack_recipes_repo:
            self._attack_recipes_repo.reload()
    
    def clear_all_caches(self) -> None:
        """Clear all repository caches."""
        if self._behavior_repo:
            self._behavior_repo.clear_cache()
        if self._converter_repo:
            self._converter_repo.clear_cache()
        if self._evaluator_repo:
            self._evaluator_repo.clear_cache()
        if self._template_repo:
            self._template_repo.clear_cache()
        if self._converter_template_repo:
            self._converter_template_repo.clear_cache()
        if self._attack_strategies_repo:
            self._attack_strategies_repo.clear_cache()
        if self._attack_recipes_repo:
            self._attack_recipes_repo.clear_cache()
    
    def get_stats(self) -> dict:
        """Get statistics for all repositories."""
        stats = {}
        
        if self._behavior_repo:
            stats['behaviors'] = {
                'total': self._behavior_repo.count(),
                'harmbench': len(self._behavior_repo.get_by_tag('harmbench')),
                'advbench': len(self._behavior_repo.get_by_tag('advbench'))
            }
        
        if self._converter_repo:
            stats['converters'] = {
                'total': self._converter_repo.count(),
                'static': len(self._converter_repo.get_static_converters()),
                'llm': len(self._converter_repo.get_llm_converters()),
                'dynamic_code': len(self._converter_repo.get_dynamic_code_converters())
            }
        
        if self._evaluator_repo:
            stats['evaluators'] = {
                'total': self._evaluator_repo.count(),
                'static': len(self._evaluator_repo.get_static_evaluators()),
                'llm-static': len(self._evaluator_repo.get_llm_static_evaluators()),
                'llm': len(self._evaluator_repo.get_llm_evaluators()),
                'true_false': len(self._evaluator_repo.get_by_scorer_type('true_false')),
                'float_scale': len(self._evaluator_repo.get_by_scorer_type('float_scale'))
            }
        
        if self._template_repo:
            stats['templates'] = {
                'total': self._template_repo.count()
            }
        
        if self._converter_template_repo:
            stats['converter_templates'] = {
                'total': self._converter_template_repo.count()
            }
        
        if self._attack_strategies_repo:
            stats['attack_strategies'] = {
                'total': len(self._attack_strategies_repo.list_all()),
                'crescendo': len(self._attack_strategies_repo.get_by_strategy_type('crescendo')),
                'red_teaming': len(self._attack_strategies_repo.get_by_strategy_type('red_teaming')),
                'skeleton_key': len(self._attack_strategies_repo.get_by_strategy_type('skeleton_key')),
                'tap': len(self._attack_strategies_repo.get_by_strategy_type('tap')),
                'role_play': len(self._attack_strategies_repo.get_by_strategy_type('role_play'))
            }
        
        if self._attack_recipes_repo:
            recipe_stats = self._attack_recipes_repo.get_recipe_statistics()
            stats['attack_recipes'] = recipe_stats
        
        return stats


# Global factory instance
_repo_factory: Optional[RepositoryFactory] = None


def get_repo_factory(data_dir: Optional[str] = None) -> RepositoryFactory:
    """
    Get the global repository factory instance.
    
    Args:
        data_dir: Optional data directory (only used on first call)
        
    Returns:
        The global repository factory instance
    """
    global _repo_factory
    
    if _repo_factory is None:
        _repo_factory = RepositoryFactory(data_dir)
    
    return _repo_factory


def get_behaviors(data_dir: Optional[str] = None) -> BehaviorRepository:
    """Get the behavior repository."""
    return get_repo_factory(data_dir).behaviors


def get_converters(data_dir: Optional[str] = None) -> ConverterRepository:
    """Get the converter repository."""
    return get_repo_factory(data_dir).converters


def get_templates(data_dir: Optional[str] = None) -> PromptTemplateRepository:
    """Get the prompt template repository."""
    return get_repo_factory(data_dir).templates


def get_evaluators(data_dir: Optional[str] = None) -> EvaluatorRepository:
    """Get the evaluator repository."""
    return get_repo_factory(data_dir).evaluators


def get_converter_templates(data_dir: Optional[str] = None) -> ConverterPromptTemplateRepository:
    """Get the converter prompt template repository."""
    return get_repo_factory(data_dir).converter_templates


def get_attack_strategies(data_dir: Optional[str] = None) -> AttackStrategiesRepository:
    """Get the attack strategies repository."""
    return get_repo_factory(data_dir).attack_strategies


def get_attack_recipes(data_dir: Optional[str] = None) -> AttackRecipesRepository:
    """Get the attack recipes repository."""
    return get_repo_factory(data_dir).attack_recipes
