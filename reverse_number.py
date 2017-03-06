num = int(input('Type A Number: '))

y1 = num // 100
help = num % 100
y2 = help // 10
y3 = help % 10

num_reversed = y3 * 100 + y2 * 10 + y1
print ('{0} becomes {1}'.format(num, num_reversed))
