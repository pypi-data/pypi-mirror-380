#!/usr/bin/env python3
"""
Test script to verify filtering functionality and confidence thresholds.
"""

import os
import sys
import json
import subprocess
from pathlib import Path

# Add parent directory to path so we can import from main
sys.path.insert(0, str(Path(__file__).parent.parent))

def test_category_filtering():
    """Test filtering by betterment categories."""
    print("Testing category filtering...")
    
    # Define test files
    pws_file = "../examples/sample_pws.txt"
    proposal_file = "../examples/sample_proposal.txt"
    
    # Create output directory
    os.makedirs("./test_outputs", exist_ok=True)
    
    # Test filtering by Performance/Quality category
    print("Testing Performance/Quality category filter...")
    subprocess.check_call([
        "python", "../main.py",
        "--pws", pws_file,
        "--proposal", proposal_file,
        "--categories", "Performance/Quality",
        "--format", "json",
        "--output", "./test_outputs/filtered_performance.json"
    ])
    
    # Verify filtered output
    with open("./test_outputs/filtered_performance.json", 'r') as f:
        json_data = json.load(f)
        for betterment in json_data.get('betterments', []):
            assert "Performance/Quality" in betterment.get('betterment_types', []), \
                "Non-Performance/Quality betterment found in filtered results"
    print("✅ Category filtering test passed")

def test_priority_filtering():
    """Test filtering by priority level."""
    print("Testing priority filtering...")
    
    # Define test files
    pws_file = "../examples/sample_pws.txt"
    proposal_file = "../examples/sample_proposal.txt"
    
    # Test filtering by P1 priority
    print("Testing P1 priority filter...")
    subprocess.check_call([
        "python", "../main.py",
        "--pws", pws_file,
        "--proposal", proposal_file,
        "--priority", "P1",
        "--format", "json",
        "--output", "./test_outputs/filtered_p1.json"
    ])
    
    # Verify filtered output
    with open("./test_outputs/filtered_p1.json", 'r') as f:
        json_data = json.load(f)
        for betterment in json_data.get('betterments', []):
            assert betterment.get('priority') == 'P1', \
                "Non-P1 betterment found in filtered results"
    print("✅ Priority filtering test passed")

def test_confidence_threshold():
    """Test confidence threshold settings."""
    print("Testing confidence threshold...")
    
    # Define test files
    pws_file = "../examples/sample_pws.txt"
    proposal_file = "../examples/sample_proposal.txt"
    
    # Test with high confidence threshold (0.8)
    print("Testing high confidence threshold (0.8)...")
    subprocess.check_call([
        "python", "../main.py",
        "--pws", pws_file,
        "--proposal", proposal_file,
        "--confidence", "0.8",
        "--format", "json",
        "--output", "./test_outputs/high_confidence.json"
    ])
    
    # Verify confidence-filtered output
    with open("./test_outputs/high_confidence.json", 'r') as f:
        json_data = json.load(f)
        for betterment in json_data.get('betterments', []):
            assert betterment.get('confidence', 0) >= 0.8, \
                "Betterment with confidence < 0.8 found in high confidence results"
    print("✅ Confidence threshold test passed")

if __name__ == "__main__":
    test_category_filtering()
    test_priority_filtering()
    test_confidence_threshold()
    print("All filtering and confidence threshold tests passed!")
