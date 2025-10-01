#!/usr/bin/env python3
"""
Model classes for RFP Betterment Analyzer
"""

from dataclasses import dataclass, field, asdict
from typing import List, Dict, Optional, Tuple, Any
from .analyzer import BettermentType, ImpactLevel, PriorityLevel


@dataclass
class Requirement:
    """Class representing a requirement from the PWS"""
    req_id: str
    text: str
    source_line: Optional[int] = None
    source_para: Optional[str] = None
    source_file: Optional[str] = None
    section: Optional[str] = None
    
    def to_dict(self):
        """Convert to dictionary representation"""
        return asdict(self)
    
    def __post_init__(self):
        """Validate requirement after initialization"""
        if not self.req_id:
            raise ValueError("Requirement ID cannot be empty")
        if not self.text:
            raise ValueError("Requirement text cannot be empty")


@dataclass
class MetricUnit:
    """Class for representing a metric with its unit and value"""
    name: str
    value: float
    unit: str
    higher_is_better: bool = True
    
    def is_better_than(self, other: 'MetricUnit'):
        """Compare if this metric is better than another"""
        if self.name != other.name or self.unit != other.unit:
            raise ValueError(f"Cannot compare different metrics: {self.name}({self.unit}) vs {other.name}({other.unit})")
            
        if self.higher_is_better:
            return self.value > other.value
        else:
            return self.value < other.value
    
    def percentage_improvement(self, other: 'MetricUnit'):
        """Calculate percentage improvement over baseline"""
        if self.name != other.name or self.unit != other.unit:
            raise ValueError(f"Cannot compare different metrics: {self.name}({self.unit}) vs {other.name}({other.unit})")
            
        if self.higher_is_better:
            return ((self.value - other.value) / other.value) * 100
        else:
            return ((other.value - self.value) / other.value) * 100
    
    def __str__(self):
        return f"{self.name}: {self.value} {self.unit}"


@dataclass
class Betterment:
    """Class representing a betterment identified in the proposal"""
    title: str
    req_id: str
    baseline_requirement: str
    betterment_text: str
    proposal_quote: str
    source_location: Optional[str] = None
    source_file: Optional[str] = None
    metrics: Dict[str, Tuple[MetricUnit, MetricUnit]] = field(default_factory=dict)
    betterment_types: List[BettermentType] = field(default_factory=list)
    justification: str = ""
    confidence: float = 0.0
    impact: ImpactLevel = ImpactLevel.LOW
    priority: PriorityLevel = PriorityLevel.P3
    
    def to_dict(self):
        """Convert to dictionary representation"""
        result = asdict(self)
        
        # Convert enum types to their string representations
        result['betterment_types'] = [bt.label() for bt in self.betterment_types]
        result['impact'] = self.impact.label()
        result['priority'] = self.priority.label()
        
        # Convert metrics to dict format
        metrics_dict = {}
        for metric_name, (baseline, improved) in self.metrics.items():
            metrics_dict[metric_name] = {
                'baseline': {
                    'name': baseline.name,
                    'value': baseline.value,
                    'unit': baseline.unit,
                    'higher_is_better': baseline.higher_is_better
                },
                'improved': {
                    'name': improved.name,
                    'value': improved.value,
                    'unit': improved.unit,
                    'higher_is_better': improved.higher_is_better
                },
                'improvement_percentage': improved.percentage_improvement(baseline)
            }
        result['metrics'] = metrics_dict
        
        return result
    
    def __post_init__(self):
        """Validate betterment after initialization"""
        if not self.title:
            raise ValueError("Betterment title cannot be empty")
        if not self.req_id:
            raise ValueError("Requirement ID cannot be empty")
        if not self.baseline_requirement:
            raise ValueError("Baseline requirement cannot be empty")
        if not self.betterment_text:
            raise ValueError("Betterment text cannot be empty")
        if not self.proposal_quote:
            self.proposal_quote = self.betterment_text
        if self.confidence < 0 or self.confidence > 1:
            raise ValueError("Confidence score must be between 0 and 1")
    
    def get_improvement_summary(self):
        """Get a summary of the improvements"""
        if not self.metrics:
            return ""
            
        improvements = []
        for metric_name, (baseline, improved) in self.metrics.items():
            perc = improved.percentage_improvement(baseline)
            improvements.append(f"{metric_name}: {baseline.value} {baseline.unit} → {improved.value} {improved.unit} ({perc:.2f}% improvement)")
            
        return ", ".join(improvements)


@dataclass
class MeetsOnly:
    """Class representing a feature that only meets (not exceeds) requirements"""
    req_id: str
    baseline_requirement: str
    proposal_text: str
    justification: str
    source_location: Optional[str] = None
    source_file: Optional[str] = None
    
    def to_dict(self):
        """Convert to dictionary representation"""
        return asdict(self)
    
    def __post_init__(self):
        """Validate meets-only item after initialization"""
        if not self.req_id:
            raise ValueError("Requirement ID cannot be empty")
        if not self.baseline_requirement:
            raise ValueError("Baseline requirement cannot be empty")
        if not self.proposal_text:
            raise ValueError("Proposal text cannot be empty")


@dataclass
class AmbiguousItem:
    """Class representing a potential betterment that needs more details"""
    req_id: str
    baseline_requirement: str
    proposal_text: str
    missing_details: str
    source_location: Optional[str] = None
    source_file: Optional[str] = None
    
    def to_dict(self):
        """Convert to dictionary representation"""
        return asdict(self)
    
    def __post_init__(self):
        """Validate ambiguous item after initialization"""
        if not self.req_id:
            raise ValueError("Requirement ID cannot be empty")
        if not self.baseline_requirement:
            raise ValueError("Baseline requirement cannot be empty")
        if not self.proposal_text:
            raise ValueError("Proposal text cannot be empty")
        if not self.missing_details:
            raise ValueError("Missing details description cannot be empty")
