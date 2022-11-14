n = int(input())

b_input = int(input())
min = b_input
max = b_input

for i in range(1, n):
    b_input = int(input())

    if b_input < min:
        min = b_input
    elif b_input > max:
        max = b_input
    
print(min)
print(max)