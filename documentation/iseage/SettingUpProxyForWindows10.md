<!-- Created by Aksel Rasmussen in 2024 -->

# Windows 10 Proxy Settings

A guide for setting up Windows 10 on Iserink with internet.

> ### A Quick note before we begin
> This guide is based on Win10.
> It is also based on a fresh install.
> If you feel like reinstalling windows will make it work better, than do that.
> It is not known if this guide will work on later versions of Windows. 

## Setup

1. Navigate: Settings > Network & Internet > Ethernet.
2. Click the network. It should be called somthing like "Unidentified network".
3. Under "IP settings", press the "Edit" button.
4. In the dialog that pops up, change the dropdown from "Automatic (DHCP)" to "Manual".
5. Turn on the "IPv4" switch.
6. Set "IP address" to a free address in the form "144.76.90.*". Check with the team for which addresses are available.
7. Set "Subnet prefix length" to "24".
8. Set "Gateway" to "144.76.90.254".
9. Set the DNS server to "199.100.16.100" and press the "Save button".
10. Navigate: Settings > Network & Internet > Proxy.
11. Under "Automatic proxy setup", turn off "Automatically detect settings".
12. Under "Manual proxy setup", turn on "Use a proxy server".
13. Set "Address" to "199.100.16.100".
14. Set "Port" to "3128".
15. Press the "Save" button.

## Verifying the Proxy

1. In a webbrowser, go to your favourite external website. (eg. not google)
2. If it loads, you got it.
3. If it doesn't load, and you can't debug the issue on your own, ask for help from the CDC crowd on Discord or from us on Zulip
