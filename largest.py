print("hello")
input1 = raw_input("enter the input\n")
# print(input1)
list1 = []
count  = 1

list1.extend(input1)

# print(list1)



# print(list2)

d1 ={}

for i in range(len(list1)-1):
		if (list1[i] == list1[i+1] ):
			
			
			count = count + 1
			save = list1[i]

			if ( i < (len(list1) -2)):
				if(list1[i] != list1[i+2]):
					d1[save] = count
					count = 1
			else:
				d1[save] = count
				count = 1
# print(d1)

value = 0
char = "null"

for i in d1:

	
	if(d1[i] > value):
		value =d1[i]
		char = i

# print(char,value)

char = char * value
print(char)

# largestSeries = []
# appearences = 3
# save = 0
# for i in range(input1.length):
# 	print(i)
# for i in range(len(list1) - 1):

# 	print(list1[i])
# 	if (list1[i] == list1[i+1] ):
# 		largestSeries.append(list1[i])

# 		print("helloo")
# 		count = count + 1

# 		save = list1[i]


# print(largestSeries)