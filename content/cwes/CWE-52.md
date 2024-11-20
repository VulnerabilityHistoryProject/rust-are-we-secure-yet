+++
title = "CWE-52: Path Equivalence: '/multiple/trailing/slash//'"
description	= "The product accepts path input in the form of multiple trailing slash ('/multiple/trailing/slash//') without appropriate validation, which can lead to ambiguous path resolution and allow an attacker to traverse the file system to unintended locations or access arbitrary files."
weight = 52

[extra]
id = 52
name = "Path Equivalence: '/multiple/trailing/slash//'"
url = "https://cwe.mitre.org/data/definitions/52.html"
vote = "Discouraged via Borrow Checker"
clippy_helps = false
rust_docs_links = [
	
]
+++
