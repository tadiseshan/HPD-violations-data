import string

file = open('Violation20160331.txt', 'r')

file = file.read().replace('|', ',')

test = open("newfile.csv", "w")
test.write(file)
test.close()

print(test)
