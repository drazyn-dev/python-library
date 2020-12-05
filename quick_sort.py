# Quick sort works by taking a list and sorting smaller sections of it around a pivot.

def quick_sort(sequence: list) -> list:
	"""This will take a list and return the sorted version"""
	if len(sequence) < 2:
		return sequence
		# Base case. If the list looks like either of these:
		# []
		# [3]
		# It is sorted.
	else:
		# Otherwise, we need to sort the two sides around the pivot.
		pivot = sequence.pop()
		# Just taking the last value and using it as the pivot. Not
		# particularly important.

	lower_values, higher_values = [], []
	# Creating two lists to store the left and right sides of
	# the pivot.
	for value in sequence:
		if value > pivot:
			higher_values.append(value)
		else:
			lower_values.append(value)
	# Here, we go through every value in the sequence.
	# For example, let's say that the sequence was:
	# [1, -4, 3, 3, -5]
	# We decided our pivot will be -5 as that is the last value.
	# Now we check each value and see if it is greater.
	# If it is, it goes into the right side. Otherwise, it goes into
	# the left.
	# [-5] [1, -4, 3, 3]
	return quick_sort(lower_values) + [pivot] + quick_sort(higher_values)
	# Lastly, we need to sort the newly created lists.

if __name__ == '__main__':
	test = [1, -4, 3, 3, -5]
	print(test)
	test = quick_sort(test)
	print(test) 
