What is an Operating System?


**Definition:**

An Operating System (OS) is system software that manages computer hardware, software resources, and provides common services for computer programs.


**Core Functions:**

Process Management: Manages the execution of programs.

Memory Management: Handles allocation and deallocation of memory.

File System Management: Organizes, stores, and retrieves data on storage devices.

Device Management: Controls peripheral devices through drivers.

User Interface: Provides a user interface, either command-line or graphical, for interaction.

What Does an Operating System Do?


**Resource Allocation:**

Distributes CPU time, memory, and storage to various programs running on the system.


**Security and Access Control:**

Ensures data security through user authentication, permissions, and encryption.


**System Stability and Error Handling:**

Monitors the system to detect and respond to errors, ensuring smooth operation.


**Task Scheduling:**

Manages the execution of multiple tasks, allowing for multitasking and efficient resource use.


**Hardware Abstraction:**

Abstracts the complexities of hardware, providing a consistent way for software to interact with it.

Differences Between Linux and Windows


**Source Model:**

Linux: Open-source, freely available for modification and distribution.

Windows: Proprietary software by Microsoft.


**User Interface:**

Linux: Command-line interface (CLI) is powerful.

Windows: Predominantly GUI-based with a standard desktop environment.


**Security:**

Linux: Generally more secure due to its permissions model and open-source nature.

Windows: More vulnerable to viruses and malware, though security has improved in recent versions.


**Customization:**

Linux: Highly customizable, from the kernel to the desktop environment.

Windows: Limited customization options compared to Linux.

Benefits of Using Linux


**Cost:**

Free to use and distribute, with no licensing fees.


**Security:**

Built with security in mind; fewer vulnerabilities and faster patches.


**Stability and Reliability:**

Known for its robustness; often used in servers and critical systems.


**Performance:**

Efficient resource usage, making it ideal for both old and new hardware.


**Community Support:**

Extensive online communities, forums, and documentation provide support and resources.

Popular Linux Distributions


**Ubuntu:**

User-friendly, widely used by beginners and experienced users alike.


**Fedora:**

Known for cutting-edge features and technologies, supported by Red Hat.


**Debian:**

A stable and versatile distribution, with a focus on free software.


**CentOS:**

Enterprise-class operating system, community-driven, and derived from Red Hat Enterprise Linux.

Overview of Linux Directory Structure


**/ (Root Directory):**

The top-level directory in the Linux file system.

All other directories and files are located under this directory.


**/bin (Binary Executables):**

Contains essential command binaries (e.g., ls, cp, mv) needed for the system to boot and run in single-user mode.


**/boot (Boot Loader Files):**

Stores boot loader files (e.g., GRUB), kernel images, and other essential files required to start the system.


**/dev (Device Files):**

Contains special files representing hardware devices (e.g., /dev/sda for a hard drive).


**/etc (Configuration Files):**

System-wide configuration files and shell scripts used to boot and start system services.


**/home (User Home Directories):**

Each user gets a directory in /home (e.g., /home/user1).

Stores personal files, settings, and user-specific data.


**/lib (Shared Libraries):**

Contains shared libraries needed by the binaries in /bin and /sbin.

Holds kernel modules and system libraries.


**/var (Variable Files):**

Stores files that are expected to grow in size, such as logs (/var/log), mail (/var/mail), and spool files.


**/tmp (Temporary Files):**

Used to store temporary files created by applications.

Data in /tmp is typically cleared on reboot.


**/usr (User Programs):**

Contains user-installed software and libraries.

Subdirectories include /usr/bin, /usr/lib, /usr/local, and /usr/share.

Basic System Information


**Command: uname**


*Example: uname*


```bash
Output: Linux (or other operating system)
```


**Command: uname -r**


*Example: uname -r*


```bash
Output: 5.15.0-58-generic (or other kernel version)
```


**Command: uname -a**


*Example: uname -a*


```bash
Output: Linux ubuntu 5.15.0-58-generic SMP PREEMPT RT x86_64 x86_64 x86_64 GNU/Linux (or similar)
```

System Uptime and Time


**Command: uptime**


*Example: uptime*


```bash
Output: 15:34:21 up 1 day, 17 min, 20 users, load average: 0.00, 0.00, 0.00
```


**Command: uptime -s**


*Example: uptime -s*


```bash
Output: 2024-08-23 15:17:01
```


**Command: hostname**


*Example: hostname*


```bash
Output: ubuntu (or other hostname)
```


**Command: hostname -i**


*Example: hostname -i*


```bash
Output: 192.168.1.100 (or other IP address)
```

Network Information


**Command: ip route**


*Example: ip route*


```bash
Output: default via 192.168.1.1 dev eth0 metric 202 (or similar)
```


**Command: date**


*Example: date*


```bash
Output: Fri Aug 23 15:34:21 IST 2024
```


**Command: timedatectl**


*Example: timedatectl*


```bash
Output: Local time: Fri 2024-08-23 15:34:21 IST (or similar)
```

Calendar and System History


**Command: cal**


*Example: cal*


```bash
Output: (displays current month's calendar)
```


**Command: cal 2023**


*Example: cal 2023*


```bash
Output: (displays calendar for 2023)
```


**Command: cal 09 2024**


*Example: cal 09 2024*


```bash
Output: (displays calendar for September 2024)
```


**Command: last reboot**


*Example: last reboot*


```bash
Output: (displays system reboot history)
```

User Information and System Processes


**Command: who**


*Example: who*


```bash
Output: user tty date time ip (displays logged-in users)
```


**Command: whoami**


*Example: whoami*


```bash
Output: user (displays current user)
```


**Command: top**


*Example: top*


```bash
Output: (displays running processes)
```

Hostname and Timezone


**Command: hostnamectl**


*Example: hostnamectl*


```bash
Output: (displays hostname information)
```


**Command: hostnamectl set-hostname flm**


*Example: hostnamectl set-hostname flm*


```bash
Output: (sets hostname to "flm")
```


**Command: ip address**


*Example: ip address*


```bash
Output: (displays network interface information)
```


**Command: timedatectl set-timezone Asia/Kolkata**


*Example: timedatectl set-timezone Asia/Kolkata*


```bash
Output: (sets timezone to Asia/Kolkata)
```

CPU Information Commands


1. 1. lscpu


>Description: Displays detailed information about the CPU architecture of your system, including the number of CPUs, cores, threads, model name, speed, and cache size.


*Usage:*

lscpu


1. 2. cat /proc/cpuinfo


>Description: Reads and displays detailed information about the CPU from the /proc filesystem. It provides information per CPU core.


*Usage:*

cat /proc/cpuinfo

cat /proc/meminfo


>Description: Displays detailed information about the system's memory usage, including total available memory, free memory, buffers, cached memory, and swap space.


1. 2. free


>Description: Displays the total amount of free and used physical and swap memory in the system, as well as the buffers and caches used by the kernel.


*Usage:*

free


**Example Output (in Kilobytes):**

total        used        free      shared  buff/cache   available

Mem:       16389876    11234567     2123456      345678     3012345     5432100

Swap:       2097148           0     2097148


**Usage with Megabytes:**

bash

Copy code

free -m


**Example Output (in Megabytes):**

total        used        free      shared  buff/cache   available

Mem:          16012       10967        2075         337        2942        5303

Swap:          2047           0        2047

Disk Usage Commands


1. 1. lsblk -a


>Description: Lists information about all block devices attached to the system, including their names, sizes, types, and mount points. The -a option includes empty devices as well.


*Usage:*

lsblk -a


**Example Output:**

NAME   MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT

sda      8:0    0 476.9G  0 disk

├─sda1   8:1    0   512M  0 part /boot/efi

├─sda2   8:2    0   732M  0 part /boot

└─sda3   8:3    0 475.7G  0 part /

sr0     11:0    1  1024M  0 rom


1. 2. df -h


>Description: Reports file system disk space usage, showing how much space is used, available, and the percentage of use on each mounted filesystem. The -h option displays sizes in a human-readable format.


*Usage:*

df -h

sudo mkfs -t xfs /dev/xvdb (making the device as filesystem)
sudo mount /dev/xvdb /opt/data (this is mount dir)


1. 3. du filename


>Description: Estimates the disk usage of the specified file or directory. It shows how much space a file or directory consumes.


*Usage:*

du filename


*Example:*

du /var/log/syslog


**Example Output:**

2048    /var/log/syslog

(Output indicates that /var/log/syslog is using 2048 kilobytes of disk space.)


1. 4. du -sh filename


>Description: Provides a summarized and human-readable estimate of disk usage for the specified file or directory. The -s option summarizes, and the -h option formats the size in human-readable units.


*Usage:*

du -sh /var/log


**Example Output:**

150M    /var/log

(This indicates that the /var/log directory is consuming 150 megabytes of disk space.)


1. 5. fdisk -l


>Description: Lists all available disk partitions and their details, including device names, sizes, types, and identifiers. Useful for getting detailed information about disk volumes.


*Usage:*

sudo fdisk -l


**Example Output:**

python

Copy code

Disk /dev/sda: 477 GB, 477019264000 bytes, 931520000 sectors

Units: sectors of 1 * 512 = 512 bytes

Sector size (logical/physical): 512 bytes / 4096 bytes

I/O size (minimum/optimal): 4096 bytes / 4096 bytes

Disklabel type: gpt

Disk identifier: B1234567-89AB-CDEF-0123-456789ABCDEF

Device         Start       End   Sectors   Size Type

/dev/sda1       2048   1050623   1048576   512M EFI System

/dev/sda2    1050624   2562047   1511424   738M Linux filesystem

/dev/sda3    2562048 931517439 928955392 443.1G Linux filesystem

Process Management Commands


1. 1. ps


>Description: Displays information about the currently running processes. By default, it shows processes running in the current shell session.


*Usage:*

ps


**Example Output:**

PID TTY          TIME CMD

2345 pts/0    00:00:00 bash

3456 pts/0    00:00:00 ps


**Common Options:**

ps aux: Shows all running processes on the system with detailed information.

ps -ef: Another format to display all processes with full details.


**Example with Options:**

ps aux | grep java


1. 2. kill -9 PID


>Description: Forcefully terminates a process by specifying its Process ID (PID). The -9 option sends the SIGKILL signal, which immediately stops the process.


*Usage:*

kill -9 1234

(This command will forcefully terminate the process with PID 1234.)


>Steps to Use:

Identify the PID of the process you want to terminate using commands like ps or top.

Execute the kill -9 PID command with the appropriate PID.


>Caution:

Use this command carefully, as terminating critical system processes can lead to system instability.

Prefer using kill PID without -9 first, which sends a gentle termination signal.


1. 3. dmesg


>Description: Displays kernel-related messages, including bootup messages, hardware errors, and driver information. Useful for diagnosing hardware and system issues.


*Usage:*

dmesg


**Common Options:**

dmesg | less: View messages page by page.

dmesg | grep error: Filter and display only error messages.

dmesg -T: Show human-readable timestamps.


**Example with Options:**

dmesg -T | grep USB


**Example Output:**

yaml

Copy code

[Fri Aug 23 10:00:00 2024] USB Serial support registered for FTDI USB Serial Device

[Fri Aug 23 10:00:01 2024] usbcore: registered new interface driver usb

File Creation Commands

touch filename

Used to create a single file.


*Example: touch file1*

touch f1 f2 f3

Used to create multiple files.


*Example: touch f1 f2 f3*

touch file{1..5}

Create 5 files at a time.


*Example: touch file{1..5} (Creates file1, file2, file3, file4, file5)*

File Deletion Commands

Title: File Deletion with rm

rm filename

Used to remove a single file.


*Example: rm file1*

rm f1 f2 f3

Used to remove multiple files.


*Example: rm f1 f2 f3*

rm file{1..5}

Used to remove 5 files at a time.


*Example: rm file{1..5}*

rm -f filename

Used to forcefully remove a file without prompting for confirmation.


*Example: rm -f file1*

rm -f *

Used to remove all files in the current directory at once.


*Example: rm -f **

Directory Creation Commands

mkdir folder

Used to create a single directory.


*Example: mkdir folder*

mkdir 1 2 3

Used to create multiple directories.


*Example: mkdir 1 2 3 (Creates directories 1, 2, 3)*

mkdir a/b

Creates folder b inside folder a if a exists; otherwise, displays an error.


*Example: mkdir a/b*

mkdir -p a/b

Creates folder b inside folder a. If a doesn't exist, it creates a first.


*Example: mkdir -p a/b*

mkdir folder{1..7}

Used to create multiple directories at once.


*Example: mkdir folder{1..7} (Creates folder1, folder2, ..., folder7)*

Directory Deletion Commands

rmdir folder

Used to remove an empty directory.


*Example: rmdir folder*

rmdir *

Used to remove all empty directories in the current directory.


*Example: rmdir **

rm -rf folder/*

Deletes all files inside the folder but leaves the folder itself.


*Example: rm -rf folder/**

rm -rf folder/filename

Deletes a particular file inside a specified folder.


*Example: rm -rf folder/file1*

rm -rf folder

Deletes the specified folder along with all its contents.


*Example: rm -rf folder*

rm -rf *

Removes all files and directories in the current directory.


*Example: rm -rf **

Navigating Directories

cd foldername

Changes the current directory to foldername.


*Example: cd folder1*

cd ..

Moves one directory up.


*Example: cd ..*

cd ../../..

Moves three directories up.


*Example: cd ../../..*

cd -

Switches back to the previous directory.


*Example: cd -*

cd ~ or cd

Changes to the home directory.


*Example: cd ~*

cd /

Changes to the root directory.


*Example: cd /*

Viewing Directory Contents

Title: Viewing Files with ls and ll

pwd

Displays the current working directory.


*Example: pwd*

ll or ls -l

Lists all files in the directory with detailed information.


*Example: ll*

ls

Lists file names only.


*Example: ls*

ls folder1

Lists the files in folder1.


*Example: ls folder1*

ll -a or ls -al

Lists all files, including hidden ones.


*Example: ll -a*

ll -r or ls -r

Lists files in reverse order.


*Example: ll -r*

ll -t

Lists the latest modified files at the top.


*Example: ll -t*

ll -ltr

Lists files in long format, sorted by modification time, newest first, then reversed.


*Example: ll -ltr*

Copying Files

cp file1 file2

Copies content from file1 to file2. If file2 doesn’t exist, it is created.


*Example: cp file1 file2*

cp file1 folder1

Copies file1 to folder1.


*Example: cp file1 folder1*

Moving and Renaming Files

mv file1 file2

Moves or renames file1 to file2.


*Example: mv file1 file2*

mv file1 folder1

Cuts file1 and pastes it into folder1.


*Example: mv file1 folder1*

Comparing Files

cmp file1 file2

Compares file1 and file2 byte by byte.


*Example: cmp file1 file2*

diff file1 file2

Displays differences between file1 and file2 line by line.


*Example: diff file1 file2*

Working with cat Command

cat > filename

Creates a file and allows you to write data. Press Ctrl+D to save and exit.


*Example: cat > file1*

cat >> filename

Appends data to an existing file.


*Example: cat >> file1*

cat -n filename

Displays file contents with line numbers.


*Example: cat -n file1*

cat filename

Reads and displays the contents of a file.


*Example: cat file1*

cat f1 f2 f3

Concatenates and displays the contents of multiple files.


*Example: cat f1 f2 f3*

Reversing and Displaying File Contents

tac filename

Reverses the contents of a file (bottom to top).


*Example: tac file1*

rev filename

Reverses the contents of a file (left to right).


*Example: rev file1*

Displaying Specific Lines

head filename

Prints the first 10 lines of a file.


*Example: head file1*

tail filename

Prints the last 10 lines of a file.


*Example: tail file1*

sed -n '5,9p' filename

Prints lines 5 to 9 of a file.


*Example: sed -n '5,9p' file1*

sed 's/old_word/new_word/g' filename

sed -i 's/old_word/new_word/g' filename

sed -n '7p' filename

Prints the 7th line of a file.


*Example: sed -n '7p' file1*

head -n 8 filename

Prints the first 8 lines of a file.


*Example: `head -n*

Locating Files


**locate:**


>Description: Lightweight command used to find files quickly by searching a pre-built database.


>Behavior: Searches for the given file in a backend database, which updates once a day.

Issue: May not find newly created files if the database hasn’t been updated.


**Commands:**

Update the database: sudo updatedb

Locate a file: locate filename


**find:**


>Description: Searches for files or folders by scanning the actual filesystem.


>Advantages: Does not depend on a database and provides multiple search options (by name, size, user, date, permissions, etc.).


**Commands:**

Find by name: find / -name filename

Case-insensitive search: find / -iname f1

Find in a specific directory: find /home/ec2-user -name filename

Find directories by name: find / -type d -name dirname

Find files by permissions: find / -type f -perm 0644

Comparing Files


**cmp:**


>Description: Compares two files byte by byte.


>Behavior: If the files are identical, it returns no output; if they differ, it shows the location of the first difference.


**Command:**

Compare two files: cmp f1 f2


**diff:**


>Description: Compares files line by line and prints the differences between them.


**Command:**

Compare and display differences: diff f1 f2

Searching Inside Files with grep


**grep:**


>Description: Searches for a word or pattern inside a file without opening it.


**Usage Examples:**

Basic search: grep "searchword" filename

Search with line numbers: grep -n "wordname" filename

Case-insensitive search: grep -i "wordname" filename

Count occurrences: grep -c "wordname" filename

Search multiple words: grep -e "word1" -e "word2" filename

Search across multiple files: grep -e "wordname" file1 file2

Date Filters


**date Command Filters:**


**Retrieve Specific Date/Time Components:**

Day: date +"%d"

Month: date +"%m"

Year: date +"%y"

Hour: date +"%H"

Minute: date +"%M"

Seconds: date +"%S"


**Formatted Date Outputs:**

Date with format change: date +"%D" or date +"%F"

Day in English: date +"%A"

Month in English: date +"%B"

Time: date +"%T"

Manual Pages and Binary Search

Title: Using man, whereis, and which


**man:**


>Description: Displays a detailed manual for commands.


**Usage Examples:**

General command manual: man command


*Example: man ls, man nmap*


**whereis:**


>Description: Locates the binary, source, and manual page for a command.

Usage Example: whereis locate


**which:**


>Description: Specifically searches for a binary in the directories listed in the PATH environment variable.

Usage Example: which locate

User Management - Adding Users


**Adding a User:**


**Commands:**

Basic: adduser username

With User ID (UID): adduser -u 8765 pop

With UID and Group ID (GID): adduser -u 6578 -gid 8765 bob


>Note:

Creating a user also creates a group with the same name.

A directory is automatically created in /home with the username.


**Backend Processes:**

/etc/passwd: Contains user information.

/etc/shadow: Stores user password information.

/etc/group: Stores group information.

/etc/gshadow: Contains group password information.


**Example Entry:**

kali:x:1000:1000:,,,:/home/kali:/usr/bin/zsh

kali: Username

x: Password (stored in /etc/shadow)

1000: UID

1000: GID

/home/kali: Home directory

/usr/bin/zsh: Default shell


**Setting a Password:**


**Command: passwd pop**


**Login as User:**


**Command: su - pop**

User Management - Removing Users

Title: Removing Users with userdel


**Removing a User:**

Basic Command: userdel username


*Example: userdel dhoni*


**Remove User and Home Directory:**


**Command: userdel -r virat**


**Force Removal (User and Files):**


**Command: userdel -r -f rohit**


>Note:

Deleting a user does not delete their home folder unless specified with -r.

Only one user can be deleted at a time.

User Management - Expiration and Groups


**User Expiration:**


**Set Expiration Date:**


**Command: useradd -e 2023-08-25 username**

Effect: User account is automatically disabled after the specified date.


**Managing Groups:**

Adding a Group Manually: groupadd groupname


*Example: groupadd Sandy*

Deleting a Group: groupdel groupname


*Example: groupdel Sandy*


**Changing File Ownership:**

Change File Owner: chown username filename

Change Group Owner: chgrp groupname filename

Change Both User and Group: chown username:groupname filename

File Permissions


**Understanding File Permissions:**


**Permission Types:**

Read (r): 4

Write (w): 2

Execute (x): 1


**Permission Sets:**

Owner (u), Group (g), Others (o)


**Changing Permissions:**


**Using Symbols:**

Add Execute for Owner: chmod u+x file

Remove Write for Group: chmod g-w file

Set Permissions Exactly: chmod u=rwx,g=rw,o=r file


**Using Numeric Codes:**

All Permissions: chmod 777 file

Read-Write for Owner, Read-Only for Others: chmod 644 file


**Recursive Permission Change:**

Change Permissions for Directory and Contents: chmod -R 777 folder

SSH - Secure Shell

What is SSH?


>Description: SSH (Secure Shell) is a protocol used to securely connect and control remote systems.


**Basic SSH Commands:**

Check SSH Status: service ssh status

Start SSH: service ssh start

Stop SSH: service ssh stop

Restart SSH: service ssh restart


**Login to Remote Server:**


**Command: ssh username@server_public_IP**


>Note:

SSH requires both systems to be on the same network or accessible via the internet.

Process Management Overview


**Process:**

A process is a program in execution.

In Linux, all commands run in the terminal/shell.

Process Management: The act of tuning or controlling the execution of a process.


**Types of Processes:**


**Foreground Process:**

Runs in the terminal and blocks it until completion.


*Example: Running a script directly in the terminal.*


**Background Process:**

Runs in the background, allowing terminal use for other commands.

Must be manually created using & after the command.


*Example: python file.py &*

Types of Processes


**Parent Process:**

Created by the user.

All processes have a parent process.

If initiated directly by the user, the kernel process is the parent.


**Child Process:**

Created by another process.


**Orphan Process:**

A child process whose parent has completed its execution.

Adopted by the init process.


**Zombie Process:**

A process that has completed execution but still appears in the process table.


**Daemon Process:**

System-related background processes.

Critical for OS functionality.

Process Management Commands

ps: Displays current process information.

ps -e: Shows daemon processes.

ps -f: Full process information, showing parent-child relationships.

ps aux: Shows all processes running on the system.

jobs: Lists jobs running or suspended in the background.


**Creating Background Processes:**

Foreground: command

Background: command &


**Managing Processes:**

Bring to Foreground: fg %PID

View Processes: top (press q to quit)

Understanding top Command

top: Displays a real-time dynamic view of running processes.


**Key Metrics:**

PID: Process ID.

PR: Process priority (lower value = higher priority).

NI: Nice value (lower = higher priority).

VIRT: Virtual memory used by the process.

USER: User who created the process.

%CPU: CPU usage percentage.

%MEM: Memory usage percentage.

COMMAND: Command that created the process.

Managing Processes with kill


**Kill Signals:**

kill -signal PID: Sends a signal to a process.


**Common Signals:**

kill -2 PID: Interrupt (Ctrl + C).

kill -9 PID: Forceful termination.

kill -15 PID: Graceful termination.

kill -STOP PID: Stop process.


**Use Cases:**

Terminate unresponsive processes.

Pause and resume processes.

Networking Commands

ifconfig -a: Displays network configuration for all interfaces.

eth0: Ethernet/LAN info.

lo: Loopback interface (typically Wi-Fi configuration).

hostname: Displays machine hostname.

hostname -i: Displays IP address.

host: DNS lookup activity.


*Example: host instagram.com*

netstat: Displays all listening ports and active connections.

netstat -l: List all listening ports.

netstat -t: Show active TCP connections.

Popular Network Tools


**Popular Ports:**

SSH: Port 22

HTTP: Port 80

DNS: Port 53

HTTPS: Port 443

ping: Checks network connectivity.


*Example: ping google.com*

dig: Queries DNS servers for information.


*Example: dig instagram.com*

whois: Displays website information.


*Example: whois instagram.com*

Advanced Network Commands

ip: Command-line tool for network administration.

ip addr: Similar to ifconfig.

ip route: Displays routing table.

ifstat: Displays IN/OUT packet information.


*Example: ifstat*

traceroute: Displays path to a destination, showing all intermediate routers.


*Example: traceroute www.google.com*

ethtool: Displays detailed network interface information.


*Example: ethtool eth0*

Web Utilities - curl and wget

curl: Retrieves data from the internet via the terminal.


*Example: curl https://www.facebook.com/*

Log Parsing Example: curl "log path file" | grep ERROR

wget: Downloads files from the web to the local system.


*Example: wget log_link*


**Difference:**

curl: Performs the task in a single command.

wget: Typically involves downloading and then processing the file.

Aliases and Crontab


**Aliases:**

Definition: Temporarily renaming a command for convenience.


*Example: alias dhoni="ls -l"*

Permanent Alias: Edit .zshrc or .bashrc and add the alias.


**Crontab:**

Purpose: Schedule tasks to be executed in the future.


**Commands:**

View Crontabs: crontab -l

Edit/Add Crontab: crontab -e


**Scheduling Example:**


**Command: 18 11 * * * echo "hi" > file.txt**

Meaning: Executes at 11:18 AM.

Disk Usage and Piping

du: Displays memory usage of a file or directory.

Human-Readable Format: du -h /home/kali/Downloads


**Piping (|):**

Purpose: Redirects output of one command as input to another.


*Example: command1 | command2*

Use Case: top | head (shows top processes and their details).

Process and Data Filtering with awk

ps -ef: Provides detailed process information, including daemon processes.

nproc: Displays the number of CPUs in the current machine.

awk: Powerful tool for filtering and processing data.


*Example: awk -F" " '{print $n}' (where n is the column number).*


**Difference between grep and awk:**

grep: Returns entire lines that match a pattern.

awk: Allows selection of specific columns from the output.