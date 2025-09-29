<div align="center">
		<img src="https://img.shields.io/pypi/v/CaesarCipher?color=blue" alt="PyPI version" />
		<img src="https://img.shields.io/github/license/ViratiAkiraNandhanReddy/CaesarCipher.encryption" alt="License" />
		<!-- <img src="https://img.shields.io/github/actions/workflow/status/ViratiAkiraNandhanReddy/CaesarCipher.encryption/python-app.yml?label=build" alt="Build Status" /> -->
		<img src="https://img.shields.io/github/actions/workflow/status/ViratiAkiraNandhanReddy/CaesarCipher.encryption/tests.yml?label=tests" alt="Test Status" />
		<img src="https://img.shields.io/pypi/dm/CaesarCipher" alt="PyPI Downloads" />
		<!-- <img src="https://img.shields.io/github/last-commit/ViratiAkiraNandhanReddy/CaesarCipher.encryption" alt="Last Commit" /> -->
		<img src="https://img.shields.io/github/issues/ViratiAkiraNandhanReddy/CaesarCipher.encryption" alt="Issues" />
		<img src="https://img.shields.io/github/stars/ViratiAkiraNandhanReddy/CaesarCipher.encryption?style=social" alt="Stars" />
	<h1>CaesarCipher.encryption</h1>
	<p><em>Simple, creative, and practical Caesar cipher encryption for Python projects.</em></p>
</div>

---

## 🚀 Why CaesarCipher?

Ever wanted to add a layer of protection to your data without the complexity of modern cryptography? CaesarCipher.encryption brings the classic Caesar cipher to Python, making it easy to obfuscate text, passwords, usernames, and more. It's not military-grade, but it's a huge step up from plain text!

---

## 🔑 What is the Caesar Cipher?

The Caesar cipher is one of the oldest and simplest encryption techniques. Each character in your text is shifted by a fixed number of positions. This package extends the classic algorithm to support:

- **Letters** (upper & lower case)
- **Digits** (optional)
- **Symbols** (optional)
	- Symbols <br>
	- Emojis (some support)

You choose what gets encrypted and how!

---

## ✨ Features

- Encrypt and decrypt text with a customizable shift
- Optionally include digits and symbols
- Input validation for safety
- Intuitive API for quick integration
- Perfect for small to mid-scale projects
- Much better than storing plain text

---

## 📦 Installation

Install from PyPI:

```bash
pip install CaesarCipher
```

Or clone from GitHub:

```bash
git clone https://github.com/ViratiAkiraNandhanReddy/CaesarCipher.encryption.git
cd CaesarCipher.encryption
```

---

## 🛠️ Usage

### Encrypting Text

```python
from CaesarCipher import Encryption

# Basic encryption
enc = Encryption("Hello, World! 123")
print("Encrypted:", enc.encrypt())

# Advanced: shift everything
enc2 = Encryption("Secret123!", shift = 7, alterNumbers = True, alterSymbols = True)
print("Encrypted:", enc2.encrypt())
```

### Decrypting Text

```python
from CaesarCipher import Decryption

# Basic decryption
dec = Decryption("Olssv, Dvysk! 890", shift = 7, isNumbersAltered = True, isSymbolsAltered = True)
print("Decrypted:", dec.decrypt())
```

---

## 📚 API Reference

### Encryption

```python
Encryption(text: str, shift: int = 3, alterSymbols: bool = False, alterNumbers: bool = False)
```

- `text`: The string to encrypt
- `shift`: How many positions to shift (default: 3)
- `alterSymbols`: Shift symbols? (default: False)
- `alterNumbers`: Shift digits? (default: False)

#### `.encrypt() -> str`
Returns the encrypted string.

### Decryption

```python
Decryption(text: str, shift: int = 3, isSymbolsAltered: bool = False, isNumbersAltered: bool = False)
```

- `text`: The string to decrypt
- `shift`: How many positions to shift back (default: 3)
- `isSymbolsAltered`: Were symbols shifted? (default: False)
- `isNumbersAltered`: Were digits shifted? (default: False)

#### `.decrypt() -> str`
Returns the decrypted string.

---

## 🔍 Comparison Table

See how CaesarCipher transforms your data:

| Stage                | Example Text                |
|----------------------|---------------------------- |
| **Original**         | HelloWorld123!              |
| **After Encryption** | KhoorZruog456!              |
| **After Decryption** | HelloWorld123!              |

**How it works:**
- Encryption shifts each character by a fixed amount (default: 3).
- Decryption reverses the shift, restoring the original text.

You can customize the shift and choose to include digits and symbols for even more flexibility!

---

## ⚠️ Limitations & Security

- **Not for high-security needs!** Vulnerable to brute-force and frequency analysis.
- Symbol shifting may produce non-printable characters.
- For real password storage, use cryptographic hashes (bcrypt, Argon2, etc).

---

## 💡 When Should You Use This?

- Small to mid-scale projects
- Obfuscating sensitive data (usernames, passwords, tokens)
- Educational demos
- Quick-and-dirty protection for logs or configs

Some encryption is always better than none. This package is a practical upgrade from plain text!

---

## 🌐 Social & Links


<p align="center">
	<a href="https://www.linkedin.com/in/viratiakiranandhanreddy/">
		<img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white"/>
	</a>
	<a href="https://x.com/Viratiaki53">
		<img src="https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=x&logoColor=white"/>
	</a>
	<a href="https://instagram.com/viratiaki53">
		<img src="https://img.shields.io/badge/Instagram-E1306C?style=for-the-badge&logo=instagram&logoColor=white"/>
	</a>
	<a href="https://facebook.com/ViratiAkiraNandhanReddy">
		<img src="https://img.shields.io/badge/Facebook-1877F2?style=for-the-badge&logo=facebook&logoColor=white"/>
	</a>
	<a href="https://gist.github.com/ViratiAkiraNandhanReddy">
		<img src="https://img.shields.io/badge/-My%20Latest%20Gists-2b3137?style=for-the-badge&logo=github&logoColor=white"/>
	</a>
    <a href="https://github.com/ViratiAkiraNandhanReddy/CaesarCipher.encryption">
        <img src="https://img.shields.io/badge/Repository-333?style=for-the-badge&logo=github&logoColor=white"/>
    </a>
    <a href="https://viratiakiranandhanreddy.github.io/CaesarCipher.encryption/">
        <img src="https://img.shields.io/badge/Website-0077b6?style=for-the-badge&logo=google-chrome&logoColor=white"/>
    </a>
    <a href="https://pypi.org/project/CaesarCipher/">
        <img src="https://img.shields.io/badge/PyPI-3775A9?style=for-the-badge&logo=pypi&logoColor=white"/>
    </a>
    <a href="mailto:viratiaki@gmail.com">
        <img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white"/>
    </a>
</p>

---

## 📝 License

***This project is licensed under the `GNU GENERAL PUBLIC LICENSE`.***

---

## 👤 Author

### Created and maintained by [ViratiAkiraNandhanReddy](https://github.com/ViratiAkiraNandhanReddy)

---

<h3 align="center"> Questions, suggestions, or want to contribute? Open an issue or pull request on GitHub! </h3>

<p align="center"> <img src="https://capsule-render.vercel.app/api?type=waving&color=0e8fff&height=100&section=footer" width="100%" /> </p> 