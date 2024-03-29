# task 1


if (2024 % 4 == 0) and (1900 % 100 != 0):
    print(2024, "is a leap year.")

elif (1900 % 100 == 0) and (1900 % 400 == 0):
    print(1900, "is a leap year.")

else:
    print(1900, "is not a leap year.")
    print(2020, "is a leap year")
    print(2024, "is a leap year")

