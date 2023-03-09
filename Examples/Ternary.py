# USING TERNARY OPERATOR
to_check = 6
msg = "Even" if to_check%2 == 0 else "Odd"
print(msg) 

# USING USUAL IF-ELSE
msg = ""
if(to_check%2 == 0):
  msg = "Even"
else:
  msg = "Odd"
print(msg)