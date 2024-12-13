+++
title = "CWE-22: Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal')\n"
description = "The product uses external input to construct a pathname that is intended to identify a file or directory that is located underneath a restricted parent directory, but the product does not properly neutralize special elements within the pathname that can cause the pathname to resolve to a location that is outside of the restricted directory.\n"
weight = 22

[extra]
id = 22
name = "Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal')\n"
url = "https://cwe.mitre.org/data/definitions/22.html"
class = "Base"
rust_docs_links = [ "https://doc.rust-lang.org/std/path/struct.PathBuf.html",]
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
"Attack Vector" = "NETWORK"
"Attack Complexity" = "MEDIUM"
Confidentiality = "NONE"
Integrity = "PARTIAL"
Availability = "NONE"

+++

There is SOME discouragement via typing