+++
title = '''
CWE-51: Path Equivalence: '/multiple//internal/slash'
'''
description	= '''
The product accepts path input in the form of multiple internal slash ('/multiple//internal/slash/') without appropriate validation, which can lead to ambiguous path resolution and allow an attacker to traverse the file system to unintended locations or access arbitrary files.
'''
weight = 51

[extra]
id = 51
name = '''
Path Equivalence: '/multiple//internal/slash'
'''
url = "https://cwe.mitre.org/data/definitions/51.html"
vote = "Discouraged via Borrow Checker"
class = "Variant"
clippy_helps = false
rust_docs_links = [
	
]
+++