#### But what is this command?

We wll break down each part of this command, explain what it does, and explore the concept of modules in Ansible, including examples of other commonly used modules.

#### 🛠️ Understanding the Ansible Command: ```ansible all -m ping```
📌 Breaking Down the Command
ansible: This is the Ansible command-line tool used to run Ansible tasks on managed nodes directly from the command line, without writing a playbook, we call them as adhoc commands.

`all`: This specifies the inventory pattern that tells Ansible which hosts to target. In this case, all means all the hosts listed in your inventory file.

`-m ping`: The -m option tells Ansible which module to use. Here, we are using the ping module.

#### 🧐 What Does This Command Do?
When you run ansible all -m ping, Ansible attempts to:

Connect to all the hosts defined in your inventory file.
Execute the ping module on each host.
Report the success or failure of the connection.

The ping module checks if Ansible can connect to the managed nodes, execute Python, and return a JSON response. It is a quick way to verify that your Ansible setup is correctly configured and that the master can communicate with the slaves.

#### 🗂️ What is the Ansible Inventory File?

It is where Ansible keeps track of all the machines (servers, virtual machines, cloud instances, etc.) that it can manage.

```bash
[webservers]
192.168.1.10
192.168.1.11

[dbservers]
192.168.1.20

[all]
192.168.1.10
192.168.1.11
192.168.1.20
```

you can group all the machines according to your requirements. By default the ansible inventory file location is `etc/ansible/hosts` file.

you can also create a inventory file and use that too..

But how do you use that to execute, we can use `-i` parameter adn specify the location of inventory file.

```bash
ansible-playbook -i inventory.ini playbook.yaml
```

### Now let's discuss about modules

#### what are modules?

Modules are the main building blocks of Ansible playbooks.

| Module Type     | Description                                                                       |
|-----------------|-----------------------------------------------------------------------------------|
| System Modules  | Manage system-level tasks like user accounts, groups, cron jobs, and system services. |
| File Modules    | Manage files, directories, and permissions.                                       |
| Command Modules | Execute commands or scripts on remote machines.                                   |
| Package Modules | Manage package installations, updates, and removals across Linux systems.         |
| Service Modules | Control system services like starting, stopping, restarting, and enabling services to run at boot. |


### Description of Commonly Used Modules and Example Commands

#### 1. System Modules
**Commonly Used Modules:**
- **user**: Manages user accounts.
- **group**: Manages groups.
- **cron**: Manages cron jobs.
- **hostname**: Manages the system hostname.
- **sysctl**: Manages kernel parameters.

**Example Commands:**
- `ansible all -m user -a "name=ansible state=present"`  
  Creates the `ansible` user.
- `ansible all -m cron -a "name=backup job='* * * * *' user=root"`  
  Creates a cron job for backups.

#### 2. File Modules
**Commonly Used Modules:**
- **copy**: Copies files from the controller to hosts.
- **file**: Manages file attributes like permissions.
- **template**: Processes Jinja2 templates before copying them to hosts.
- **stat**: Gathers statistics for files or directories.

**Example Commands:**
- `ansible all -m copy -a "src=/local/path/file dest=/remote/path/file"`  
  Copies a file to the remote host.
- `ansible all -m file -a "path=/tmp/test mode=0755 state=directory"`  
  Creates a directory with specified permissions.

#### 3. Command Modules
**Commonly Used Modules:**
- **command**: Runs commands without invoking a shell.
- **shell**: Runs shell commands with support for shell features like pipes.
- **raw**: Executes low-level commands without a shell, useful for bootstrapping systems.

**Example Commands:**
- `ansible all -m command -a "ls /var/log"`  
  Lists the contents of `/var/log`.
- `ansible all -m shell -a "echo 'Hello World' > /tmp/hello.txt"`  
  Writes "Hello World" to a file on the remote system.

#### 4. Package Modules
**Commonly Used Modules:**
- **apt**: Manages packages on Debian/Ubuntu-based systems.
- **yum**: Manages packages on RHEL/CentOS-based systems.
- **dnf**: Manages packages on Fedora/RHEL8+ systems.
- **pip**: Manages Python packages.

**Example Commands:**
- `ansible all -m apt -a "name=nginx state=latest"`  
  Installs the latest version of `nginx` on Debian systems.
- `ansible all -m yum -a "name=httpd state=absent"`  
  Removes `httpd` from RHEL-based systems.

#### 5. Service Modules
**Commonly Used Modules:**
- **service**: A generic module for managing services.
- **systemd**: Manages services on systemd-based systems.
- **supervisorctl**: Manages services using Supervisor.

**Example Commands:**
- `ansible all -m service -a "name=nginx state=started"`  
  Starts the `nginx` service.
- `ansible all -m systemd -a "name=nginx state=enabled"`  
  Enables the `nginx` service to start at boot.

okay!! Now lets install httpd server.

```ansible
ansible all -m yum -a "name=httpd state=present" --become
```

```ansible
ansible all -m copy -a "src=/home/ansible/index.html dest=/var/www/html/index.html" --become
```
```bash
ansible all -m service -a "name=httpd state=restarted" --become
```

we have now installed httpd server.

Executing Individual commands is not convineint, we can use Playbook file which is yaml file.
lets try to run the playbook.

### Convert Ad-Hoc Commands to an Ansible Playbook

```yaml
---
- name: Install and Configure HTTPD server.
  hosts: all
  become: true
  tasks:
    - name: Install httpd
      yum:
       name: httpd
       state: present
    - name: Copy index.html file
      copy:
       src: /home/ansible/index.html
       dest: /var/www/html/index.html
    - name: Restart the server
      service:
        name: httpd
        state: restarted
```