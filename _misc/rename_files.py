import os
from tkinter import filedialog
import sys

def select_files():
	# Select multiple files, check if list of names is big enough
	file_paths = filedialog.askopenfilenames(title="Select files to rename", initialdir=os.getcwd())
	if not file_paths:
		print("Canceled.")
		sys.exit()
	if len(file_paths) > len(new_names):
		print("Error: Number of selected files is larger than the number of names in the list.")
		return
		sys.exit()

	# Sort the filenames alphabetically
	file_paths = sorted(file_paths, key=lambda x: os.path.basename(x))

	return file_paths

def rename_files(file_paths, new_names):
	for file_path, new_name in zip(file_paths, new_names):
		# Get the directory and extension
		file_dir = os.path.dirname(file_path)
		file_ext = os.path.splitext(file_path)[1]
		# Create the full path for the new filename
		new_file_path = os.path.join(file_dir, new_name + file_ext)

		os.rename(file_path, new_file_path)
		print(f"Renamed {os.path.basename(file_path)} to {new_name}")


if __name__ == '__main__':
	new_names = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26","27", "28", "29", "30", "31", "32", "33","34","35", "36", "37", "38", "39", "40", "41", "42", "43", "44","45", "46", "47", "48", "49", "50", "51", "52", "53"]

	file_paths = select_files()
	rename_files(file_paths, new_names)

	new_names = [
	"01_skyscrapers", 
	"02_office_blocks", 
	"03_office_blocks", 
	"04_hotels", 
	"05_hotels", 
	"06_hotels", 
	"07_government_buildings", 
	"08_town_halls", 
	"09_castle_churches", 
	"10_small_churches", 
	"11_historic_houses", 
	"12_historic_houses", 
	"13_historic_houses", 
	"14_historic_houses", 
	"15_historic_houses", 
	"16_downtown_houses", 
	"17_downtown_houses", 
	"18_high_rises", 
	"19_high_rises", 
	"20_high_rises", 
	"21_high_rises", 
	"22_high_rises", 
	"23_high_rises", 
	"24_high_rises", 
	"25_blocks_of_flats", 
	"26_blocks_of_flats", 
	"27_apartments", 
	"28_flats", 
	"29_flats", 
	"30_modern_apartments", 
	"31_modern_family_houses", 
	"32_modern_family_houses", 
	"33_family_houses", 
	"34_village_buildings", 
	"35_schools", 
	"36_stadiums", 
	"37_shopping", 
	"38_fire_stations", 
	"39_theaters_and_cinemas", 
	"40_local_services", 
	"41_statues", 
	"42_statues", 
	"43_parks", 
	"44_parks", 
	"45_fences", 
	"46_fences", 
	"47_fences", 
	"48_fences", 
	"49_construction", 
	"50_construction",
	"51_construction",
	"52_construction",
	"53_construction"
	]

	rename_files(["01.png","02.png","03.png","04.png","05.png","06.png","07.png","08.png","09.png","10.png","11.png","12.png","13.png","14.png","15.png","16.png","17.png","18.png","19.png","20.png","21.png","22.png","23.png","24.png","25.png","26.png","27.png","28.png","29.png","30.png","31.png","32.png","33.png","34.png","35.png","36.png","37.png","38.png","39.png","40.png","41.png","42.png","43.png","44.png","45.png","46.png","47.png","48.png","49.png","50.png", "51.png", "52.png", "53.png"], new_names)