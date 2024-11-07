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
