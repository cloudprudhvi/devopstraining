![It's not working on my machine](../images/docker/worksonmymachine.jfif)

### Why Docker
Imagine you've developed an application that works flawlessly on your machine. When you share it with a colleague, they run into issues because their environment is different—different libraries, dependencies, or configurations. What if you could package your entire application, along with all its dependencies and settings, into a single unit that your colleague can run on their system without any compatibility problems? That's essentially what Docker allows you to do.


## Virtual Machine Vs Containers

![Vm vs Container](../images/docker/vmvscontainer.png)

### What is Hypervisor
A hypervisor, also known as a virtual machine monitor or VMM, is software that creates and runs virtual machines (VMs). A hypervisor allows one host computer to support multiple guest VMs by virtually sharing its resources, such as memory and processing.




| Aspect              | Virtual Machines (VMs)                                   | Containers                                       |
|---------------------|----------------------------------------------------------|--------------------------------------------------|
| **Architecture**    | Includes the entire guest operating system               | Shares the host operating system's kernel        |
| **Resource Usage**  | Heavyweight; requires more memory and storage            | Lightweight; uses less memory and storage        |
| **Isolation**       | Full isolation with separate OS instances                | Isolated processes within the same OS            |
| **Performance**     | Slower startup and performance due to full OS            | Faster startup and performance                   |
| **Size**            | Larger size (usually in gigabytes)                       | Smaller size (often in megabytes)                |
| **Boot Time**       | Takes minutes to start                                   | Starts in seconds                                |
| **Portability**     | Less portable; depends on hypervisor and hardware        | Highly portable across different environments    |
| **Use Cases**       | Running multiple operating systems on one machine        | Deploying microservices and scalable apps        |
| **Management**      | More complex to set up and maintain                      | Easier to manage with tools like Docker          |
| **Security**        | Strong isolation provides better security                | Shares kernel; requires careful security measures |

## Architecture of Docker

![Architecture](../images/docker/Architecture-of-Docker.png)


## Docker Installation on Amazon Linux 2

  - ```bash
     sudo su
     yum update -y
     yum install docker -y
     systemctl enable docker
     systemctl status docker
     ```

Now you have all the docker components installed on your machine. you are ready to go!!

## Let's Run an Nginx Container

So, you might be thinking, "Let's run an Nginx container." But how do we actually do that?

## How Do I Run It?

To run an Nginx container, we use the `docker run` command. Open your terminal and type:

```bash
docker run nginx
```

## **What Happened in the background?**

Docker Pulled something called as Image.

### What Is a Docker Image?

A Docker image is a lightweight, stand-alone package that includes everything needed to run a piece of software:

- **Code**: The application code you want to run.
- **Runtime**: The necessary runtime or interpreter (e.g., Node.js, Python).
- **Libraries**: All required system libraries and dependencies.
- **Environment Variables**: Configuration settings.
- **Files**: Any additional files or assets.

### Where Is It Picked From?

When you run `docker run nginx`, Docker looks for the `nginx` image locally on your machine:

- **Local Check**: Docker first checks if the image exists in your local image repository.
- **Docker Hub**: If not found locally, Docker pulls the image from [Docker Hub](https://hub.docker.com/), a public registry with millions of images.

### That is Great!! I am finally running my Nginx Container

But I am seeing something like this on my terminal
```
2024/09/17 16:02:34 [notice] 1#1: using the "epoll" event method
2024/09/17 16:02:34 [notice] 1#1: nginx/1.27.1
2024/09/17 16:02:34 [notice] 1#1: built by gcc 12.2.0 (Debian 12.2.0-14) 
2024/09/17 16:02:34 [notice] 1#1: OS: Linux 5.10.224-212.876.amzn2.x86_64
2024/09/17 16:02:34 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 32768:65536
2024/09/17 16:02:34 [notice] 1#1: start worker processes
2024/09/17 16:02:34 [notice] 1#1: start worker process 29
```
Seems like it is running the foreground, I think it should be running in the background, Because i have other work to be done on my terminal.

### Detached Mode in Docker

When running containers, you can choose to run them in the foreground or in the background. Running a container in **detached mode** means it runs in the background of your terminal.

- **Detached Mode (`-d`)**:
  - Using the `-d` flag with `docker run` starts the container in detached mode.
  - The container runs in the background, and you get back to your command prompt.
  - This is useful for running applications that need to stay up without tying up your terminal.

**Example:**

```bash
docker run -d nginx
```
## Great! I Am Able to Run Nginx

Great! I have successfully run the Nginx container. I can't wait to access it. But how do I access it?

### How Do I Access It?

Since my Docker is running on an **EC2 instance**, I can use the IP address of my EC2 instance to access Nginx. I'll use port **80** as well, so I should be able to access the Nginx server directly.

## Oops! 😅 I'm Not Able to Access Nginx Using Port 80 and EC2 Public IP

Oops! 😅 I am not able to access Nginx by using port **80** and my EC2 public IP address. Is there any issue? Let me check if the container is running or not.

### But How Do I Check?

Is there any command to check if my Docker container is running? Yes! We can use the `docker ps` command.

### Explaining `docker ps`

The `docker ps` command is used to list all the running Docker containers on your system.

- **Basic Command:**

  ```bash
  docker ps
  ```
### Hmm.. COntainer is running absloutely fine, what could be the Issue? Am I missing Something? 🤔

YES, 

## Understanding Port Mapping in Docker 🛳️🔌

When running Docker containers, you might want to make the services inside the container accessible to the outside world or your host machine. This is where **port mapping** comes into play.

### What Is Port Mapping? 🌐➡️🌐

Port mapping allows you to forward a port from your host machine (or EC2 instance) to a port inside the Docker container. This way, you can access services running inside the container via the host's IP address and specified port.

### How Does Port Mapping Work?

- **Containers Have Their Own Network Stack:**
  - Each Docker container runs in its own isolated environment with its own network stack.
  - By default, services inside the container are not accessible from the host machine.

- **Exposing Ports:**
  - To make a service accessible, you need to expose the container's port to the host.
  - This is done using the `-p` or `--publish` flag with `docker run`.

### Syntax of Port Mapping

```bash
docker run -p [host_port]:[container_port] [image_name]
```

## Great! 🎉 Now I Am Able to See My Container from the Browser

## Stopping the Container 🛑

I'm done with my work, so let me stop the container. Do I have some commands for that?

### How Do I Stop the Container?

Let's try the `docker stop` command.

But how do I get the running container list? Oh, I have `docker ps`.

```bash
docker ps
```

This command lists all the running containers.

Now, let's stop the container:

```bash
docker stop <container_id>
```

Replace `<container_id>` with the actual ID of your container from the `docker ps` output.

Cool! 😎 Everything is down.

### Checking All Containers 🔍

Wait, can you check `docker ps -a`?

```bash
docker ps -a
```

Oh... I see my container is still there. But I stopped it. How do I remove it?

### Removing the Container 🗑️
We can use the docker rm command to remove the container:

```bash
docker rm <container_id>
Again, replace <container_id> with the actual ID of your container.
```

### **What Is the Difference Between stop vs rm? 🤔**
- **docker stop**: Stops a running container. The container still exists on your system but is not running.
- **docker rm**: Removes a container from your system entirely. This deletes the container whether it's running or stopped.


## Docker Workflow

![Workflow](../images/docker/dockerflow.webp)
