# def welcome():
#     print("Fuck You")

# if __name__=="__main__":
#     welcome()

stack=[]
pointer=-1

def push(num:int):
    global pointer
    stack.append(num)
    pointer+=1

def pop():
    global pointer
    stack.pop()
    pointer-=1

def show():
    return stack[pointer]

def clear_stack():
    stack.clear()

