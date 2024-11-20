+++
title = '''
CWE-23: Relative Path Traversal
'''
description	= '''
The product uses external input to construct a pathname that should be within a restricted directory, but it does not properly neutralize sequences such as ".." that can resolve to a location that is outside of that directory.
'''
weight = 23

[extra]
id = 23
name = '''
Relative Path Traversal
'''
url = "https://cwe.mitre.org/data/definitions/23.html"
vote = "Discouraged via Language, Library Design"
class = "Base"
clippy_helps = false
rust_docs_links = [

]
+++
Same as whatever is decided for [CWE-22: Path Traversal](/cwes/cwe-22).
