+++
title = '''
CWE-22: Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal')
'''
description	= '''
The product uses external input to construct a pathname that is intended to identify a file or directory that is located underneath a restricted parent directory, but the product does not properly neutralize special elements within the pathname that can cause the pathname to resolve to a location that is outside of the restricted directory.
'''
weight = 22

[extra]
id = 22
name = '''
Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal')
'''
url = "https://cwe.mitre.org/data/definitions/22.html"
vote = "Discouraged via Borrow Checker"
class = "Base"
clippy_helps = false
rust_docs_links = [
	"https://doc.rust-lang.org/std/path/struct.PathBuf.html"
]
+++
There is SOME discouragement via typing