def doubles_input(i):
    print(i)
    print(i)
doubles_input('hello')

def is_short(i):
    if len(i) > 10:
        print("That's long!")
    elif len(i) == 10:
        print("It's 10!")
    else:
        print("That's short!")
is_short('hello')

def counting(first, second):
    while first <= second:
        print(first)
        first += 1
counting(5, 8)

def double_each(alist):
    _=[]
    for i in alist:
        _.append(i*2)
    return _
print(double_each([1,2,3,4,5]))