var = input("Enter a variable data: ")
try:
    var = eval(var)
except:
    pass
print("Data type of the variable is:", type(var))
