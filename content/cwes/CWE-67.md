+++
title = "CWE-67: Improper Handling of Windows Device Names"
description	= "The product constructs pathnames from user input, but it does not handle or incorrectly handles a pathname containing a Windows device name such as AUX or CON. This typically leads to denial of service or an information exposure when the application attempts to process the pathname as a regular file."
weight = 67

[extra]
id = 67
name = "Improper Handling of Windows Device Names"
url = "https://cwe.mitre.org/data/definitions/67.html"
vote = "No Help, or Langs Won't Help"
clippy_helps = false
rust_docs_links = [
	
]
+++

