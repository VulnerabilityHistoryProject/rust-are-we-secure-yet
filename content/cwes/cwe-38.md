+++
title = '''
CWE-38: Path Traversal: '\absolute\pathname\here'
'''
description	= '''
The product accepts input in the form of a backslash absolute path ('\absolute\pathname\here') without appropriate validation, which can allow an attacker to traverse the file system to unintended locations or access arbitrary files.
'''
weight = 38

[extra]
id = 38
name = '''
Path Traversal: '\absolute\pathname\here'
'''
url = "https://cwe.mitre.org/data/definitions/38.html"
vote = "Discouraged via Language, Library Design"
class = "Variant"
clippy_helps = false
rust_docs_links = [

]
+++
Same as whatever is decided for [CWE-22: Path Traversal](rust-are-we-secure-yet/cwes/cwe-22).
