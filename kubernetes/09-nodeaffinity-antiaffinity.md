In the last lecture, we discussed **nodeSelector**, which allows you to place a pod on a specific node by specifying a tag. However, the limitation of nodeSelector is that it doesn't support advanced expressions.

With **nodeAffinity**, you gain more control and flexibility by using multiple labels and operators to match specific nodes. In addition to simply specifying labels like "large" or "medium," you can also define operators like `In`, `NotIn`, `Exists`, etc.

### Understanding Operators in Node Affinity
- **In**: Pod will be scheduled on nodes that have at least one of the specified labels.
- **NotIn**: Pod will not be scheduled on nodes that contain any of the specified labels.
- **Exists**: Pod will be scheduled on nodes where the label exists, regardless of its value.
- **DoesNotExist**: Pod will be scheduled on nodes where the label is absent.

````yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx-pod
spec:
  containers:
  - name: nginx
    image: nginx
  affinity:
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
        - matchExpressions:
          - key: size
            operator: In
            values:
            - large
````

Here’s a table summarizing the types of **Node Affinity** in Kubernetes, covering the four primary configurations:

| **Type**                                      | **Description**                                                                                                        | **Behavior During Scheduling**                                                | **Behavior After Pod is Running**                                          |
|-----------------------------------------------|------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| `requiredDuringSchedulingIgnoredDuringExecution` | Strictly requires the node to match specified labels during scheduling.                                                | Pod will only be scheduled on nodes that meet specified label requirements.  | Label changes on the node do not affect the Pod once it is running.          |
| `preferredDuringSchedulingIgnoredDuringExecution` | Preferentially schedules on nodes that match specified labels but does not strictly require them.                      | Pod prefers nodes with matching labels but can still be scheduled elsewhere if no match. | Label changes on the node do not affect the Pod once it is running.          |
| `requiredDuringSchedulingRequiredDuringExecution`* | Requires the node to match specified labels during both scheduling and execution.                                       | Pod will only be scheduled on nodes with matching labels.                    | If node labels change and no longer match, Pod may be evicted (not currently available in Kubernetes). |
| `preferredDuringSchedulingRequiredDuringExecution`* | Prefers matching labels during scheduling and strictly requires them during execution.                                  | Pod prefers nodes with matching labels for scheduling but may be scheduled on another node if no match. | If node labels change and no longer match, Pod may be evicted (not currently available in Kubernetes). |


# Pod Anti-Affinity in Kubernetes

## Introduction

**Pod Anti-Affinity** in Kubernetes allows you to control the placement of Pods to avoid scheduling them close to each other or on specific nodes. This feature is especially useful for enhancing application resilience and resource distribution by ensuring that similar Pods do not run on the same node or within close proximity.

### When to Use Pod Anti-Affinity

Pod Anti-Affinity is ideal in scenarios where you want to:
1. **Distribute Pods across nodes** to avoid a single point of failure. For example, in a multi-replica setup, this approach can help ensure that a failure on one node doesn't impact multiple Pods of the same type.
2. **Reduce resource contention** by spreading out Pods with similar resource needs to avoid potential bottlenecks or performance degradation.

## Types of Pod Anti-Affinity

Kubernetes provides two types of Pod Anti-Affinity:

1. **requiredDuringSchedulingIgnoredDuringExecution**: A strict rule that only schedules Pods on nodes that meet the anti-affinity requirements. If no nodes match, the Pod will not be scheduled.
   
2. **preferredDuringSchedulingIgnoredDuringExecution**: A preferred rule that tries to schedule Pods according to the anti-affinity rule but can still place them on a different node if necessary.

## Example: Pod Anti-Affinity YAML

In this example, we’ll configure Pod Anti-Affinity for an `nginx` Pod to ensure that it is not scheduled on the same node as other Pods labeled `app: nginx`.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx-pod-antiaffinity
  labels:
    app: nginx
spec:
  affinity:
    podAntiAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        - labelSelector:
            matchExpressions:
            - key: app
              operator: In
              values:
              - nginx
          topologyKey: "kubernetes.io/hostname"
  containers:
  - name: nginx
    image: nginx
```

### Explanation of YAML

- **labelSelector**: The anti-affinity rule specifies that this Pod should avoid nodes where other Pods with the label `app: nginx` are already running.

- **topologyKey**: By setting the `topologyKey` to `kubernetes.io/hostname`, this anti-affinity rule applies at the node level. The Pod will be scheduled on a different node from other `nginx` Pods, if possible.

### How It Works

- **requiredDuringSchedulingIgnoredDuringExecution**: This type ensures that no two Pods with the label `app: nginx` are placed on the same node.

- If there is no available node that meets this condition, the Pod will remain unscheduled until a compatible node becomes available.

This configuration helps achieve greater resilience by distributing Pods across multiple nodes, which reduces the risk of a single node failure affecting multiple instances of your application.

# Pod Affinity in Kubernetes

## Introduction

**Pod Affinity** in Kubernetes allows you to control the placement of Pods to ensure they are scheduled *close to* or *together with* other Pods that have specific characteristics. This feature is useful for applications that require low-latency communication between Pods or that benefit from running on the same node or within close proximity.

### When to Use Pod Affinity

Pod Affinity is ideal in scenarios where you want to:
1. **Place related Pods together**: For example, placing a back-end Pod on the same node as front-end Pods to minimize network latency and improve performance.
2. **Group Pods with similar requirements**: When multiple Pods share resources or need to be close for efficient inter-Pod communication.

## Types of Pod Affinity

Kubernetes provides two types of Pod Affinity:

1. **requiredDuringSchedulingIgnoredDuringExecution**: This is a strict rule. The Pod will only be scheduled on nodes that meet the affinity requirements. If no nodes match, the Pod will not be scheduled.
   
2. **preferredDuringSchedulingIgnoredDuringExecution**: This is a preferred rule rather than a strict requirement. Kubernetes tries to schedule the Pod based on the affinity rule but will still place it on another node if necessary.

## Example: Pod Affinity YAML

In this example, we’ll configure Pod Affinity for an `nginx` Pod to ensure it is scheduled on the same node as other Pods labeled `app: frontend`. This is useful if the `nginx` Pod is acting as a back-end that needs to be close to the front-end Pods to reduce communication latency.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx-pod-affinity
  labels:
    app: backend
spec:
  affinity:
    podAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        - labelSelector:
            matchExpressions:
            - key: app
              operator: In
              values:
              - frontend
          topologyKey: "kubernetes.io/hostname"
  containers:
  - name: nginx
    image: nginx
```

### Explanation of YAML

- **labelSelector**: The affinity rule specifies that this Pod should be scheduled on the same node as other Pods with the label `app: frontend`. This rule is useful when you want related Pods to be located close to each other.

- **topologyKey**: By setting the `topologyKey` to `kubernetes.io/hostname`, this affinity rule applies at the node level. Kubernetes will try to schedule this `nginx` Pod on the same node as other Pods labeled `app: frontend`.

### How It Works

- **requiredDuringSchedulingIgnoredDuringExecution**: This type enforces a strict requirement for the Pod to be scheduled on a node that already has other Pods with the specified label (`app: frontend` in this example).

- If no node meets this condition, the Pod will remain unscheduled until a compatible node becomes available.

This setup is useful when you want to ensure that related Pods are placed together to enhance communication efficiency and reduce latency between components of your application.
