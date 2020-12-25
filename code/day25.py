dkey = 14205034
ckey = 18047856
v=1
it=0
while dkey != v :
	v*=7
	v = v%20201227
	it+=1
c=1
for _ in range(it):
	c*=ckey
	c = c% 20201227
print(c)

