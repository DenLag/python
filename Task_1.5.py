revenue = int(input("Input revenue")) # выручка
cost = int(input("Input costs")) # издержки
f_res = revenue - cost # прибыль & убыток
prof = f_res / revenue # рентабельность
if f_res > 0:
    stuff = int(input("Input staff number")) # штатная численность
    print("Your profit: ", f_res)
    print("Your profitability: ", round(prof,2))
    print("Your profitability on one person: ", round(f_res / stuff, 2))
else:
    print("Your loss: ", (f_res) * (-1))
