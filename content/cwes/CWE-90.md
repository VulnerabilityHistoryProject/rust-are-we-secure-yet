+++
title = "CWE-90: Improper Neutralization of Special Elements used in an LDAP Query ('LDAP Injection')"
description	= "The product constructs all or part of an LDAP query using externally-influenced input from an upstream component, but it does not neutralize or incorrectly neutralizes special elements that could modify the intended LDAP query when it is sent to a downstream component."
weight = 90

[extra]
id = 90
name = "Improper Neutralization of Special Elements used in an LDAP Query ('LDAP Injection')"
url = "https://cwe.mitre.org/data/definitions/90.html"
vote = "No Help, or Langs Won't Help"
clippy_helps = false
rust_docs_links = [
	
]
+++
LDAP isn't in std
