"""
Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы.
Например, если было введено "abc cde def", то должно быть выведено "abcdef".
"""

s1 = input().replace(" ","")
s2 = ""
for i in s1:
    if s2.find(i) == -1:
        s2 += i
print(s2)