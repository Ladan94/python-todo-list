# To-Do List CLI Project 🚀
### Debugging & Troubleshooting Experience

During the development of this project, I encountered several issues and worked through them step by step. Here are some of the most significant challenges I faced and how I solved them:

### 🔍 Challenges I Encountered:
1️⃣ Program only echoed the input number without executing any functionality.  
   🔹 Issue: The choice variable was not processed correctly, and the program would just display the input instead of executing any logic.  
   🔹 Solution: Converted choice to an integer using int(input()) and ensured proper condition checks.

2️⃣ Program worked in Code Runner but not in PowerShell.  
   🔹 Issue: The correct Python interpreter was not selected in VS Code.  
   🔹 Solution: Selected the right Python interpreter and verified the version using python --version.

3️⃣ Error: `name 'name' is not defined` in `if __name__ == "__main__":`  
   🔹 Issue: Incorrect typing of __name__ (extra spaces or incorrect characters).  
   🔹 Solution: Fixed the statement if __name__ == "__main__": and tested by printing print(__name__) to verify execution.

### ✅ Lessons Learned:
After resolving these issues, the program finally worked as expected. This experience taught me how to debug systematically, use appropriate tools for troubleshooting, and ensure that my development environment is correctly configured.
