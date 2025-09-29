day = int(input("введите день: ")) # задаю переменную
month = int(input("введите месяц: "))# задаю переменную
if (day>=1) and (day <= 31) and ( month>=3) and (month <=5): # задаю условия для весны
    season = "Весна"   # если условие выполняется
elif (day>=1) and (day <= 31) and ( month>=6) and (month <=8): # то же самоедля лета и тд
    season = "Лето"
elif (day>=1) and (day <= 31) and ( month>=9) and (month <=11):
    season = "Осень"
elif (day>=1) and (day <= 31) and ( month==12) and (month <=2):
    season = "Зима"
else:
    season = "неправильная дата" # если ничего не выполняется
print("Сезон:", season) # вывожу результат