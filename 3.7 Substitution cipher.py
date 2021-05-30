# https://stepik.org/lesson/3380/step/2?unit=963
# Программа, которая умеет шифровать и расшифровывать шифр подстановки.
# Программа принимает на вход две строки одинаковой длины,
# на первой строке записаны символы исходного алфавита,
# на второй строке — символы конечного алфавита, после чего идёт строка,
# которую нужно зашифровать переданным ключом, и ещё одна строка, которую нужно расшифровать

intab = str(input())  # строка, имеющая действительные символы
outab = str(input())  # строка, имеющая соответствующее отображение символов
strok = str(input())  # что надо зашифровать
trant = str(input())  # шифр ввод

print(strok.translate(strok.maketrans(intab, outab)))  # таблица перевода из интаб в оутаб
print(trant.translate(strok.maketrans(outab, intab)))  # таблица перевода из оутаб в интаб
# maketrans задаёт правило перевода, а translate непосредственно совершает перевод используя ранее созданное правила
