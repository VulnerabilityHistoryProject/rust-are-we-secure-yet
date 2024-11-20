"""
This script will
1. Download the latest CWE XML file from the official CWE website.
2. Parse the XML file to get the relevant data needed.
3. Load new data into the CWE content md files (with out removing voter data)
	3.5 This will require loading each file in content/cwes/cwe-... and parsing the toml metadata
4. Create new files for missing CWEs
"""

import os
import requests
import xml.etree.ElementTree as ET
import frontmatter
import re
from zipfile import ZipFile as zipfile
from tqdm import tqdm

CWE_PAGES = os.path.join(os.path.dirname(__file__), '../content/cwes')
CWE_XML_PATH = os.path.join(os.path.dirname(__file__), 'cwec_latest')
CWE_XML_DL_LINK = "https://cwe.mitre.org/data/xml/cwec_latest.xml.zip"
CWE_MITRE_URL = "https://cwe.mitre.org/data/definitions/{}.html"

class CWE_Data:
	"""
	This class will hold and define the necessary data for the CWEs
	"""
	def __init__(
		self,
		cwe_id:int=int(),
		name:str =str(),
		classification_type:str =str(),
		description: str=str(),
		mitre_url: str=str(),
		vote: str=str(),
		clippy_helps: bool=bool(),
		rust_docs_links: list[str]=list(),
		notes: str=str()
	):
		self.id = cwe_id
		self.type = classification_type
		self.name = name
		self.description = description
		self.url = mitre_url
		self.vote = vote
		self.clippy_helps = clippy_helps
		self.docs = rust_docs_links
		self.notes = notes

	@classmethod
	def from_metadata(cls, metadata: dict, content: str):
		extra = metadata.get('extra', {})
		return cls(
			cwe_id = extra['id'],
			name = extra['name'],
			classification_type = extra.get('class', ""),
			description = metadata.get('description', ""),
			mitre_url = extra['url'],
			vote = extra['vote'],
			clippy_helps = extra['clippy_helps'],
			rust_docs_links = extra['rust_docs_links'],
			notes = content,
		)

	def add_vote(self, other):
		self.vote = other.vote
		self.clippy_helps = other.clippy_helps
		self.docs = other.docs
		self.notes = other.notes

	def to_page_str(self): return f"""+++
title = '''
CWE-{self.id}: {self.name}
'''
description	= '''
{self.description}
'''
weight = {self.id}

[extra]
id = {self.id}
name = '''
{self.name}
'''
url = "{self.url}"
vote = "{self.vote}"
class = "{self.type}"
clippy_helps = {"true" if self.clippy_helps else "false"}
rust_docs_links = [
	{",\n".join([f'"{link}"' for link in self.docs])}
]
+++
{self.notes}"""

	def __repr__(self):
		return f"CWE-{self.id}: {self.name}"

	def __eq__(self, other):
		return (
			self.id == other.id
			and self.name.strip() == other.name.strip()
			and self.description.strip() == other.description.strip()
			and self.type == other.type
		)

	def __hash__(self):
		return hash(self.id)


def fetch_cwe_data() -> dict[str, CWE_Data]:
	"""
	Fetches CWE (Common Weakness Enumeration) data from the official CWE website.
	Downloads and parses the latest CWE XML file to extract relevant CWE entries and their metadata.
	Returns:
		A set of CWE_Data objects containing the parsed CWE information,
			including IDs, names, classifications, descriptions and URLs.
	"""

	cwe_data = dict()

	# Download XML.ZIP
	response = requests.get(CWE_XML_DL_LINK)
	if response.status_code != 200:
		raise Exception(f"Failed to download CWE XML file: {response.status_code}")
	try:
		with open(f"{CWE_XML_PATH}.zip", 'wb') as f:
			f.write(response.content)
	except Exception as e:
		raise Exception(f"Failed to save CWE XML zip file: {e}")

	# Extract XML.ZIP to XML
	try:
		with zipfile(f"{CWE_XML_PATH}.zip", 'r') as z:
			z.extractall(CWE_XML_PATH)
	except Exception as e:
		raise Exception(f"Failed to extract CWE XML file: {e}")

	# Load XML
	try:
		cwec_xml = os.listdir(CWE_XML_PATH)[0]
		with open(os.path.join(CWE_XML_PATH, cwec_xml), 'r') as f:
			data = f.read()
			xml_data = ET.fromstring(data)
	except Exception as e:
		raise Exception(f"Failed to parse CWE XML file: {e}")

	# Parse XML data into CWE_Data objects
	version = xml_data.attrib.get('{http://www.w3.org/2001/XMLSchema-instance}schemaLocation', '').split(" ")[0]
	for w in xml_data.findall(f'{{{version}}}Weaknesses') or []:
		for c in w:
			#{'ID', 'Name', 'Abstraction', 'Structure', 'Status'}
			id = c.attrib.get('ID', "")
			name = c.attrib.get('Name', "")
			classification = c.attrib.get('Abstraction', "")
			desc = c[0].text
			desc = " ".join(desc.split()) if desc else ""
			url = CWE_MITRE_URL.format(id)

			cwe = CWE_Data(cwe_id=int(id), name=name, classification_type=classification, description=desc, mitre_url=url)
			cwe_data[id] = cwe

	return cwe_data

def merge_cwe_data_pages(cwe_data: dict[str, CWE_Data]) -> tuple[set[CWE_Data], set[CWE_Data]]:
	"""
	Merges CWE data from in-memory parsed XML with existing CWE markdown files.
	Reads current CWE file contents and metadata from the filesystem and compares
	with the provided CWE data set. Detects new CWEs and changes to existing CWEs.

	Args:
		cwe_data: Set of CWE_Data objects containing latest CWE information from XML

	Returns:
		Tuple containing:
				- Set of CWE_Data for existing files that have changed content
				- Set of CWE_Data for new CWEs that don't have files yet
	"""
	changed_files = set()
	new_files = set()
	hit_files = set()
	missing_data = set()

	# Get updates for existing CWEs
	for file in os.listdir(CWE_PAGES):
		if file.startswith('_'): # Ignore _index.md
			continue

		try:
			with open(os.path.join(CWE_PAGES, file), 'r') as f:
				metadata = frontmatter.load(f)
				old_cwe = CWE_Data.from_metadata(metadata.metadata, metadata.content)
				cwe = cwe_data.get(str(old_cwe.id), None)

				if cwe is None:
					missing_data.add(old_cwe) # Error in fetching cwe
				elif cwe != old_cwe:
					cwe.add_vote(old_cwe)
					changed_files.add(cwe)
				hit_files.add(str(old_cwe.id))
		except Exception as e:
			print(f"Error Reading {file}")

	# Add new CWEs
	unhit_files = set(cwe_data.keys()) - hit_files
	for id in unhit_files:
		new_files.add(cwe_data[id])

	# If this gets printed there is a problem D:
	if missing_data:
		print("Missing data for the following CWEs:")
		print(missing_data)

	return changed_files, new_files

def update_cwe_data_files(changed_files: set[CWE_Data], new_files: set[CWE_Data]):
	"""
	Updates CWE markdown files on disk with updated and new CWE data.
	For existing CWEs, merges new metadata while preserving manually entered data like
	votes and notes. For new CWEs, creates new markdown files with initial metadata.

	Args:
		changed_files: Set of CWE_Data objects containing updated data for existing CWEs
		new_files: Set of CWE_Data objects containing data for newly added CWEs
	"""

	# Update existing CWEs
	for cwe in tqdm(changed_files, desc="Updating existing CWEs"):
		file = os.path.join(CWE_PAGES, f"cwe-{cwe.id}.md")
		new_page_data = cwe.to_page_str()
		with open(file, 'w') as f:
			f.write(new_page_data)

	# Add new CWEs
	for cwe in tqdm(new_files, desc="Adding new CWEs"):
		file = os.path.join(CWE_PAGES, f"cwe-{cwe.id}.md")
		new_page_data = cwe.to_page_str()
		with open(file, 'w') as f:
			f.write(new_page_data)

def main():
	cwe_data = fetch_cwe_data()
	changed_files, new_files = merge_cwe_data_pages(cwe_data)
	print(len(changed_files), len(new_files))
	update_cwe_data_files(changed_files, new_files)

if __name__ == "__main__":
	main()
