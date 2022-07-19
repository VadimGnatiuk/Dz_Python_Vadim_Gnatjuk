# Задание 2
# Пользователь вводит с клавиатуры три числа. Первое
# число — зарплата за месяц, второе число — сумма месячного платежа по кредиту в банке, третье число — задолженность
# за коммунальные услуги. Необходимо вывести на экран сумму, которая останется у пользователя после
# всех выплат.
# Введите значение зарплаты за месяц
# Введите значение ежемесячного платежа по кредиту
# Введите сумму платежа за коммунальные услуги
# сумма на счету, которая останется после всех выплат, составит
# Enter the value of the salary for the month
# Enter the value of the monthly loan payment
# Enter the amount of payment for utilities
# the amount on the account that will remain after all payments will be
salary_for_the_month = float(input("Enter the value of the salary for the month : "))
monthly_loan_payment = float(input("Enter the value of the monthly loan payment : "))
payment_for_utilities = float(input("Enter the amount of payment for utilities : "))
print("The amount on the account that will remain after all payments will be...",
      salary_for_the_month - (monthly_loan_payment + payment_for_utilities))
