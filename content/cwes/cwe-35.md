+++
title = '''
CWE-35: Path Traversal: '.../...//'
'''
description	= '''
The product uses external input to construct a pathname that should be within a restricted directory, but it does not properly neutralize '.../...//' (doubled triple dot slash) sequences that can resolve to a location that is outside of that directory.
'''
weight = 35

[extra]
id = 35
name = '''
Path Traversal: '.../...//'
'''
url = "https://cwe.mitre.org/data/definitions/35.html"
vote = "Discouraged via Language, Library Design"
class = "Variant"
clippy_helps = false
rust_docs_links = [

]
+++
Same as whatever is decided for [CWE-22: Path Traversal](/rust-are-we-secure-yet/cwes/cwe-22).
