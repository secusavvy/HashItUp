# HashItUp

HashItUp is a simple Python script that allows users to hash their messages using the SHA-256 algorithm. It provides a basic command-line interface where users can input their message, and the script will compute and display the corresponding SHA-256 hash.

### Features
- Hash any textual message using SHA-256.
- Simple and straightforward command-line interface.
- Delays between messages for a conversational effect.

### Technologies Used
- Python 3
- hashlib library for hashing

### Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/0xRekin/HashItUp.git
   cd HashItUp
   ```

2. Run the script:
   ```bash
   Code.py
   ```

3. Follow the prompts to enter your message.

4. The script will compute the SHA-256 hash of your message and display it.

### How It Works
- The script starts by introducing itself and explaining its purpose.
- It prompts the user to input a message.
- It encodes the message into bytes and computes its SHA-256 hash using the `hashlib` library.
- Finally, it displays the computed hash value in hexadecimal format.
