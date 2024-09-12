# Jenkins Master-Slave Configuration

When dealing with large-scale Jenkins environments, the traditional single-server setup can become a bottleneck. To address this, Jenkins introduces the Master-Slave architecture. This distributed model allows for efficient management of numerous builds across multiple machines.
## Why Use a Master-Slave Architecture?

### Benefits of the Master-Slave Setup:
- **Scalability**: The master can manage multiple slaves, allowing you to run parallel builds across different environments.
- **Resource Isolation**: Slaves can be provisioned with different configurations, ensuring that builds have dedicated resources without impacting the master’s performance.
- **Cost-Efficiency**: In cloud environments like AWS, you can spin up slaves dynamically based on demand, optimizing your usage and reducing costs.

The Jenkins master handles job management, while the slaves (agents) execute the build jobs. This architecture is particularly useful for complex projects requiring different environments or heavy resource consumption.

---

## Jenkins Master

The Jenkins master is responsible for scheduling jobs, assigning them to appropriate slaves based on the labels defined, and dispatching build tasks to those slaves for execution. It also monitors the status of the slaves (whether they are online or offline), retrieves build results from the slaves, and displays the output in the console.

## Jenkins Slave

The Jenkins slave is responsible for receiving job assignments from the master and executing the build tasks as instructed. It runs the builds in its environment, processes the tasks, and then sends the results back to the master. The slave operates under the master's direction and only performs builds when requested by the master.

## Configuring the Slave on AWS EC2

Follow these steps to configure the Jenkins slave (agent) on an AWS EC2 instance.

### Step 1: Launch an EC2 Instance (Slave Machine)

Make sure both the Master and Slave nodes are in same VPC and subnet. Launch Amazon Linux2 Instance, as the below steps will be suited for Amazon Linux2

### Step 2: Install Java & generate ssh file on the EC2 Instance (Slave)

1. **Connect to the EC2 Instance(Slave)**:
   Use either ssh or session-manager to connect to ec2 instance
   ```bash
   ssh -i "your-key.pem" ec2-user@<ec2-public-ip>

   ##switch to root user
   sudo su
   
   ## Install Java 17
   yum update -y
   sudo yum install java-17-amazon-corretto-devel -y
   
   ##generate a ssh-keypair using ssh-keygen command
   ssh-keygen ##press enter for all user prompts
   cd /root/.ssh/
   ls -la
   
   ###Now you cna see the generated files
   cat id_rsa.pub >> authorized_keys

   ## Copy the id_rsa file to a text file (not id_rsa.pub)
   cat id_rsa
 
   ```

### Step 3: Configure Master Server with Slave Configuration

- **Step1**: Click on **Manage Jenkins** from the Jenkins homepage.
- **Step2**: Under **System Configuration**, click **Nodes**.
- **Step3**: On the Nodes page, click on **New Node**. This will prompt you to enter a node name. Enter the name, select **Permanent Agent**, and click **Create**.
- **Step4**: On the configuration page, you will need to provide information about the node you launched in AWS:
    - **RemoteRootDirectory**: Jenkins asks you to specify where the jobs should be executed on the Slave Node. All jobs built will reside in the provided directory. For example, you can use **/opt/data/**.
    - **Labels**: Add a label name for this node. This label will be needed for any job that runs on this node.
    - **Usage Method**: Select **Jobs matching labels**.
    - **Launch Method**: Choose **Launch via SSH**. Provide the hostname details (IP address of the slave server).
        - Since no credentials are configured, click on **Add Credentials**. In the dropdown, select **SSH Username with Private Key**. Provide the username as **root**.
        - Click on **Add file manually**, then paste the private key (refer to Step 2 for generating the SSH key). Create the credentials.
    - After setting the launch method, select the credentials and choose **Non-Verifying Verification Strategy**.

#### Additional Configuration:
- **RemoteRootDirectory**: Specify where jobs are executed on the Slave Node.
- **Labels**: Define the label for job execution on the node.
- **UsageMethod**: Configure the node to run jobs matching the labels.
- **LaunchMethod**: Choose SSH, provide the hostname, configure credentials, and apply a non-verifying strategy.


              
   
