import os
import csv
from enum import Enum
from pathlib import Path
import frontmatter

# Input files/folders
CHILD_MAP = os.path.join(os.path.dirname(__file__), 'child_map.csv')
CWE_PAGES = os.path.join(os.path.dirname(__file__), '../content/cwes')

# Output files
OUTPUT = os.path.join(os.path.dirname(__file__), 'rust_cwe_data.csv')

class CWE_Data():
	"""
	This class will hold and define the necessary data for the CWEs
	"""
	def __init__(self):
		self.cwe = 0
		self.name = ""
		self.classification = ""
		self.vote = None
		self.parent = 0
		
	def __str__(self):
		return f"CWE: {self.cwe}, Name: {self.name}, Class: {self.classification}, Vote: {self.vote.to_num()}, Parent: {self.parent}"
  

class VoteClassifications:
	"""_summary_
		Represents the different classifications of votes for a CWE.
		In the CWE Markdowns these votes are stored as a dict, and in the CSV they are stored as a 8-digit bit-number.
	"""
	def __init__(self):
		self.virtually_impossible = False
		self.discouraged = False
		self.discouraged_library = False
		self.discouraged_borrow_checker = False
		self.discouraged_debug_mode = False
		self.clippy = False
		self.no_help = False

	@classmethod
	def from_dict(cls, data):
		self = cls()
		self.no_help = data["No Help, or Langs Wont Help"]
		self.discouraged = data["Discouraged"]
		self.discouraged_library = data["Discouraged via Library"]
		self.discouraged_borrow_checker = data["Discouraged via Borrow Checker"]
		self.discouraged_debug_mode = data["Discouraged via Debug Mode"]
		self.clippy = data["Discouraged via Clippy"]
		self.virtually_impossible = data["Virtually Impossible"]
		return self

	def to_num(self):
		return f"{int(self.virtually_impossible)}{int(self.discouraged)}{int(self.discouraged_library)}{int(self.discouraged_borrow_checker)}{int(self.discouraged_debug_mode)}{int(self.clippy)}{int(self.no_help)}"
    

def get_cwe_data() -> list:
	"""
	The function `get_cwe_data` reads the CWE data from the markdown files and returns a dictionary containing the CWE data.

	:return: A list containing CWE data.
	"""

	cwes = list()

	for file in os.listdir(CWE_PAGES):
		if file.startswith('_'): # Ignore _index.md
			continue

		try:
			with open(os.path.join(CWE_PAGES, file), 'r') as f:
				metadata = frontmatter.load(f)
				cwe_data = CWE_Data()
				cwe_data.name = metadata.metadata['extra']['name']
				cwe_data.cwe = metadata.metadata['weight']
				cwe_data.classification = metadata.metadata['extra']['class']
				cwe_data.vote = VoteClassifications.from_dict(metadata.metadata['extra']['vote'])
				cwe_data.parent = metadata.metadata['extra']['parent']
				cwes.append(cwe_data)
		except Exception as e:
			print(f"Error Reading {file}: {e}")
		
	return cwes

def create_csv(cwes: dict):
	"""
	The function `create_csv` writes CWE data to a CSV file.
	
	:param cwes: A dictionary containing CWE data.
	"""

	with open(OUTPUT, mode='w') as file:
		writer = csv.writer(file)
		writer.writerow(["CWE", "Name", "Class", "Vote", "Parent"])
		for cwe in cwes:
			name = cwe.name.replace("\n", "") # Remove newlines from name
			vote = cwe.vote.to_num() # Convert vote to 8-digit bit-number
			writer.writerow([cwe.cwe, name, cwe.classification, vote, cwe.parent])
	
def main():
  cwes = get_cwe_data()
  create_csv(cwes)
  print(f"CSV file created at {OUTPUT}")

if __name__ == "__main__":
  main()
