# Password Leakage Checker  

*A simple tool to check if your password has been leaked without relying on untrusted online services.*  

## Features  
- Check if your password has been compromised without sharing it with third-party websites.  
- Works with both command-line arguments and manual input.  
- Provides a simple executable for easy usage.  

## Installation  

### Running from Source Code  
1. Install the required dependencies:  
   ```bash
   pip install requests

2.	Run the script with a password as a command-line argument:
   ```bash
   python main.py PASSWORD

•	You can check multiple passwords at once by passing them as additional arguments.
•	On macOS or Linux, use python3 instead of python.

Running with User Input
•	If you prefer manual input, run:
   ```bash
   python main.py

•	The program will prompt you to enter a password.
•	On macOS or Linux, use python3 instead of python.

Running as an Executable
	•	To run the program without any setup, execute:

   main.exe

	•	Enter your password when prompted.