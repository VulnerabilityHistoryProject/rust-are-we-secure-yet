+++
title = "CWE-66: Improper Handling of File Names that Identify Virtual Resources\n"
description = "The product does not handle or incorrectly handles a file name that identifies a \"virtual\" resource that is not directly specified within the directory that is associated with the file name, causing the product to perform file-based operations on a resource that is not a file.\n"
weight = 66

[extra]
id = 66
name = "Improper Handling of File Names that Identify Virtual Resources\n"
url = "https://cwe.mitre.org/data/definitions/66.html"
class = "Base"
rust_docs_links = []
parent = "706"

[extra.vote]
"No Help, or Langs Wont Help" = true
Discouraged = false
"Discouraged via Library" = false
"Discouraged via Borrow Checker" = false
"Discouraged via Debug Mode" = false
"Discouraged via Clippy" = false
"Virtually Impossible" = false

[extra.vector]

+++