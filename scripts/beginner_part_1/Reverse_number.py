val =[]
# val = input('Enter a number:')
val = "1234"

def reverse1(val):
	l=[]
	
	for x in reversed(val):
		l.append(x)
		print(l)
	print(l)

reverse1(val)