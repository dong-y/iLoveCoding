#20150929_count_unique_user_id.py

#goal: find the unique values in a list (similar to Codebook command in Stata)

#input: [u1231545, u34123642, u12341235, u13451341, u09879789, u94587329, u92319759, u13451341, u13451341, u09879789]

#output: 7

#####################################

list = ['u1231545', 'u34123642', 'u12341235', 'u13451341', 'u09879789', 'u94587329', 'u92319759', 'u13451341', 'u13451341', 'u09879789']

length = len(list)
print length

count = 0
for i in range(len(list)):
	for j in range(len(list)):
		if i > j and list[i] == list[j]:
			print list[i] + '=' + list[j]
			break
	else:	
		count += 1

print count