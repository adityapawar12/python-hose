import os

for a, b, c in os.walk('./puzzle-extract/extracted_content'):
    print(f'{a} \n {b} \n {c}')
