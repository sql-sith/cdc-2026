<!-- markdownlint-disable MD033 -->
<!-- markdownlint-disable MD041 -->

<table style="font-size: 0.85em; line-height: 1.0;">
  <tr>
    <th colspan="2" style="padding: 2px;">Cedar Rapids Area Homeschools Cyber Defense Club</th>
  </tr>
  <tr>
    <td style="padding: 2px;"><strong>Date</strong></td>
    <td style="padding: 2px;">2025-11-15</td>
  </tr>
  <tr>
    <td style="padding: 2px;"><strong>Presenter</strong></td>
    <td style="padding: 2px;">Chris Leonard</td>
  </tr>
  <tr>
    <td style="padding: 2px;"><strong>Document</strong></td>
    <td style="padding: 2px;">AI Summary from Teams</strong></td>
  </tr>
</table>
<!-- markdownlint-enable MD033 -->

# Introduction to PowerShell

## Meeting notes

* **PowerShell Introduction and Environment Setup:** Chris led the group through an introduction to PowerShell, guiding participants such as Hans and Naomi in setting up their environments, verifying PowerShell versions, and ensuring access to the necessary tools for the session.

  * **PowerShell Version Selection:** Chris explained the differences between PowerShell 5 (Windows PowerShell) and PowerShell 7, emphasizing the preference for version 7 due to its cross-platform capabilities, but defaulting to version 5 if version 7 was unavailable on the participants' systems.
  * **Accessing PowerShell:** Participants were instructed to launch PowerShell by typing 'PWSH' for version 7 or 'PowerShell' for version 5, with Chris and Chad assisting Naomi and Hans in confirming which version was running and troubleshooting any issues with launching the correct shell.
  * **Using Virtual Machines:** Chris described the use of Windows server VMs (e.g., in Ice Lake) for those without local Windows installations, clarifying that the VM names were arbitrary and that participants could select any available instance for their work.
  * **Password and Access Management:** Chris provided guidance on accessing the VMs, including sharing the password format and discussing the typical password management practices for the competition environments, noting the use of well-known or unchanged passwords for school resources.

* **PowerShell Command Structure and Object Model:** Chris detailed the verb-noun syntax of PowerShell commandlets, the object-oriented nature of its output, and compared these features to Bash, highlighting the advantages and technical distinctions for the group.

  * **Verb-Noun Commandlet Syntax:** Chris explained that PowerShell commandlets strictly follow a verb-noun naming convention (e.g., Get-ChildItem, Set-Location), and Microsoft enforces a list of approved verbs, which helps with discoverability and consistency across scripts.
  * **Object-Based Output:** Unlike Bash, which outputs plain text, PowerShell commands return objects (e.g., System.IO.DirectoryInfo for directories), allowing users to access properties and methods directly, as demonstrated with commands like 'Make-Dir' and 'Select-Object'.
  * **Command Discovery Tools:** Chris demonstrated the use of 'Get-Command' and wildcards to discover available commandlets, and discussed the use of aliases and help commands (e.g., 'man', 'help', 'Get-Help') to assist users transitioning from other shells.
  * **Comparison to Bash:** The group discussed how Bash treats everything as a file and outputs text, while PowerShell's object model enables more complex data manipulation, with Chris providing examples of how properties can be accessed and piped between commands.

* **File System Operations in PowerShell:** Chris guided the team through creating, viewing, and manipulating files and directories in PowerShell, covering commandlets for file operations, directory navigation, and the use of editors, with hands-on examples for participants.

  * **Creating Files and Directories:** Participants practiced using 'New-Item' to create files and directories, with Chris explaining the use of parameters such as -Path and -ItemType, and demonstrating how to check the resulting objects and their properties.
  * **Directory Navigation:** Chris showed the use of 'Set-Location' (with aliases like 'cd' and 'sl') for changing directories, and 'Get-Location' for displaying the current directory, emphasizing the importance of using explicit commandlets in scripts.
  * **Viewing and Editing Files:** The group explored 'Get-Content' for displaying file contents, discussed pagination with 'more', and reviewed the use of editors such as Notepad, Notepad++, Nano, and VS Code, including installation via Winget and considerations for server environments.
  * **PowerShell Drives:** Chris introduced the concept of PowerShell drives, which abstract hierarchical data sources (e.g., file system, registry, environment variables) and demonstrated listing them with 'Get-PSDrive'.

* **Permissions and Security in PowerShell and Windows:** Chris provided an in-depth walkthrough of Windows file and folder permissions, comparing them to Linux, and demonstrated how to view and modify permissions using both GUI and command-line tools in PowerShell.

  * **Viewing Permissions:** Chris demonstrated viewing permissions through the Windows GUI (folder properties and security tab) and via PowerShell using 'Get-Acl', 'Format-List', and 'Select-Object', explaining the complexity and richness of Windows ACLs compared to Linux permissions.
  * **Modifying Permissions:** The group discussed the use of 'icacls' for granting or removing permissions for users and groups, and Chris cautioned about the risks of using 'Set-Acl' directly, recommending GUI tools or 'icacls' for most scenarios.
  * **Inheritance and Advanced Security:** Chris explained inheritable permissions in Windows, the use of the advanced security dialog to propagate permissions, and the potential pitfalls of modifying permissions on system directories.
  * **Comparison to Linux:** The discussion highlighted the limitations of Linux's nine-character permission model (rwx) versus the more granular and flexible Windows ACL system, and noted the rarity of using advanced ACLs in Linux.

* **Searching and Filtering with PowerShell:** Chris introduced searching and filtering techniques in PowerShell, focusing on the 'Select-String' commandlet as an analogue to grep, and provided practical exercises for the group to reinforce these concepts.

  * **Using Select-String:** Chris demonstrated searching for patterns in files using 'Select-String', showing how it returns match info objects with details such as file name and line number, and discussed parameters for controlling output.
  * **Regular Expressions:** The group practiced using regular expressions with 'Select-String', including alternation (e.g., 'quick|Ethernet') and case insensitivity, to match multiple patterns in text files.
  * **Copying and Editing Files for Search:** Participants created and edited multiple files to test search functionality, using 'Copy-Item' (with aliases like 'cp') and editors to insert unique lines for demonstration.

* **Testing Paths and Conditional Logic:** Chris explained the use of 'Test-Path' for verifying the existence and type of files and directories, and introduced basic conditional logic in PowerShell, preparing the group for future scripting exercises.

  * **Test-Path Usage:** Chris showed how to use 'Test-Path' to check for the existence of files or directories, and explained the use of the -PathType parameter to distinguish between containers (directories) and leaves (files).
  * **Conditional Statements:** The group briefly discussed using 'if' statements in PowerShell to perform actions based on the results of 'Test-Path', including outputting warnings or errors depending on the condition.

* **Planning for Next Session and Feedback:** Chris and the group discussed plans for the next meeting, including a focus on scripting, more hands-on exercises, and reviewing concepts from both Bash and PowerShell, while soliciting feedback and suggestions from participants.

  * **Session Structure and Goals:** The group agreed to allocate more time for hands-on activities, such as scripting and file-based exercises, and to review concepts from both shells to reinforce learning.
  * **Participant Feedback:** Chris encouraged participants to share questions and suggestions, and the group discussed the value of seeing tasks from multiple perspectives (GUI and command-line) and the importance of environment variable manipulation and editor usage.

## Follow-up tasks

* **Class Calendar and Resource Sharing:** Upload and share the updated class calendar on the wiki or website to provide students and parents with access. (Chris)
* **Class Schedule Adjustment:** Adjust the class schedule to push Active Directory and email topics down a week and update the calendar accordingly. (Chris)
* **Password Documentation:** Add the Windows test scan password to the shared notes for student access. (Chris)
* **Hands-On Practice for Students:** Prepare more walk-through examples and hands-on activities for next week's session to reinforce learning and allow students to practice locally. (Chris, Chad)
* **PowerShell Scripting Introduction:** Plan a review activity for next week that involves students creating simple scripts using concepts from both Bash and PowerShell. (Chris, Chad)
