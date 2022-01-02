import re

text = "The phone number is 503-348-3539. call on this phone."
print('phone' in text)

pattern = 'phone'

match = re.search(pattern, text)
matches = re.findall(pattern, text)

print(match)
print(match.span())
print(match.start())
print(match.end())
print(matches)

for m in re.finditer(pattern, text):
    print(m)
    print(m.span())
    print(m.group())

# re_match = re.search(r'\d\d\d-\d\d\d-\d\d\d\d', text)
re_match = re.search(r'\d{3}-\d{3}-\d{4}', text)
print(re_match)

phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
results = re.search(phone_pattern, text)

print(results)
print(results.group())
print(results.group(2))

print(re.search(r'cat|dog', 'this will have cat'))
print(re.findall(r'.at', 'this hat is not a bat.'))
print(re.search(r'^\d', '1 starts with number.'))
print(re.search(r'\d$', 'ends with number 1'))
print(re.findall(r'[^\d]+', 'this 1 sentence had 2 three numbers 3.'))
print(re.findall(r'[^!.,?]+', 'this ! sentence . will , remove symbols ?')) 
