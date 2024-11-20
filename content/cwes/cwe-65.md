+++
title = '''
CWE-65: Windows Hard Link
'''
description	= '''
The product, when opening a file or directory, does not sufficiently handle when the name is associated with a hard link to a target that is outside of the intended control sphere. This could allow an attacker to cause the product to operate on unauthorized files.
'''
weight = 65

[extra]
id = 65
name = '''
Windows Hard Link
'''
url = "https://cwe.mitre.org/data/definitions/65.html"
vote = "Discouraged via Language, Library Design"
class = "Variant"
clippy_helps = false
rust_docs_links = [
	
]
+++
