for i in range(1, 101):
    if i == 1 or i % 10 == 1 and i != 11:
        print(f"{i} процент")
    elif i in range(2,5) or i % 10 in range(2,5) and i > 20:
        print(f"{i} процента")
    else:
        print(f"{i} процентов")

