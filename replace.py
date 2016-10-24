import string, glob

files = glob.glob('data/*.txt')

for file in files:
	f = open(file, 'r')
	f = f.read().replace('|', ',')
	n = open(file + ".csv", "w")
	n.write(f)
	n.close()
