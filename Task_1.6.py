a = int(input("Input your first result"))
b = int(input("Input your purpose"))
res = a
num_of_day = 1
while res <= b:
    print(f"{num_of_day :01d} day:{res:.2f}")
    res *=   1.1
    num_of_day += 1
print(f"{num_of_day :01d} day:{res:.2f}")
print("Your result will be achieved on:", num_of_day, "day")
