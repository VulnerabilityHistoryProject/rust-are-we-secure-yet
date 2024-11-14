+++
title = "CWE-89: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')"
description	= "The product constructs all or part of an SQL command using externally-influenced input from an upstream component, but it does not neutralize or incorrectly neutralizes special elements that could modify the intended SQL command when it is sent to a downstream component. Without sufficient removal or quoting of SQL syntax in user-controllable inputs, the generated SQL query can cause those inputs to be interpreted as SQL instead of ordinary user data."
weight = 89

[extra]
id = 89
name = "Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')"
url = "https://cwe.mitre.org/data/definitions/89.html"
vote = "No Help, or Langs Won't Help"
clippy_helps = false
rust_docs_links = [
	
]
+++
SQL isn't in std
