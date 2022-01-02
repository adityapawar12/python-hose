"""
    USING OS AND SHUTIL FOR WORKING WITH FILES.
"""

import os
import shutil

test = open('test.txt', 'w+')
test.write('this is jus the test text.')
test.close()

print(os.getcwd())
print(os.listdir())

shutil.move('test.txt', '/home/aditya/')
shutil.move('/home/aditya/test.txt', os.getcwd())

os.unlink('test.txt')

for folder, subfolder, files in os.walk('./ex-top-level'):
    
    print(f'Currently looking at: {folder}')
    
    print('\n')
    print('The subfolders are.')
    for sub_fold in subfolder:
        print(f'\t Subfolder : {sub_fold}')

    print('\n')
    print('The files are.')
    for f in files:
        print(f'\t File : {f}')

    print('\n')
