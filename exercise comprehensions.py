#fom 100 to 470 find numbers divided by 7 and not by 5


numbers = [number
        for number in range(2,471)
        if number % 7 == 0
        and number % 5 != 0
           ]
print(numbers)




numbersGen = (number
        for number in range(2,471)
        if number % 7 == 0
        and number % 5 != 0
           )
for number in numbersGen:
    print(number)
