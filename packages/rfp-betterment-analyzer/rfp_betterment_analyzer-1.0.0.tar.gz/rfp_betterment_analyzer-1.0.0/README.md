# RFP Betterment Analyzer

A command-line tool to evaluate proposal content and identify elements that qualify as betterments for U.S. Government RFP responses.

## Overview

This tool analyzes proposal content against baseline requirements from a Performance Work Statement (PWS) to identify and classify features that exceed the government's stated requirements. These "betterments" are categorized, scored, and prioritized to highlight the most impactful additions in your proposal.

## Definition of Betterment

A **betterment** is any solution feature that:
- Exceeds or enhances the government's stated requirement
- Goes beyond what is required in the solicitation
- Delivers meaningful improvements to the goals underlying the needed work

## Features

- Parses requirements from PWS text and/or explicit requirements lists
- Identifies candidate betterments in proposal text
- Classifies betterments into 10 different categories
- Scores betterments based on confidence, impact, and priority
- Distinguishes between betterments and mere compliance (meets-only)
- Flags ambiguous items that need more detail
- Provides justification with evidence for each betterment

## Security

**"RFP Betterment Analyzer: Where Your Sensitive Data Never Leaves Home"**

The RFP Betterment Analyzer is designed with security in mind for handling sensitive proposal data:

- **100% Local Processing**: All analysis runs entirely on your machine - no data is sent to external servers
- **Zero Cloud Connections**: No API keys, no external dependencies, no mysterious "black box" processing
- **Complete Data Control**: Your proprietary content, pricing strategies, and technical innovations remain private
- **Transparent Analysis**: Open-source pipeline that you can audit yourself
- **Perfect For**: Classified environments, competitive proposals, and situations where data sovereignty is non-negotiable

Because winning more contracts shouldn't mean risking your most valuable information.

## Installation

Ensure you have Python installed (version 3.8 or higher is recommended).

```bash
pip install -r requirements.txt
```

The tool uses the following external libraries:
- NLTK for natural language processing
- scikit-learn for text matching and similarity
- pandas for data manipulation
- tqdm for progress indicators

## Usage

### Command Line

```bash
python main.py --pws path/to/pws.txt --proposal path/to/proposal.txt [OPTIONS]
```

### Basic Arguments

- `--pws`: Path to the PWS text file (required)
- `--proposal`: Path to the proposal text file (required)
- `--requirements`: Path to a requirements list file (optional)
- `--output`: Path to save the output file (optional)

### Output Options

- `--format`: Output format: json, text, csv, or html (default: json)
- `--summary-only`: Show only summary results, not detailed output

### Analysis Configuration

- `--confidence`: Minimum confidence threshold (0.0-1.0) for betterments (default: 0.5)
- `--categories`: Filter betterments by specific categories (can specify multiple)
- `--priority`: Filter betterments by priority level: P1, P2, P3, or all (default: all)
- `--impact`: Filter betterments by impact level: Low, Med, High, or all (default: all)

### Execution Options

- `--verbose`: Enable verbose output with detailed logging
- `--no-progress`: Disable progress indicators during analysis

### Input Formats

1. **PWS_Baseline**: Plain text of the Performance Work Statement.
2. **Requirements_List** (optional): A text file with requirements in the format:
   ```
   REQ-1: System must provide 99.5% uptime.
   REQ-2: Data must be encrypted at rest using AES-256.
   ```
3. **Proposal_Text**: Plain text of the proposal section to evaluate.

### Example

```bash
python main.py --pws examples\sample_pws.txt --proposal examples\sample_proposal.txt --requirements examples\sample_requirements.txt
```

## Output

The tool generates JSON output with the following sections:
- `betterments`: List of identified betterments with details
- `meets_only`: List of features that meet but don't exceed requirements
- `ambiguous`: List of potential betterments needing more detail
- `requirements`: List of all parsed requirements

For each betterment, the tool provides:
- Title
- Associated requirement ID
- Baseline requirement text
- Betterment text from the proposal
- Betterment categories
- Justification of how it exceeds the baseline
- Confidence score (0-1)
- Impact assessment (Low/Med/High)
- Priority level (P1/P2/P3)

## Betterment Categories

1. **Performance/Quality**: Exceeds performance metrics, quality standards, or precision requirements
2. **Security/Compliance**: Provides security features beyond minimum compliance requirements
3. **Cost/Value/TCO**: Offers cost savings or additional value beyond requirements
4. **Schedule/Speed**: Delivers faster implementation or response times than required
5. **Reliability/Availability**: Exceeds uptime or availability requirements
6. **Scalability/Capacity**: Provides higher capacity or better scalability than required
7. **Risk Reduction**: Offers additional risk mitigation beyond requirements
8. **User Experience/Accessibility**: Enhances user experience or accessibility beyond requirements
9. **Maintainability/Operability**: Improves ease of maintenance or operation
10. **Innovation/Modernization**: Introduces innovative or modern approaches beyond requirements

## Decision Process

A feature is classified as a betterment if:
1. It **exceeds** a baseline requirement (not just meets it)
2. The improvement is **meaningful** and advances PWS objectives
3. The claim is **verifiable** with metrics, standards, or benchmarks

## Project Structure

```
rfp_betterment_analyzer/
├── main.py               # Main script with the betterment analyzer logic
├── requirements.txt      # Dependencies (none required beyond standard library)
├── README.md             # This documentation file
└── examples/             # Example input files
    ├── sample_pws.txt              # Sample Performance Work Statement
    ├── sample_requirements.txt     # Sample requirements list
    └── sample_proposal.txt         # Sample proposal text
```

## Future Enhancements

Potential future enhancements include:
- Web-based user interface
- Integration with proposal management tools
- Support for PDF input files
- Enhanced NLP for more accurate requirement matching
- Export options for proposal teams
