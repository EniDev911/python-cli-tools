import os 
import shutil
import sys
import time
import getpass


USER_PATH = os.getenv('userprofile')
USERNAME = getpass.getuser()
DOWNLOADS = os.path.join(USER_PATH, "Downloads")
FOLDERS = {"Desktop": "[1].DESKTOP", 
		   	"Documents": "[2].DOCUMENTS", 
		    "Downloads": "[3].DOWNLOADS"}

	
def directory(file_extension: str) -> str:

	if not file_extension:
		return

	folder_by_extension = {
		"exe": "Software",
		"msi": "Software",
		"txt": "Texts",
		"pdf": "PDF Documents",
		"epub": "Books",
		"jpg": "Images",
		"jpeg": "Images",
		"png": "Images",
		"svg": "Images",
		"ico" : "Icons",
		"raw": "Images",
		"mp3": "Music",
		"mp4": "Videos",
		"mkv": "Videos",
		"avi": "Videos",
		"xlsx": "Excel Files",
		"csv": "Excel Files",
		"xls": "Excel Files",
		"ppt": "Slides",
		"pptx": "Slides",
		"doc": "Documents",
		"rar": "Compressed Files",
		"zip": "Compressed Files",
		"iso": "Iso Files",
		"html": "Pages",
		"js": "Scripts",
		"py": "Scripts",
		"bat": "Scripts"
	}

	return folder_by_extension.get(file_extension, 'Extras')

def organizer(path: str):
	if not os.path.exists(path):
		print(f"ERROR. Not found {path} or not exists.")
		return
	files = os.listdir(path)
	extensions = [os.path.splitext(file)[1].strip(".") for file in files]

	for ext in extensions:
		dir = directory(ext) or ""
		new_directory = os.path.join(path, dir)
		if dir and not os.path.exists(new_directory):
			os.makedirs(new_directory)

	for file in files:
		ext = os.path.splitext(file)[1].strip(".")
		_dir = directory(ext)
		if not _dir:
			continue

		source_filepath = os.path.join(path, file)
		destination_filepath = os.path.join(path, _dir, file)

		if not os.path.exists(destination_filepath):
			shutil.move(source_filepath, destination_filepath)
			print(f'Was moved {file} into {_dir} directory. \n')

	print()
	print("All the files was organized".center(40))
	print(f"sucessfully in {path}".center(40))
	print()
	time.sleep(1)
	os.system("explorer %s" % (path))

#if __name__ == "__main__":
#	try:
#		directory_location = sys.argv[1]
#		organizer(directory_location)
#	except Exception as e:
#		print(f"There was an error: {str(e)}")
