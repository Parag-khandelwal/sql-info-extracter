# SQL Info Extractor

## Overview
The SQL Info Extractor is a Python script designed to extract useful information from SQL files, such as table names, column names, stored procedures, and comments. The extracted data is then saved into a JSON file for easy access and further processing.

## Features
- **Table Extraction**: Identifies all tables involved in the SQL queries (`FROM`, `JOIN`).
- **Column Extraction**: Extracts all column names specified in the `SELECT` statements.
- **Procedure Extraction**: Detects stored procedures within the SQL file.
- **Comment Extraction**: Captures and removes comments for a cleaner data extraction process.
- **JSON Output**: The extracted data is saved in a structured JSON format.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Parag-khandelwal/sql-info-extracter.git
    cd sql-info-extractor
    ```

2. **Create a virtual environment (optional but recommended)**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install dependencies**:
    The script uses standard Python libraries, so no additional dependencies are required.

## Usage

### Command Line Interface (CLI)
To extract SQL information from a file and save it as JSON, run the following command:

```bash
python extractor.py <sql_file>
