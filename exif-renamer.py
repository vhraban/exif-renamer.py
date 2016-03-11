import os,sys
from PIL import Image
from PIL.ExifTags import TAGS
import time


if len(sys.argv) != 2:
	print("usage: " + sys.argv[0] + " <directory>")
	sys.exit(1) 

path = sys.argv[1]

def getDateTaken(file: str):
	try:
		img = Image.open(file)
		# Tag I need is 36867
		# http://www.awaresystems.be/imaging/tiff/tifftags/privateifd/exif/datetimeoriginal.html
		dateTaken = img._getexif()[36867]
		return time.strptime(dateTaken, "%Y:%m:%d %H:%M:%S")
	except IOError:
		print(file + " is not image")
		return

def formatDate(date: str):
	return time.strftime('%Y-%m-%d %H.%M.%S', date)

def rename(path: str, oldFilename: str, newFileName: str, sequence: int = 1):
	oldPath = os.path.join(path, oldFilename)

	fileName, fileExtension = os.path.splitext(oldFilename)

	# Do we need to append the sequence to the file name?
	additionalBit = ""
	if(sequence > 1):
		additionalBit = "-"+str(sequence)

	newPath = os.path.join(path, newFileName + additionalBit + fileExtension)

	if os.path.isfile(newPath):
		sequence+=1
		return rename(path, oldFilename, newFileName, sequence)
	print(oldPath + " => " + newPath);
	os.rename(oldPath, newPath)



def processImage(path: str, file: str):
	fullPath = os.path.join(path, file)
	date = getDateTaken(fullPath)

	if date is None:
		return

	formattedDate = formatDate(date)
	rename(path, file, formattedDate)
	

def main(path: str):
	for file in os.listdir(path):
		processImage(path, file);	
	print("Done")

main(path)
