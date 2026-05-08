# Smart Parking Blockchain System

## Overview

The Smart Parking Blockchain System is a Python-based mini project developed using blockchain technology concepts. This project securely stores parking transaction records using SHA-256 hashing and linked blockchain blocks.

Each parking transaction is stored as a separate block containing:

* Vehicle Number
* Parking Amount
* Parking Slot
* Timestamp
* Previous Hash
* Current Hash

The blockchain structure helps maintain data integrity and security by linking every block with the previous block hash.

This project is suitable for:

* Blockchain beginners
* Python mini projects
* Academic lab experiments
* Cryptocurrency and Blockchain Technologies subject
* Blockchain concept demonstrations

---

# Features

* Blockchain-based parking transaction storage
* SHA-256 hashing algorithm
* Genesis block creation
* Dynamic parking record addition
* Previous hash linking
* Secure transaction validation
* Simple and easy-to-understand Python code
* Console-based application
* Lightweight and beginner-friendly

---

# Technologies Used

* Python 3
* hashlib
* datetime

---

# Project Structure

```text
smart-parking-blockchain-system/
│
├── parking_blockchain.py
├── README.md
└── screenshots/
```

---

# Requirements

Before running the project, ensure the following software is installed:

* Python 3.x

Check Python installation:

```bash
python --version
```

---

# Installation Steps

## Step 1: Clone the Repository

```bash
git clone https://github.com/TAMILKINGHACKER/smart-parking-blockchain-system.git
```

---

## Step 2: Navigate to Project Directory

```bash
cd smart-parking-blockchain-system
```

---

## Step 3: Run the Python Program

```bash
python parking_blockchain.py
```

---

# How the System Works

1. The program creates a Genesis Block.
2. User enters parking transaction details.
3. Each transaction becomes a new block.
4. SHA-256 hashing generates a unique hash value.
5. Each block stores the previous block hash.
6. Blockchain records are displayed securely.

---

# Sample Input

```text
Enter Number of Vehicles : 2

Enter Vehicle Number : TN19AB1234
Enter Parking Amount : 50
Enter Parking Slot : A1

Enter Vehicle Number : TN22CD5678
Enter Parking Amount : 100
Enter Parking Slot : B2
```

---

# Sample Output

```text
SMART PARKING BLOCKCHAIN RECORDS

Block Index : 1
Vehicle No  : TN19AB1234
Amount      : 50
Slot        : A1
Previous Hash : 8f4a1d...
Current Hash  : a4c78b...

--------------------------------------------------

Block Index : 2
Vehicle No  : TN22CD5678
Amount      : 100
Slot        : B2
Previous Hash : a4c78b...
Current Hash  : 98d5ef...
```

---

# Blockchain Concepts Used

## Genesis Block

The first block in the blockchain created manually.

## SHA-256 Hashing

Used to generate secure hash values for every block.

## Previous Hash Linking

Every block stores the previous block hash to maintain chain integrity.

## Data Integrity

If any block data changes, the hash value changes, making tampering detectable.

---

# Educational Purpose

This project was developed for educational and learning purposes to demonstrate:

* Basic blockchain concepts
* Hash generation
* Block linking
* Secure transaction storage

---

# Future Improvements

Possible future enhancements:

* GUI Interface
* Database Integration
* QR-based parking system
* Vehicle entry/exit tracking
* Real-time blockchain validation
* Smart contract integration
* Web-based dashboard

---

# Author

Krishnamoorthy G
B.E CSE (Cyber Security)

---

# License

This project is licensed under the MIT License.
