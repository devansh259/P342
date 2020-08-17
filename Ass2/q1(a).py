sum=0
for i in range(6):
	for j in range(6):
		sum+=abs(j-i)
print("average distance between points=" + str(sum/36))

	
