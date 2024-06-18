stack = []


def push(element):
    stack.append(element)


def pop():
    if not stack:
        print("Stack is empty!")
    else:
        stack.pop()


def peak():
    if not stack:
        print("Stack EMPTY")
    else:
        print(stack[-1])
def display():
    print('Stack data:', stack)


def menu():
    print('1. Push Element')
    print('2. Pop Element')
    print('3. Display')
    print('4) Peak')


while True:
    menu()
    choice = int(input('Enter your choice: '))

    match choice:
        case 1:
            push(int(input("Enter element to push: ")))
        case 2:
            pop()
        case 3:
            display()
        case 4:
            peak()
        case _:
            print("Invalid choice! Please try again.")
