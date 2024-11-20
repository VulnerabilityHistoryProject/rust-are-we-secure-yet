+++
title = '''
CWE-95: Improper Neutralization of Directives in Dynamically Evaluated Code ('Eval Injection')
'''
description	= '''
The product receives input from an upstream component, but it does not neutralize or incorrectly neutralizes code syntax before using the input in a dynamic evaluation call (e.g. "eval").
'''
weight = 95

[extra]
id = 95
name = '''
Improper Neutralization of Directives in Dynamically Evaluated Code ('Eval Injection')
'''
url = "https://cwe.mitre.org/data/definitions/95.html"
vote = "Virtually Impossible"
class = "Variant"
clippy_helps = false
rust_docs_links = [
	
]
+++
