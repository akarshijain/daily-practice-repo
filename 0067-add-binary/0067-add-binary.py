class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # ToDo: Write Your Code Here.
        if len(b) > len(a):
            a, b = b, a

        index_a = len(a) - 1
        index_b = len(b) - 1

        binary_sum = ""
        carry = 0
        while index_a >= 0:
            binary_a = int(a[index_a])

            if index_b < 0:
                binary_b = 0
            else:
                binary_b = int(b[index_b])
            
            temp_sum = carry + binary_a + binary_b
            binary_sum += str(temp_sum % 2)
            carry = temp_sum // 2

            index_a -= 1
            index_b -= 1

        if carry:
            binary_sum += str(carry)    

        return binary_sum[::-1]