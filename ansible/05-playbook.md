### The Challenge
By default, Ansible executes tasks sequentially. Even if tasks are independent, they wait for the previous one to finish. This can be inefficient when dealing with long-running operations.

#### Scenario:

- You have multiple servers to configure.

- Each server setup is independent.

- Running tasks one after another is slow.

**`😩 Problem:`** Playbook execution is taking too much time!

**Solution:** Async to there to help you
Ansible's async feature allows you to run tasks asynchronously. This means Ansible will start a task and immediately move on to the next one without waiting for the previous one to finish. 🎉

**Benefits**
- Efficiency: Reduce total execution time.
- Scalability: Manage more hosts and tasks concurrently.
- Flexibility: Control over task execution and polling.

#### Implementing Async Tasks

Let's see how to implement async tasks in your playbook.

```yaml
- name: Run a long task asynchronously
  shell: sleep 300
  async: 600   # Time in seconds
  poll: 0      # Don't wait for task completion
```
- `async:` Maximum time allowed for the task to complete.
- `poll`: If set to 0, Ansible won't wait for the task to finish.

```yaml
- hosts: all
  tasks:
    - name: Performing maintenance tasks asynchronously
      shell: "sleep 30 && echo 'Maintenance Completed!'"
      async: 60
      poll: 0
      register: maintenance_job

    - name: Checking maintenance status
      async_status:
        jid: "{{ maintenance_job.ansible_job_id }}"
      register: maintenance_result
      until: maintenance_result.finished
      retries: 10
      delay: 6
```


### 🔄 How Async and Poll Work Together
`Async (async):` Specifies the maximum time (in seconds) that Ansible will allow a task to run. It's like saying, "I'll wait up to X minutes for a task to be completed, if not completed it will be failed."

`Poll (poll):` Determines how often Ansible checks if the task is completed. If you set poll: 0, it's like saying, "Don't call me; I'll check back later."

#### Checking Task Status Made Easy
When you run tasks asynchronously, Ansible doesn't wait around for them to finish. But you'll eventually want to know if they're done, right? Here's how you can check:


`Start the Async Task:` Begin the task and tell Ansible to run it in the background.

```yaml
- name: Start background task
  shell: "sleep 30 && echo 'Done!'"
  async: 60
  poll: 0
  register: task_info
```  
- `register:` task_info saves the task details, including a unique job ID.

Check the Task Status: Use the async_status module to ask Ansible, "Is my task done yet?"

```yaml
- name: Check if task is finished
  async_status:
    jid: "{{ task_info.ansible_job_id }}"
  register: task_result
  until: task_result.finished
  retries: 5
  delay: 5
```
- `jid:` The job ID of the task we're checking.
-  `until:` Keep checking until the task is finished.
- `retries and delay:` Check every delay seconds, up to retries times.

## 🛠️ Ansible Execution Strategies
Ansible strategies determine how tasks are executed across multiple hosts in your inventory. By default, Ansible uses the linear strategy, but there are other strategies you can leverage to optimize your playbook execution.

#### What are Ansible Strategies?
Ansible strategies control the order and manner in which tasks are executed on your target hosts. They can help optimize performance, manage dependencies, and handle failures gracefully.

#### Main Strategies:

- Linear (Default) Strategy
- Free Strategy
- Serial Strategy

**Default (Linear) Strategy**

🔄 How It Works

`Sequential Execution:` Ansible runs each task one at a time across all hosts before moving to the next task.
`Host Synchronization:` All hosts execute the same task simultaneously.

`Error Handling:` If a task fails on any host, Ansible can stop the playbook execution based on your failure settings.

**📝 Example**

Imagine you're deploying an application to multiple servers:

- Task 1: Install dependencies.
- Task 2: Configure application.
- Task 3: Start services.
Linear Strategy Execution:

All servers perform Task 1 together.
Once Task 1 is complete on all servers, they move to Task 2, and so on.

**🎯 When to Use**

Consistency is crucial: Ensures all hosts are at the same step.
Tasks depend on previous tasks: Sequential execution maintains order.

#### Free Strategy

**`🏃‍♂️ How It Works`**

`Asynchronous Execution:` Hosts run tasks independently of each other.

`No Host Synchronization:` Each host moves to the next task as soon as it's done with the current one.

`Faster Execution:` Can significantly reduce total playbook runtime.

#### 📝 Example
Using the same deployment scenario:

Server A might finish Task 1 quickly and move to Task 2.

Server B takes longer on Task 1 but doesn't hold up Server A.

**🎯 When to Use**

Tasks are independent: No inter-host dependencies.
Speed is important: Ideal for large inventories where hosts can proceed at their own pace.

```yaml
- hosts: all
  strategy: free
  tasks:
    - name: Task 1
      
```

#### What is serial?

**`🔢 Controlling Batch Size of Hosts`**

serial allows you to control how many hosts Ansible configures at a time during a play.

It breaks down the list of hosts into batches, running the play on one batch at a time.

**🎯 Benefits**

`Manage Load:` Prevents overwhelming your network or services.

`Controlled Rollouts:` Useful for rolling updates or deployments.

`Error Isolation:` If a batch fails, you can stop before affecting all hosts.

```yaml
- hosts: webservers
  serial: 2
  tasks:
    - name: Deploy application
      shell: "deploy_app.sh"
```
- Execution Flow:
  - Ansible runs the play on 2 hosts at a time.
  - Once the first batch completes, it moves to the next 2 hosts.


```yaml
- hosts: webservers
  serial:
    - 1
    - 2
    - 5
  tasks:
    - name: Deploy application
      shell: "deploy_app.sh"
```

- Execution Flow:
  -  First Batch: 1 host.
  - Second Batch: 2 hosts.
  - Remaining Batches: 5 hosts at a time.
