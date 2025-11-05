# Creating a Windows Server Virtual Machine (VM) in ISERINK

To begin the process of creating a new VM in vSphere, navigate to School 14's inventory page. Right-click the **School 14** icon on the left and choose **New Virtual Machine**. Here is a summary of what to fill out in each step.

## Setting up the VM Definition in vSphere

1. In the **Select a creation type** tab, choose **Create a new virtual machine**. Click **Next**.
2. In the **Select a name and folder** tab, give your VM a name (see bullets below)and choose **School 14** as the folder.
   * This VM name can be anything you want, as long as it starts with your name, initials, or hacker name.
   * Please always start your VM names the same way so we can tell who owns each one.
   * **Note:** this does not set the hostname for your VM. It is just a way to label the VM in the vSphere UI.
   * After supplying the VM name and selecting the **School 14** Folder, click **Next**.
3. In the **Select a compute resource** tab, choose **School 14**. Click **Next**.
4. In the **Select Storage**  tab, choose **Highschool Storage.**
5. In the **Select compatibility** tab, leave the value at its default value and click **Next**.
6. In the **Select a guest OS** tab, select **Windows** as the **Guest OS Family** and **Microsoft Windows Server 2022 (64-bit)** as the **Guest OS Version**. Click **Next**.
7. In the **Customize hardware** tab, change the contents of the virtual CD/DVD drive.
   * For the **New Hard disk** section:
     * **THIS STEP IS VERY IMPORTANT. IF YOU FORGET TO DO THIS YOU MAY HAVE TO DESTROY AND REBUILD YOUR VM**
     * Expand this section and find the setting for **Disk Provisioning**.
     * Set **Disk Provisioning** to **Thin Provisoin**.
   * For the **New CD/DVD Drive** section:
     * Click the dropdown list that currently says **Client Device**.
     * Select **Datastore ISO File**. This will pop up an file selection interface.
     * Choose the file **SERVER_EVAL_x64FRE_en-us.iso** inside the **Playground ISO Datastore** folder and click OK.
       * VM managers like vSphere can mount an image file, like the one you have just selected, and treat it like a device. In this case, vSphere will treat the ISO file you selected like a CD/DVD disk.
     * Click the checkbox labeled **Connect at Power On** (you might not be able to see the full label - it might only display the "Connect" part).
   * Click **Next**.
8. In the **Ready to complete** tab, review the contents to be sure everything looks right.

At this point, your new VM should appear in the list of VMs on Team 14. If it does not, and if you can't determine what went wrong, put a message in Zulip (either under the relevant class thread or in the #help channel).

## Installing Windows Server on the VM

Since the new VM has a Windows Server DVD connected to it, it will try to boot from that (virtual) DVD. However, this particular DVD asks you to press a key before it will load. That screen is likely to time out in between the time when you start your VM and when you can load the web console.

This isn't a big problem, though. The web console has a button that will let you send Ctrl-Alt-Delete to the VM. Click that button and then click inside the VM so that you are ready to press a key when prompted to, and you will enter the Windows installer.

Instructions for the Windows installation may be written out verbosely later. Here are some key facts:

1. Include the desktop experience unless you have a reason not to.
2. You will need a password for the local administrator account that passes a complexity check. Sadly, and conveniently, 'P@ssw0rd' works and you can use it as an easy-to-remember password in a playground environment.
3. You'll probably want to install the **VMware Tools**. They make the web console experience a lot more enjoyable.
4. If you rename your computer, make sure nobody else on our subnet (on our team, basically) is using the same computer name. Two computers on the same network with the same name breaks stuff.
5. Networking
   * Subnet: 144.76.90.0/24
     * This is the same as 144.76.90.0 and a subnet mask of 255.255.255.0
     * Both of them mean "anything that starts 144.76.90.0 is on the same network."
   * Default gateway: 144.76.90.254
   * DNS: 199.100.16.100
   * Proxy
     * http://199.100.16.100:3128
     * Bypass proxy for local server addresse: on
