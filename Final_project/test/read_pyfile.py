import re

usd_name = 'name'

with open('/libs/hou_lib/post_render_pre_input.py', 'r') as original_file:
    file_contents = original_file.read()

modified_contents = re.sub(r'input', usd_name, file_contents)

with open('/libs/hou_lib/post_render.py', 'w') as new_file:
    new_file.write(modified_contents)
