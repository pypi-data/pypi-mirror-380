#!/usr/bin/env python3
"""
RFP Betterment Analyzer

A tool to evaluate proposal content and identify elements that qualify as betterments 
in government RFP responses. The tool identifies features in proposal text that exceed 
baseline requirements from a Performance Work Statement (PWS).
"""

import argparse
import os
import json
import re
import glob
import fnmatch
from dataclasses import dataclass, field, asdict
from enum import Enum, auto
from typing import List, Dict, Tuple, Optional, Union, Any
import csv
from pathlib import Path
import difflib
from collections import defaultdict

# Import required libraries
try:
    import nltk
    from nltk.tokenize import word_tokenize, sent_tokenize
    nltk.download('punkt', quiet=True)
    
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity
    
    import pandas as pd
    from tqdm import tqdm
except ImportError:
    print("Required libraries not found. Installing dependencies...")
    import subprocess
    subprocess.call(['pip', 'install', 'nltk', 'scikit-learn', 'pandas', 'tqdm'])
    
    import nltk
    from nltk.tokenize import word_tokenize, sent_tokenize
    nltk.download('punkt', quiet=True)
    
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity
    
    import pandas as pd
    from tqdm import tqdm


# Define output format options
class OutputFormat(str, Enum):
    """Enum for output format options"""
    JSON = "json"
    TEXT = "text"
    CSV = "csv"
    HTML = "html"
    
    @classmethod
    def from_string(cls, s: str):
        """Convert string to OutputFormat enum"""
        try:
            return cls(s.lower())
        except ValueError:
            valid_options = [e.value for e in cls]
            raise ValueError(f"Invalid format: {s}. Valid options are: {', '.join(valid_options)}")


# Define betterment types with descriptions
class BettermentType(Enum):
    """Enum for betterment categories with descriptions"""
    PERFORMANCE_QUALITY = ("Performance/Quality", "Exceeds performance metrics, quality standards, or precision requirements")
    SECURITY_COMPLIANCE = ("Security/Compliance", "Provides security features beyond minimum compliance requirements")
    COST_VALUE_TCO = ("Cost/Value/TCO", "Offers cost savings or additional value beyond requirements")
    SCHEDULE_SPEED = ("Schedule/Speed", "Delivers faster implementation or response times than required")
    RELIABILITY_AVAILABILITY = ("Reliability/Availability", "Exceeds uptime or availability requirements")
    SCALABILITY_CAPACITY = ("Scalability/Capacity", "Provides higher capacity or better scalability than required")
    RISK_REDUCTION = ("Risk Reduction", "Offers additional risk mitigation beyond requirements")
    USER_EXPERIENCE = ("User Experience/Accessibility", "Enhances user experience or accessibility beyond requirements")
    MAINTAINABILITY = ("Maintainability/Operability", "Improves ease of maintenance or operation")
    INNOVATION = ("Innovation/Modernization", "Introduces innovative or modern approaches beyond requirements")
    
    def label(self):
        """Get the display label for the betterment type"""
        return self.value[0]
    
    def description(self):
        """Get the description of the betterment type"""
        return self.value[1]
    
    @classmethod
    def from_label(cls, label: str):
        """Get betterment type from label string"""
        for bt in cls:
            if bt.label() == label:
                return bt
        raise ValueError(f"Invalid betterment type label: {label}")
    
    @classmethod
    def get_categories(cls):
        """Get list of all category labels"""
        return [bt.label() for bt in cls]


# Define impact levels with descriptions
class ImpactLevel(Enum):
    """Enum for impact levels with descriptions"""
    LOW = ("Low", "Minor improvement with limited benefit to overall objectives")
    MEDIUM = ("Med", "Meaningful improvement that noticeably advances objectives")
    HIGH = ("High", "Significant improvement with substantial benefit to objectives")
    
    def label(self):
        """Get the display label for the impact level"""
        return self.value[0]
    
    def description(self):
        """Get the description of the impact level"""
        return self.value[1]
    
    @classmethod
    def from_label(cls, label: str):
        """Get impact level from label string"""
        for il in cls:
            if il.label() == label:
                return il
        raise ValueError(f"Invalid impact level label: {label}")


# Define priority levels with descriptions
class PriorityLevel(Enum):
    """Enum for priority levels with descriptions"""
    P1 = ("P1", "Highest priority, recommended for executive summary highlight")
    P2 = ("P2", "Medium priority, significant but not showcase material")
    P3 = ("P3", "Lower priority, worth mentioning but not highlighting")
    
    def label(self):
        """Get the display label for the priority level"""
        return self.value[0]
    
    def description(self):
        """Get the description of the priority level"""
        return self.value[1]
    
    @classmethod
    def from_label(cls, label: str):
        """Get priority level from label string"""
        for pl in cls:
            if pl.label() == label:
                return pl
        raise ValueError(f"Invalid priority level label: {label}")
