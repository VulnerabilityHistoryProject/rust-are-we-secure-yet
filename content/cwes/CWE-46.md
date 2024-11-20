+++
title = '''
CWE-46: Path Equivalence: 'filename ' (Trailing Space)
'''
description	= '''
The product accepts path input in the form of trailing space ('filedir ') without appropriate validation, which can lead to ambiguous path resolution and allow an attacker to traverse the file system to unintended locations or access arbitrary files.
'''
weight = 46

[extra]
id = 46
name = '''
Path Equivalence: 'filename ' (Trailing Space)
'''
url = "https://cwe.mitre.org/data/definitions/46.html"
vote = "Discouraged via Borrow Checker"
class = "Variant"
clippy_helps = false
rust_docs_links = [
	
]
+++
