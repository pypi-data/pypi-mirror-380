"""
DeEscalation Scoring Module

A Python module for evaluating escalation and de-escalation patterns 
in chat conversations using AI-powered scoring.
"""

__version__ = "0.1.1"

from .core import DeEscalationScorer, score_chat

__all__ = ["DeEscalationScorer", "score_chat"]