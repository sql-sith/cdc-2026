
# Installing VSCode and its main Python Extensions

Date: November 1, 2025
Presenter: Chris

## Sometimes things don't go as planned...

We had hoped to do more, but we had some trouble getting Python to work correctly in VSCode until Dan realized that Haddon might not be on the same computer he had been the week before. Dan's intuition was correct! The problem was that Python was not installed on the computer Haddon was using. Live and learn. :)

## Discussion Notes

* **Installing Visual Studio Code Using Winget:** Chris guided haddon through verifying their Windows version, using the command prompt to check for and install Visual Studio Code via the Winget package manager, and troubleshooting command syntax and search results.
  * **Windows Version Verification:** Chris asked haddon to check their Windows version using the 'winver' command to ensure compatibility with the installation steps, and haddon confirmed they were on Windows 10 version 22H2.
  * **Winget Availability and Usage:** Chris instructed haddon to test if the Winget tool was available by running 'winget' in the command prompt, and upon confirmation, guided them through searching for Visual Studio Code using 'winget search VS code'.
  * **Correct Command Syntax:** Chris clarified the correct syntax for installing Visual Studio Code, emphasizing the use of 'winget install --id Microsoft.VisualStudioCode --exact', and helped haddon identify and use the correct package ID from the search results.
  * **Troubleshooting Installation Issues:** Chris and haddon addressed issues such as incorrect command input and package identification, with Chris providing step-by-step corrections and explanations for each encountered error.
* **Setting Up Python Development Environment in VS Code:** Chris assisted haddon in configuring Visual Studio Code for Python development by installing the Python extension, creating a new Python file, and ensuring the correct file extension and environment setup.
  * **Python Extension Installation:** Chris directed haddon to the Extensions panel in VS Code and had them search for and install the 'ms-python.python' extension to enable Python language support.
  * **Creating and Saving Python Files:** Chris demonstrated how to create a new Python file in VS Code, ensuring the file type was set to Python and the file was saved with a '.py' extension.
  * **Explaining File Type and Extensions:** Chris explained the importance of selecting the correct file type and extension for Python files, and provided guidance on saving files in accessible directories.
* **Configuring Python Interpreter and Running Python Code:** Chris and haddon worked through selecting the correct Python interpreter in VS Code, troubleshooting missing Python installations, and successfully running a Python script after installing Python via Winget.
  * **Interpreter Selection Prompt:** When attempting to run a Python script, haddon was prompted to select a Python interpreter, leading Chris to guide them through checking available interpreters and entering the correct path.
  * **Verifying Python Installation:** Chris had haddon check for Python installation by running 'python' and 'python3' in the command prompt, discovering that Python was not installed on the PC, which explained previous issues.
  * **Installing Python via Winget:** Chris provided haddon with the appropriate Winget command to install Python, and confirmed the installation process was underway.
  * **Running Python Code in VS Code:** After installing Python and selecting the correct interpreter, haddon was able to successfully run a Python script in VS Code, confirming the environment was set up correctly.
* **Introduction to Python Programming Concepts:** Chris introduced haddon to Python programming basics, including function definitions, indentation rules, loops, and the use of built-in libraries, and discussed potential homework assignments involving string manipulation and password hashing.
  * **Function Definitions and Indentation:** Chris explained how Python uses indentation instead of curly braces to define code blocks within functions, emphasizing the need for consistent use of spaces or tabs.
  * **Loops and String Libraries:** Chris demonstrated the use of for-loops in Python, including iterating over ranges and characters, and introduced the 'string' library for accessing character sets like ASCII letters.
  * **Homework Assignments:** Chris discussed possible homework tasks, such as analyzing a ROT13 encoding function, parsing calculator input strings, and exploring brute-force password generation and hashing using SHA-256.
  * **Regular Expressions and Parsing:** Chris mentioned the eventual need for regular expressions to handle more complex string parsing tasks, such as extracting numbers and operators from user input.
* **Troubleshooting and Guidance for Future Sessions:** Chris provided troubleshooting support for installation and configuration issues, outlined homework for haddon to replicate the setup on their laptop, and previewed topics for the next session, including password brute-forcing and hashing.
  * **Homework Instructions:** Chris assigned haddon the task of installing Python and VS Code on their laptop before the next session to streamline future setup.
  * **Preview of Next Session:** Chris indicated that the next meeting would cover generating and brute-forcing passwords, hashing with SHA-256, and further Python programming exercises.

## Follow-up tasks

* **Python and VS Code Setup on Laptop:** Install Python and Visual Studio Code on your laptop before the next meeting to ensure the development environment is ready. (haddon/naomi)
