+++
title = "CWE-65: Windows Hard Link\n"
description = "The product, when opening a file or directory, does not sufficiently handle when the name is associated with a hard link to a target that is outside of the intended control sphere. This could allow an attacker to cause the product to operate on unauthorized files.\n"
weight = 65

[extra]
id = 65
name = "Windows Hard Link\n"
url = "https://cwe.mitre.org/data/definitions/65.html"
class = "Variant"
rust_docs_links = []
parent = "59"

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