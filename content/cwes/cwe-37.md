+++
title = '''
CWE-37: Path Traversal: '/absolute/pathname/here'
'''
description	= '''
The product accepts input in the form of a slash absolute path ('/absolute/pathname/here') without appropriate validation, which can allow an attacker to traverse the file system to unintended locations or access arbitrary files.
'''
weight = 37

[extra]
id = 37
name = '''
Path Traversal: '/absolute/pathname/here'
'''
url = "https://cwe.mitre.org/data/definitions/37.html"
vote = "Discouraged via Language, Library Design"
class = "Variant"
clippy_helps = false
rust_docs_links = [

]
+++
Same as whatever is decided for [CWE-22: Path Traversal](/rust-are-we-secure-yet/cwes/cwe-22).
