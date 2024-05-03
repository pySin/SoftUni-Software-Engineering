# Scope Mess

x = "global"


def outer():
    x = "local"

    def inner():
        x = "nonlocal"
        print("inner:", x)
        return x

    def change_global():
        # global x
        x = "global: changed!"
        return x

    print("outer:", x)
    x = inner()
    print("outer:", x)
    x = change_global()
    return x


print(x)
x = outer()
print(x)
