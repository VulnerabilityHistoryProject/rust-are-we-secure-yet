+++
title = '''
CWE-93: Improper Neutralization of CRLF Sequences ('CRLF Injection')
'''
description	= '''
The product uses CRLF (carriage return line feeds) as a special element, e.g. to separate lines or records, but it does not neutralize or incorrectly neutralizes CRLF sequences from inputs.
'''
weight = 93

[extra]
id = 93
name = '''
Improper Neutralization of CRLF Sequences ('CRLF Injection')
'''
url = "https://cwe.mitre.org/data/definitions/93.html"
vote = "No Help, or Langs Won't Help"
class = "Base"
clippy_helps = false
rust_docs_links = [
	
]
+++
Not really. Strings are pretty standard.