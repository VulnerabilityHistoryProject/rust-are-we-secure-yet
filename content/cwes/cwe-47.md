+++
title = '''
CWE-47: Path Equivalence: ' filename' (Leading Space)
'''
description	= '''
The product accepts path input in the form of leading space (' filedir') without appropriate validation, which can lead to ambiguous path resolution and allow an attacker to traverse the file system to unintended locations or access arbitrary files.
'''
weight = 47

[extra]
id = 47
name = '''
Path Equivalence: ' filename' (Leading Space)
'''
url = "https://cwe.mitre.org/data/definitions/47.html"
vote = "Discouraged via Language, Library Design"
class = "Variant"
clippy_helps = false
rust_docs_links = [

]
+++
Same as whatever is decided for base [CWE-41: Improper Resolution of Path Equivalence](/cwes/cwe-41)
