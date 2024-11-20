+++
title = '''
CWE-55: Path Equivalence: '/./' (Single Dot Directory)
'''
description	= '''
The product accepts path input in the form of single dot directory exploit ('/./') without appropriate validation, which can lead to ambiguous path resolution and allow an attacker to traverse the file system to unintended locations or access arbitrary files.
'''
weight = 55

[extra]
id = 55
name = '''
Path Equivalence: '/./' (Single Dot Directory)
'''
url = "https://cwe.mitre.org/data/definitions/55.html"
vote = "Discouraged via Borrow Checker"
class = "Variant"
clippy_helps = false
rust_docs_links = [
	
]
+++