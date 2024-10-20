a = [0,1,2,3,4,5,6,7,8,9]
c = [True, False, True, False, True, False, True, False, True, False]

def is_greater_than_5(num):
    return num > 5



b = filter(is_greater_than_5, a)
for n in b:
    print(n)


# Example lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Bitwise XOR
xor_result = [a ^ b for a, b in zip(list1, list2)]
print("Bitwise XOR:", xor_result)