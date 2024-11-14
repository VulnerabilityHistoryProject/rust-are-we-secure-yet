+++
title = "CWE-78: Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection')"
description	= "The product constructs all or part of an OS command using externally-influenced input from an upstream component, but it does not neutralize or incorrectly neutralizes special elements that could modify the intended OS command when it is sent to a downstream component."
weight = 78

[extra]
id = 78
name = "Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection')"
url = "https://cwe.mitre.org/data/definitions/78.html"
vote = "Opt-In Measures Only"
clippy_helps = false
rust_docs_links = [
	"https://doc.rust-lang.org/std/process/struct.Command.html"
]
+++
Documentation has a warning about it - no real help after that?
