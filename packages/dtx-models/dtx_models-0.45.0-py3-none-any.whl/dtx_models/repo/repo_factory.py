"""
Repository factory for managing all repositories with lazy loading.
"""

from typing import Optional

from .base_repo import BaseRepository
from .behavior_repo import BehaviorRepository
from .converter_repo import ConverterRepository
from .prompt_template_repo import PromptTemplateRepository
from .converter_prompt_template_repo import ConverterPromptTemplateRepository


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
        self._template_repo: Optional[PromptTemplateRepository] = None
        self._converter_template_repo: Optional[ConverterPromptTemplateRepository] = None
    
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
    
    def reload_all(self) -> None:
        """Reload all repositories."""
        if self._behavior_repo:
            self._behavior_repo.reload()
        if self._converter_repo:
            self._converter_repo.reload()
        if self._template_repo:
            self._template_repo.reload()
        if self._converter_template_repo:
            self._converter_template_repo.reload()
    
    def clear_all_caches(self) -> None:
        """Clear all repository caches."""
        if self._behavior_repo:
            self._behavior_repo.clear_cache()
        if self._converter_repo:
            self._converter_repo.clear_cache()
        if self._template_repo:
            self._template_repo.clear_cache()
        if self._converter_template_repo:
            self._converter_template_repo.clear_cache()
    
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
        
        if self._template_repo:
            stats['templates'] = {
                'total': self._template_repo.count()
            }
        
        if self._converter_template_repo:
            stats['converter_templates'] = {
                'total': self._converter_template_repo.count()
            }
        
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


def get_converter_templates(data_dir: Optional[str] = None) -> ConverterPromptTemplateRepository:
    """Get the converter prompt template repository."""
    return get_repo_factory(data_dir).converter_templates
