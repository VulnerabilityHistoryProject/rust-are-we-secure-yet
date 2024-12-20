+++
title = '''
CWE-41: Improper Resolution of Path Equivalence
'''
description	= '''
The product is vulnerable to file system contents disclosure through path equivalence. Path equivalence involves the use of special characters in file and directory names. The associated manipulations are intended to generate multiple names for the same object.
'''
weight = 41

[extra]
id = 41
name = '''
Improper Resolution of Path Equivalence
'''
url = "https://cwe.mitre.org/data/definitions/41.html"
vote = "Discouraged via Language, Library Design"
class = "Base"
clippy_helps = false
rust_docs_links = [

]
+++
Same as whatever is decided for [CWE-22: Path Traversal](/rust-are-we-secure-yet/cwes/cwe-22).
