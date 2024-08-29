import re
import json
import sys
import logging

# Set up logging
logging.basicConfig(
    filename="extractor.log",
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='utf-8'
)
logger = logging.getLogger(__name__)


logger.info("Writing function to extract SQL info from SQL files")
def extract_sql_info(sql_file_path):
    """Extract SQL file information using Regular Expressions.
    
    Args:
        sql_file_path (str): Path to the SQL file.

    Returns:
        dict: Extracted SQL information containing tables, columns,
              procedures, and comments.
    """

    table_pattern = re.compile(r'\bFROM\s+(\w+)|\bJOIN\s+(\w+)', re.IGNORECASE)
    column_pattern = re.compile(r'\bSELECT\s+(.*?)\s+FROM', re.IGNORECASE)
    procedure_pattern = re.compile(r'\bPROCEDURE\s+(\w+)', re.IGNORECASE)
    comment_pattern = re.compile(r'--.*?$|/\*.*?\*/', re.DOTALL | re.MULTILINE)

    sql_info = {
        'tables': [],
        'columns': [],
        'procedures': [],
        'comments': []
    }

    try:
        with open(sql_file_path, 'r') as sql_file:
            content = sql_file.read()

            # Extract and remove comments
            comments = comment_pattern.findall(content)
            sql_info['comments'].extend(comments)
            content = comment_pattern.sub('', content)

            # Extract tables
            tables = table_pattern.findall(content)
            all_tables = {table for pair in tables for table in pair if table}
            sql_info['tables'].extend(list(all_tables))

            # Extract columns
            columns = column_pattern.findall(content)
            cols_cleaned = [col.strip() for col_group in columns
                            for col in re.split(r',\s*', col_group)]
            sql_info['columns'].extend(list(set(cols_cleaned)))

            # Extract procedures
            procedures = procedure_pattern.findall(content)
            sql_info['procedures'].extend(procedures)

    except FileNotFoundError as e:
        logger.error(f'An error occurred: {e}')
        print(f'Error: {e}')
        return None

    logger.info("Successfully extracted all information from SQL file")
    return sql_info


def save_as_json(data, output_file_name):
    """Save data as a JSON file.
    
    Args:
        data (dict): Data to be saved.
        output_file_name (str): Name of the output JSON file.
    """

    try:
        with open(output_file_name, 'w') as json_file:
            json.dump(data, json_file, indent=4)
        logger.info(f"SQL data saved to {output_file_name} successfully!")
        print(f'SQL data saved to {output_file_name} successfully!')

    except Exception as e:
        logger.error(f'An error occurred: {e}')
        print(f'Error: {e}')


def main():
    if len(sys.argv) != 2:
        print('USAGE: python extractor.py <sql_file>')
        sys.exit(1)

    sql_file = sys.argv[1]
    output_file = sql_file.replace('.sql', '.json')

    sql_info = extract_sql_info(sql_file)
    if sql_info:
        save_as_json(sql_info, output_file)


if __name__ == "__main__":
    main()
