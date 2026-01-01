import re
text="hello to this cat !"
pattern=r"this"

match=re.search(pattern,text)
if match:
    print("it is match")
else:
    print("not match")     