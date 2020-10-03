import re

input_value = 'asfdSFBGgvsDCSDvsv'

"""
 Using two regex to get individual groups
"""

lowercase_regex = re.compile(r'([a-z])')
uppercase_regex = re.compile(r'([A-Z])')

lowercase_group = lowercase_regex.findall(input_value)
uppercase_group = uppercase_regex.findall(input_value)

output_value = ''.join(lowercase_group) + ''.join(uppercase_group)
print(output_value)

"""
Using tuples to compile groups
"""

regex = re.compile(r'([a-z]+)|([A-Z]+)')

output_value_tuple = ([], [])

for match in regex.findall(input_value):
  output_value_tuple[0].append(match[0])
  output_value_tuple[1].append(match[1])

output_value = ''.join(output_value_tuple[0]) + ''.join(output_value_tuple[1])

print(output_value)
