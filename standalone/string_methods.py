text = "This is a sample text"
# text[1] = 'R' | Strings are immutable. TypeError: 'str' object does not support item assignment.
print(text)

print(text.upper(), text, sep=" Transform from ", end=".\n")
print(text.lower(), text, sep=" Transform from ", end=".\n")
print(text.capitalize(), text, sep=" Transform from ", end=".\n")
print(text.title(), text, sep=" Transform from ", end=".\n")

# strip will remove start and end space and new lines.
text = "\n Text with space around \n"
print(text)

print(text.lstrip())
print(text.rstrip())
print(text.strip())

# find and replace
text = "Sample text"
print(text.find("text"))
print(text.replace("Sample", "New")) # only replace not assign to the variable.
print(text)
print(text.find("Sample"))

# split and join
text = "A,B,C,D"
print(text)

print(text.split(','))
print(', '.join(['A','B','C','D']))

# check string
text = "AlphaNumericText123456"

print(text.isalpha()) # check if the string contain only alphabets?
print(text.isdigit()) # check if the string contain only digits?
print(text.isalnum()) # check if the string contain both alphabets and digits?
print(text.isspace()) # check if the string contain only space?

# ord and chr
print(ord("A")) #65
print(chr(66)) #B
print(ord("a")) #97
print(chr(99)) #c

# format
text = "User name is {}. He is {} years old."
print(text)

name = "Pallab Roy"
age = 25

print(text.format(name, age))
print(f"User name is {name}. He is {age} years old.")