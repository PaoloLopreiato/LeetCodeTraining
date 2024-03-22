"""
Given two binary strings a and b, return their sum as a binary string.
 
Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"
 
Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
"""
"""
How to convert binary to decimal
For binary number with n digits:

dn-1 ... d3 d2 d1 d0

The decimal number is equal to the sum of binary digits (dn) times their power of 2 (2n):

decimal = d0×20 + d1×21 + d2×22 + ...
"""
a = "11"
b = "1"

def main():
    #print(sum_binary_number(a, b))
    print(sum_binary_number_done_properly(a, b))

def sum_binary_number_done_properly(a, b):
    result = ""
    carry = 0
    a, b = a[::-1], b[::-1]

    for i in range(max(len(a),len(b))):
        if i < len(a):
            Da = ord(a[i]) - ord("0")
        else:
            Da = 0
        if i < len(b):
            Db = ord(b[i]) - ord("0")
        else:
            Db = 0      
        
        total = Da + Db + carry
        char = str(total%2)     
        result = char + result
        carry = total // 2
        
    if carry != 0:
        result = "1" + result
    return result
#Works BUT not it
def sum_binary_number(a, b):
    #Binary string to int
    int_a = int(a, 2)
    int_b = int(b, 2)
    
    sum_int = int_a + int_b    
    # Convert the sum back into a binary string
    result = bin(sum_int)[2:]  # [2:] removes the '0b' prefix added by bin()   
    return result

if __name__ == "__main__":
    main()
