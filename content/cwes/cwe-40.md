+++
title = "CWE-40: Path Traversal: '\\\\UNC\\share\\name\\' (Windows UNC Share)\n"
description = "The product accepts input that identifies a Windows UNC share ('\\\\UNC\\share\\name') that potentially redirects access to an unintended location or arbitrary file.\n"
weight = 40

[extra]
id = 40
name = "Path Traversal: '\\\\UNC\\share\\name\\' (Windows UNC Share)\n"
url = "https://cwe.mitre.org/data/definitions/40.html"
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