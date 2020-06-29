years = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for year in years:
    if year == 1:
        age = str("год")
    elif year == 2 or year == 3 or year == 4:
        age = str("годa")
    else:
        age = str("лет")
    print ("Мне " +str(year),str(age))
