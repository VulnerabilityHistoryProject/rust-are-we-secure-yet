+++
title = "CWE-36: Absolute Path Traversal\n"
description = "The product uses external input to construct a pathname that should be within a restricted directory, but it does not properly neutralize absolute path sequences such as \"/abs/path\" that can resolve to a location that is outside of that directory.\n"
weight = 36

[extra]
id = 36
name = "Absolute Path Traversal\n"
url = "https://cwe.mitre.org/data/definitions/36.html"
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

Same as above whatever we decide