#target = 12
#position = [10,8,0,5,3]
#speed = [2,4,1,1,3]
target = 10
position = [6,8]
speed = [3,2]

def main():
    print(fleet_calculator_1(target,position,speed))

def fleet_calculator_0(target,position,speed):
    pos_sp = [[]]*len(position)
    for i in range(len(position)):
        pos_sp[i] = [position[i],speed[i]]
    pos_sp = sorted(pos_sp, reverse=True)
    stack = []
    for p, s in pos_sp:
        stack.append((target-p) / s)
        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            stack.pop()
    return len(stack)

if __name__ == "__main__":
    main()