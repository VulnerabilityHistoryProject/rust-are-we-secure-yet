+++
title = "CWE-30: Path Traversal: 'dir..filename'"
description	= "The product uses external input to construct a pathname that should be within a restricted directory, but it does not properly neutralize 'dir..filename' (leading backslash dot dot) sequences that can resolve to a location that is outside of that directory."
weight = 30

[extra]
id = 30
name = "Path Traversal: 'dir..filename'"
url = "https://cwe.mitre.org/data/definitions/30.html"
vote = "Discouraged via Borrow Checker"
clippy_helps = false
rust_docs_links = [
	
]
+++
