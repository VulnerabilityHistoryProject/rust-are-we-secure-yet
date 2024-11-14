+++
title = "CWE-23: Relative Path Traversal"
description	= "The product uses external input to construct a pathname that should be within a restricted directory, but it does not properly neutralize sequences such as .. that can resolve to a location that is outside of that directory."
weight = 23

[extra]
id = 23
name = "Relative Path Traversal"
url = "https://cwe.mitre.org/data/definitions/23.html"
vote = "Discouraged via Borrow Checker"
clippy_helps = false
rust_docs_links = [
	
]
+++
Same as above whatever we decide
