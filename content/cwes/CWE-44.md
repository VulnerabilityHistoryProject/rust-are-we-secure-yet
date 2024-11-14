+++
title = "CWE-44: Path Equivalence: 'file.name' (Internal Dot)"
description	= "The product accepts path input in the form of internal dot ('file.ordir') without appropriate validation, which can lead to ambiguous path resolution and allow an attacker to traverse the file system to unintended locations or access arbitrary files."
weight = 44

[extra]
id = 44
name = "Path Equivalence: 'file.name' (Internal Dot)"
url = "https://cwe.mitre.org/data/definitions/44.html"
vote = "Discouraged via Borrow Checker"
clippy_helps = false
rust_docs_links = [
	
]
+++

