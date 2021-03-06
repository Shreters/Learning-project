# https://stepik.org/lesson/3363/step/2?unit=1135
# Напишите программу, которая считывает строку,
# соответствующую тексту, сжатому с помощью кодирования повторов,
# и производит обратную операцию, получая исходный текст.
import re  # импортируем модуль регулярных выражений


s = 'o12S5Q19O20L4a4b13t2r10A2r10C18q11a15t10c5h5i20G18V17L17k13T1Y9l20e11C10Q9'
newS = ''
alpha_lst = [i for i in s if i.isalpha()]  # формируем список букв
num_list = re.compile(r'\d+').findall(s)  # формируем список чисел регулярными выражениями

for i in range(len(alpha_lst)):  # проходим по индексам списков и перемножаем буквы
    newS += (alpha_lst[i] * int(num_list[i]))  # на соответствующие цифры

print(newS)
