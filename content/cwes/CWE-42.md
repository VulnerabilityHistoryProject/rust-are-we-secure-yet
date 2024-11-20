+++
title = "CWE-42: Path Equivalence: 'filename.' (Trailing Dot)"
description	= "The product accepts path input in the form of trailing dot ('filedir.') without appropriate validation, which can lead to ambiguous path resolution and allow an attacker to traverse the file system to unintended locations or access arbitrary files."
weight = 42

[extra]
id = 42
name = "Path Equivalence: 'filename.' (Trailing Dot)"
url = "https://cwe.mitre.org/data/definitions/42.html"
vote = "Discouraged via Borrow Checker"
clippy_helps = false
rust_docs_links = [
	
]
+++
