# Password Leakage Checker  

*(Case Study)*  

If you want to check whether your password has been leaked—without submitting it to a random website—you can use this program to do so safely, without relying on online services you might not fully trust.  

## Installation  

### Running from Source Code  
1. Install the required dependency:  

   ```bash
   pip install requests
   ```  

2. Run `main.py` from the `src/sys_args` folder with a command-line argument:  

   ```bash
   python main.py PASSWORD
   ```  

   - You can check multiple passwords at once by passing them as additional arguments.  
   - On macOS or Linux, use `python3` instead of `python`.  

### Running with User Input  
- If you prefer to enter passwords manually, run `main.py` from the `src/input` folder:  

   ```bash
   python main.py
   ```  

   - The program will prompt you to enter a password for checking.  
   - On macOS or Linux, use `python3` instead of `python`.  

### Running as an Executable  
- To run the program easily without any setup, simply execute:  

   ```bash
   main.exe
   ```  

   - Enter your password when prompted.  

## License  
This project is open-source. Feel free to modify and contribute!  