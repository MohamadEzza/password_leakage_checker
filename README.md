Password Leakage Checker

(Case Study)

If you want to check whether your password has been leaked—without submitting it to a random website—you can use this program to do so safely, without relying on online services you might not fully trust.

Instructions

Running from Source Code
	1.	If you’re running the program from the source code, you need to install the requests package first. Simply run:

pip install requests


	2.	You can run main.py from the src/sys_args folder with a command-line argument:

python main.py PASSWORD

	•	You can check multiple passwords at once by passing them as additional arguments.
	•	On macOS or Linux, use python3 instead of python.

Running with User Input
	•	If you prefer to enter passwords manually, run main.py from the src/input folder:

python main.py

	•	The program will prompt you to enter a password for checking.
	•	On macOS or Linux, use python3 instead of python.

Running as an Executable
	•	To run the program easily without any setup, simply execute main.exe and enter your password when prompted.