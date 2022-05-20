num = int(input("Input number"))
max = num % 10
num2 = num
num1 = num
while num2 // 10 != 0:
    num1 = num2 % 10
    num2 = num2 // 10
    if max < num1:
        max = num1
if max < num2:
    max = num2
print("Maximum =", max)
