# w = write
# a = append
# r = read
f = open('test.txt', 'w')
f.write('Test\n')
print('My', 'name', 'is', 'Odung', sep='#', end='!', file=f)
f.close()