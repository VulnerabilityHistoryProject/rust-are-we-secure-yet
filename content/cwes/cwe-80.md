+++
title = '''
CWE-80: Improper Neutralization of Script-Related HTML Tags in a Web Page (Basic XSS)
'''
description	= '''
The product receives input from an upstream component, but it does not neutralize or incorrectly neutralizes special characters such as "<", ">", and "&" that could be interpreted as web-scripting elements when they are sent to a downstream component that processes web pages.
'''
weight = 80

[extra]
id = 80
name = '''
Improper Neutralization of Script-Related HTML Tags in a Web Page (Basic XSS)
'''
url = "https://cwe.mitre.org/data/definitions/80.html"
vote = "No Help, or Langs Won't Help"
class = "Variant"
clippy_helps = false
rust_docs_links = [
	
]
+++
