def greet(name):
    print("Hi " + name + "!")
    greet2(name)
    print("Preparing to say goodbye")
    bye(name)


def greet2(name):
    print("How are you " + name + "?")


def bye(name):
    print("Goodbye " + name + "!")


greet("Mateus")
