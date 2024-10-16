## Introduction to Roles
### 📖 What Are Roles?
Ansible Roles are a way of organizing playbooks and sharing reusable content. They allow you to break down your configurations into smaller, reusable components.

In simple terms, roles are self-contained units of automation that can be reused and shared. They help you:

- Organize your playbooks.
- Promote reusability.
- Simplify complex playbooks.

### 🎯 Benefits of Using Roles

**Reusability:** Write once, use everywhere!

**Maintainability:** Easier to manage and update.

**Readability:** Cleaner and more organized code.

**Collaboration:** Share roles with others or use community roles.

Role Directory Structure
Ansible expects roles to have a specific directory structure. Here's what a typical role looks like:

```css
roles/
└── my_role/
    ├── defaults/
    │   └── main.yml
    ├── files/
    ├── handlers/
    │   └── main.yml
    ├── meta/
    │   └── main.yml
    ├── tasks/
    │   └── main.yml
    ├── templates/
    ├── vars/
    │   └── main.yml
    └── README.md
```
### 📂 Directory Breakdown
- **tasks/:** Contains the main list of tasks to be executed.
- **handlers/:** Contains handlers, which are tasks that are triggered by notify.
- **files/:** Contains files that can be deployed to hosts.
- **templates/:** Contains Jinja2 templates that can be deployed.
- **vars/:** Contains variables for the role.
- **defaults/:** Default variables with the lowest priority.
- **meta/:** Defines metadata for the role, including dependencies.
- **README.md:** Documentation about the role.

### Creating Role

Let's create a role step by step! 🚀

**Step 1:** Create the Role Directory

Use the ansible-galaxy command to create the role skeleton.

```yaml
ansible-galaxy init my_first_role
```

This command creates a directory called `my_first_role` with the standard structure.

Now lets try to create a role for **NGINX**

**Step 2:** Define Tasks
Edit the tasks/main.yml file.

```yaml
# roles/my_first_role/tasks/main.yml
- name: Enable and install NGINX 1.12 via amazon-linux-extras
  command:
    cmd: amazon-linux-extras install -y nginx1
- name: Start Nginx
  service:
    name: nginx
    state: started

- name: Deploy index.html using a template
  template:
    src: index.html.j2
    dest: /usr/share/nginx/html/index.html
  notify: Restart Nginx

```
**Step 3:** Define Handlers

Edit the handlers/main.yml file.

```yaml
# roles/my_first_role/handlers/main.yml
- name: Restart Nginx
  service:
    name: nginx
    state: restarted
```

**Step 4:** Set Default Variables

Edit the defaults/main.yml file.

```yaml
# roles/my_first_role/vars/main.yml
nginx_port: 80
title: "Welcome to My Nginx Server"
```

**Step 5:** Create the Template

Place index.html.j2 in the templates/ directory.

```html
<!-- roles/my_first_role/templates/index.html.j2 -->
<!DOCTYPE html>
<html>
<head>
    <title>{{ title }}</title>
</head>
<body>
    <h1>{{ title }}</h1>
    <p>Nginx is running on port {{ nginx_port }}.</p>
</body>
</html>
```

**Step 6:** Use the Role in a Playbook

Create a playbook to use the role.

```yaml
- hosts: all
  become: yes
  roles:
    - my_first_role
```
Now, we've:

- Installed Nginx in tasks/main.yml.
- Started the Nginx service in tasks/main.yml.
- Used templates to deploy index.html.
- Used variables from the vars directory only (vars/main.yml).


But Writing the complex roles will be hard , how to lear all this, and write.

No need to worry! The open-source community has already created many Ansible roles that are freely available. You can easily download these roles from Ansible Galaxy and quickly get started. If needed, just make a few tweaks to fit your specific requirements. This way, you save time and effort by not reinventing the wheel. Simply customize and use them as part of your automation! 😊🚀

#### 🔍 Search for a Role
To search for a role in Ansible Galaxy, use the search command:

```bash
ansible-galaxy search <role_name>
```
Example: Searching for an Nginx role:

```bash
ansible-galaxy search nginx
```
#### Install a Role
To download and install a role from Galaxy:

```bash
ansible-galaxy install <role_name>
```
Example: Installing an Nginx role:
```bash
ansible-galaxy install geerlingguy.nginx
```

#### 🗑️ Remove an Installed Role
To remove a role that you have installed:

```bash
ansible-galaxy remove <role_name>
```
Example: Removing the Nginx role:
```bash
ansible-galaxy remove geerlingguy.nginx
```

#### 📦 List Installed Roles
To see which roles you have installed:

```bash
ansible-galaxy list
```

#### Using Downloaded Roles 🛠️
After installing the role, you can use it in your playbook by specifying the role's name:

```yaml
- hosts: all
  roles:
    - geerlingguy.nginx
```

#### Default Role Installation Directory
Roles are installed in one of two default locations, depending on your system setup:

**System-wide installation:**
Roles are installed in the global system directory:

```bash
/etc/ansible/roles/
```
**Project-specific installation:**

If you're working in a project directory, roles will be installed locally in the roles/ directory within your project:

```
<your_project_directory>/roles/
```

#### How to Install Roles to a Custom Directory
If you want to install roles to a custom directory instead of the default ones, you can specify a path using the -p flag:

```bash
ansible-galaxy install <role_name> -p <custom_path>
```
For example:

```bash
ansible-galaxy install geerlingguy.nginx -p ./my_roles/
```

This will install the geerlingguy.nginx role in the my_roles/ directory within your current folder.
