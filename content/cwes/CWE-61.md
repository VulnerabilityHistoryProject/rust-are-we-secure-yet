+++
title = "CWE-61: UNIX Symbolic Link (Symlink) Following"
description	= "The product, when opening a file or directory, does not sufficiently account for when the file is a symbolic link that resolves to a target outside of the intended control sphere. This could allow an attacker to cause the product to operate on unauthorized files."
weight = 61

[extra]
id = 61
name = "UNIX Symbolic Link (Symlink) Following"
url = "https://cwe.mitre.org/data/definitions/61.html"
vote = "Discouraged via Borrow Checker"
clippy_helps = false
rust_docs_links = [
	
]
+++

