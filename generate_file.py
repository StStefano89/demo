 for x in range(10000):
	with open("data.txt","a") as f:
		f.write(f"{x} line changes in feature2 \n")
print("new")
