<!-- markdownlint-disable MD033 -->

<!-- markdownlint-disable MD041 -->

<table style="font-size: 0.85em; line-height: 1.0;">
  <tr>
    <th colspan="2" style="padding: 2px;">Cedar Rapids Area Homeschools Cyber Defense Club</th>
  </tr>
  <tr>
    <td style="padding: 2px;"><strong>Date</strong></td>
    <td style="padding: 2px;">2025-11-22</td>
  </tr>
  <tr>
    <td style="padding: 2px;"><strong>Presenter</strong></td>
<<<<<<< HEAD
    <td style="padding: 2px;">Chad Hanson</td>
=======
    <td style="padding: 2px;">Chad Johnson</td>
>>>>>>> 768535ccd10de135f56a3e772337fbb82d3c515e
  </tr>
  <tr>
    <td style="padding: 2px;"><strong>Document</strong></td>
    <td style="padding: 2px;">AI Summary from Teams</strong></td>
  </tr>
</table>
<!-- markdownlint-enable MD033 -->

# PowerShell Scripting

## Meeting notes

* **PowerShell Looping and File Operations:** Chad, with support from Chris and other participants including Hans, Dan, and Carl, led a hands-on session demonstrating PowerShell scripting concepts such as loops, file creation, dynamic file naming, content writing, reading, and code refactoring using variables, with active troubleshooting and debugging in VS Code.
  * **Introduction to PowerShell Loops:** Chad reviewed the basics of PowerShell loops, explaining the syntax and logic of while loops, comparison operators like -le and -lt, and how to increment variables within the loop. Participants were guided to create a test.ps1 file in VS Code and implement a simple while loop to iterate a set number of times.
  * **VS Code Setup and Debugging:** Chad and the group discussed setting up VS Code for PowerShell development, including installing the necessary PowerShell extension, using breakpoints for debugging, and troubleshooting issues with the debugger. Hans shared their screen to demonstrate running scripts and using breakpoints, while others provided input on resolving extension and execution policy issues.
  * **Dynamic File Creation and Content Writing:** The team enhanced their script to create multiple files with dynamic names by embedding the loop counter variable into the filename (e.g., hello1.txt, hello2.txt). They then added content to each file using the Add-Content cmdlet, incorporating both static text and the loop variable to personalize each file's contents.
  * **Reading and Outputting File Content:** Participants implemented reading file content using Get-Content, storing the result in a variable, and outputting it to the console with Write-Output. The group discussed variable naming conventions and the importance of code organization, with Chad emphasizing the value of standardization and clean code practices.
  * **Refactoring with Variables and Debugging:** Chad challenged the group to refactor their code by consolidating repeated path expressions into a single variable, guiding them through the process of variable assignment, string interpolation, and resolving syntax errors. Chris demonstrated using the VS Code debugger to inspect variables and step through code execution, highlighting the benefits of debugging tools for troubleshooting.
* **Bash Scripting and Linux Command Review:** Chris led a session on Bash scripting, guiding participants through setting up a Bash environment, creating and copying text files, and reviewing essential Linux commands such as echo, cat, wc, and head, with hands-on exercises in a shared directory.
  * **Bash Environment Setup:** Chris assisted participants in setting up a Bash environment, including installing WSL on Windows where necessary, and ensuring everyone could access a local Bash shell. The group created a working directory named Bash Playground and navigated into it using standard Linux commands.
  * **File Preparation for Scripting:** Participants copied system files such as /etc/passwd and .profile into their Bash Playground directory, renaming them with a .txt extension to prepare for scripting exercises. Chris provided guidance on using cp and tab completion, and addressed issues related to file locations and permissions.
  * **Review of Core Linux Commands:** Chris reviewed the usage of echo (for outputting text), cat (for displaying file contents), wc (for counting lines, words, and bytes), and head (for displaying the first lines of a file). The group discussed the differences between these commands and their PowerShell equivalents, with Chris providing examples and explanations.
  * **Introduction to Bash Scripting Structures:** Chris introduced the syntax and structure of Bash for loops and if statements, noting the historical context and differences from other programming languages. The group prepared to use provided scripts (child.sh, runner.sh, standardize.sh) for further exercises, with plans to continue in the next session.
* **Troubleshooting Development Environments:** Throughout the meeting, participants including Chad, Chris, Hans, and others collaboratively addressed technical issues related to VS Code extensions, execution policies, debugger errors, and Bash environment setup, ensuring all attendees could follow along with the exercises.
  * **VS Code and PowerShell Extension Issues:** The group encountered and resolved issues with missing PowerShell extensions in VS Code, execution policy restrictions, and debugger malfunctions. Solutions included installing the correct extension, restarting VS Code, and running scripts without the debugger when necessary.
  * **Bash and WSL Installation Challenges:** Some participants needed to install WSL to access a Bash shell on Windows. Chris provided step-by-step instructions for installing WSL, discussed alternatives such as using Bash on Windows directly, and helped troubleshoot installation and environment configuration problems.
* **Best Practices and Coding Standards Discussion:** Chad and Chris emphasized the importance of code organization, variable naming conventions, and adherence to team or community standards, encouraging participants to adopt best practices for maintainable and readable code.
  * **Variable Naming and Code Organization:** The group discussed strategies for naming variables to avoid conflicts with reserved words, using descriptive names, and following team conventions. Chris highlighted the value of standardization, even in legacy or inherited codebases, and recommended consulting community guidelines or official standards where available.
  * **Importance of Clean and Maintainable Code:** Chad and Chris advised participants to prioritize code readability and maintainability, especially in larger projects, and to refactor duplicated code into variables or functions. They shared experiences of troubleshooting issues caused by minor inconsistencies and stressed the benefits of consistent coding practices.

## Follow-up tasks

* **VS Code Environment Preparation:** Ensure VS Code and necessary extensions are installed and configured on personal systems to facilitate future programming sessions and avoid setup delays. (the team)
* **Bash Environment Setup:** Install WSL (Windows Subsystem for Linux) or ensure Bash is available on personal laptops to enable running Bash scripts in upcoming sessions. (the team)
* **Class Notes Branch Access:** Switch to the "class notes rolling" branch on GitHub and review the "20251122 scripting" topic, ensuring access to the three scripts (child.sh, runner.sh, standardize.sh) for future use. (the team)
* **Script Preparation for Next Session:** Copy the three scripts (child.sh, runner.sh, standardize.sh) to the appropriate directory and verify their availability before the next meeting. (Chris)
