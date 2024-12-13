+++
title = "CWE-32: Path Traversal: '...' (Triple Dot)\n"
description = "The product uses external input to construct a pathname that should be within a restricted directory, but it does not properly neutralize '...' (triple dot) sequences that can resolve to a location that is outside of that directory.\n"
weight = 32

[extra]
id = 32
name = "Path Traversal: '...' (Triple Dot)\n"
url = "https://cwe.mitre.org/data/definitions/32.html"
class = "Variant"
rust_docs_links = []
parent = "23"

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