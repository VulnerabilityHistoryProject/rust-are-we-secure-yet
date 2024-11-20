+++
title = '''
CWE-53: Path Equivalence: '\multiple\\internal\backslash'
'''
description	= '''
The product accepts path input in the form of multiple internal backslash ('\multiple\trailing\\slash') without appropriate validation, which can lead to ambiguous path resolution and allow an attacker to traverse the file system to unintended locations or access arbitrary files.
'''
weight = 53

[extra]
id = 53
name = '''
Path Equivalence: '\multiple\\internal\backslash'
'''
url = "https://cwe.mitre.org/data/definitions/53.html"
vote = "Discouraged via Language, Library Design"
class = "Variant"
clippy_helps = false
rust_docs_links = [

]
+++
Same as whatever is decided for base [CWE-41: Improper Resolution of Path Equivalence](/cwes/cwe-41)
