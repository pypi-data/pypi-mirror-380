#!/usr/bin/env python3
"""
Test script to verify all output formats work correctly.
"""

import os
import sys
import json
import subprocess
from pathlib import Path

# Add parent directory to path so we can import from main
sys.path.insert(0, str(Path(__file__).parent.parent))

from main import BettermentAnalyzer, AnalysisConfig, format_results_as_text, export_to_csv, export_to_html

def test_all_formats():
    """Test all output formats using sample data."""
    print("Testing all output formats...")
    
    # Define test files
    pws_file = "../examples/sample_pws.txt"
    proposal_file = "../examples/sample_proposal.txt"
    requirements_file = "../examples/sample_requirements.txt"
    
    # Create output directory
    os.makedirs("./test_outputs", exist_ok=True)
    
    # Test JSON output
    print("Testing JSON output...")
    subprocess.check_call([
        "python", "../main.py",
        "--pws", pws_file,
        "--proposal", proposal_file,
        "--requirements", requirements_file,
        "--format", "json",
        "--output", "./test_outputs/test_results.json"
    ])
    
    # Verify JSON output exists and is valid
    with open("./test_outputs/test_results.json", 'r') as f:
        json_data = json.load(f)
        assert 'betterments' in json_data, "JSON output missing betterments section"
        print("✅ JSON output test passed")
    
    # Test Text output
    print("Testing Text output...")
    subprocess.check_call([
        "python", "../main.py",
        "--pws", pws_file,
        "--proposal", proposal_file,
        "--requirements", requirements_file,
        "--format", "text",
        "--output", "./test_outputs/test_results.txt"
    ])
    
    # Verify text output exists
    assert os.path.exists("./test_outputs/test_results.txt"), "Text output file not created"
    print("✅ Text output test passed")
    
    # Test CSV output
    print("Testing CSV output...")
    subprocess.check_call([
        "python", "../main.py",
        "--pws", pws_file,
        "--proposal", proposal_file,
        "--requirements", requirements_file,
        "--format", "csv",
        "--output", "./test_outputs/test_results.csv"
    ])
    
    # Verify CSV output exists
    assert os.path.exists("./test_outputs/test_results_betterments.csv"), "CSV output file not created"
    print("✅ CSV output test passed")
    
    # Test HTML output
    print("Testing HTML output...")
    subprocess.check_call([
        "python", "../main.py",
        "--pws", pws_file,
        "--proposal", proposal_file,
        "--requirements", requirements_file,
        "--format", "html",
        "--output", "./test_outputs/test_results.html"
    ])
    
    # Verify HTML output exists
    assert os.path.exists("./test_outputs/test_results.html"), "HTML output file not created"
    print("✅ HTML output test passed")
    
    print("All output format tests passed!")

if __name__ == "__main__":
    test_all_formats()
