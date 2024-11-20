+++
title = "CWE-48: Path Equivalence: 'file name' (Internal Whitespace)"
description	= "The product accepts path input in the form of internal space ('file(SPACE)name') without appropriate validation, which can lead to ambiguous path resolution and allow an attacker to traverse the file system to unintended locations or access arbitrary files."
weight = 48

[extra]
id = 48
name = "Path Equivalence: 'file name' (Internal Whitespace)"
url = "https://cwe.mitre.org/data/definitions/48.html"
vote = "Discouraged via Borrow Checker"
clippy_helps = false
rust_docs_links = [
	
]
+++
