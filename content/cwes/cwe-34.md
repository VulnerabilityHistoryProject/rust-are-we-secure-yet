+++
title = '''
CWE-34: Path Traversal: '....//'
'''
description	= '''
The product uses external input to construct a pathname that should be within a restricted directory, but it does not properly neutralize '....//' (doubled dot dot slash) sequences that can resolve to a location that is outside of that directory.
'''
weight = 34

[extra]
id = 34
name = '''
Path Traversal: '....//'
'''
url = "https://cwe.mitre.org/data/definitions/34.html"
vote = "Discouraged via Borrow Checker"
class = "Variant"
clippy_helps = false
rust_docs_links = [
	
]
+++
