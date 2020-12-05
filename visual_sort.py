# sorts a list of strings by their length so they look like a mountain

def visual_sort(strings: list) -> None:
	"""Sorts visually, smallest in length to highest, by length"""
	# gonna try and use quick sort for this one

	if len(strings) < 2:
		return strings
	else:
		pivot = strings.pop()

		lower, higher = [], []

		for string in strings:
			if len(string) > len(pivot):
				higher.append(string)
			else:
				lower.append(string)
	return visual_sort(lower) + [pivot] + visual_sort(higher)

def l_print(strings: list) -> None:
	"""Just prints out everything in a list but one item per line"""
	for string in strings:
		print(string)

if __name__ == '__main__':
	some_string = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus feugiat elementum est, eget gravida erat viverra sit amet. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Suspendisse id tortor et ex pharetra suscipit. Donec et turpis id lorem eleifend varius. Etiam a suscipit augue. Vestibulum iaculis turpis metus, a hendrerit purus bibendum ac. Nulla placerat magna mi, quis facilisis libero consequat id. Fusce dictum imperdiet urna eget viverra. Donec ornare nibh vitae ultricies pharetra. """
	l_print(visual_sort(some_string.split()))
