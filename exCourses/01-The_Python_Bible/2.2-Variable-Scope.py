
# global and local variable scopes


a=[3,6,9]         #Global scope
b=369          #Global scope


def f1():
    print('Global Scope=', a)      #Global Scope
f1()
#Global Scopes are global & remains same everywhere untill and unless you reassign it !


def f2():
    a=666     #Local Scope
    print('Local Scope=', a)
f2()
#Local Scopes are Genrated by Python & will destroyed after the function() ends !


def f3():
    a[0]=33       #Changing One Element Of Global Scope without using global key
    print('Changed First Element Of Global Scope ; ',a)
f3()


def f4():
    global a      #Using Global Scope
    a=999             #Changing global scope's variable value
    print('Updated Global Scope using global keyword=', a)
f4()


print('Global Scope; ',a)



