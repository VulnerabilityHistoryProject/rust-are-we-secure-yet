+++
title = "CWE-41: Improper Resolution of Path Equivalence\n"
description = "The product is vulnerable to file system contents disclosure through path equivalence. Path equivalence involves the use of special characters in file and directory names. The associated manipulations are intended to generate multiple names for the same object.\n"
weight = 41

[extra]
id = 41
name = "Improper Resolution of Path Equivalence\n"
url = "https://cwe.mitre.org/data/definitions/41.html"
class = "Base"
rust_docs_links = []
parent = "706"

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