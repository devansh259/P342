sum=0
num_points=0
for i in range(6):
	for j in range(6):
		for k in range(6):
			for l in range(6):
				sum+=abs(i-j)+abs(k-l)
				num_points+=1
print("average distance between points=" + str(sum/num_points))
