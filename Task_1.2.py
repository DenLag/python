data = int(input("Input number of seconds please"))
hour = data // 3600
min = (data - hour * 3600) // 60
sec = data % 60
print(f"{hour:02d}:{min:02d}:{sec:02d}")
