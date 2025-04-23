import re

text = "This is the sample text, which have the beautiful context."

result = re.search("beautiful", text)

print(result.span())

result = re.findall("the", text)
print(result)

result = re.sub("have", "has", text)
print(result)
