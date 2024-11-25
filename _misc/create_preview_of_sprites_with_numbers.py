from PIL import Image
import os
import sys
from tkinter import filedialog

numbers_pixel_data_blue = [(0, 0, 255), (0, 0, 255), (0, 0, 255), (255, 255, 255), (0, 0, 255), (0, 0, 255), (255, 255, 255), (255, 255, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (255, 255, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (255, 255, 255), (0, 0, 255), (255, 255, 255), (0, 0, 255), (255, 255, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (255, 255, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (255, 255, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (255, 255, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (255, 255, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (255, 255, 255), (0, 0, 255), (255, 255, 255), (255, 255, 255), (0, 0, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (0, 0, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (0, 0, 255), (255, 255, 255), (0, 0, 255), (255, 255, 255), (0, 0, 255), (255, 255, 255), (0, 0, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (0, 0, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (0, 0, 255), (255, 255, 255), (0, 0, 255), (255, 255, 255), (0, 0, 255), (255, 255, 255), (0, 0, 255), (255, 255, 255), (0, 0, 255), (0, 0, 255), (255, 255, 255), (0, 0, 255), (255, 255, 255), (255, 255, 255), (0, 0, 255), (255, 255, 255), (255, 255, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (255, 255, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (255, 255, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (255, 255, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (255, 255, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (0, 0, 255), (255, 255, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (255, 255, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (255, 255, 255), (0, 0, 255), (255, 255, 255), (255, 255, 255), (0, 0, 255), (255, 255, 255), (255, 255, 255), (0, 0, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (0, 0, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (0, 0, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (0, 0, 255), (255, 255, 255), (0, 0, 255), (255, 255, 255), (0, 0, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (0, 0, 255), (255, 255, 255), (0, 0, 255), (255, 255, 255), (0, 0, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (255, 255, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (255, 255, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (255, 255, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (0, 0, 255), (255, 255, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (255, 255, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (0, 0, 255), (255, 255, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (255, 255, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255)]
numbers_pixel_data_red  = [(255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 255, 255), (255, 0, 0), (255, 0, 0), (255, 255, 255), (255, 255, 255), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 255, 255), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 255, 255), (255, 0, 0), (255, 255, 255), (255, 0, 0), (255, 255, 255), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 255, 255), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 255, 255), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 255, 255), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 255, 255), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 255, 255), (255, 0, 0), (255, 255, 255), (255, 255, 255), (255, 0, 0), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 0, 0), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 0, 0), (255, 255, 255), (255, 0, 0), (255, 255, 255), (255, 0, 0), (255, 255, 255), (255, 0, 0), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 0, 0), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 0, 0), (255, 255, 255), (255, 0, 0), (255, 255, 255), (255, 0, 0), (255, 255, 255), (255, 0, 0), (255, 255, 255), (255, 0, 0), (255, 0, 0), (255, 255, 255), (255, 0, 0), (255, 255, 255), (255, 255, 255), (255, 0, 0), (255, 255, 255), (255, 255, 255), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 255, 255), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 255, 255), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 255, 255), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 255, 255), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 0, 0), (255, 255, 255), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 255, 255), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 255, 255), (255, 0, 0), (255, 255, 255), (255, 255, 255), (255, 0, 0), (255, 255, 255), (255, 255, 255), (255, 0, 0), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 0, 0), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 0, 0), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 0, 0), (255, 255, 255), (255, 0, 0), (255, 255, 255), (255, 0, 0), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 0, 0), (255, 255, 255), (255, 0, 0), (255, 255, 255), (255, 0, 0), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 255, 255), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 255, 255), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 255, 255), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 0, 0), (255, 255, 255), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 255, 255), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 0, 0), (255, 255, 255), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 255, 255), (255, 0, 0), (255, 0, 0), (255, 0, 0)]

def sort_files_by_creation_time(folder_path, files):
	sorted_files = sorted(files, key=lambda x: os.path.getmtime(os.path.join(folder_path, x)))
	return sorted_files

def find_max_dimensions(image_files):
	max_width = 0
	max_height = 0
	for filename in image_files:
		with Image.open(filename) as img:
			width, height = img.size
			if width > max_width:
				max_width = width
			if height > max_height:
				max_height = height
	return max_width, max_height

def number_sprites(sprite_sheet, number):
	""" Function to extract number sprites from the provided fonts.
		Creates numbers by concatenating the number sprites, returns an Image object. """
	# Numbers are 3(+1 for space) x 5 pixel sprites
	digit_width = 4
	digit_height = 5
	
	# Create an empty image to place the number sprites
	number_str = str(number)
	total_width = len(number_str) * digit_width
	combined_image = Image.new('RGBA', (total_width, digit_height), (255, 255, 255, 0))

	# Extract each digit and paste it into the combined image
	for i, digit_char in enumerate(number_str):
		digit = int(digit_char)
		x_offset = digit * digit_width
		# Crop the specific number from the sprite sheet and paste in the appropriate position within the combined image
		sprite = sprite_sheet.crop((x_offset, 0, x_offset + digit_width, digit_height))
		combined_image.paste(sprite, (i * digit_width, 0), sprite)
	
	return combined_image

def concatenate_images(input_files, output_path, columns, padding, starting_number=False, color_numbers="blue"):
	image_files = [os.path.basename(f) for f in input_files]

	# Load the number sprites
	numbers_sprite_sheet = Image.new('RGBA', (39, 5) )
	if color_numbers == "red":
		numbers_sprite_sheet.putdata(numbers_pixel_data_red)
	else:
		numbers_sprite_sheet.putdata(numbers_pixel_data_blue)

	# Get dimensions of the biggest image + padding between images in pixels
	width, height = find_max_dimensions(image_files)
	half_padding = int(padding / 2)
	# Calculate the number of rows needed based on the number of columns
	rows = (len(image_files) + columns - 1) // columns
	# Create a new image with the size to accommodate all images in rows and columns
	output_image = Image.new('RGB', ((width + padding) * columns, (height + padding) * rows), "white")

	# Paste each image into the new image
	for i, image_file in enumerate(image_files):
		image = Image.open(image_file)

		# Calculate the position for the image and paste it into the grid
		row = i // columns
		col = i % columns
		x_offset = col * (width + padding) + half_padding
		y_offset = row * (height + padding) + half_padding
		output_image.paste(image, (x_offset, y_offset))

		if isinstance(starting_number, int) and not isinstance(starting_number, bool):
			# Add number to the image, paste the number on top of the image on given position
			number = starting_number + i
			sprite_number = number_sprites(numbers_sprite_sheet, number)
			number_x = x_offset + 1
			number_y = y_offset - 6
			output_image.paste(sprite_number, (number_x, number_y), sprite_number)

			# Add divider
			if color_numbers == "red":
				divider = Image.new("RGB", (width - 15, 3), "red")
			else:
				divider = Image.new("RGB", (width - 15, 3), "blue")
			output_image.paste(divider, (x_offset + 15, y_offset - 5))

	# Save the concatenated image
	output_folder = os.path.dirname(input_files[1])
	if not os.path.exists(output_folder):
		os.mkdir(output_folder)
	output_image.save(output_folder + "/" + output_image_name)

if __name__ == "__main__":
	input_files = filedialog.askopenfilenames(initialdir=os.getcwd(), filetypes=[('PNG files', '*.png'), ('All files', '*.*')])
	if not input_files:
		print("Canceled.")
		sys.exit()

	output_image_name = "plbo.png"
	num_columns = 1
	padding = 14
	starting_number = 1
	color_numbers = "red"

	concatenate_images(input_files, output_image_name, num_columns, padding, starting_number, color_numbers)
