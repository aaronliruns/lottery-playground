def checkpair(n):
	s = str(n)
	l = len(s)
	o = ''
	for i in range(0,3-l):
		o = o + '0'
	o = o + str(n)
	return o[0]==o[1] or o[1]==o[2] or o[0]==o[2]

def checkfirsttwo(n):
	s = str(n)
	l = len(s)
	o = ''
	for i in range(0,3-l):
		o = o + '0'
	o = o + str(n)
	return o[0]==o[1] and o[1] != o[2]



j=0
c=0
for i in range (0,1000):
	if (checkfirsttwo(i)):
		c=c+1
		print(str(i)+"\n")
print("===========\n")
print(c)