+++
title = "CWE-5: Avoid Sending Data Without Encryption"
description = "Learn how to prevent insecure data transmission in Rust by using HTTPS and secure protocols."
date = 2023-10-10T10:00:00+00:00
updated = 2023-10-10T10:00:00+00:00
draft = false
template = "blog/page.html"

[taxonomies]
authors = ["Rustaceans"]

[extra]
lead = "Sending sensitive data without encryption can expose your application to attacks. Learn how to fix this issue in Rust with HTTPS and secure practices."
+++

## What is CWE-5?

**CWE-5** refers to the risk of transmitting sensitive data over a network without encryption. When data is sent in plaintext, attackers can intercept and read or modify it during transmission. While this vulnerability is traditionally associated with J2EE applications, it applies universally to any language, including Rust.

In Rust, this issue can occur when developers use insecure protocols like HTTP instead of HTTPS or fail to encrypt sensitive data before sending it over the network.

---

### Example of the Problem

Here’s an example of insecure data transmission in Rust using the `reqwest` crate to send data over HTTP:

```rust
use reqwest::blocking::Client;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new();
    let sensitive_data = "password=supersecret"; // Sensitive data in plaintext

    // Sending sensitive data over HTTP (unencrypted)
    let response = client.post("http://example.com/api")
        .body(sensitive_data) // Data is sent in plaintext
        .send()?;

    println!("Response: {:?}", response.text()?);
    Ok(())
}
```

Why This Is Problematic?

- The data (password=supersecret) is sent over HTTP , which is unencrypted.
- An attacker could intercept the request and read the sensitive data.
- Even if HTTPS is used, sending sensitive data in plaintext can still be risky if additional protections (like encryption) are not applied.

---

### Simple Solution

To fix this issue, we need to:

1. Use HTTPS instead of HTTP.
2. Optionally, encrypt sensitive data before sending it for an extra layer of security.

Here’s the corrected code:

```rust
use reqwest::blocking::Client;
use openssl::symm::{encrypt, Cipher};

// Function to encrypt sensitive data
fn encrypt_data(data: &str, key: &[u8]) -> Vec<u8> {
    let cipher = Cipher::aes_256_cbc();
    let iv = b"0123456789abcdef"; // Initialization vector (IV)
    encrypt(cipher, key, Some(iv), data.as_bytes()).unwrap()
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new();

    // Sensitive data
    let sensitive_data = "password=supersecret";

    // Encryption key (must be securely stored in production)
    let key = b"0123456789abcdef0123456789abcdef"; // 256-bit key

    // Encrypt the sensitive data before sending
    let encrypted_data = encrypt_data(sensitive_data, key);

    // Send the encrypted data over HTTPS
    let response = client.post("https://example.com/api")
        .body(encrypted_data) // Encrypted data is sent
        .send()?;

    println!("Response: {:?}", response.text()?);
    Ok(())
}
```

1. Use HTTPS :
    - The URL is changed from http:// to https://, ensuring the data is encrypted during transmission.
2. Encrypt Sensitive Data :
    - Before sending the data, we use the openssl crate to encrypt it with AES-256-CBC.
    - This ensures that even if the data is intercepted, it cannot be read without the decryption key.
3. Initialization Vector (IV) :
    - An IV is used to make the encryption more secure. In production, the IV should be randomly generated and securely transmitted.
4. Secure Key Management :
    - The encryption key (key) must be securely stored and managed in a real-world application. Hardcoding keys in the source code is not recommended.