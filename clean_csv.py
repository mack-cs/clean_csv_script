import pandas as pd 

#This file receives a CSV file, remove .0s from each entry,
#remove duplicate entries and then exported a clean CSV file
  
#Path to the file that needs to be cleaned
unsorted_file = "test_data.csv"
#Path to save the cleaned CSV
sorted_file = "clead_data.csv"



def openCSVToDataFrame(file):
	"""This function opens a CSV file and returns a DataFrame of that opened CSV file"""
	return pd.read_csv(file) 

def removeTrailingZeros(argv):
	"""This function remove trailing 0s from each of the list passed"""
	row = []
	for arg in argv:
		row.append(str(arg).strip(".0"))
	return row


def removeDecimalsReturnDataFrame(data):
	""" This function loops over DataFrame from CSV and calls the function to remove trailing 0s. After that it returns a clead DataFrame"""
	sorted_items=[]
	for index, row in data.iterrows():
		sorted_items.append(removeTrailingZeros(row))
	df = pd.DataFrame(sorted_items, columns = ["barcode","length","width","height"])
	return df


def removeDuplicatesExportToCSV(old_file, new_file):
	"""This function receives a data frame that has been cleaned of 0s and remove duplicate entries from it then exports a sorted CSV file"""
	data = removeDecimalsReturnDataFrame(openCSVToDataFrame(old_file))
	data.sort_values("barcode", inplace = True) 
	data.drop_duplicates(subset ="barcode", 
                     keep = "first", inplace = True)
	try:
		data.to_csv(new_file, sep=",", encoding="utf-8",index=False)
		print("File created! Your new File -> <{}>".format(new_file))
	except Exception as e:
		print("Error occured!")
	


if __name__ == "__main__":
	removeDuplicatesExportToCSV(unsorted_file,sorted_file)
