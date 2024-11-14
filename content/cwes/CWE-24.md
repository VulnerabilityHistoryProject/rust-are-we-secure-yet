+++
title = "CWE-24: Relative Path Traversal"
description	= "The product uses external input to construct a pathname that should be within a restricted directory, but it does not properly neutralize ../ sequences that can resolve to a location that is outside of that directory."
weight = 24

[extra]
id = 24
name = "Relative Path Traversal"
url = "https://cwe.mitre.org/data/definitions/24.html"
vote = "Discouraged via Borrow Checker"
clippy_helps = false
rust_docs_links = [
	
]
+++

