# Illumio_technical_assessment

## Overview

This project solves Illumio's technical assessment by parsing flow log data, mapping each log entry to tags using a lookup table, and generating summary reports:

1. **Tag Counts**: Counts of matches for each tag, including unmatched entries labeled as "Untagged."
2. **Port/Protocol Combination Counts**: Counts of occurrences for each destination port and protocol combination.

The program is implemented in Python and ensures outputs are clear and easy to verify.

---

## Features

- Reads flow log data and lookup table from input files.
- Maps destination ports and protocols to tags using a case-insensitive lookup.
- Generates output files for:
  - Tag counts.
  - Port/protocol combination counts.
- Handles up to 10 MB of flow log data and 10,000 lookup table mappings.
- Gracefully ignores malformed or missing data.

---

## Project Structure

## Assumptions

- **Flow Logs**: The program only supports the default format (version 2).
- **Protocol Mapping**: Protocol numbers in flow logs are converted to names (e.g., `6` → `tcp`, `17` → `udp`) using a predefined mapping.
- **Case-Insensitive Matching**: Protocol and tag matching is case-insensitive.
- **Error Handling**: Malformed or incomplete rows in input files are ignored.

---

## Installation

### Prerequisites

- Python 3.x installed on your system.
- No additional dependencies required.

### Setup

1. Clone this repository:
   ```bash
   git clone <>
   cd illumio-assessment
   ```

Ensure the required input files (flow_logs.txt and lookup_table.csv) are in the input/ directory.
How to Run
Execute the program from the root directory:
python3 src/flow_log_parser.py
Output files will be generated in the output/ directory:
tag_counts.csv: Counts of matches for each tag and unmatched entries.
port_protocol_counts.csv: Counts for each port/protocol combination.

Testing
The tests/ folder contains sample test cases for validation.

Files
test_flow_logs.txt: Sample flow logs for testing.
test_lookup_table.csv: Sample lookup table for testing.
test_expected_tags.csv: Expected output for tag counts.
test_expected_ports.csv: Expected output for port/protocol counts.
Steps to Test
Replace the files in the input/ directory with test_flow_logs.txt and test_lookup_table.csv from the tests/ folder.
Run the program:

python3 src/flow_log_parser.py
Compare the generated files in output/ with the expected files:
test_expected_tags.csv
test_expected_ports.csv
Known Limitations
Only supports default flow log format (version 2).
No support for custom log formats or dynamic protocol mappings.
Contact
If you have any questions or need further assistance, feel free to contact me at [roopasree2509@gmail.com].
