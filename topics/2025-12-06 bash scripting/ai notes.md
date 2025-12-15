<!-- markdownlint-disable MD033 -->
<<<<<<< HEAD
<!-- markdownlint-disable MD041 -->
=======

<!-- markdownlint-disable MD041 -->

>>>>>>> 768535ccd10de135f56a3e772337fbb82d3c515e
<table style="font-size: 0.85em; line-height: 1.0;">
  <tr>
    <th colspan="2" style="padding: 2px;">Cedar Rapids Area Homeschools Cyber Defense Club</th>
  </tr>
  <tr>
    <td style="padding: 2px;"><strong>Date</strong></td>
    <td style="padding: 2px;">2025-12-06</td>
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

# Bash Scripting

## Meeting notes

* **Bash Scripting Workshop and Technical Demonstrations:** Chris led the group, including participants such as Isaac, Naomi, Kaiser, Hans, and others, through a hands-on workshop focused on Bash scripting, covering file inspection commands, scripting techniques, command-line utilities, and the differences between Bash and PowerShell, with detailed technical explanations and live demonstrations.
<<<<<<< HEAD
  
=======
>>>>>>> 768535ccd10de135f56a3e772337fbb82d3c515e
  * **File Inspection Commands:** Chris demonstrated how to use commands like ls, cat, head, tail, more, less, and alternatives such as bat or batcat to inspect files and directories in Linux, explaining their usage, differences, and when to use each, including how to view configuration files and hidden files using command-line options.
  * **Counting and Parsing File Data:** The group explored the wc command to count lines, words, and bytes in files, and discussed how to use pipes and command combinations to process file lists, including using glob patterns to match multiple files and extracting specific information with cut and awk.
  * **Bash Scripting Constructs:** Chris guided participants through building Bash scripts with for loops, variable assignment, quoting, and command substitution, illustrating how to iterate over files, capture command output into variables, and print formatted results, while highlighting the importance of quoting and the differences in variable usage between Bash and PowerShell.
  * **Using awk and cut for Data Extraction:** The session included a comparison of awk and cut for extracting fields from command output, with Chris explaining awk's syntax, field selection, and the rationale for using single versus double quotes, as well as the limitations of cut when handling space-delimited data.
  * **Paginating Script Output:** Chris showed how to paginate script output using more or less, discussed the use of read and sleep for pausing between outputs, and explained how to pipe the output of a loop to a pager for improved readability when processing multiple files.
<<<<<<< HEAD
  
* **Environment Variables and Process Inheritance in Bash:** Chris provided an in-depth explanation of environment variables, session variables, and how variable inheritance works between parent and child processes in Bash, using live shell demonstrations and custom scripts to illustrate exporting variables and passing parameters.

=======
* **Environment Variables and Process Inheritance in Bash:** Chris provided an in-depth explanation of environment variables, session variables, and how variable inheritance works between parent and child processes in Bash, using live shell demonstrations and custom scripts to illustrate exporting variables and passing parameters.
>>>>>>> 768535ccd10de135f56a3e772337fbb82d3c515e
  * **Parent and Child Processes:** Chris explained the relationship between parent and child processes in Bash, using the ps command to show process IDs and parent process IDs, and demonstrated how launching a new shell creates a child process with its own environment.
  * **Session vs. Environment Variables:** The group learned that variables set in a Bash session are not automatically inherited by child processes unless exported, and Chris demonstrated how to use export to make variables available to child shells.
  * **Passing Variables and Parameters to Scripts:** Chris showed how to pass variables to scripts either by exporting them or by setting them inline before script execution, and discussed the use of positional parameters ($1, $2, etc.) and named variables for passing data into scripts.
  * **Script Execution Permissions:** The process of making a shell script executable using chmod was demonstrated, along with a discussion of default file permissions and the role of umask in determining those defaults.
<<<<<<< HEAD
  
* **Learning Strategies and Use of Documentation Tools:** Chris and the group discussed effective strategies for learning command-line tools and scripting, including the use of man, tldr, --help, info, AI tools, and mind mapping for organizing knowledge, as well as the importance of understanding idiomatic usage in different programming languages.

  * **Documentation Resources:** Participants identified and compared various resources for learning about commands, such as man pages, tldr, --help, info, vendor documentation, and online resources like Stack Overflow and AI tools, emphasizing their respective strengths and when to use each.
  * **Mind Mapping for Learning:** Chris introduced mind mapping tools as a way to organize and visualize knowledge about scripting and command-line usage, demonstrating how to build a mind map of commands, options, and learning strategies.
  * **Idiomatic Usage and Cross-Language Learning:** The group discussed the concept of idiomatic usage in programming languages, the importance of learning the 'right way' to do things in each language, and strategies for translating knowledge between Bash, PowerShell, Python, and other environments.
  
* **Upcoming Sessions and Team Activities:** Chris and the group planned future sessions focused on email protocols and server setup, discussed possible technical topics such as SMTP, Postfix, and security protocols, and considered organizing a team-building event at the Fun Station.

  * **Email Protocols and Server Setup:** The group agreed to dedicate the next two sessions to exploring email protocols, installing and configuring email servers like Postfix or Redmail, and examining related security protocols such as DKIM, SPF, and DMARC, with hands-on activities and possible use of Wireshark for protocol analysis.
  * **Team-Building Event Planning:** A proposal was made to hold a team-building event at the Fun Station, with details shared in the team's general communication channel and an invitation for interested members to participate.

* **Discussion of Mock Trial and Team Experiences:** Chris briefly recounted recent experiences with mock trial competitions, including issues of perceived bias, team dynamics, and lessons learned, referencing participants such as Isaac and Naomi.

=======
* **Learning Strategies and Use of Documentation Tools:** Chris and the group discussed effective strategies for learning command-line tools and scripting, including the use of man, tldr, --help, info, AI tools, and mind mapping for organizing knowledge, as well as the importance of understanding idiomatic usage in different programming languages.
  * **Documentation Resources:** Participants identified and compared various resources for learning about commands, such as man pages, tldr, --help, info, vendor documentation, and online resources like Stack Overflow and AI tools, emphasizing their respective strengths and when to use each.
  * **Mind Mapping for Learning:** Chris introduced mind mapping tools as a way to organize and visualize knowledge about scripting and command-line usage, demonstrating how to build a mind map of commands, options, and learning strategies.
  * **Idiomatic Usage and Cross-Language Learning:** The group discussed the concept of idiomatic usage in programming languages, the importance of learning the 'right way' to do things in each language, and strategies for translating knowledge between Bash, PowerShell, Python, and other environments.
* **Upcoming Sessions and Team Activities:** Chris and the group planned future sessions focused on email protocols and server setup, discussed possible technical topics such as SMTP, Postfix, and security protocols, and considered organizing a team-building event at the Fun Station.
  * **Email Protocols and Server Setup:** The group agreed to dedicate the next two sessions to exploring email protocols, installing and configuring email servers like Postfix or Redmail, and examining related security protocols such as DKIM, SPF, and DMARC, with hands-on activities and possible use of Wireshark for protocol analysis.
  * **Team-Building Event Planning:** A proposal was made to hold a team-building event at the Fun Station, with details shared in the team's general communication channel and an invitation for interested members to participate.
* **Discussion of Mock Trial and Team Experiences:** Chris briefly recounted recent experiences with mock trial competitions, including issues of perceived bias, team dynamics, and lessons learned, referencing participants such as Isaac and Naomi.
>>>>>>> 768535ccd10de135f56a3e772337fbb82d3c515e
  * **Competition Outcomes and Lessons:** Chris described the outcomes of recent mock trial competitions, discussed the impact of perceived judging bias, and reflected on the importance of maintaining professionalism and learning from both victories and defeats.

## Follow-up tasks

* **Upcoming Email Presentations:** Coordinate with all three students to prepare and present on email topics in the next two weeks, including installation and configuration of an email server and related protocols. (Chris, all three students)
* **SMTP Server Setup for Learning:** Set up a local SMTP server (e.g., Postfix, Citadel, or Redmail) for hands-on demonstration and protocol exploration in upcoming sessions. (Chris)
* **Domain and Email Security Configuration:** Provide access to a domain for students to practice setting up email security protocols (DKIM, SPF, DMARC) during the email server exercise. (Chris)
* **Review of Previous Linux Sessions:** Listen to the recordings of the two Linux-focused sessions missed while in California to ensure continuity and preparation for upcoming topics on system services. (Chris)
* **Team Building Event Coordination:** Share details and coordinate interest for a team building event at the Fun Station, including confirming attendance and logistics with the group. (Chris)
