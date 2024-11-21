+++
title = '''
CWE-40: Path Traversal: '\\UNC\share\name\' (Windows UNC Share)
'''
description	= '''
The product accepts input that identifies a Windows UNC share ('\\UNC\share\name') that potentially redirects access to an unintended location or arbitrary file.
'''
weight = 40

[extra]
id = 40
name = '''
Path Traversal: '\\UNC\share\name\' (Windows UNC Share)
'''
url = "https://cwe.mitre.org/data/definitions/40.html"
vote = "Discouraged via Language, Library Design"
class = "Variant"
clippy_helps = false
rust_docs_links = [

]
+++
Same as whatever is decided for [CWE-22: Path Traversal](rust-are-we-secure-yet/cwes/cwe-22).
