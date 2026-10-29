import re

text ="The quick brown fox jumps over the lazy brown dog"
pattern = r"brown"

replace = "red"

new_text = re.sub(pattern, replace,text)
print("Modified text:", new_text)