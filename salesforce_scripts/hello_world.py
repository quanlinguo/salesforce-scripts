from . import hello_world_helper
def hello_world():
    print("Hello World!")

def hello_world_with_helper():
    print(hello_world_helper.get_hello_world())

def hello_world_hidden():
    print("Hello World Hidden!")

if __name__ == "__main__":
    hello_world()
    hello_world_with_helper()
