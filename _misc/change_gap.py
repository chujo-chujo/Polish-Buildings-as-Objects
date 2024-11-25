from PIL import Image
import os
import sys
from tkinter import filedialog

def increase_gap(file, gap=10, new_gap=14):
	# Calculate the difference we need to add to the gap
	gap_diff = new_gap - gap
	img = Image.open(file)
	width, height = img.size
	
	# Find the y-coordinate of the bottom row
	top_section_height = (height - gap) // 2
	
	# Create a new image with extra gap
	new_height = height + gap_diff
	new_image  = Image.new('RGB', (width, new_height), "white")
	
	# Get the top and bottom parts, paste them into new image
	top_part    = img.crop((0, 0, width, top_section_height))
	bottom_part = img.crop((0, top_section_height + gap, width, height))
	new_image.paste(top_part, (0, 0))
	new_image.paste(bottom_part, (0, top_section_height + new_gap))

	return new_image

def save_new_image(output_directory, file, new_image):
	filename = os.path.basename(file)
	new_image.save(os.path.join(output_directory, filename))


if __name__ == "__main__":
	selected_files = filedialog.askopenfilenames(initialdir=os.getcwd(), multiple=True)
	if not selected_files:
		sys.exit()

	output_directory = os.path.dirname(selected_files[0]) + "/new_gap"
	os.makedirs(output_directory, exist_ok=True)

	for file in selected_files:
		if file.endswith('.png'):
			new_image = increase_gap(file, gap=10, new_gap=14)
			save_new_image(output_directory, file, new_image)
