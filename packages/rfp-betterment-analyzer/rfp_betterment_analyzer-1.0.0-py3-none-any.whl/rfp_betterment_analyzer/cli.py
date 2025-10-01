#!/usr/bin/env python3
"""
Command-line interface for the RFP Betterment Analyzer
"""

import argparse
import os
import sys
import json
import glob
from pathlib import Path
from typing import List, Tuple, Optional, Dict, Any

from .analyzer import OutputFormat, BettermentType, PriorityLevel, ImpactLevel
from .utils import (
    find_file_pairs,
    save_results,
    print_result_summary
)
from .core import BettermentAnalyzer, AnalysisConfig


def main():
    """Command-line interface for the betterment analyzer"""
    parser = argparse.ArgumentParser(description='Analyze proposal text for betterments')
    
    # Input file options
    input_group = parser.add_argument_group('Input Files')
    input_group.add_argument('--pws', help='Path to PWS text file')
    input_group.add_argument('--proposal', help='Path to proposal text file')
    input_group.add_argument('--requirements', help='Path to requirements list file')
    
    # Batch processing options
    batch_group = parser.add_argument_group('Batch Processing')
    batch_group.add_argument('--batch', help='Directory containing multiple PWS/proposal pairs')
    batch_group.add_argument('--pws-pattern', default='*pws*.txt', help='Filename pattern for PWS files')
    batch_group.add_argument('--proposal-pattern', default='*proposal*.txt', help='Filename pattern for proposal files')
    batch_group.add_argument('--requirements-pattern', default='*req*.txt', help='Filename pattern for requirements files')
    batch_group.add_argument('--pair-by', choices=['name', 'index'], default='name', 
                            help='How to pair files - by similar name or index in sorted list')
    batch_group.add_argument('--recursive', action='store_true', help='Search subdirectories recursively')
    
    # Output options
    output_group = parser.add_argument_group('Output')
    output_group.add_argument('--output', help='Path to output file or directory for batch mode')
    output_group.add_argument('--format', default='json', choices=['json', 'text', 'csv', 'html'], 
                             help='Output format (default: json)')
    output_group.add_argument('--summary-only', action='store_true', help='Show only summary results')
    
    # Analysis configuration
    config_group = parser.add_argument_group('Analysis Configuration')
    config_group.add_argument('--confidence', type=float, default=0.5, 
                             help='Minimum confidence threshold (0.0-1.0)')
    config_group.add_argument('--categories', nargs='+', help='Filter betterments by specific categories')
    config_group.add_argument('--priority', choices=['P1', 'P2', 'P3', 'all'], default='all', 
                             help='Filter betterments by priority level')
    config_group.add_argument('--impact', choices=['Low', 'Med', 'High', 'all'], default='all', 
                             help='Filter betterments by impact level')
    
    # Execution options
    exec_group = parser.add_argument_group('Execution')
    exec_group.add_argument('--verbose', action='store_true', help='Enable verbose output')
    exec_group.add_argument('--no-progress', action='store_true', help='Disable progress indicators')
    
    args = parser.parse_args()
    
    # Validate basic arguments
    if not args.batch and (not args.pws or not args.proposal):
        parser.error("Either --batch or both --pws and --proposal must be specified")
    
    # Create config
    config = AnalysisConfig(
        confidence_threshold=args.confidence,
        impact_threshold=ImpactLevel.from_label(args.impact) if args.impact != 'all' else None,
        categories_filter=args.categories,
        priority_filter=[args.priority] if args.priority != 'all' else None,
        use_nlp_matching=True,
        show_progress=not args.no_progress,
        verbose=args.verbose
    )
    
    # Create analyzer
    analyzer = BettermentAnalyzer(config)
    
    # Process either batch mode or single file mode
    if args.batch:
        # Batch processing mode
        if args.verbose:
            print(f"Batch processing mode: Scanning directory {args.batch}")
        
        # Find matching file pairs
        file_pairs = find_file_pairs(
            args.batch, 
            args.pws_pattern, 
            args.proposal_pattern, 
            args.requirements_pattern,
            args.pair_by,
            args.recursive
        )
        
        if not file_pairs:
            print("No matching PWS/proposal pairs found.")
            return 1
            
        if args.verbose:
            print(f"Found {len(file_pairs)} PWS/proposal pairs")
            
        # Create output directory if needed
        if args.output:
            os.makedirs(args.output, exist_ok=True)
        
        # Process each pair
        results_list = []
        success_count = 0
        failed_count = 0
        
        for pws_file, proposal_file, req_file in file_pairs:
            if args.verbose:
                print(f"Processing: PWS={pws_file}, Proposal={proposal_file}, Requirements={req_file}")
            
            try:
                # Read files
                with open(pws_file, 'r', encoding='utf-8') as f:
                    pws_text = f.read()
                    
                with open(proposal_file, 'r', encoding='utf-8') as f:
                    proposal_text = f.read()
                    
                req_text = None
                if req_file:
                    with open(req_file, 'r', encoding='utf-8') as f:
                        req_text = f.read()
                
                # Run analysis
                results = analyzer.analyze_proposal(
                    pws_text, 
                    proposal_text, 
                    req_text
                )
                
                # Add metadata
                results['metadata'] = {
                    'pws_file': pws_file,
                    'proposal_file': proposal_file,
                    'requirements_file': req_file
                }
                
                # Save individual results
                if args.output:
                    output_filename = os.path.basename(proposal_file)
                    output_path = os.path.join(args.output, os.path.splitext(output_filename)[0] + f".{args.format}")
                    save_results(results, output_path, args.format)
                
                results_list.append(results)
                success_count += 1
                
                # Print summary
                if not args.summary_only:
                    print_result_summary(results)
                    print()
                    
            except Exception as e:
                print(f"Error processing {proposal_file}: {e}")
                failed_count += 1
        
        # Create batch summary
        batch_summary = {
            'total': len(file_pairs),
            'success': success_count,
            'failed': failed_count,
            'betterment_count': sum(len(r.get('betterments', [])) for r in results_list),
            'meets_only_count': sum(len(r.get('meets_only', [])) for r in results_list),
            'ambiguous_count': sum(len(r.get('ambiguous', [])) for r in results_list)
        }
        
        # Save batch summary
        if args.output:
            summary_path = os.path.join(args.output, f"batch_summary.json")
            with open(summary_path, 'w', encoding='utf-8') as f:
                json.dump(batch_summary, f, indent=2)
        
        # Print batch summary
        print("\nBatch Processing Summary:")
        print(f"  Total pairs processed: {batch_summary['total']}")
        print(f"  Successfully analyzed: {batch_summary['success']}")
        print(f"  Failed to analyze: {batch_summary['failed']}")
        print(f"  Total betterments found: {batch_summary['betterment_count']}")
        print(f"  Total meets-only items: {batch_summary['meets_only_count']}")
        print(f"  Total ambiguous items: {batch_summary['ambiguous_count']}")
        
    else:
        # Single file mode
        if args.verbose:
            print("Single file processing mode")
        
        # Read input files
        with open(args.pws, 'r', encoding='utf-8') as f:
            pws_text = f.read()
            
        with open(args.proposal, 'r', encoding='utf-8') as f:
            proposal_text = f.read()
            
        requirements_text = None
        if args.requirements:
            with open(args.requirements, 'r', encoding='utf-8') as f:
                requirements_text = f.read()
        
        # Run analysis
        results = analyzer.analyze_proposal(
            pws_text, 
            proposal_text, 
            requirements_text
        )
        
        # Add metadata
        results['metadata'] = {
            'pws_file': args.pws,
            'proposal_file': args.proposal,
            'requirements_file': args.requirements
        }
        
        # Save results if output specified
        if args.output:
            save_results(results, args.output, args.format)
        
        # Print results
        if not args.summary_only:
            if args.output:
                print(f"Results saved to {args.output}")
            else:
                # Print to console if no output file specified
                output_format = OutputFormat.from_string(args.format)
                if output_format == OutputFormat.JSON:
                    print(json.dumps(results, indent=2))
                else:
                    from .utils import format_results_as_text
                    print(format_results_as_text(results))
        
        # Always print summary
        print_result_summary(results)
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
