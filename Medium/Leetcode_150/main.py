tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
#Output: 22

def main():
    print(reverse_polish(tokens))

def reverse_polish(tokens):
    stack = []
    for token in tokens:
        if token == "+":
            stack.append(stack.pop() + stack.pop())
        elif token == "-":
            A = stack.pop()
            B = stack.pop()
            stack.append(B -  A)
        elif token == "*":
            stack.append(stack.pop() * stack.pop())
        elif token == "/":
            A = stack.pop()
            B = stack.pop()
            if B * A < 0 and B % A != 0:
                stack.append(B // A + 1)
            else:
                stack.append(B // A)
        else:
            stack.append(int(token))
    return stack.pop()

if __name__ == "__main__":
    main()