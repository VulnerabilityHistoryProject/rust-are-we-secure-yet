+++
title = "CWE-30: Path Traversal: '\\dir\\..\\filename'\n"
description = "The product uses external input to construct a pathname that should be within a restricted directory, but it does not properly neutralize '\\dir\\..\\filename' (leading backslash dot dot) sequences that can resolve to a location that is outside of that directory.\n"
weight = 30

[extra]
id = 30
name = "Path Traversal: '\\dir\\..\\filename'\n"
url = "https://cwe.mitre.org/data/definitions/30.html"
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