import re
txt="i love python ,i love regex"
x='love(?=\s regex)'
match1=re.search(x,txt)
print(match1)