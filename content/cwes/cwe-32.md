+++
title = '''
CWE-32: Path Traversal: '...' (Triple Dot)
'''
description	= '''
The product uses external input to construct a pathname that should be within a restricted directory, but it does not properly neutralize '...' (triple dot) sequences that can resolve to a location that is outside of that directory.
'''
weight = 32

[extra]
id = 32
name = '''
Path Traversal: '...' (Triple Dot)
'''
url = "https://cwe.mitre.org/data/definitions/32.html"
vote = "Discouraged via Language, Library Design"
class = "Variant"
clippy_helps = false
rust_docs_links = [

]
+++
Same as whatever is decided for [CWE-22: Path Traversal](/rust-are-we-secure-yet/cwes/cwe-22).
