# Kubernetes Volumes README

## Overview
Kubernetes pods are ephemeral, meaning that when a pod is deleted, any data stored within that pod is lost. To persist data beyond the lifecycle of a pod, Kubernetes allows volumes to be attached to pods.

## Simple Volume Configuration Example
Below is an example of how to configure a volume using a host path on the node.

### `pod-with-volume.yaml`
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: simple-volume-pod
spec:
  containers:
  - name: app-container
    image: nginx
    volumeMounts:
    - mountPath: "/opt"
      name: data-volume
  volumes:
  - name: data-volume
    hostPath:
      path: "/data"
      type: DirectoryOrCreate
```

## Explanation
- **`hostPath`**: The `hostPath` volume type mounts a directory from the host node’s filesystem into the pod. The path `/data` on the host node is mounted to `/opt` inside the container.
- **`DirectoryOrCreate`**: Ensures that the `/data` directory is created on the host if it does not already exist.

### Important Note
The `hostPath` volume type is suitable for single-node clusters but should be used with caution in multi-node clusters due to potential data inconsistency across nodes.

## Persistent Volumes in Kubernetes

### Introduction
Persistent Volumes (PVs) and Persistent Volume Claims (PVCs) are used in Kubernetes for managing storage. Administrators create PVs, and users create PVCs to request storage.

### How PVCs Work
When a PVC is created, Kubernetes binds it to an available PV that matches the request. Each PVC is linked to a single PV. Kubernetes ensures the chosen PV meets the requirements of the PVC, such as size and access modes.

### Binding and Matching
If there are multiple PVs that match the PVC, labels and selectors can be used to choose the specific PV to bind. A smaller PVC can be matched with a larger PV if there is no exact match available. The binding is one-to-one, so no other PVC can use the remaining space in that PV.

### `persistent-volume.yaml`
```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: pv-vol1
spec:
  capacity:
    storage: 1Gi
  accessModes:
    - ReadWriteOnce
  persistentVolumeReclaimPolicy: Retain
  hostPath:
    path: "/data/pv"
```

If no suitable PV is found, the PVC will remain in a pending state until a matching PV is created or becomes available.

### Creating a PVC
To create a PVC:
- Use a template and set the API version to `v1` and `kind` to `PersistentVolumeClaim`.
- Specify the storage size and access modes (e.g., `ReadWriteOnce`).
- Create the PVC using:
```bash
kubectl create -f [pvc-file]
```
Kubernetes will then search for an available PV that meets the PVC's requirements.

### Example Scenario
If a PVC requests 500 MB of storage but only a 1 GB PV is available, the PVC will bind to that PV if it meets the other requirements.

### `persistent-volume-claim.yaml`
```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: pvc-claim1
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 500Mi
```

### Deleting a PVC
To delete a PVC, use:
```bash
kubectl delete pvc [pvc-name]
```
What happens to the PV after a PVC is deleted depends on its `reclaimPolicy`:
- **Retain**: The PV is not available for reuse until manually handled by an administrator.
- **Delete**: The PV and its data are automatically deleted.
- **Recycle**: The data is cleared, and the PV becomes available for new claims.

### Centralized Storage Management
Persistent Volumes allow for centralized storage management. Administrators can set up a pool of storage resources that users can access using PVCs. This makes storage allocation easier and consistent across the cluster.

### Benefits of Persistent Volumes
- **Flexible and Cluster-wide**: PVs provide a flexible storage solution across the cluster.
- **Simplified Deployment**: Users don’t need to configure storage for each pod.
- **Centralized Management**: Administrators can manage storage centrally for better oversight.

Persistent Volumes help users deploy applications efficiently without the need to set up storage for each pod individually.

### `pod-using-pvc.yaml`
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod-using-pvc
spec:
  containers:
  - name: app-container
    image: nginx
    volumeMounts:
    - mountPath: "/usr/share/nginx/html"
      name: storage-volume
  volumes:
  - name: storage-volume
    persistentVolumeClaim:
      claimName: pvc-claim1
```
