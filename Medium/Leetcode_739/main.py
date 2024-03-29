"""
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
"""
temperatures = [73,74,75,71,69,72,76,73]

def main():
    print(count_days_temperature_1(temperatures))

#Surely
def count_days_temperature_0(temperatures):
    stack = []  
    answer = [0] * len(temperatures) 
    for i, temperature in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < temperature:
            idx = stack.pop()
            answer[idx] = i - idx
        stack.append(i)
    return answer

def count_days_temperature_1(temperatures):
    stack = [] # Pair:[temp, idx]
    answer = [0]*len(temperatures)
    for i, temperature in enumerate(temperatures):
        while stack and temperature > stack[-1][0]:
            stackT, stackIdx = stack.pop()
            answer[stackIdx] = i - stackIdx
        stack.append([temperature, i])
    return answer
            

if __name__ == "__main__":
    main()
    