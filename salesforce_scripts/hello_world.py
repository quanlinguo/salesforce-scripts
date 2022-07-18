def hello_world():
    print("Hello World")

def get_hello_world():
    return "Hello World!"

def hello_world_with_helper():
    print(hello_world_helper.get_hello_world())

def hello_world_hidden():
    print("Hello World Hidden!")

if __name__ == "__main__":
    hello_world()
    hello_world_with_helper()

    PRINT_SYS_PATH=False
    if PRINT_SYS_PATH: 
        import sys
        for p in sys.path:
            print(p)
