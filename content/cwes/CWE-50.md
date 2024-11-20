+++
title = "CWE-50: Path Equivalence: '//multiple/leading/slash'"
description	= "The product accepts path input in the form of multiple leading slash ('//multiple/leading/slash') without appropriate validation, which can lead to ambiguous path resolution and allow an attacker to traverse the file system to unintended locations or access arbitrary files."
weight = 50

[extra]
id = 50
name = "Path Equivalence: '//multiple/leading/slash'"
url = "https://cwe.mitre.org/data/definitions/50.html"
vote = "Discouraged via Borrow Checker"
clippy_helps = false
rust_docs_links = [
	
]
+++
