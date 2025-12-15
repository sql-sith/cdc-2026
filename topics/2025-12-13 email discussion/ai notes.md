<!-- markdownlint-disable MD033 -->
<!-- markdownlint-disable MD041 -->
<table style="font-size: 0.85em; line-height: 1.0;">
  <tr>
    <th colspan="2" style="padding: 2px;">Cedar Rapids Area Homeschools Cyber Defense Club</th>
  </tr>
  <tr>
    <td style="padding: 2px;"><strong>Date</strong></td>
    <td style="padding: 2px;">2025-12-13</td>
  </tr>
  <tr>
    <td style="padding: 2px;"><strong>Presenter</strong></td>
    <td style="padding: 2px;">Isaac Palmersheim</td>
  </tr>
  <tr>
    <td style="padding: 2px;"><strong>Document</strong></td>
    <td style="padding: 2px;">AI Summary from Teams</strong></td>
  </tr>
</table>
<!-- markdownlint-enable MD033 -->

# Email Protocols and Tools

## Meeting notes

* **Upcoming Office Move and Room Reservation Changes:** Chris informed the group, including Kaizik, Hans, and others, about the upcoming move of the 'vault' office across the street, discussed uncertainties about the exact move date, and explained changes to the conference room reservation policy and backup plans for meeting spaces.

  * **Office Relocation Details:** Chris announced that the vault office is moving across the street and promised to share a video walkthrough once they know the exact location and move-in date. The team is awaiting confirmation on whether the move will occur next week or on the 3rd.
  * **Conference Room Policy Changes:** Chris explained that the new pricing structure for the meeting space now includes only 8 hours of conference room time per month, with 50% off additional hours, but the cost of extra hours is unclear. Chris has asked the vault management about possible grandfathering or other arrangements.
  * **Backup Meeting Space Arrangements:** As a contingency, Chris has spoken with the Armstrong building's management and secured a backup meeting space, ensuring the group will not be without a location even if the vault arrangement changes.

* **Technical Deep Dive into Email Security Protocols:** Isaac, Chris, Kaizik, and others conducted a detailed walkthrough of email security protocols, including SMTP, SPF, DKIM, and DMARC, using live demonstrations, DNS queries, and practical examples to explain how modern email security and authentication work.

  * **SMTP Protocol Overview:** Chris and Isaac led a discussion on the Simple Mail Transfer Protocol (SMTP), explaining its original lack of encryption and the implications for email security. They used Gmail as an example to show how SMTP headers reveal sender and recipient information.
  * **Sender Policy Framework (SPF):** The group demonstrated how SPF records are used to specify which mail servers are authorized to send emails for a domain. They used DNS tools to look up SPF records and explained how mail servers validate incoming messages against these records to prevent spoofing.
  * **DomainKeys Identified Mail (DKIM):** Isaac and Chris explained DKIM, showing how it uses cryptographic signatures to verify the sender's identity. They walked through extracting the DKIM selector from email headers and using tools to retrieve the public key for validation.
  * **DMARC Policy Enforcement:** The team discussed DMARC, which builds on SPF and DKIM to provide domain owners with control over how email receivers handle authentication failures. They demonstrated querying DMARC records and interpreting policy settings such as 'reject' and 'quarantine.'
  * **Limitations and Encryption Challenges:** The group highlighted that while protocols like TLS encrypt email in transit, much metadata and sometimes content remain unencrypted, especially when emails traverse multiple servers. They discussed the challenges of end-to-end encryption and the role of tools like OpenPGP.

* **Plans for Hands-On Email Server and DNS Setup:** Isaac and Chris outlined plans for the group to set up a private network with an authoritative DNS server and a mail server, aiming to implement and observe the discussed security protocols in a controlled environment.

  * **Project Goals and Approach:** Isaac proposed setting up a private network with an authoritative DNS server and a mail server, allowing the group to implement SPF, DKIM, and DMARC policies and observe their effects in practice.
  * **Technical Stack and Tools:** Chris mentioned using Docker-based mail stacks, including Postfix, Dovecot, and OpenDMARC, to simplify deployment and management. The plan includes providing VMs or laptops for participants to access the environment.
  * **Contingency and Rollback Plans:** Chris emphasized the importance of using snapshots for the VMs to allow easy rollback in case of configuration errors, ensuring a safe learning environment.

* **Discussion on DNS Security and Outage Management:** Chris, Chad, and others discussed the critical role of DNS in internet security, shared real-world examples of DNS hijacking and outages, and described best practices for operational resilience and incident management.

  * **DNS Security Risks:** The group discussed the risks of DNS poisoning and hijacking, emphasizing the importance of securing DNS infrastructure to prevent large-scale security breaches.
  * **Password Stuffing and Account Takeover:** Chris explained how attackers use password stuffing to compromise email accounts, which can then be leveraged to reset passwords on other services and potentially hijack domains by altering DNS records.
  * **Incident Response and Outage Stories:** Chris recounted incidents involving DNS misconfigurations and outages, including a major event caused by a routing table update, and described the importance of rollback procedures and operational discipline.
  * **Operational Best Practices:** The team discussed the use of orchestration tools like Puppet for controlled patch deployment, the importance of testing updates before production rollout, and strategies for minimizing downtime during incidents.

* **Programming Education, AI Tools, and Workflow Automation:** Chris, Isaac, and others shared their experiences learning programming, discussed the use of AI tools for code generation and review, and demonstrated a Python script for domain suffix analysis, highlighting the evolving role of automation in development.

  * **Learning Programming Pathways:** Isaac described their journey into programming, starting with Minecraft modding, moving to Python, and emphasizing the value of self-driven projects and hybrid approaches combining tutorials with hands-on problem-solving.
  * **AI-Assisted Development:** Chris demonstrated how AI tools can be used to generate, refactor, and review code, treating the AI as a junior programmer and iteratively refining specifications and implementations.
  * **Domain Suffix Analysis Script:** Chris showcased a Python script, developed with AI assistance, that analyzes domain names to determine valid public suffixes and registrable parts, using the public suffix list as a reference.
  * **Security and Code Review:** The group discussed the importance of code auditing, both manual and automated, to catch vulnerabilities such as injection flaws, and shared experiences where AI-assisted reviews identified issues missed by human reviewers.

* **SQL Server Management and Development Practices:** Chris and others discussed SQL Server Management Studio (SSMS) settings, best practices for query execution, and the integration of AI features in recent versions of SSMS.

  * **SSMS Configuration:** Chris explained how to configure SSMS for optimal query execution, including setting isolation levels and enabling advanced features for materialized views and indexed columns.
  * **AI Integration in SSMS:** The group noted that SSMS 22 includes AI-powered features, discussed their potential impact, and expressed caution about relying on AI for database operations.

## Follow-up tasks

* **Vault Relocation Update:** Shoot a short video showing the new vault location and share it with the group once the move details are confirmed. (Chris)
* **Conference Room Pricing Clarification:** Follow up with the vault management to determine if grandfathering or alternative arrangements for conference room hours are possible under the new pricing structure. (Chris)
* **Class Notes Repository Update:** Merge the class notes into the main branch to ensure all materials are up to date. (Chris)
* **Authoritative DNS Server Setup:** Set up an authoritative DNS server for the group's private network to support the upcoming mail server implementation. (Isaac)
* **Statistical Analysis of Layoffs and Attire:** Obtain data on total employees, number laid off, and number who wore T-shirts, and perform a statistical analysis to explore any correlation. (Chris)
