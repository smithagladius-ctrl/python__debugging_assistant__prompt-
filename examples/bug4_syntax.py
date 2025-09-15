# Bug: Logical condition uses 'and' instead of 'or'
# Expected: detect x out of range (x < 0 OR x > 10)
# Actual: always prints "x is valid" for most numbers

x = 5
if x < 0 and x > 10:
    print("x is out of range")
else:
    print("x is valid")
