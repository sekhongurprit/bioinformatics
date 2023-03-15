import os 
from re import * 
def main():
	i=0
	for filename in os.listdir ("."):
		if "_" in filename:
			(first, second, third) = filename.split ('_', 2)
			string=""
			first.join(string)
			print (filename, string)
			os.rename (filename, first+".pdbqt")
if __name__ == '__main__':
	main()
