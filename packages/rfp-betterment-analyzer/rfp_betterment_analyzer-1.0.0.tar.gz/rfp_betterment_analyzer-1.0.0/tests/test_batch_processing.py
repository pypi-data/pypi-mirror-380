#!/usr/bin/env python3
"""
Test script to verify batch processing capabilities.
"""

import os
import sys
import json
import shutil
import subprocess
from pathlib import Path

# Add parent directory to path so we can import from main
sys.path.insert(0, str(Path(__file__).parent.parent))

def setup_test_batch_directory():
    """Set up a test directory with multiple PWS/proposal pairs."""
    print("Setting up test batch directory...")
    
    # Create test batch directory
    batch_dir = Path("./test_batch")
    if batch_dir.exists():
        shutil.rmtree(batch_dir)
    batch_dir.mkdir(exist_ok=True)
    
    # Copy sample files to create multiple pairs
    sample_pws = Path("../examples/sample_pws.txt")
    sample_proposal = Path("../examples/sample_proposal.txt")
    sample_req = Path("../examples/sample_requirements.txt")
    
    # Create first pair
    shutil.copy(sample_pws, batch_dir / "project1_pws.txt")
    shutil.copy(sample_proposal, batch_dir / "project1_proposal.txt")
    shutil.copy(sample_req, batch_dir / "project1_requirements.txt")
    
    # Create second pair with slight modifications
    with open(sample_pws, 'r') as f:
        pws_content = f.read()
    with open(batch_dir / "project2_pws.txt", 'w') as f:
        f.write(pws_content.replace("3.1.1", "3.1.1 (Modified)"))
        
    with open(sample_proposal, 'r') as f:
        proposal_content = f.read()
    with open(batch_dir / "project2_proposal.txt", 'w') as f:
        f.write(proposal_content.replace("99.95%", "99.99%"))
        
    with open(sample_req, 'r') as f:
        req_content = f.read()
    with open(batch_dir / "project2_requirements.txt", 'w') as f:
        f.write(req_content.replace("REQ-1", "PROJ2-REQ-1"))
    
    print("✅ Test batch directory created successfully")
    return batch_dir

def test_batch_processing():
    """Test batch processing capabilities."""
    print("Testing batch processing...")
    
    # Set up test batch directory
    batch_dir = setup_test_batch_directory()
    
    # Create output directory
    output_dir = Path("./test_outputs/batch_results")
    if output_dir.exists():
        shutil.rmtree(output_dir)
    
    # Run batch processing
    print("Running batch processing test...")
    subprocess.check_call([
        "python", "../main.py",
        "--batch", str(batch_dir),
        "--pws-pattern", "*_pws.txt",
        "--proposal-pattern", "*_proposal.txt",
        "--requirements-pattern", "*_requirements.txt",
        "--pair-by", "name",
        "--format", "json",
        "--output", str(output_dir)
    ])
    
    # Verify batch results
    assert output_dir.exists(), "Batch output directory not created"
    
    # Check for summary file
    summary_file = output_dir / "batch_summary.json"
    assert summary_file.exists(), "Batch summary file not created"
    
    # Check for individual result files
    with open(summary_file, 'r') as f:
        summary = json.load(f)
        assert summary.get('success', 0) >= 2, "Expected at least 2 successful analyses"
        assert summary.get('failed', 0) == 0, "Found failed analyses in batch processing"
    
    # Check that individual output files exist
    assert (output_dir / "project1_proposal.json").exists(), "Project 1 output file not created"
    assert (output_dir / "project2_proposal.json").exists(), "Project 2 output file not created"
    
    print("✅ Batch processing test passed")
    
    # Test pair-by-index option
    print("Testing pair-by-index option...")
    output_dir_index = Path("./test_outputs/batch_index_results")
    if output_dir_index.exists():
        shutil.rmtree(output_dir_index)
    
    subprocess.check_call([
        "python", "../main.py",
        "--batch", str(batch_dir),
        "--pws-pattern", "*_pws.txt",
        "--proposal-pattern", "*_proposal.txt",
        "--requirements-pattern", "*_requirements.txt",
        "--pair-by", "index",
        "--format", "json",
        "--output", str(output_dir_index)
    ])
    
    # Verify pair-by-index results
    assert output_dir_index.exists(), "Batch output directory (index pairing) not created"
    summary_file_index = output_dir_index / "batch_summary.json"
    assert summary_file_index.exists(), "Batch summary file (index pairing) not created"
    
    print("✅ Batch processing with index pairing test passed")

if __name__ == "__main__":
    test_batch_processing()
    print("All batch processing tests passed!")
