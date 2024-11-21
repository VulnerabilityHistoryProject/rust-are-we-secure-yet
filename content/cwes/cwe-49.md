+++
title = '''
CWE-49: Path Equivalence: 'filename/' (Trailing Slash)
'''
description	= '''
The product accepts path input in the form of trailing slash ('filedir/') without appropriate validation, which can lead to ambiguous path resolution and allow an attacker to traverse the file system to unintended locations or access arbitrary files.
'''
weight = 49

[extra]
id = 49
name = '''
Path Equivalence: 'filename/' (Trailing Slash)
'''
url = "https://cwe.mitre.org/data/definitions/49.html"
vote = "Discouraged via Language, Library Design"
class = "Variant"
clippy_helps = false
rust_docs_links = [

]
+++
Same as whatever is decided for base [CWE-41: Improper Resolution of Path Equivalence](rust-are-we-secure-yet/cwes/cwe-41)
