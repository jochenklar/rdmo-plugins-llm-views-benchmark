import json

from config import JSON_PATH
from tabulate import tabulate

rows = []
for file_path in sorted(JSON_PATH.glob('**/*.json')):
    row_data = json.loads(file_path.read_text())

    if row_data:
        row = {
            'Provider': file_path.parts[1],
            'Model': file_path.with_suffix('').parts[2],
        }

        for key in (
            'Elapsed time',
            'Input tokens',
            'Output tokens',
            'Total tokens',
        ):
            row[key] = row_data[key] if 'error' not in row_data else '-'

        row['Quality'] = '' if 'error' not in row_data else 'Error'

        rows.append(row)

print(tabulate(rows, headers='keys', tablefmt='github'))
