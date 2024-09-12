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

### Step 3: Configure Master server with Slave Configuration

- **Step1**: Click on Manage jenkins from Jenkins homepage.
- **Step2**: Under System Configuration click Nodes
- **Step3**: Now in the node page click on New Node this will ask you to enter Nodename enter the name, select as permanent agent and Create.
- **Step4**: This is configuration Page, we will need to provide some information regarding the node we launched in aws.
              - **RemoteRootDirectory**: here in this block jenkins is asking us to confirm where the new jobs should be executed in SlaveNode, ALl the jobs which will be built, will be in the directory provided. For Eg: we can use **/opt/data/**
              - **Labels**: Add the label name for this node, Remember this label will be required for any job to run on this Node.
              - **UsageMethod**: Select Jobs matching labels 
              - **LaunchMethod**: launch via ssh, Provide th ehostname details,(Ipaddress of the slave server)
                                Since we have no credentails configured click on Add Credentails and in the dropdown, select ssh username with key, Provide the username as root and click on add file manually, here you need to paste teh private key. (Refer: In Step2 while generating ssh) Create Credentails.
              Now again the teh launch method, select the credentails and select Non Verifying Verification Strategy.

Keep the rest of the configuration same and save it.

Headover to Nodes in manage jenkins you should see the Node as connected.


              
   
