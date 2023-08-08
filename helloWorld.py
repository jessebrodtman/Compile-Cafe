s = """all ivies minus dartmouth, mit, stanford, cmu, gtech, uf, UCs (i applied cs for those), vandy, rice, fsu, uchic, duke, nyu, caltech"""

for line in s.split(','):
    if line!='arrow_drop_down': print(line)