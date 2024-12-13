+++
title = "CWE-58: Path Equivalence: Windows 8.3 Filename\n"
description = "The product contains a protection mechanism that restricts access to a long filename on a Windows operating system, but it does not properly restrict access to the equivalent short \"8.3\" filename.\n"
weight = 58

[extra]
id = 58
name = "Path Equivalence: Windows 8.3 Filename\n"
url = "https://cwe.mitre.org/data/definitions/58.html"
class = "Variant"
rust_docs_links = []
parent = "41"

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

Same as whatever is decided for base [CWE-41: Improper Resolution of Path Equivalence](/rust-are-we-secure-yet/cwes/cwe-41)