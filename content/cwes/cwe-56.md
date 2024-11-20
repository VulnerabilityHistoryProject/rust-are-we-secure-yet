+++
title = '''
CWE-56: Path Equivalence: 'filedir*' (Wildcard)
'''
description	= '''
The product accepts path input in the form of asterisk wildcard ('filedir*') without appropriate validation, which can lead to ambiguous path resolution and allow an attacker to traverse the file system to unintended locations or access arbitrary files.
'''
weight = 56

[extra]
id = 56
name = '''
Path Equivalence: 'filedir*' (Wildcard)
'''
url = "https://cwe.mitre.org/data/definitions/56.html"
vote = "Discouraged via Borrow Checker"
class = "Variant"
clippy_helps = false
rust_docs_links = [
	
]
+++