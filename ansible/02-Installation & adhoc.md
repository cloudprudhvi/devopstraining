# 🛠️ Ansible Setup
We will set up Ansible for managing remote servers, commonly referred to as "slaves" or "managed nodes." Our goal is to establish communication between the master (controller) and slave (managed node) using SSH for automation, followed by installing Ansible on the master node.


###  🌟 Step 1: Create the "ansible" user on both Master and Slave nodes
#### 🔧 Why?
We’ll create a dedicated ansible user on both master and slave machines. This user will execute commands remotely. Keeping tasks under a specific user helps improve security and simplifies management.

Log in to both Master and Slave nodes with an existing user that has sudo privileges.

Create the ansible user on both nodes:

```bash
sudo useradd -m -s /bin/bash ansible
```
This creates the ansible user with a home directory (-m) and sets the default shell to /bin/bash.

Set the password for the ansible user:

```bash
sudo passwd ansible
```
You’ll be prompted to enter a password. Use the same password for the ansible user on both the master and slave nodes.

### 🔐 Step 2: Add ansible user to the sudoers file for Password-less Sudo
#### 🤔 Why is this step important?
By adding the ansible user to the sudoers file, we allow it to run commands with sudo privileges without needing to enter a password every time. This is helpful because:

Ansible often needs elevated privileges to perform tasks (like installing software, editing system files, etc.).
Without password-less sudo, you’d be prompted for a password every time Ansible executes tasks requiring sudo.
#### ✨ How to do it:
Edit the sudoers file using visudo:

```bash
sudo visudo
```
This opens the file in a safe way that prevents syntax errors.

Add the following line to give ansible password-less sudo access:

```bash
ansible ALL=(ALL) NOPASSWD:ALL
```
This line means: The ansible user can execute all commands (ALL) on all hosts (ALL) without needing a password (NOPASSWD).

### 🔧 Step 3: Enable Password Authentication in SSH (if disabled)
#### 🤔 Why is this needed?
Some systems have password authentication disabled by default for security reasons, allowing only key-based authentication. Since we’ll first log in using a password before switching to key-based authentication, we need to make sure password authentication is enabled.

Edit the SSH configuration file on both master and slave nodes:

```bash
sudo vi /etc/ssh/sshd_config
```
Ensure these lines are set as follows:

```bash
PasswordAuthentication yes
```
This enables password-based logins.

Restart the SSH service to apply changes:

```bash
sudo service sshd restart
```
### 🔐 Step 4: Set Up SSH Key-based Authentication
Now, we’ll set up SSH key-based authentication for password-less access between the master and slave.

On the master node, switch to the ansible user:

```bash
su - ansible
ssh-keygen -t rsa -b 4096
```

When prompted, accept the default file location by pressing Enter. You can also leave the passphrase blank (just press Enter).

Copy the SSH key to the slave node:

```bash
ssh-copy-id ansible@<slave-ip-address>
```
Replace <slave-ip-address> with the actual IP of the slave node.

Enter the password for the ansible user on the slave when prompted.

Test password-less SSH login from master to slave:

```bash
ssh ansible@<slave-ip-address>
```
If everything is set up correctly, you should be able to log in without being asked for a password. 🎉

### 🤖 Step 5: Install Ansible on the Master Node
Update your package list on the master node:


```bash
sudo yum update -y
sudo yum install epel-release ansible -y
```
Verify the installation by checking the Ansible version:

```bash
ansible --version
```
### 🗂️ Step 6: Set Up Ansible Inventory
Ansible uses an inventory file to keep track of the nodes it manages. The default location for the inventory is /etc/ansible/hosts.

Edit the Ansible inventory file:

```bash
sudo vi /etc/ansible/hosts
```
Add your slave node’s IP or hostname to the inventory:

To ensure that everything is working correctly, we can test the connection using the Ansible ping module.

Run the following command from the master node:

```bash
ansible all -m ping
```

If everything is configured correctly, you should see a pong response from the slave node, confirming communication between the master and slave.

🎉 Success!
