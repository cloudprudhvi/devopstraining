# Creating a Docker Image for Your Application 🐳

All the code that I have, I need to copy to my Docker container and run my app. **Is there any way?**

Yes! We can create our own Docker image.

## Understanding How We Usually Run an App

Before creating an image, let's understand how we usually run our app:

1. **You will need some OS.**
2. **You need software like Python, Node.js, Java, etc.**
3. **You need related dependencies.**
4. **You need your code.**
5. **Build the code.**
6. **Start the app.**

These are the steps we usually follow.

## Translating Steps into Docker

Now, I want all these steps to be executed and run using Docker. For that, I need to write a **Dockerfile**.

Let's try one by one.

### Dockerfile Instructions

For taking step by step in a Dockerfile, we have something called **instructions**. We will be using these instructions to build the Docker image.

### Step 1: Specify the Base OS

**How can I take my OS?**

We have the `FROM` instruction.

I need Debian OS, so I'll specify:

```dockerfile
FROM debian:latest
```
### Step 2: Install Required Software

Now, I need Python to be installed.

**How do I install Python?**

I can use the `RUN` instruction and provide the Linux commands.
```
# Install Python
RUN apt-get update && apt-get install -y python3 python3-pip
```

- `apt-get update`: Updates the package lists.
- `apt-get install -y python3 python3-pip`: Installs Python 3 and pip without prompting for confirmation (`-y`).

### Step 3: Install Dependencies

Assuming my application has a `requirements.txt` file for Python dependencies, I will copy it into the image and install the dependencies.
For copying we will use **`copy`** instruction, and for WORKING DIR we use **`WORKDIR`** Instruction.

```
# Copy requirements.txt
COPY requirements.txt /app/requirements.txt

# Set the working directory
WORKDIR /app

# Install Python dependencies
RUN pip3 install -r requirements.txt
```

### Step 4: Add Your Code

Next, I need to copy my application code into the image.
```
# Copy application code
COPY . /app
```
This copies all files from your current directory into the `/app` directory in the image.

### Step 5: Build the Code

If your application needs to be built or compiled, include the necessary commands. For Python applications, this step may not be necessary unless you have specific build steps.

### Step 6: Start the Application

Use the `CMD` or `ENTRYPOINT` instruction to specify the command that runs when the container starts.
```
# Start the application
CMD ["python3", "app.py"]
```

Replace `app.py` with the entry point of your application.

### Complete Example of the Dockerfile

Putting it all together, your Dockerfile might look like this:

```dockerfile
# Use Debian as the base image
FROM debian:latest

# Set environment variables to ensure no prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Install Python
RUN apt-get update && apt-get install -y python3

# Set the working directory
WORKDIR /app

# Copy application code
COPY . /app

# Expose the port your application runs on (optional)
EXPOSE 8080

# Start the application
CMD ["python3", "app.py"]
```

Here if you Observe we are using **`EXPOSE`** instruction also, it helps to expose you app on specific port.

## Building the Docker Image

To build the Docker image using the Dockerfile, run the following command in your terminal:
```
docker build -t my-app-image .
```

- `-t my-app-image`: Tags the image with the name `my-app-image`.
- `.`: Tells Docker to look for the Dockerfile in the current directory.

## Running the Docker Container

Once the image is built, you can run a container from it:
```
docker run -d -p 80:80 --name my-app-container my-app-image
```

- `-d`: Runs the container in detached mode (in the background).
- `-p 80:80`: Maps port **8000** in the container to port **8000** on your host machine.
- `--name my-app-container`: Names the container `my-app-container`.
- `my-app-image`: The name of the image to create the container from.
