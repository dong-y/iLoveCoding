# charupaixu
# insert sort

# inputnum = [12,10,11,9,1,3,2]
# print(inputnum)
# output[0] = input[0]

# for i in length(input):
# 	if output[i] < input[i+1]:
# 		output[i+1] = input[i+1]
# 	else:
# 		output[i+1] = output[ i]
# 		output[i] = input[i+1]

# output = 

#############################
##### selection sort v1 #####
#############################
# def minf(nums):
# 	print nums
# 	if len(nums) != 0:
# 		minimum = nums[0]
# 		for i in range(len(nums)):
# 			if minimum < nums[i]:
# 				continue 
# 			else:
# 				minimum = nums[i]
# 		return minimum
# 	else:
# 		return "NULL"

# def sortf(nums2):
# 	nums_new = []
# 	if len(nums2) != 0:
# 		for i in range(len(nums2)):
# 			minimum = minf(nums2)
# 			nums2.remove(minimum)
# 			nums_new.append(minimum)
# 		return nums_new
# 	else:
# 		return "NULL"

# sortnum = sortf(inputnum)
# print(sortnum)

#############################
##### selection sort v2 #####
#############################
# import random

# inputnum = []
# inputnum1 = [413,324,31,565,768,45,768]
# inputnum2 = [1,2,3,4,5,6,7]
# # print(inputnum)

# for i in range(10000000):
# 	inputnum.append(random.uniform(1, 1000000000))

# print('haha')



# def minf(nums):
# 	# print nums
# 	if len(nums) != 0:
# 		minimum = nums[0]
# 		for i in range(len(nums)):
# 			if minimum < nums[i]:
# 				continue 
# 			else:
# 				minimum = nums[i]
# 		return minimum
# 	else:
# 		return "NULL"

# def sortf(nums):
# 	if len(nums) != 0:
# 		for i in range(len(nums)):
# 			# print(i)
# 			minimum = minf(nums[0:len(nums)-i])
# 			nums.append(minimum)
# 			nums.remove(minimum)
# 		return nums
# 	else:
# 		return "NULL"

# print(sortf(inputnum))
# print(sortf(inputnum1))
# print(sortf(inputnum2))

#############################
##### selection sort v3 #####
#############################
import random

inputnum = []
inputnum1 = [413,324,31,565,768,45,768]
inputnum2 = [1,2,3,4,5,6,7]
# print(inputnum)

for i in range(1000):
	inputnum.append(random.uniform(1, 1000000000))

print('haha')

def minf(nums):
	if len(nums) != 0:
		minimum = nums[0]
		for i in range(len(nums)):
			if minimum < nums[i]:
				continue 
			else:
				minimum = nums[i]
		return minimum
	else:
		return "NULL"

def minindexf(nums):
	if len(nums) != 0:
		minimum = nums[0]
		for i in range(len(nums)):
			if minimum < nums[i]:
				continue 
			else:
				return i 
				break
	else:
		return "NULL"

# def swap(nums):
# 	if len(nums) != 0:
# 		minimum = minf(nums)
# 		if nums[0] < minimum:
# 			nums[minindexf(nums)] = nums[0]
# 			nums[0] = minimum
# 			return nums
# 		else:
# 			return nums
# 	else:
# 		return "NULL"

def sortf2(nums):
	if len(nums) != 0:
		for i in range(len(nums)):
			print i
			print nums
			# numssub = nums[i:]
			minimum = numssub[minindexf(numssub)]
			numssub[minindexf(numssub)] = numssub[0]
			numssub[0] = minimum
		return nums
	else:
		return "NULL"

# print(sortf2(inputnum1))
# print(sortf2(inputnum2))
# print(sortf2(inputnum))

def getminindex(l,i):
	if len(l)==i+1:
		return i
	else:
		ni = getminindex(l,i+1)
		if l[i]<l[ni]:
			return i
		else:
			return ni

print(getminindex([1,3,2],0))

def selection_sort(l):
	def selection_sort_help(l,i):
		if len(l)<=i+1:
			return l
		else:
			m = getminindex(l,i)
			tmp = l[i]
			l[i] = l[m]
			l[m] = tmp
			return selection_sort_help(l,i+1)
	return	selection_sort_help(l,0)

print(selection_sort([1,3,2,7,9,10,5,13]))






