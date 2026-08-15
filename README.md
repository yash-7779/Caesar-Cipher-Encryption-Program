# Caesar Cipher Encryption Program

A simple Python implementation of the **Caesar Cipher** that can be used to encrypt and decrypt messages using a specified shift amount.

## Features

* Encrypt messages using a Caesar Cipher.
* Decrypt previously encrypted messages.
* Accepts a custom shift amount.
* Preserves spaces, numbers, and other non-alphabetic characters.
* Allows the user to run the program multiple times.
* Displays a goodbye message when the user exits.

## How Caesar Cipher Works

The Caesar Cipher is a substitution cipher in which each letter in a message is shifted by a fixed number of positions in the alphabet.

For example, with a shift of `3`:

```text
a → d
b → e
c → f
...
x → a
y → b
z → c
```

### Example

```text
Original:  hello
Shift:     3
Encoded:   khoor
```

To decode the message, the same shift is applied in the opposite direction:

```text
Encoded:   khoor
Shift:     3
Decoded:   hello
```

## Requirements

* Python 3.x

No external libraries are required.

## How to Run

1. Make sure Python 3 is installed.
2. Open a terminal in the directory containing `DAY8.py`.
3. Run:

```bash
python DAY8.py
```

## Usage

When the program starts, enter:

```text
Enter your message:
```

Then enter the desired shift amount:

```text
Enter shift amount:
```

Finally, choose whether you want to encode or decode:

```text
Type 'encode' to encrypt or 'decode' to derypt the message:
```

### Example Run

```text
Enter your message: hello world
Enter shift amount: 3
Type 'encode' to encrypt or 'decode' to derypt the message: encode

The encoded message is 'khoor zruog'.
```

The program then asks:

```text
Type 'yes' if you want to go again. otherwise type 'no':
```

Enter `yes` to perform another encryption/decryption operation or `no` to exit.

## Program Structure

### `alphabets`

The program stores the English alphabet in a list:

```python
alphabets = ['a', 'b', 'c', ..., 'z']
```

### `cipher()`

The main function is:

```python
cipher(text, shift_amount, direction)
```

It takes three parameters:

* `text` — The message to encrypt or decrypt.
* `shift_amount` — The number of positions by which letters are shifted.
* `direction` — Either `encode` or `decode`.

### Encoding

When the direction is `encode`, the program moves each alphabetic character forward by the specified shift amount.

### Decoding

When the direction is `decode`, the program moves each alphabetic character backward by the specified shift amount.

### Repeating the Program

A `while` loop allows the user to use the cipher repeatedly until they enter `no`.

## Important Notes

* The program converts the entered message to lowercase.
* Characters that are not present in the alphabet list are left unchanged.
* Large positive shift values are handled by repeatedly subtracting `26` during encoding.
* The program is intended as a learning project demonstrating functions, loops, conditionals, lists, strings, and user input.

## Concepts Demonstrated

This project demonstrates several Python concepts:

* Variables
* Lists
* Functions
* Parameters and arguments
* `if`, `elif`, and `else`
* `for` loops
* `while` loops
* String manipulation
* User input
* Type conversion using `int()`
* Boolean control variables

## File

```text
Cipher.py
```

## License

This project is intended for educational and learning purposes.
