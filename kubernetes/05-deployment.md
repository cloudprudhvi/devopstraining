# Deploying Applications in a Production Environment

Let’s take a step back from Kubernetes concepts like PODs and ReplicaSets and focus on how you might want to deploy your application in a **production environment**. 

### Key Challenges in Deploying Applications:

1. **Multiple Instances of Web Server:**
   - Imagine you have a web server that needs to be deployed in production.
   - You don’t want just **one instance** of the web server, but **many instances** running simultaneously. This ensures **high availability** and the ability to handle user traffic efficiently.

2. **Seamless Upgrades:**
   - When newer versions of your application (or web server) become available on the Docker registry, you want to **upgrade your Docker instances** without causing disruptions.
   - You need to upgrade instances **seamlessly** without downtime for users.

3. **Rolling Updates:**
   - You don’t want to upgrade **all instances at once**, because doing so might affect users currently accessing your application.
   - Instead, you want to upgrade them **one by one**. This process is called a **Rolling Update**. It allows you to gradually replace old versions with new ones without downtime.

4. **Rollback to Previous Versions:**
   - What if the upgrade introduces a problem or unexpected error?
   - In that case, you should have the ability to **rollback** to the previous version of your application. This ensures that the application remains stable even if a deployment fails.

5. **Pausing and Resuming Deployments:**
   - Suppose you want to make **multiple changes** to your production environment—such as:
     - Upgrading the web server version,
     - Scaling the number of instances,
     - Modifying resource allocations.
   - You don’t want to apply each change immediately after running a command.
   - Instead, you might want to **pause the environment**, make all the changes, and then **resume** the environment, so that all changes are applied together. This ensures smooth and controlled rollouts.

### How Kubernetes Deployments Help

All of these capabilities are provided by **Kubernetes Deployments**:

- **PODs**: We’ve already discussed how **PODs** encapsulate single instances of your application (like a web server) in containers.
- **ReplicaSets**: We also discussed how **ReplicaSets** deploy and manage multiple instances of PODs to ensure availability.
  
  Now, we introduce **Deployments**, which sit **higher in the hierarchy** of Kubernetes objects. Deployments provide a powerful set of features that manage the entire lifecycle of applications.

### Capabilities of Kubernetes Deployments:

- **Rolling Updates**: Perform smooth, seamless updates of application instances by gradually replacing old Pods with new ones.
- **Rollback**: Easily revert to a previous version of your application if a deployment fails or introduces bugs.
- **Pause and Resume**: Make multiple changes to your environment, pause the deployment to prepare changes, and then resume it to apply all changes at once.
- **Scaling and Resource Management**: Scale your application up or down and manage the resources allocated to your Pods, all within the same deployment framework.

# How to Create a Kubernetes Deployment

Creating a deployment in Kubernetes follows a familiar process if you’ve already worked with other components like **ReplicaSets** or **PODs**. The deployment allows us to manage our application with features like **Rolling Updates**, **Rollbacks**, and **Pause/Resume** functionality.

### Step-by-Step: Creating a Deployment

1. **Create a Deployment Definition File**:
   - Like other Kubernetes objects, we begin by creating a definition file (e.g., `deployment-definition.yml`).
   - The structure of the **deployment definition file** is very similar to the **ReplicaSet definition file**, but with one key difference:
     - The `kind` field is now set to `Deployment`.
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  labels:
    app: nginx-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx-app
  template:
    metadata:
      labels:
        app: nginx-app
    spec:
      containers:
      - name: nginx-container
        image: nginx
```

2. **Walkthrough of Deployment Definition File**:
   The deployment definition file includes the following sections:
   - **apiVersion**: Specifies the API version for the Deployment object, which is `apps/v1`.
   - **kind**: In this case, it will be `Deployment`.
   - **metadata**: Contains the **name** and **labels** for the deployment.
   - **spec**: Defines the specification of the deployment. It includes:
     - **replicas**: The number of replicas (or instances) you want to run.
     - **selector**: Defines the labels used to identify the Pods managed by the deployment.
     - **template**: Inside the template section, there’s a full **POD definition**, similar to the structure you would use when creating Pods manually.

3. **Running the Deployment**:
   - Once your **deployment-definition.yml** file is ready, you can create the deployment by running the following command:
     ```
     kubectl create -f deployment-definition.yml
     ```
   - This command instructs Kubernetes to create the deployment based on the definition you provided.

4. **Verify the Deployment**:
   - To verify that the deployment was created successfully, run the following command:
     ```
     kubectl get deployments
     ```
   - This will show the newly created deployment and its current state.

5. **Automatic ReplicaSet Creation**:
   - When you create a deployment, it automatically creates a **ReplicaSet** to manage the Pods. To see the new ReplicaSet created by the deployment, run:
     ```
     kubectl get replicaset
     ```
   - This ReplicaSet is created with the same name as the deployment and is responsible for ensuring the correct number of Pods are running.

6. **View the Pods**:
   - The ReplicaSet will, in turn, create the Pods. To view the Pods that have been created as part of the deployment, run the following command:
     ```
     kubectl get pods
     ```
   - You will see the Pods created with the name of the deployment and the ReplicaSet.

### Key Differences Between ReplicaSet and Deployment:

So far, you may have noticed that the process of creating a **Deployment** and a **ReplicaSet** is quite similar. The primary difference is that **Deployments** introduce a higher-level Kubernetes object that allows for more advanced features, such as:

- **Rolling Updates**: Gradual updates to new versions without downtime.
- **Rollbacks**: The ability to revert back to a previous version if an issue occurs during an update.
- **Pause and Resume**: The ability to pause and make multiple changes to a deployment and then resume, applying all the changes at once.

These features make **Deployments** the preferred method for managing long-running applications in production environments. We’ll explore these advanced features in upcoming sections.

### Understanding Rollouts and Versioning in a Kubernetes Deployment

Before we look at how to upgrade an application in Kubernetes, let's first understand the concepts of **Rollouts** and **Versioning** in a deployment.

### Rollouts in Kubernetes

Whenever you create a new deployment or upgrade the images in an existing deployment, it triggers a **Rollout**. A rollout is the process of **gradually deploying** or **upgrading** your application containers.

### Deployment Revisions

- When you first create a deployment, it triggers a rollout and a new deployment **revision** is created (let’s call this **Revision 1**).
- In the future, when the application is upgraded (e.g., when the container image is updated), a **new rollout** is triggered and a new **Revision** (Revision 2) is created.

This system allows Kubernetes to **track changes** made to your deployment and enables you to **rollback** to a previous version if needed.

### Checking Rollout Status

- To see the status of your rollout, use the following command:
  ```bash
  kubectl rollout history <deployment-name>
  ```

## Deployment Strategies

There are two main deployment strategies in Kubernetes:

### 1. **Recreate Strategy**

- Imagine you have **5 replicas** of your web application running.
- In this strategy, all **5 running instances** are destroyed, and then **5 new instances** of the upgraded application are created.
- **Issue**: During the transition, the application is down and **inaccessible** to users because all old instances are destroyed before new ones are created.

### 2. **Rolling Update Strategy**

- In this strategy, Kubernetes **does not destroy** all Pods at once.
- Instead, it **takes down** the old version **one by one**, and **brings up** the new version **one by one**.
- This ensures that the application **never goes down** and the upgrade is **seamless** for users.

> **Note**: If you do not specify a strategy while creating the deployment, Kubernetes will use **Rolling Update** by default.

## Upgrading a Deployment

When upgrading a deployment, you can make various changes such as:
- Updating the **application version** (by changing the Docker container image version).
- Modifying **labels**.
- Updating the **number of replicas**.

### How to Update a Deployment:

1. **Modify the Deployment Definition File**:
 - Edit your deployment definition file to make the necessary changes (e.g., update the container image version).
 - Run the following command to apply the changes:
   ```
   kubectl apply -f <deployment-file>
   ```
 - This triggers a **new rollout** and a **new revision** of the deployment is created.

2. **Using `kubectl set image` Command**:
 - Another way to update the image is by using the `kubectl set image` command.
   ```
   kubectl set image deployment/<deployment-name> <container-name>=<new-image>
   ```
 - **Warning**: If you update the image this way, the configuration of the **deployment-definition file** will be different from what’s currently running, so you need to be careful when making future changes using the same definition file.

## Comparing Deployment Strategies

You can observe the difference between the **Recreate** and **Rolling Update** strategies by running the `kubectl describe deployment` command.

- With the **Recreate strategy**, the **old ReplicaSet** is scaled down to 0 before the **new ReplicaSet** is scaled up.
- With the **Rolling Update strategy**, the **old ReplicaSet** is scaled down one Pod at a time, while the **new ReplicaSet** is scaled up one Pod at a time.

## How Kubernetes Handles Upgrades

When you create a new deployment (e.g., deploying 5 replicas), Kubernetes automatically creates a **ReplicaSet** under the hood, which in turn creates the Pods needed to meet the replica count.

When you **upgrade** the application (e.g., by updating the image), Kubernetes creates a **new ReplicaSet**. It starts deploying new Pods to the new ReplicaSet while **simultaneously taking down** Pods from the old ReplicaSet following the **Rolling Update strategy**.

### Viewing ReplicaSets During Upgrade

You can list all ReplicaSets with:
```bash
kubectl get replicasets
```

You will see:
- The **old ReplicaSet** with **0 Pods**.
- The **new ReplicaSet** with **5 Pods** (or the desired number of replicas).

## Rolling Back to Previous Revisions

If something goes wrong after an upgrade (e.g., a new version has a bug), Kubernetes allows you to **rollback** to a previous revision.

### Rollback Command

To rollback to the previous version, use the following command:
```
kubectl rollout undo <deployment-name>
```

This will:
- Destroy the Pods in the **new ReplicaSet**.
- Bring up the older Pods from the **old ReplicaSet**, restoring the application to its previous state.

### Viewing ReplicaSets Before and After Rollback

Before rollback:
- The **old ReplicaSet** has **0 Pods**.
- The **new ReplicaSet** has the desired number of Pods (e.g., 5 Pods).

After rollback:
- The **new ReplicaSet** will be scaled down to 0.
- The **old ReplicaSet** will scale back up to the desired number of Pods.

## Creating a Deployment with `kubectl run`

When we first learned about Pods, we used the `kubectl run` command to create a Pod. However, the `kubectl run` command actually creates a **Deployment** behind the scenes, not just a Pod.

This command automatically creates:
- A **Deployment**.
- A **ReplicaSet**.
- The required **Pods**.

> Using a **definition file** to create deployments is generally recommended because it allows you to save, version, and modify the configuration as needed in the future.
