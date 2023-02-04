var='anji'#global variable
def show():
    global var1
    var1='tall'
    print("in func var is",var)
show()
print("outside fun:",var1)
print("var is:",var)
