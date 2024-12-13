+++
title = "CWE-23: Relative Path Traversal\n"
description = "The product uses external input to construct a pathname that should be within a restricted directory, but it does not properly neutralize sequences such as \"..\" that can resolve to a location that is outside of that directory.\n"
weight = 23

[extra]
id = 23
name = "Relative Path Traversal\n"
url = "https://cwe.mitre.org/data/definitions/23.html"
class = "Base"
rust_docs_links = []
parent = "22"

[extra.vote]
"No Help, or Langs Wont Help" = false
Discouraged = true
"Discouraged via Library" = true
"Discouraged via Borrow Checker" = false
"Discouraged via Debug Mode" = false
"Discouraged via Clippy" = false
"Virtually Impossible" = false

[extra.vector]

+++

Same as whatever is decided for [CWE-22: Path Traversal](/rust-are-we-secure-yet/cwes/cwe-22).