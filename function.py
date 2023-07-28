def announce(f):
    def wrapper():
        print("about to bust")
        f()
        print("i busted")
    return wrapper

@announce
def hello():
    print("hi bitch")

hello()