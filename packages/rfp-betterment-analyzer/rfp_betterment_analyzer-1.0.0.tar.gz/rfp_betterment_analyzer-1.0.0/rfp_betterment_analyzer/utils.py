#!/usr/bin/env python3
"""
Utility functions for RFP Betterment Analyzer
"""

import os
import json
import glob
import fnmatch
import csv
import difflib
from pathlib import Path
from typing import List, Tuple, Optional, Dict, Any, Union

from .analyzer import OutputFormat


def format_results_as_text(results: dict) -> str:
    """Format analysis results as readable text
    
    Args:
        results: Analysis results dictionary
        
    Returns:
        Formatted text output
    """
    output = []
    
    # Add metadata if available
    if 'metadata' in results:
        output.append("# Analysis Metadata")
        output.append(f"PWS File: {results['metadata'].get('pws_file', 'Unknown')}")
        output.append(f"Proposal File: {results['metadata'].get('proposal_file', 'Unknown')}")
        if results['metadata'].get('requirements_file'):
            output.append(f"Requirements File: {results['metadata']['requirements_file']}")
        output.append("")
    
    # Add betterments
    output.append("# Betterments")
    output.append(f"Found {len(results.get('betterments', []))} betterments:")
    output.append("")
    
    for i, betterment in enumerate(results.get('betterments', []), 1):
        output.append(f"## Betterment {i}: {betterment['title']}")
        output.append(f"Requirement: {betterment['req_id']}")
        output.append(f"Baseline: {betterment['baseline_requirement']}")
        output.append(f"Betterment: {betterment['betterment_text']}")
        output.append(f"Categories: {', '.join(betterment['betterment_types'])}")
        output.append(f"Justification: {betterment['justification']}")
        output.append(f"Confidence: {betterment['confidence']:.2f}")
        output.append(f"Impact: {betterment['impact']}")
        output.append(f"Priority: {betterment['priority']}")
        output.append("")
    
    # Add meets-only items
    if 'meets_only' in results and results['meets_only']:
        output.append("# Meets-Only Items")
        output.append(f"Found {len(results['meets_only'])} items that only meet requirements:")
        output.append("")
        
        for i, item in enumerate(results['meets_only'], 1):
            output.append(f"## Meets-Only {i}")
            output.append(f"Requirement: {item['req_id']}")
            output.append(f"Baseline: {item['baseline_requirement']}")
            output.append(f"Proposal: {item['proposal_text']}")
            output.append(f"Explanation: {item['justification']}")
            output.append("")
    
    # Add ambiguous items
    if 'ambiguous' in results and results['ambiguous']:
        output.append("# Ambiguous Items")
        output.append(f"Found {len(results['ambiguous'])} items that need clarification:")
        output.append("")
        
        for i, item in enumerate(results['ambiguous'], 1):
            output.append(f"## Ambiguous {i}")
            output.append(f"Requirement: {item['req_id']}")
            output.append(f"Baseline: {item['baseline_requirement']}")
            output.append(f"Proposal: {item['proposal_text']}")
            output.append(f"Missing Details: {item['missing_details']}")
            output.append("")
    
    # Add requirements list
    output.append("# Requirements")
    output.append(f"Found {len(results.get('requirements', []))} requirements:")
    output.append("")
    
    for i, req in enumerate(results.get('requirements', []), 1):
        output.append(f"## Requirement {i}: {req['req_id']}")
        output.append(f"{req['text']}")
        if req.get('source_para'):
            output.append(f"Source: {req['source_para']}")
        output.append("")
    
    return "\n".join(output)


def export_to_csv(results: dict, output_path: str) -> None:
    """Export analysis results to CSV format
    
    Args:
        results: Analysis results dictionary
        output_path: Path to save the CSV file
    """
    base_path = os.path.splitext(output_path)[0]
    
    # Export betterments
    if results.get('betterments'):
        betterments_path = f"{base_path}_betterments.csv"
        with open(betterments_path, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['title', 'req_id', 'baseline_requirement', 'betterment_text',
                        'betterment_types', 'justification', 'confidence', 'impact', 'priority']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            for b in results['betterments']:
                row = {
                    'title': b['title'],
                    'req_id': b['req_id'],
                    'baseline_requirement': b['baseline_requirement'],
                    'betterment_text': b['betterment_text'],
                    'betterment_types': ', '.join(b['betterment_types']),
                    'justification': b['justification'],
                    'confidence': b['confidence'],
                    'impact': b['impact'],
                    'priority': b['priority']
                }
                writer.writerow(row)
    
    # Export meets-only
    if results.get('meets_only'):
        meets_path = f"{base_path}_meets_only.csv"
        with open(meets_path, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['req_id', 'baseline_requirement', 'proposal_text', 'justification']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            for m in results['meets_only']:
                writer.writerow(m)
    
    # Export ambiguous
    if results.get('ambiguous'):
        ambig_path = f"{base_path}_ambiguous.csv"
        with open(ambig_path, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['req_id', 'baseline_requirement', 'proposal_text', 'missing_details']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            for a in results['ambiguous']:
                writer.writerow(a)


def export_to_html(results: dict, output_path: str) -> None:
    """Export analysis results to HTML format
    
    Args:
        results: Analysis results dictionary
        output_path: Path to save the HTML file
    """
    html = []
    
    # HTML header
    html.append("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>RFP Betterment Analysis</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        .betterment { background-color: #d4edda; }
        .meets-only { background-color: #fff3cd; }
        .ambiguous { background-color: #f8d7da; }
        .requirement { background-color: #e2e3e5; }
        .p1 { border-left: 5px solid #198754; }
        .p2 { border-left: 5px solid #0d6efd; }
        .p3 { border-left: 5px solid #6c757d; }
        .high-impact { font-weight: bold; }
        .medium-impact { font-weight: normal; }
        .low-impact { font-weight: lighter; }
        .card { margin-bottom: 1rem; }
    </style>
</head>
<body>
    <div class="container mt-4">
        <h1 class="mb-4">RFP Betterment Analysis</h1>
""")
    
    # Add metadata if available
    if 'metadata' in results:
        html.append('<div class="card mb-4">')
        html.append('<div class="card-header">Analysis Metadata</div>')
        html.append('<div class="card-body">')
        html.append(f'<p><strong>PWS File:</strong> {results["metadata"].get("pws_file", "Unknown")}</p>')
        html.append(f'<p><strong>Proposal File:</strong> {results["metadata"].get("proposal_file", "Unknown")}</p>')
        if results["metadata"].get("requirements_file"):
            html.append(f'<p><strong>Requirements File:</strong> {results["metadata"]["requirements_file"]}</p>')
        html.append('</div></div>')
    
    # Add betterments
    html.append('<h2 class="mt-4">Betterments</h2>')
    html.append(f'<p>Found {len(results.get("betterments", []))} betterments:</p>')
    
    for betterment in results.get('betterments', []):
        priority_class = betterment['priority'].lower()
        impact_class = f"{betterment['impact'].lower()}-impact"
        
        html.append(f'<div class="card betterment {priority_class}">')
        html.append('<div class="card-header d-flex justify-content-between align-items-center">')
        html.append(f'<div><strong>{betterment["title"]}</strong></div>')
        html.append(f'<div class="badge bg-success">{betterment["priority"]}</div>')
        html.append('</div>')
        html.append('<div class="card-body">')
        html.append(f'<p><strong>Requirement:</strong> {betterment["req_id"]}</p>')
        html.append(f'<p><strong>Baseline:</strong> {betterment["baseline_requirement"]}</p>')
        html.append(f'<p><strong>Betterment:</strong> {betterment["betterment_text"]}</p>')
        html.append(f'<p><strong>Categories:</strong> {", ".join(betterment["betterment_types"])}</p>')
        html.append(f'<p><strong>Justification:</strong> {betterment["justification"]}</p>')
        html.append(f'<p><strong>Confidence:</strong> {betterment["confidence"]:.2f}</p>')
        html.append(f'<p><strong>Impact:</strong> {betterment["impact"]}</p>')
        html.append('</div></div>')
    
    # Add meets-only items
    if 'meets_only' in results and results['meets_only']:
        html.append('<h2 class="mt-4">Meets-Only Items</h2>')
        html.append(f'<p>Found {len(results["meets_only"])} items that only meet requirements:</p>')
        
        for item in results['meets_only']:
            html.append('<div class="card meets-only">')
            html.append('<div class="card-header">Meets-Only</div>')
            html.append('<div class="card-body">')
            html.append(f'<p><strong>Requirement:</strong> {item["req_id"]}</p>')
            html.append(f'<p><strong>Baseline:</strong> {item["baseline_requirement"]}</p>')
            html.append(f'<p><strong>Proposal:</strong> {item["proposal_text"]}</p>')
            html.append(f'<p><strong>Explanation:</strong> {item["justification"]}</p>')
            html.append('</div></div>')
    
    # Add ambiguous items
    if 'ambiguous' in results and results['ambiguous']:
        html.append('<h2 class="mt-4">Ambiguous Items</h2>')
        html.append(f'<p>Found {len(results["ambiguous"])} items that need clarification:</p>')
        
        for item in results['ambiguous']:
            html.append('<div class="card ambiguous">')
            html.append('<div class="card-header">Ambiguous</div>')
            html.append('<div class="card-body">')
            html.append(f'<p><strong>Requirement:</strong> {item["req_id"]}</p>')
            html.append(f'<p><strong>Baseline:</strong> {item["baseline_requirement"]}</p>')
            html.append(f'<p><strong>Proposal:</strong> {item["proposal_text"]}</p>')
            html.append(f'<p><strong>Missing Details:</strong> {item["missing_details"]}</p>')
            html.append('</div></div>')
    
    # Add requirements
    html.append('<h2 class="mt-4">Requirements</h2>')
    html.append(f'<p>Found {len(results.get("requirements", []))} requirements:</p>')
    
    html.append('<div class="accordion" id="requirementsAccordion">')
    for i, req in enumerate(results.get('requirements', [])):
        html.append(f'<div class="accordion-item requirement">')
        html.append(f'<h2 class="accordion-header" id="heading{i}">')
        html.append(f'<button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapse{i}">')
        html.append(f'{req["req_id"]}')
        html.append('</button></h2>')
        html.append(f'<div id="collapse{i}" class="accordion-collapse collapse" data-bs-parent="#requirementsAccordion">')
        html.append('<div class="accordion-body">')
        html.append(f'<p>{req["text"]}</p>')
        if req.get('source_para'):
            html.append(f'<p><small>Source: {req["source_para"]}</small></p>')
        html.append('</div></div></div>')
    html.append('</div>')
    
    # HTML footer
    html.append("""
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
""")
    
    # Write to file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(html))


def find_file_pairs(directory, pws_pattern, proposal_pattern, requirements_pattern, pair_by='name', recursive=False):
    """Find matching PWS, proposal, and requirements files in a directory
    
    Args:
        directory: Directory to search for files
        pws_pattern: Glob pattern for PWS files
        proposal_pattern: Glob pattern for proposal files
        requirements_pattern: Glob pattern for requirements files
        pair_by: How to pair files ('name' or 'index')
        recursive: Whether to recursively search subdirectories
        
    Returns:
        List of tuples (pws_file, proposal_file, requirements_file)
    """
    # Convert to absolute path
    directory = os.path.abspath(directory)
    
    # Find files matching patterns
    if recursive:
        pws_files = []
        proposal_files = []
        req_files = []
        
        for root, _, files in os.walk(directory):
            for file in files:
                abs_path = os.path.join(root, file)
                rel_path = os.path.relpath(abs_path, directory)
                
                if fnmatch.fnmatch(file, pws_pattern):
                    pws_files.append(abs_path)
                elif fnmatch.fnmatch(file, proposal_pattern):
                    proposal_files.append(abs_path)
                elif fnmatch.fnmatch(file, requirements_pattern):
                    req_files.append(abs_path)
    else:
        pws_files = glob.glob(os.path.join(directory, pws_pattern))
        proposal_files = glob.glob(os.path.join(directory, proposal_pattern))
        req_files = glob.glob(os.path.join(directory, requirements_pattern))
    
    # Sort files
    pws_files.sort()
    proposal_files.sort()
    req_files.sort()
    
    # Pair files
    pairs = []
    
    if pair_by == 'index':
        # Pair by index in sorted lists
        for i in range(min(len(pws_files), len(proposal_files))):
            pws = pws_files[i]
            proposal = proposal_files[i]
            req = req_files[i] if i < len(req_files) else None
            pairs.append((pws, proposal, req))
    else:
        # Pair by name similarity
        for proposal in proposal_files:
            proposal_base = os.path.basename(proposal)
            best_pws = None
            best_pws_score = 0
            best_req = None
            best_req_score = 0
            
            # Find best matching PWS
            for pws in pws_files:
                pws_base = os.path.basename(pws)
                score = difflib.SequenceMatcher(None, proposal_base, pws_base).ratio()
                if score > best_pws_score:
                    best_pws = pws
                    best_pws_score = score
            
            # Find best matching requirement
            for req in req_files:
                req_base = os.path.basename(req)
                score = difflib.SequenceMatcher(None, proposal_base, req_base).ratio()
                if score > best_req_score:
                    best_req = req
                    best_req_score = score
            
            if best_pws:
                pairs.append((best_pws, proposal, best_req if best_req_score > 0.5 else None))
    
    return pairs


def print_result_summary(results):
    """Print a summary of analysis results"""
    print("\nAnalysis Summary:")
    print(f"  Requirements: {len(results.get('requirements', []))}")
    print(f"  Betterments: {len(results.get('betterments', []))}")
    print(f"  Meets-only: {len(results.get('meets_only', []))}")
    print(f"  Ambiguous: {len(results.get('ambiguous', []))}")
    
    # Print priority distribution
    priority_counts = {'P1': 0, 'P2': 0, 'P3': 0}
    for betterment in results.get('betterments', []):
        priority_counts[betterment['priority']] += 1
    
    print("\nBetterment Priority Distribution:")
    print(f"  P1 (Highest): {priority_counts['P1']}")
    print(f"  P2 (Medium): {priority_counts['P2']}")
    print(f"  P3 (Lower): {priority_counts['P3']}")


def save_results(results, output_file, format_type):
    """Save results to file in the specified format
    
    Args:
        results: Analysis results dictionary
        output_file: Path to save the results
        format_type: Format to use (json, text, csv, html)
    """
    os.makedirs(os.path.dirname(os.path.abspath(output_file)), exist_ok=True)
    
    output_format = OutputFormat.from_string(format_type)
    
    if output_format == OutputFormat.JSON:
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2)
            
    elif output_format == OutputFormat.TEXT:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(format_results_as_text(results))
            
    elif output_format == OutputFormat.CSV:
        export_to_csv(results, output_file)
        
    elif output_format == OutputFormat.HTML:
        export_to_html(results, output_file)
