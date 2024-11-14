+++
title = "CWE-36: Absolute Path Traversal"
description	= "The product uses external input to construct a pathname that should be within a restricted directory, but it does not properly neutralize absolute path sequences such as /abs/path that can resolve to a location that is outside of that directory."
weight = 36

[extra]
id = 36
name = "Absolute Path Traversal"
url = "https://cwe.mitre.org/data/definitions/36.html"
vote = "Discouraged via Borrow Checker"
clippy_helps = false
rust_docs_links = [
	
]
+++
Same as above whatever we decide
