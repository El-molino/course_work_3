import os

from src.functions import sort_data, read_json, final_output

sorted_list = sort_data(read_json(os.path.join(os.path.dirname(__file__), 'operations.json')))
for item in sorted_list[0:5]:
    print(final_output(item))
    print()