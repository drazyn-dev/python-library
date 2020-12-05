
# Bubble sort runs comparisons of each item in a list and 'bubbles' the greater ones to the top.
def bubble_sort(sequence: list) -> None:
	# First, we'll need to create a flag.
	# This flag will be used to tell the main loop if we found
	# a change while comparing. We know we're done if we didn't
	# make any changes in a single loop.

	change_made = True

	# This function will sort the list in place.
	
	while change_made:
		change_made = False
		for value in sequence[1:]:
			current_index = sequence.index(value)
			previous_index = current_index - 1
			if sequence[current_index] < sequence[previous_index]:
				temp = sequence[current_index]
				sequence[current_index] = sequence[previous_index]
				sequence[previous_index] = temp
				change_made = True

if __name__ == '__main__':
	test = [1, -4, 3, 3, -5]
	print(test)
	bubble_sort(test)
	print(test)
