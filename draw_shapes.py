'''
NOTE: "width" and "height" are not needed
'''
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

	print(f"Drawing square of size {size}:")
	for row in range(height):
		if row == 0 or row == size - 1:
			draw_horizontal_border(size)
		else:
			draw_regular_row(size)
	print()


def draw_triangle(size):
	def draw_top(size):
		for _ in range(size - 1):
			print(" ", end="")
		print("*")
		for _ in range(size - 1):
			print(" ", end="")
		print()	# doesn't work...

	def draw_diagonal(size, width, row):
		midpoint = width // 2 - 1

		print(" ", end="")
		for pixel in range(width):
			if pixel == midpoint - row or pixel == midpoint + row:
				print("*", end="")
			else:
				print(" ", end="")
		print()

	def draw_bottom(size):
		for pixel in range(size):
			if pixel == size - 1:
				print("*")
			else:
				print("* ", end="")
	
	width = size * 2 - 1
	height = size

	print(f"Drawing triangle of size {size}:")
	for row in range(height):
		if row == 0:
			draw_top(size)
		elif row == size - 1:
			draw_bottom(size)
		else:
			draw_diagonal(size, width, row)
	print()


def test_squares():
	for i in range(5):
		draw_square(i)


def test_triangles():
	for i in range(5):
		draw_triangle(i)


def main():
	test_squares()
	test_triangles()


if __name__ == "__main__":
	main()
