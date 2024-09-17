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

## Let's run a Nginx Container
We'll learn how to run an Nginx container using Docker. We'll cover what a Docker image is, where it's picked from, and what Docker does to run the container.

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


## Docker Workflow

![Workflow](../images/docker/dockerflow.webp)
