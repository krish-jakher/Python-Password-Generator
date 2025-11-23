
# Python password generator 



# 🔐 Secure Password Generator

A robust and secure password generator written in Python. This script generates random, high-entropy passwords of a user-specified length, ensuring the inclusion of uppercase letters, lowercase letters, digits, and special symbols.

## 🚀 Features

  * **Cryptographically Secure:** Uses the Python `secrets` library (instead of the standard `random` library) to generate unpredictable passwords suitable for managing sensitive data.
  * **Customizable Length:** Users can define the length of the password (minimum 4 characters).
  * **Guaranteed Complexity:** Every generated password is guaranteed to contain at least:
      * 1 Uppercase letter
      * 1 Lowercase letter
      * 1 Digit
      * 1 Special symbol
  * **Input Validation:** Robust error handling ensures the user inputs valid integers.

## 🛠️ Prerequisites

  * **Python 3.6+** is required (as the `secrets` module was introduced in Python 3.6).
  * No external libraries are required (uses standard `string` and `secrets` modules).

## 💻 Installation & Usage

1.  **Save the script:**
    Save your Python code into a file, for example: `password_generator.py`.

2.  **Run the script:**
    Open your terminal or command prompt, navigate to the folder containing the file, and run:

    ```bash
    python password_generator.py
    ```

3.  **Follow the prompts:**
    Enter your desired password length when prompted.

    ```text
    Enter the desired password length (must be >=4): 12
    ```

## 📝 How It Works

The script follows a 4-step process to ensure security and randomness:

1.  **Input Collection:** It asks the user for a length and validates that it is a number greater than or equal to 4.
2.  **Mandatory Selection:** It first selects one character from each category (Lower, Upper, Digit, Symbol) to ensure the password meets standard complexity requirements.
3.  **Pool Filling:** It fills the remaining length of the password with random characters selected from a combined pool of all character types.
4.  **Shuffling:** Finally, it uses `secrets.SystemRandom().shuffle()` to mix the mandatory characters with the random ones, preventing the password from having a predictable structure (e.g., ensuring the first character isn't always a lowercase letter).

## 📄 Example Output

```text
Enter the desired password length (must be >=4): 16

Generated secure password (Length:16): m$9Lp#v2!QzX7@kR
```

## ⚠️ Why use `secrets` instead of `random`?

This script uses the `secrets` module, which is designed specifically for cryptography. The standard `random` module in Python is pseudo-random and predictable if enough data is analyzed. `secrets` uses the operating system's most secure source of randomness, making these passwords safe for real-world use.

## 📜 License

This project is open-source and free to use.

-----


