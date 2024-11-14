+++
title = "CWE-28: Path Traversal: '..filedir'"
description	= "The product uses external input to construct a pathname that should be within a restricted directory, but it does not properly neutralize .. sequences that can resolve to a location that is outside of that directory."
weight = 28

[extra]
id = 28
name = "Path Traversal: '..filedir'"
url = "https://cwe.mitre.org/data/definitions/28.html"
vote = "Discouraged via Borrow Checker"
clippy_helps = false
rust_docs_links = [
	
]
+++

