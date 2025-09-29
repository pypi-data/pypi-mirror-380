"""
LangLint - A lightweight language linter
"""

from typing import List
from dataclasses import dataclass


@dataclass
class LintResult:
    """Represents a lint result"""
    message: str
    severity: str = 'error'


class Linter:
    """Base class for linters"""
    
    def lint(self, content: str) -> List[LintResult]:
        """Lint the given content and return results"""
        return []


class LangLint:
    """Main linter class"""
    
    def __init__(self):
        self.linters: List[Linter] = []
    
    def add_linter(self, linter: Linter) -> None:
        """Add a linter to the collection"""
        self.linters.append(linter)
    
    def lint(self, content: str) -> List[LintResult]:
        """Run all linters on the content"""
        results = []
        for linter in self.linters:
            results.extend(linter.lint(content))
        return results


__version__ = '0.1.0-dev'
__all__ = ['LangLint', 'Linter', 'LintResult']

