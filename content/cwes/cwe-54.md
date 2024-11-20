+++
title = '''
CWE-54: Path Equivalence: 'filedir\' (Trailing Backslash)
'''
description	= '''
The product accepts path input in the form of trailing backslash ('filedir\') without appropriate validation, which can lead to ambiguous path resolution and allow an attacker to traverse the file system to unintended locations or access arbitrary files.
'''
weight = 54

[extra]
id = 54
name = '''
Path Equivalence: 'filedir\' (Trailing Backslash)
'''
url = "https://cwe.mitre.org/data/definitions/54.html"
vote = "Discouraged via Language, Library Design"
class = "Variant"
clippy_helps = false
rust_docs_links = [

]
+++
Same as whatever is decided for base [CWE-41: Improper Resolution of Path Equivalence](/cwes/cwe-41)
