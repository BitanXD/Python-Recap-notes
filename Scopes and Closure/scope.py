username = "Pudding"
email = "pudding@gmail.com"
def func():
    # username = "Bitan"
    print(username) # Bitan
    # if the func username variable is commented then the ouput is Pudding that means that func function takes the global scope variable

    # global keyword
    # over-writing a global varaible is not a good practice
    global email
    email = "bitan@gmail.com"

func()
print(username)  # Pudding
print(email) # bitan@gmail.com

value = 10
def f1():
    value = 20
    def f2():
        print(value)    # 20
                        # 10 when f1 value is commented
    # f2()
    return f2
myResult = f1()
myResult()



# scope and closure
def pudding(num):
    def calculate(value):
        return value ** num
    return calculate

ref1 = pudding(2) # num value is passed and ref1 has the calculate function reference

print(ref1(3)) # ref1 passes the value and function is executed