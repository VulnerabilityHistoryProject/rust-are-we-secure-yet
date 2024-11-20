+++
title = '''
CWE-39: Path Traversal: 'C:dirname'
'''
description	= '''
The product accepts input that contains a drive letter or Windows volume letter ('C:dirname') that potentially redirects access to an unintended location or arbitrary file.
'''
weight = 39

[extra]
id = 39
name = '''
Path Traversal: 'C:dirname'
'''
url = "https://cwe.mitre.org/data/definitions/39.html"
vote = "Discouraged via Borrow Checker"
class = "Variant"
clippy_helps = false
rust_docs_links = [
	
]
+++
