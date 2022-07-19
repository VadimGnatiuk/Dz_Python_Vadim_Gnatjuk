'''
Задание 5
Дан текстовый файл. Посчитать сколько раз в нем
встречается заданное пользователем слово.
'''

'''
В исходном текстовом файле, указанное Вами слово встречается ... {count} раз(а).
In the source text file, the word you specified occurs ... {count} times(a).
'''
word = str(input('Enter your word : '))
count = 0

f = open('poem.txt', 'rt')
word_i = f.readline()
while word_i:
    if word.lower() in word_i.lower():
        count += 1
    word_i = f.readline()
f.close()

print(f'In the source text file, the word you specified occurs ... {count} times(es).')