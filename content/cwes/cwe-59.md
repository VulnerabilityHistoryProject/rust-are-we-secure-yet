+++
title = "CWE-59: Improper Link Resolution Before File Access ('Link Following')\n"
description = "The product attempts to access a file based on the filename, but it does not properly prevent that filename from identifying a link or shortcut that resolves to an unintended resource.\n"
weight = 59

[extra]
id = 59
name = "Improper Link Resolution Before File Access ('Link Following')\n"
url = "https://cwe.mitre.org/data/definitions/59.html"
class = "Base"
rust_docs_links = [ "https://doc.rust-lang.org/stable/std/os/unix/fs/fn.symlink.html",]
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
"Attack Vector" = "LOCAL"
"Attack Complexity" = "HIGH"
"Privileges Required" = "LOW"
"User Interaction" = "NONE"
Scope = "UNCHANGED"
Confidentiality = "NONE"
Integrity = "HIGH"
Availability = "NONE"

+++

It is required to use the symlink types and "cannonalize" to resolve symlnks. There are also more filesystem functions to view meta-data with out traversing the symlink.