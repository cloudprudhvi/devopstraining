## Overview
Namespaces are intended to support multiple users or teams working within a single Kubernetes cluster. They help create a kind of virtual cluster on top of an existing physical cluster. This capability is crucial in environments where you have to manage resources for multiple projects, applications, or stages of development, each with their own access controls and configuration settings.

## Key Functions of Namespaces
- **Resource Organization**: They provide a logical partitioning capability within a Kubernetes cluster that allows you to group and isolate resources such as pods, services, and deployments.
- **Resource Management**: Namespaces enable fine-grained resource quota management. Administrators can limit the amount of memory, CPU, and storage that each namespace can use, preventing any single project or team from monopolizing cluster resources.
- **Access Control**: By using namespaces, you can implement policies that dictate who can access certain resources. Kubernetes Role-Based Access Control (RBAC) can be scoped to specific namespaces, allowing for detailed permissions management.
- **Simplifying Resource Names**: Namespaces allow you to reuse names for resources. For example, you might have a pod named `test` in multiple namespaces, which is useful for keeping resource naming consistent across different environments like development, testing, and production.

## Common Namespaces in Kubernetes
- **default**: This is the namespace for objects with no other namespace. It’s the out-of-the-box namespace for Kubernetes resources that do not specify a namespace.
- **kube-system**: This namespace contains the objects created by the Kubernetes system, primarily system-level objects critical for the functioning of the Kubernetes cluster itself.
- **kube-public**: This is a namespace that is automatically created and is readable by all users (including those not authenticated). This namespace is primarily reserved for cluster usage, as it is often used for public resources.

## Best Practices for Using Namespaces
- **Environment Isolation**: Use namespaces to separate different environments such as development, testing, and production. This helps prevent accidental changes or deletions in the production environment.
- **Resource Limits**: Apply resource quotas to namespaces to manage the resources used by each project or team effectively.
- **Security**: Implement RBAC to control what users can see and do within each namespace, increasing the security of your cluster resources.
- **Labels and Annotations**: Use labels and annotations to organize and categorize resources within namespaces further.

## When to Use Multiple Namespaces
- **Multiple Projects**: When a cluster is shared across different projects or teams that require separate environments.
- **Access Control**: To implement specific security policies and restrictions.
- **Resource Monitoring and Quotas**: To manage and monitor resource usage efficiently across different departments or projects.

Namespaces are a fundamental part of Kubernetes that help you manage resources efficiently, ensuring that your cluster can serve multiple users and applications without conflict. They are crucial for large-scale deployments where teams and services are numerous and need isolated management and control mechanisms.

## Resource Requests and Limits in Kubernetes

### Overview
In Kubernetes, resource requests and limits help manage how resources like CPU and memory are allocated to pods. This ensures that a pod gets the minimum amount of resources it needs to run (requests) and sets a maximum limit to prevent it from using too many resources (limits).

### What are Resource Requests?
- **Requests**: The minimum amount of CPU or memory that a pod is guaranteed. The scheduler uses this value to decide on which node to place the pod.

### What are Resource Limits?
- **Limits**: The maximum amount of CPU or memory that a pod is allowed to use. If a pod tries to use more resources than its limit, it could face consequences.

## What Happens When a Pod Exceeds Its Resource Limits?
- **Out of Memory (OOM) Killed**: If a container uses more memory than its defined limit, it may be terminated by the system. This is called an Out of Memory (OOM) kill. The pod will be restarted based on its restart policy.
- **Eviction**: If a node runs out of memory, Kubernetes may evict less critical pods to free up resources for higher-priority pods. Eviction typically happens when the overall memory on the node is under pressure.

### Example of Setting Resource Requests and Limits
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: example-pod
spec:
  containers:
  - name: app-container
    image: nginx
    resources:
      requests:
        memory: "256Mi"
        cpu: "500m"
      limits:
        memory: "512Mi"
        cpu: "1"
```

## Best Practices for Resource Management
- **Set Appropriate Requests and Limits**: Ensure that each container has appropriate resource requests and limits set to avoid overloading nodes and causing unexpected OOM kills.
- **Monitor Resource Usage**: Regularly monitor the resource usage of pods to adjust the requests and limits as needed.
- **Use Resource Quotas**: Apply resource quotas at the namespace level to limit the total amount of resources that can be consumed, preventing one namespace from consuming all cluster resources.
