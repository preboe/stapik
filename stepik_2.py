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



