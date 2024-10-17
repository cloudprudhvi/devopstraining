# Kubernetes Pods

Kubernetes uses YAML files to define objects like Pods, Deployments, Services, and more. Every Kubernetes YAML file has 4 main sections that are required.

## Key Sections of a Kubernetes YAML File

1. **apiVersion**: Defines the API version you're using.
2. **kind**: Specifies the type of object (e.g., Pod, Deployment).
3. **metadata**: Contains information about the object, like its name and labels.
4. **spec**: Specifies details about the object, such as which containers to run in a Pod.

Let’s dive into each section with an example.

### 1. apiVersion
This field defines the API version to use. For a Pod, you typically use `v1`.

```yaml
apiVersion: v1
```

### 2. kind
This specifies what type of object we are creating. Since we are creating a Pod, the kind would be `Pod`.

```yaml
kind: Pod
```

Other examples of `kind` can be Deployment, Service, etc.

### 3. metadata
This section defines the object’s name and labels. For example:
```yaml
metadata:
  name: myapp-pod
  labels:
    app: myapp
```

- `name`: The name of the Pod.
- `labels`: Labels are used to group and identify objects.

Labels are helpful for managing multiple objects. For instance, if you have several Pods, you can label them with tags like `app: frontend` or `app: backend` to differentiate them.

### 4. spec
This is where you define the actual content of the object. For a Pod, the spec section includes details about the containers, such as which image to use. 

```yaml
spec:
  containers:
    - name: myapp-container
      image: nginx
```

For example, if you want to use the `nginx` image, you would specify that here.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: myapp-pod
  labels:
    app: myapp
spec:
  containers:
    - name: myapp-container
      image: nginx
```

#### Creating the Pod
Once you've written your YAML file, you can create the Pod using the following command in the terminal:

```bash
kubectl create -f pod-definition.yml
```

This command tells Kubernetes to create the Pod as described in the YAML file (pod-definition.yml).

## How to See Your Pod After Creation

Once the Pod is created, you can use the `kubectl get pods` command to check the status of the Pods in your Kubernetes cluster. Since we’ve created one Pod, you’ll see something like:
```bash
NAME         READY   STATUS    RESTARTS   AGE
myapp-pod    1/1     Running   0          5m
```

- `NAME`: The name of the Pod (e.g., `myapp-pod`).
- `STATUS`: The status of the Pod (e.g., Running, Pending, etc.).
- `RESTARTS`: How many times the Pod has restarted.
- `AGE`: How long the Pod has been running.

If you want more detailed information about the Pod, such as its labels, container image, or events, you can use the `kubectl describe pod <pod-name>` command.

```bash
kubectl describe pod myapp-pod
```
This will give you detailed information about the Pod, such as:
- Labels assigned to the Pod.
- Which containers are part of the Pod.
- Events related to the Pod, such as when it was created or any issues that occurred.


Here’s an example of what the output might look like:

```bash
Name:         myapp-pod
Namespace:    default
Labels:       app=myapp
Status:       Running
Containers:
  myapp-container:
    Image:    nginx
    State:    Running
    Ready:    True
    Restarts: 0
Events:
  Type    Reason     Age   From               Message
  ----    ------     ----  ----               -------
  Normal  Scheduled  5m    default-scheduler  Successfully assigned myapp-pod to node-1
  Normal  Pulling    5m    kubelet            Pulling image "nginx"
  Normal  Created    4m    kubelet            Created container myapp-container
  Normal  Started    4m    kubelet            Started container myapp-container
```

## Summary of Commands

- To create a Pod, you use the `kubectl create -f <filename>.yml` command.
- To see a list of running Pods, use the `kubectl get pods` command.
- To get detailed information about a specific Pod, use the `kubectl describe pod <pod-name>` command.
