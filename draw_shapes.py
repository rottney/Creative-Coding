def draw_square(size):
	def draw_horizontal_border(size):
		for pixel in range(size):
			if pixel == size - 1:
				print("*")
			else:
				print("* ", end="")

	def draw_regular_row(size):
		for pixel in range(size):
			if pixel == 0:
				print("* ", end="")
			elif pixel == size - 1:
				print("*")
			else:
				print("  ", end="")

	width = size * 2 - 1
	height = size

	for row in range(size):
		if row == 0 or row == size - 1:
			draw_horizontal_border(size)
		else:
			draw_regular_row(size)
	print()


def test_squares():
	for i in range(5):
		draw_square(i)


def main():
	test_squares()


if __name__ == "__main__":
	main()
