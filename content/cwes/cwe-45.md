+++
title = '''
CWE-45: Path Equivalence: 'file...name' (Multiple Internal Dot)
'''
description	= '''
The product accepts path input in the form of multiple internal dot ('file...dir') without appropriate validation, which can lead to ambiguous path resolution and allow an attacker to traverse the file system to unintended locations or access arbitrary files.
'''
weight = 45

[extra]
id = 45
name = '''
Path Equivalence: 'file...name' (Multiple Internal Dot)
'''
url = "https://cwe.mitre.org/data/definitions/45.html"
vote = ""
class = "Variant"
clippy_helps = false
rust_docs_links = [
	
]
+++
