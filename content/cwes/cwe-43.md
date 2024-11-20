+++
title = '''
CWE-43: Path Equivalence: 'filename....' (Multiple Trailing Dot)
'''
description	= '''
The product accepts path input in the form of multiple trailing dot ('filedir....') without appropriate validation, which can lead to ambiguous path resolution and allow an attacker to traverse the file system to unintended locations or access arbitrary files.
'''
weight = 43

[extra]
id = 43
name = '''
Path Equivalence: 'filename....' (Multiple Trailing Dot)
'''
url = "https://cwe.mitre.org/data/definitions/43.html"
vote = ""
class = "Variant"
clippy_helps = false
rust_docs_links = [

]
+++
Same as whatever is decided for base [CWE-41: Improper Resolution of Path Equivalence](/cwes/cwe-41)
