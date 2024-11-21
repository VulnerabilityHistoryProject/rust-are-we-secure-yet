+++
title = '''
CWE-29: Path Traversal: '\..\filename'
'''
description	= '''
The product uses external input to construct a pathname that should be within a restricted directory, but it does not properly neutralize '\..\filename' (leading backslash dot dot) sequences that can resolve to a location that is outside of that directory.
'''
weight = 29

[extra]
id = 29
name = '''
Path Traversal: '\..\filename'
'''
url = "https://cwe.mitre.org/data/definitions/29.html"
vote = "Discouraged via Language, Library Design"
class = "Variant"
clippy_helps = false
rust_docs_links = [

]
+++
Same as whatever is decided for [CWE-22: Path Traversal](rust-are-we-secure-yet/cwes/cwe-22).
