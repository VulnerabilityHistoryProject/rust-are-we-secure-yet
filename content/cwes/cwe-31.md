+++
title = '''
CWE-31: Path Traversal: 'dir\..\..\filename'
'''
description	= '''
The product uses external input to construct a pathname that should be within a restricted directory, but it does not properly neutralize 'dir\..\..\filename' (multiple internal backslash dot dot) sequences that can resolve to a location that is outside of that directory.
'''
weight = 31

[extra]
id = 31
name = '''
Path Traversal: 'dir\..\..\filename'
'''
url = "https://cwe.mitre.org/data/definitions/31.html"
vote = "Discouraged via Borrow Checker"
class = "Variant"
clippy_helps = false
rust_docs_links = [
	
]
+++