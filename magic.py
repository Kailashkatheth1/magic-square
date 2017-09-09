import sys

degree = int(input('Enter dimension of the square matrix.\n'))
if (degree % 2 == 0):
	print('We have not yet written script for even magic square.  Try with odd number greater than 2 for now.')
	sys.exit()
if (degree < 3):
	print('Please enter odd number greater than 2.')
	sys.exit()
square = []
for item in range(0,int(degree)):
	temp = []
	for sub_item in range(0,int(degree)):
		temp.append(0)
	square.append(temp)

start_point = int((degree-1)/2)
i = 0

#filling out every number in the boxes
for number in range(1,degree**2 + 1):

	#checking if the place has been already occupied
	if square[i][start_point] != 0:
		i = i + 2
		start_point = start_point - 1
		if i >= degree:
			i = i - degree

	#implementing regular procedure
	square[i][start_point] = number
	i = i - 1
	start_point = start_point + 1
	if start_point >= degree:
		start_point = degree - start_point
	if abs(i) >= degree:
		i = i + degree

#for printing out the magic square values
print('\nThis is the magic square of %d by %d dimension. \n' %(degree, degree))
for item in square:
	for sub_item in item:
		print(sub_item, '      ', end = '')
	print('\n')
print('The sum of each row, each column and each diagonal is %d.' %(sum(square[0])))