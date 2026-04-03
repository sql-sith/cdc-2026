# Cyber Defense Team - Lesson Guide

## DHCP & Active Directory

---

## Topic 1: DHCP (30 minutes)

---

### Background (5 min)

**What is DHCP?**

When a device joins a network, it needs four things before it can communicate:

- An IP address
- A subnet mask
- A default gateway
- A DNS server

DHCP (Dynamic Host Configuration Protocol) hands these out automatically. Without it, someone has to configure every device by hand.

**The DORA Handshake**

Every DHCP lease starts with a four-step conversation between the client and server:

| Step                  | From   | To        | What it says                              |
| --------------------- | ------ | --------- | ----------------------------------------- |
| **D**iscover    | Client | Broadcast | "Is there a DHCP server out there?"       |
| **O**ffer       | Server | Client    | "Yes - here's an IP you can use."         |
| **R**equest     | Client | Broadcast | "I'd like that IP, please."               |
| **A**cknowledge | Server | Client    | "It's yours. Here are the full settings." |

The client broadcasts the Request (not unicast) so any other DHCP servers on the subnet know the offer was accepted and can release their own pending offers.

**Leases**

DHCP addresses are *leased*, not permanent. At 50% of the lease time, the client tries to renew with the same server. At 87.5%, it broadcasts to any DHCP server. When the lease expires, the client loses the address. This is why lease duration matters - too short floods the network with renewals; too long wastes your address pool.

**Why This Matters for Defense**

When we began our Active Directory sessions, we experienced a rogue DHCP server on your subnet. This was probably coming from one of our servers or from Iowa State. But if it was a DHCP server set up by a bad actor, this would be an attack. Let's assume for a moment that it was an attack.

In that case, this would be what happened. A rogue server responded to Discover messages faster than the legitimate one and handed out its own gateway address - pointing traffic wherever the attacker wanted. This is called a **DHCP spoofing** attack. In Active Directory, there is a built-in protection against one class of rogue DHCP server: **DHCP authorization**. When a Windows DHCP service starts on a domain-joined server, it checks AD to see if it is listed as an authorized server. If it is not, the Windows DHCP service refuses to hand out leases.

This protects against *accidental* rogue DHCP servers - for example, a Windows Server where someone inadvertently installed and started the DHCP role. It does **not** stop a deliberate attacker running a rogue DHCP server on a Linux box, a non-domain-joined machine, or any non-Windows platform. Those servers have no reason to check AD and will not honor it. For that threat, you need a network-level control like DHCP snooping on a managed switch. That is why authorizing your DHCP server in AD still matters - but it is one layer of defense, not the whole story.

---

### Hands-On (20 min)

> On your member server or the domain controller, open Server Manager.

#### Step 1 - Open the DHCP Console

`Server Manager → Tools → DHCP`

You should see your server listed in the left pane. Expand it to see **IPv4** and **IPv6**.

---

#### Step 2 - Explore an Existing Scope

Expand **IPv4 → Scope**. A scope is a pool of addresses the server can hand out.

Click on the scope and look at:

- **Address Pool** - the range of IPs available
- **Address Leases** - devices that currently hold a lease (you will see the hostname, IP, and expiration)
- **Reservations** - specific devices that always get the same IP (matched by MAC address)
- **Scope Options** - settings handed to clients: gateway (option 003), DNS servers (option 006)

> **Question for the group:** Why would you use a Reservation instead of just setting a static IP on the device itself?
>
> *Answer: Reservations keep all addressing in one place and still go through DHCP, so you can audit leases and options centrally.*

---

#### Step 3 - Check DHCP Authorization

Right-click your server name in the left pane. If you see **Authorize**, the server is not yet authorized - click it. If you see **Unauthorize**, it is already authorized (good).

Authorized servers appear with a green icon. Unauthorized servers appear with a red down-arrow and will not respond to clients on a domain network.

> This is the control that will stop a rogue DHCP server on your subnet - if the rogue server was domain-joined. A non-domain device will not check, which is why network-level controls (DHCP snooping on managed switches) are also important.

Back to what actually happened in our case: the DHCP server was not a member of our domain and it was not on our subnet, so the above defenses would not work. The way we solved this was by doing whatever we had to do to join the client to our domain. Once they were in the domain, I had a GPO that blocked the rogue server.

---

#### Step 4 - Create a New Scope

We will create a scope for a hypothetical second subnet so you can see the full process.

1. Right-click **IPv4 → New Scope**
2. **Name:** `Lab Subnet B`
3. **IP Range:** `192.168.20.1` - `192.168.20.254`, mask `255.255.255.0`
4. **Exclusions:** Add `192.168.20.1` - `192.168.20.10` (reserve low addresses for static devices like routers and servers)
5. **Lease Duration:** Leave at 8 days for a stable wired network
6. **Configure Options Now:** Yes
   - **Router (003):** `192.168.20.1`
   - **DNS Servers (006):** your domain controller's IP
   - **DNS Domain Name (015):** your domain name
7. **Activate scope:** Yes

Your new scope now appears under IPv4 with a green icon.

---

#### Step 5 - Create a Reservation

In your new scope, click **Reservations → New Reservation**.

- **Reservation Name:** `Lab-Workstation-01`
- **IP Address:** `192.168.20.50`
- **MAC Address:** enter any address in `AA-BB-CC-DD-EE-FF` format for the demo
- **Supported types:** Both

This entry ensures that whenever the device with that MAC sends a Discover, it always receives `192.168.20.50`.

---

### Wrap-Up (5 min)

Key things to remember:

- DHCP = automatic IP configuration via DORA
- Authorize your DHCP server in AD - it is a security control, not just a formality
- Scopes define the pool; options define what clients receive with the lease
- Reservations give dynamic consistency without manual static configuration
- Rogue DHCP attacks work by racing your server - defense is authorization + switch-level DHCP snooping

---

## Topic 2: Active Directory & Group Policy (30 minutes)

---

### Background (5 min)

**The AD Structure**

Active Directory organizes everything in a hierarchy:

```
Forest
└── Domain (e.g., lab.local)
    ├── Organizational Units (OUs)
    │   ├── Users OU
    │   │   └── user accounts
    │   ├── Computers OU
    │   │   └── computer accounts
    │   └── Servers OU
    │       └── server accounts
    └── Domain Controllers
```

- **Forest** - the security boundary. Everything inside trusts each other.
- **Domain** - the administrative boundary. Users, computers, and policies live here.
- **OU (Organizational Unit)** - a folder for organizing objects and applying policy. This is where you spend most of your time.

**What Group Policy Actually Does**

A Group Policy Object (GPO) is a collection of settings. You *link* a GPO to a domain, site, or OU. Every object inside that container receives the settings in the GPO.

Here is the part that trips people up:

> **GPOs have two halves: Computer Configuration and User Configuration. They are applied to different objects and at different times.**

| Half                             | Applied to           | Applied when          |
| -------------------------------- | -------------------- | --------------------- |
| **Computer Configuration** | The computer account | At boot, before login |
| **User Configuration**     | The user account     | At login              |

If you link a GPO with only User Configuration settings to a **Computers OU**, nothing happens to users - because computer accounts do not process User Configuration. The GPO applies to the computers, not the people logging into them.

This is the exact confusion from a few weeks ago. The fix is always: make sure the GPO is linked to the OU that contains the *type of object* the policy half targets.

**GPO Processing Order - LSDOU**

When multiple GPOs apply, they process in this order (last writer wins):

1. **L**ocal - local policy on the machine itself
2. **S**ite - rarely used
3. **D**omain - applies to everything in the domain
4. **OU** - most specific wins; child OU overrides parent OU

So a GPO linked to `Users\Admins` OU overrides a conflicting setting in a GPO linked to the domain.

---

### Hands-On (20 min)

#### Step 1 - Create Your Personal OU

Each student works in their own OU so your GPOs and objects do not conflict with each other. Do this before anything else.

Open **Active Directory Users and Computers**:

`Server Manager → Tools → Active Directory Users and Computers`

1. In the left pane, right-click the domain (e.g., `SCHOOL14.TEST`) → **New → Organizational Unit**
2. Name it `OU-<firstname>` (replace `<firstname>` with your first name, e.g., `OU-Alex`)
3. Leave **Protect container from accidental deletion** checked, click OK

Now move your accounts and VM into this OU. For each object, right-click it → **Move** → select your new OU:

- Your user account (`<firstname>`)
- Your admin account (`<firstname>-admin`)
- Your VM's computer account (should match your VM's hostname)

> If you are not sure where your accounts are, use **Action → Find**, search by name, and right-click the result to move it.

Your OU is now ready. All GPOs you create in the remaining steps will be linked here.

---

> Now open Group Policy Management on the domain controller.
>
> `Server Manager → Tools → Group Policy Management`

---

#### Step 2 - Orient Yourself

Expand your domain. You will see:

- **Default Domain Policy** - linked at the domain level; applies to all users and computers
- **Default Domain Controllers Policy** - applies specifically to DCs
- Any GPOs your team already created

Click on the **Default Domain Policy** and go to the **Settings** tab. This shows you what is actually configured. Notice it contains both Computer and User configuration sections.

---

#### Step 3 - Redirect Default User and Computer Containers

By default, new user accounts land in `CN=Users` and new computer accounts land in `CN=Computers`. These are plain containers, not OUs - meaning GPOs linked to your Users or Computers OUs will not apply to objects sitting in those default locations.

To redirect new accounts into the correct OUs automatically, you would run these commands on the domain controller (adjust the distinguished name to match your domain).

> Note: this did not work with my chris-admin account, so I did this with the domain administrator account SCHOOL14\Administrator. I changed the password for that account to `P@ssw0rd+` so that if you want to log in and run this command, you can. There is no harm in running it more than once.

```cmd
redirusr "OU=Users,DC=lab,DC=local"
redircmp "OU=Computers,DC=lab,DC=local"
```

After running these, any new account created without an explicit OU target will land in the specified OU and immediately fall under whatever GPOs are linked there. To see this, launch Server Manager --> Tools --> Active Directory Users and Computers, connect to the SCHOOL14.TEST domain if needed, right-click on the domain and add a new user. The values you use don't matter - just give it a name and a password and anything else that might be required but that's all. Don't supply any fields you don't have to.

When you create this user, you will see that it automatically gets put into the `Student Users` OU instead of the `Users` folder.

> Note: accounts created by tools that specify an OU explicitly will still go where the script says - `redirusr` and `redircmp` only change the default fallback.

---

#### Step 4 - Verify GPO Scope with Security Filtering

Click any GPO, then look at the **Scope** tab.

Under **Security Filtering**, you will see `Authenticated Users` by default. This means the GPO applies to all users and computers that are authenticated - everyone.

You can restrict a GPO to a specific group by removing `Authenticated Users` and adding a specific security group. This is how you apply a policy to only, say, the `Student Accounts` group rather than everyone.

---

#### Step 5 - Create a New GPO (User Configuration)

We will create a GPO that sets a desktop wallpaper for your user accounts. This is a common, visible way to verify GPO application is working.

1. In the left pane, right-click **your OU** (`OU-<firstname>`) → **Create a GPO in this domain and link it here**
2. Name it `<firstname> - Desktop Wallpaper`
3. Right-click the new GPO → **Edit**

In the Group Policy Management Editor:

4. Navigate to: `User Configuration → Policies → Administrative Templates → Desktop → Desktop`
5. Double-click **Desktop Wallpaper**
6. Set to **Enabled**
7. **Wallpaper Name:** `C:\Windows\Web\Wallpaper\Windows\img0.jpg`
8. **Wallpaper Style:** `Fill`
9. Click OK and close the editor

> This is under **User Configuration** and linked to your OU, which contains your user accounts. Your OU also contains your VM's computer account - that is fine. Computer accounts ignore User Configuration settings, and user accounts ignore Computer Configuration settings. Each object only processes the half that applies to it.

---

#### Step 6 - Create a New GPO (Computer Configuration)

Now we will make a Computer Configuration policy that disables optical drives (CD/DVD) on your VM - a useful defensive control.

1. Right-click **your OU** (`OU-<firstname>`) → **Create a GPO in this domain and link it here**
2. Name it `<firstname> - Disable Optical Drives`
3. Right-click → **Edit**
4. Navigate to: `Computer Configuration → Policies → Administrative Templates → System → Removable Storage Access`
5. Enable all three of the following settings:
   - **CD and DVD: Deny read access**
   - **CD and DVD: Deny write access**
   - **CD and DVD: Deny execute access**
6. Set each to **Enabled**, click OK

> There is no single "deny all" setting for CD/DVD the way there is for all removable storage, so you need to enable all three. Both GPOs are now linked to the same OU - your user accounts pick up the User Configuration wallpaper policy, and your VM picks up the Computer Configuration optical drive policy.

---

#### Step 7 - Force a Policy Update and Verify

On any domain-joined machine in the lab, open a command prompt and run:

```cmd
gpupdate /force
```

This immediately pulls down and applies all applicable GPOs rather than waiting for the background refresh (which runs every 90 minutes by default).

To see exactly which policies applied and where they came from, run:

```cmd
gpresult /r
```

Look for the section **Applied Group Policy Objects**. You should see your new GPOs listed under either the Computer Settings or User Settings section, depending on which you are checking.

For a full HTML report:

```cmd
gpresult /h C:\gpresult.html
```

Open that file in a browser for a complete breakdown of every applied setting, its source GPO, and whether it was filtered out.

---

#### Step 8 - Intentionally Break It (and Fix It)

To make the earlier confusion concrete, let us see what happens when you link a User Configuration GPO to an OU that contains only computer accounts.

1. In GPMC, right-click the **Student VMs** OU (the one that contains only computer accounts, not your personal OU)
2. Choose **Link an existing GPO**
3. Select the `<firstname> - Desktop Wallpaper` GPO from the list that appears
4. Run `gpupdate /force` on your VM
5. The wallpaper setting will not apply - the GPO is now linked to an OU of computer accounts, which do not process User Configuration

Remove the incorrect link by right-clicking it under the Student VMs OU and choosing **Delete Link** (not Delete GPO).

This is exactly what happened during our failed demo earlier in the year. The policy existed; it just was not linked to the right OU for the right object type.

---

### Wrap-Up (5 min)

Key things to remember:

- AD uses OUs to organize objects and target policy
- GPOs have two halves: **Computer Configuration** (applies at boot) and **User Configuration** (applies at login)
- Link your GPO to the OU containing the *object type* the policy targets
- **LSDOU** is the processing order - more specific OUs win
- `gpupdate /force` refreshes immediately; `gpresult /r` tells you what applied and from where
- Security Filtering lets you scope a GPO to a specific group instead of everyone
