"""
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

Example 1:
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

Example 2:
Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].

Example 3:
Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
"""
digits = [4,2,9,9]
#Output: [1,0]

def main():
    #print(plus_one_1(digits))
    print(plus_one_2(digits))

# put all the number in a string
# string to int. int + 1 covert back to string
# put each number in an array using append converting it to int
# Get Owned Bozo
def plus_one_1(digits):
    to_sum = ""
    for i in digits:
        to_sum += str(i)
    to_sum = int(to_sum)
    to_sum += 1
    final_digit = []
    for digit in str(to_sum):
        final_digit.append(int(digit))
    return final_digit
##########################
def plus_one_2(digits):
    # Reverse the array
    digits = digits[::-1]
    # Increment the digits individually
    carry = 1
    for i in range(len(digits)):
        digits[i] += carry
        if digits[i] < 10:
            carry = 0
            break
        else:
            digits[i] = 0
    # If there's still carry left, append it as a new digit
    if carry:
        digits.append(1)
    return digits[::-1]

if __name__ == "__main__":
    main()