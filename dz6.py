#Задача из 3 дз список чисел Фибоначчи, в том числе для отрицательных индексов
#  использовал  map.
#def fibonacci(count):
	#fib_list = [-1, 0, 1]
  
	#any(map(lambda _: fib_list.append(sum(fib_list[-2:])),
										###print(fibonacci(10))
 
# Написать программу, которая найдёт разницу между максимальным и минимальным
#  значением дробной части элементов.

lst = list(map(float, input("Введите числа через пробел:\n").split()))
new_lst = [round(i%1,2) for i in lst if i%1 != 0]
print(max(new_lst) - min(new_lst))