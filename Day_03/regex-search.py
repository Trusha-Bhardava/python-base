import re
text="hello to this cat !"
pattern= "this"

match=re.search(pattern,text)
if match:
    print("it is match")
else:
    print("not match")     