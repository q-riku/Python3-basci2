def say_hello(name):
    print("Hello, " + name)
if __name__ == "__main__":
    while True:
        name = input("What's your name：")
        say_hello(name)