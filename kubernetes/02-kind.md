## Kind Cluster Setup on EC2 Amazon Linux
#### 📋 Prerequisites
Before setting up Kind, let's get started by creating an Amazon EC2 instance. Follow these steps

#### Launch an EC2 Instance

Use Amazon Linux 2 as the OS.
Choose a t2.medium instance or higher, as Kind requires sufficient resources.
Ensure you have security group rules that allow inbound SSH traffic and outbound internet access.
Access your EC2 instance
SSH into your EC2 instance using your terminal.

#### 🚀 Installing Docker
Kind requires Docker to run. Follow these steps to install Docker on your Amazon Linux instance

```bash
sudo su
sudo yum update -y
sudo amazon-linux-extras install docker
sudo service docker start
```

To verify Docker is running

```bash
docker --version
```

#### 📥 Installing Kind
Now that Docker is ready, let's install Kind. Kind is a tool for running local Kubernetes clusters using Docker.

#### Download the Kind binary

```bash
curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.24.0/kind-linux-amd64
```

#### Make the binary executable

```bash
chmod +x ./kind
```
##### Move the binary to /usr/bin so it’s globally accessible:

```bash
sudo mv ./kind /usr/bin/kind
```

#### Verify the installation:

```bash
kind --version
```

You can also check the official Kind documentation for additional installation methods.

https://kind.sigs.k8s.io/docs/user/quick-start/#installation

#### 🏗️ Creating a Kind Cluster
Now that Kind is installed, let's create a Kubernetes cluster with one master and two worker nodes.

#### Create a file kind-config.yaml

```yaml
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
nodes:
- role: control-plane
- role: worker
- role: worker
```

#### Create the cluster using the configuration file

```bash
kind create cluster --config kind-config.yaml
```

This will create a 3-node cluster 1 control-plane (master) and 2 workers.

Alternatively, if you want a simple cluster without a custom config file:

```bash
kind create cluster --name my-cluster
kind get clusters ##to get the cluster information
```

### 🔄 Installing Kubectl
Kubectl is a command-line tool that interacts with Kubernetes clusters.

Download the Kubectl binary:

```bash
sudo curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
```

#### Make the binary executable

```bash
sudo chmod +x kubectl
```

#### Move the binary to a directory that is in the system's PATH

```bash
sudo mv kubectl /usr/bin/
```

#### Verify the Kubectl installation

```bash
kubectl version --client
```

You can also check the official AWS Kubectl installation guide for more details.

https://docs.aws.amazon.com/eks/latest/userguide/install-kubectl.html


#### 📦 Creating and Managing Pods
With your cluster up and running, you can now deploy pods.

#### Create a pod with the nginx image

```bash
kubectl run nginx-pod --image=nginx
```

Check the status of your pods:

```bash
kubectl get pods
```

You should see your nginx pod running! 🎉

🔧 Useful Tips
Use kubectl describe pod <pod-name> to get detailed information about a specific pod.

Use kubectl delete pod <pod-name> to delete a pod when you no longer need it.
🎯 Now you're all set to run your Kubernetes cluster with Kind!
