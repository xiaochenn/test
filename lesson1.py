import re


result = re.search('(1)(3)',"133")
list = []
list.append(result.group(1))
print(type(result.group(1)))
print(list)