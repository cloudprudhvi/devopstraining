#### 🤔 I Have Two Different Playbooks—Can I Simplify This?
Imagine you're working with both RedHat-based systems (like CentOS or RHEL) and Debian-based systems (like Ubuntu). Now, when you want to install a web server, you realize:

For RedHat, the package to install is httpd.
But for Ubuntu, the package is called apache2.
So, naturally, you think:

"I should write two different playbooks, right?"

Let’s give that a try!

#### 📝 Playbook 1: Installing httpd on RedHat-Based Systems
```yaml
---
- name: Install HTTPD on RedHat-based systems
  hosts: all
  become: true
  tasks:
    - name: Install httpd
      yum:
        name: httpd
        state: present
```
This playbook works perfectly fine for RedHat-based systems. It uses the yum module to install httpd. But then you think, "What about Ubuntu?"

#### 📝 Playbook 2: Installing apache2 on Ubuntu (Debian-Based Systems)
```yaml
---
- name: Install Apache2 on Debian-based systems
  hosts: all
  become: true
  tasks:
    - name: Install apache2
      apt:
        name: apache2
        state: present
```
Here, the apt module is used to install apache2 on Ubuntu or other Debian-based systems. Great, now you have two playbooks! But...

**🤨 Wait a Minute... Two Playbooks? Really?**
Now you’re thinking:

"Do I need two separate playbooks for this? What if I have a mixed environment with both RedHat and Ubuntu servers?"

Wouldn’t it be easier to combine both playbooks into one? 🤔

#### 💡 The Solution: Use One Playbook with the when Condition
Rather than writing and managing two separate playbooks, you can use one playbook for both RedHat and Debian-based systems. But how? Here's where Ansible's when condition and facts come to the rescue!

Ansible automatically gathers facts about the system, including the ansible_os_family fact, which tells you whether the machine is based on RedHat or Debian. You can use this fact to install the correct package based on the OS.

📝 Unified Playbook Using the when Condition
```yaml
---
- name: Install the correct web server based on OS family
  hosts: all
  become: true
  tasks:
    - name: Install httpd on RedHat-based systems
      yum:
        name: httpd
        state: present
      when: ansible_os_family == "RedHat"

    - name: Install apache2 on Debian-based systems
      apt:
        name: apache2
        state: present
      when: ansible_os_family == "Debian"
```

#### 🔍 How Does This Work?
This single playbook does the following:

It checks the ansible_os_family fact for each system. This fact is automatically gathered by Ansible and tells us whether the system is RedHat or Debian-based.

The when condition ensures:

- If the OS family is RedHat, it installs httpd using yum.

- If the OS family is Debian, it installs apache2 using apt.
🤯 Isn't That Easier?

Now, instead of managing two separate playbooks, you have one unified playbook that works on both RedHat and Debian-based systems. The playbook is smarter, cleaner, and more efficient. 💡

🚀 Running the Unified Playbook
You can run this single playbook across both types of systems with one simple command:

```bash
ansible-playbook webserver_install.yml
```
Ansible will take care of the rest by installing the correct package on each server based on its OS family. 🎉

### 📚 Understanding Variables in Ansible
#### 🤔 What are Variables in Ansible?
You might be asking yourself, "What are these variables everyone keeps talking about in Ansible?"

Well, variables in Ansible are like containers that store data values (such as text, numbers, lists, etc.). Think of them as labels that help you reuse information across your playbooks, tasks, and roles without hardcoding the same value multiple times.

#### 🎯 Why Use Variables?
"Okay, but why should I care about variables?"

Here’s why they’re awesome:

`🧹 Cleaner Playbooks`: Instead of repeating the same values over and over, you define a variable once and use it everywhere.

`🔄 Dynamic Playbooks`: You can pass different values to your playbook depending on the environment (like development or production).

`💡 Flexibility`: You can change variables easily without needing to modify the entire playbook.

#### 📝 How Do You Define Variables?
"How do I create a variable?"

It’s super easy! You define variables using YAML syntax. Here’s a basic example:

```yaml
---
- hosts: all
  vars:
    my_message: "Hello, Ansible students!"  # This is a variable
  tasks:
    - name: Display the message
      debug:
        msg: "{{ my_message }}"  # Use the variable with double curly braces
```
In this example:

 - my_message is the variable name.
 - "Hello, Ansible students!" is the value stored in the variable.
 - The debug module is used to display the variable's value.
