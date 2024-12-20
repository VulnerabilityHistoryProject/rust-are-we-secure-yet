+++
title = '''
CWE-57: Path Equivalence: 'fakedir/../realdir/filename'
'''
description	= '''
The product contains protection mechanisms to restrict access to 'realdir/filename', but it constructs pathnames using external input in the form of 'fakedir/../realdir/filename' that are not handled by those mechanisms. This allows attackers to perform unauthorized actions against the targeted file.
'''
weight = 57

[extra]
id = 57
name = '''
Path Equivalence: 'fakedir/../realdir/filename'
'''
url = "https://cwe.mitre.org/data/definitions/57.html"
vote = "Discouraged via Language, Library Design"
class = "Variant"
clippy_helps = false
rust_docs_links = [

]
+++
Same as whatever is decided for base [CWE-41: Improper Resolution of Path Equivalence](/rust-are-we-secure-yet/cwes/cwe-41)
