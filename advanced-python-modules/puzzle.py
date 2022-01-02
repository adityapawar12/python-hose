import shutil
import os
import re

shutil.unpack_archive('unzip_me_for_instructions.zip', 'puzzle-extract', 'zip')

with open('./puzzle-extract/extracted_content/Instructions.txt') as f:
    content = f.read()
    print(content)

print('\n')

for path, sub_folders, files in os.walk('./puzzle-extract/extracted_content'):
    for f in files:
        fi = open(f'{path}/{f}', 'r')
        fr = fi.read()
        result = re.search(r'\d{3}-\d{3}-\d{4}', fr)
        if result != None:
            print(f'THE NUMBER {result.group()} FOUND INSIDE FILE {f} WHICH IS IN {path}.')
