# n = int(input())
# print((n // -4) * -1)

# a = int(input())
# print(a, "мин - это", a // 60, "час", a % 60, "минут")


# Задача 1. Напиите программу, определяющую число десятков и едениц в двухзначном числолке

# Решение. Число едениц - это последняя цифра числа, десятков - первая цифра. Чтобы получить последнию
# цифру любого числа, нужно найти отстаток от диления на 10. Чтобы найти первую цифру двухзначного числа,
# нужно поделить числа нацело на 10. Программа, решающфя поставленную задачу, можно иметь следущий вид:

num = int(input())
last_digit = num % 10
first_digit = num // 10
print('Числа десятков = ', first_digit)
print('Числа единиц =', last_digit)


# Задача 2. Напишите программу, в которой рассчитывается смумма цифр двузначного числа.

# Решения. Программа, решающая поставленые задачи, могут иметь следущий вид:

num = int(input())
last_digit = num % 10
first_digit = num // 10
print('Сумма цифр =', last_digit + first_digit)


# 3 задача.  Напишите программу, которая печатает
#            число, образованное при перестановке цифр двузначного числа.

# Решение. Программа, решающая поставленную задачу, может иметь следующий вид:

num = int(input())
last_digit = num % 10
first_digit = num // 10
print('Искомое число = ', last_digit * 10 + first_digit)


# 4 Задача. Напишите программу, в которую вводится трёхзначное число и которая
#           выводит на экран его цифры через запятую.

# Решение. Программа, решающая поставленную задачу, может иметь следующий вид:

num = int(input())
digit3 = num % 10
digit2 = (num // 10) % 10
digit1 = num // 100
print(digit1, digit2, digit3, sep=',')



