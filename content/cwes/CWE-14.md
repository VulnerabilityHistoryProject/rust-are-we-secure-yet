+++
title = "CWE-14: Compiler Removal of Code to Clear Buffers"
description	= "Sensitive memory is cleared according to the source code, but compiler optimizations leave the memory untouched when it is not read from again, aka dead store removal."
weight = 14

[extra]
id = 14
name = "Compiler Removal of Code to Clear Buffers"
url = "https://cwe.mitre.org/data/definitions/14.html"
vote = "No Help, or Langs Won't Help"
clippy_helps = false
rust_docs_links = [
	
]
+++

