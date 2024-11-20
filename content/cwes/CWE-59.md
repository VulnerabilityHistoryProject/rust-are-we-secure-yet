+++
title = '''
CWE-59: Improper Link Resolution Before File Access ('Link Following')
'''
description	= '''
The product attempts to access a file based on the filename, but it does not properly prevent that filename from identifying a link or shortcut that resolves to an unintended resource.
'''
weight = 59

[extra]
id = 59
name = '''
Improper Link Resolution Before File Access ('Link Following')
'''
url = "https://cwe.mitre.org/data/definitions/59.html"
vote = "Discouraged via Borrow Checker"
class = "Base"
clippy_helps = false
rust_docs_links = [
	"https://doc.rust-lang.org/stable/std/os/unix/fs/fn.symlink.html"
]
+++
It is required to use the symlink types and "cannonalize" to resolve symlnks. There are also more filesystem functions to view meta-data with out traversing the symlink.