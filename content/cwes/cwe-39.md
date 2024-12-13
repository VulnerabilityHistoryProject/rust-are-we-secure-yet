+++
title = "CWE-39: Path Traversal: 'C:dirname'\n"
description = "The product accepts input that contains a drive letter or Windows volume letter ('C:dirname') that potentially redirects access to an unintended location or arbitrary file.\n"
weight = 39

[extra]
id = 39
name = "Path Traversal: 'C:dirname'\n"
url = "https://cwe.mitre.org/data/definitions/39.html"
class = "Variant"
rust_docs_links = []
parent = "36"

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