+++
title = '''
CWE-33: Path Traversal: '....' (Multiple Dot)
'''
description	= '''
The product uses external input to construct a pathname that should be within a restricted directory, but it does not properly neutralize '....' (multiple dot) sequences that can resolve to a location that is outside of that directory.
'''
weight = 33

[extra]
id = 33
name = '''
Path Traversal: '....' (Multiple Dot)
'''
url = "https://cwe.mitre.org/data/definitions/33.html"
vote = "Discouraged via Language, Library Design"
class = "Variant"
clippy_helps = false
rust_docs_links = [

]
+++
Same as whatever is decided for [CWE-22: Path Traversal](rust-are-we-secure-yet/cwes/cwe-22).
