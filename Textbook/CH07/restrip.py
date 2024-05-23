def custom_strip(string, chars=None):
    if chars is None:
        return string.strip()
    else:
        return string.strip(chars)

text = "   Hello, world!   "
print(custom_strip(text))

text_with_chars = "---Hello, world!---"
print(custom_strip(text_with_chars, '-'))

 
