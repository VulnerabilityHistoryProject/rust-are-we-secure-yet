+++
title = '''
CWE-64: Windows Shortcut Following (.LNK)
'''
description	= '''
The product, when opening a file or directory, does not sufficiently handle when the file is a Windows shortcut (.LNK) whose target is outside of the intended control sphere. This could allow an attacker to cause the product to operate on unauthorized files.
'''
weight = 64

[extra]
id = 64
name = '''
Windows Shortcut Following (.LNK)
'''
url = "https://cwe.mitre.org/data/definitions/64.html"
vote = "Discouraged via Borrow Checker"
class = "Variant"
clippy_helps = false
rust_docs_links = [
	
]
+++
