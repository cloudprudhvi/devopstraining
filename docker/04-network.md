# Docker Networks

## Introduction

Docker allows containers to communicate with each other, the host machine, and external networks through different network drivers. The main Docker network types are:

- `Bridge`
- `Host`
- ` None`
- `Overlay`
- `Macvlan`

Each of these network types serves different use cases, making Docker networking flexible and powerful.

## How do I create these networks?🤔 
🛠️ You don’t need to manually create the default networks! Docker automatically creates three networks when installed:

- `Bridge` (Default)

- `Host`

- `None`

By default, all created containers will use the bridge network, which is an internal private network for communication between containers on the same Docker host.

If you want to create custom networks (like overlay or macvlan), you can use specific commands, but for most use cases, Docker’s pre-installed networks are sufficient.

### What if I don’t want to use the default bridge network while creating a container? 🤔 
**No problem!** Docker gives you the flexibility to use different networks other than the default bridge network when running a container. You can specify the desired network using the --network flag.

For example:

To run a container on the host network 🌐:

```bash
docker run nginx --network=host
```
To run a container on the none network 🚫 (no network access):
```
docker run nginx --network=none
```
This way, you can select which network to use when launching a container, rather than defaulting to the bridge network.

🔍 **Deep Dive: Bridge Network**

The bridge network 🌉 is the default network for Docker containers. Here’s what you need to know:

`Internal, Private Network:` It allows communication between containers on the same Docker host but isolates them from the outside world unless you configure it otherwise.

`Automatic Attachment:` If you don’t specify a network when creating a container, Docker will automatically attach the container to the bridge network.

`IP Address Range:` The bridge network typically uses an address range starting with 172.17.x.x. Each container gets assigned an IP address from this range, allowing them to communicate with each other.

If your container needs to communicate with the outside world (e.g., the internet or external services), you can achieve this using port mapping. You can map a container’s internal port to a port on the Docker host, like this:

```
docker run -p 8080:80 nginx
```

This maps port 8080 on the host to port 80 inside the container, enabling external traffic to reach the container’s services.

#### Can I use a different network instead of the default 172.x.x.x bridge network?🤔
💡 Yes, you absolutely can! Docker allows you to create custom networks with different subnet ranges. This is useful when you want more control over your network configuration or avoid conflicts with the default 172.17.x.x range used by Docker's bridge network.

To create a custom bridge network with a different subnet, you can use the following command:

```
docker network create --driver=bridge --subnet=173.17.0.0/16 custom-bridge
```

- `--driver=bridge:` Specifies that you are creating a bridge network.
- `--subnet=173.17.0.0/16:` This defines the IP address range for your custom network.
- `custom-bridge:` The name of your new bridge network.

Once this new network is created, you can attach containers to it by specifying the network when running them:
```bash
docker run --network=custom-bridge nginx
```
This allows you to use a custom IP address range (173.x.x.x in this case) and avoid the default 172.x.x.x range used by Docker's default bridge network.

### How do I know if a container is using the new network?🤔
🔍 You can verify which network a container is using by running the docker inspect command. This command provides detailed information about the container, including its network configuration.

To check the network of a specific container, run:

```bash
docker inspect <container_name_or_id>
```
This will return a large JSON output, but the part you’re looking for is under the "Networks" section. For example:

```json
"Networks": {
    "custom-bridge": {
        "IPAddress": "173.17.0.2",
        "Gateway": "173.17.0.1",
        ...
    }
}
```

**Network Name:** The `"Networks"` section will list the network the container is connected to (in this case, `custom-bridge`).

**IP Address:** You will also see the IP address of the container within that network (e.g., 173.17.0.2).

### How do I inspect a Docker network?
🔍 If you want to inspect a specific Docker network, you can use the docker network inspect command. This command gives you detailed information about the network's configuration, such as its subnet, connected containers, and other settings.

To inspect a network, use the following command:

```bash
docker network inspect <network_name>
```
For example, if you created a network called custom-bridge, you would run:

```bash
docker network inspect custom-bridge
```

This will return information such as:

**Subnet:** The IP address range used by the network.
**Connected Containers:** A list of containers attached to this network.
**Network Driver:** Whether the network is using the bridge, overlay, or another driver.

A sample output might look like this:

```json
{
    "Name": "my-custom-bridge",
    "Id": "e3a3e8a9e0...",
    "Driver": "bridge",
    "Subnet": "173.17.0.0/16",
    "Containers": {
        "container_id": {
            "Name": "nginx",
            "IPv4Address": "173.17.0.2/16",
            "MacAddress": "02:42:ac:11:00:02"
        }
    }
}
```

This command helps you inspect and verify the details of the network, including which containers are connected and their corresponding IP addresses.


Here's the enhanced explanation about the host network with examples, following the same style:

### Deep Dive: Host Network
The host network allows a Docker container to share the network stack with the Docker host (i.e., the machine running Docker). This effectively removes the network isolation between the container and the host, meaning the container uses the host’s IP address and network interface directly.

#### How to use the host network
To run a container using the host network, you can specify the --network=host flag in your docker run command:

```bash
docker run --network=host nginx
```

In this example, the nginx container will use the host’s network, meaning:
It will not have its own IP address.

Any ports exposed by the container will be available directly on the host’s IP address, without needing to perform any port mapping.

For instance, if you have an Nginx server running in the container on port 80, it will be accessible directly through the host’s IP address at port 80, without needing to map the port like in bridge networks (-p 8080:80).

 #### Key Characteristics of Host Network
`No Network Isolation:` The container shares the network stack of the host. Any port exposed by the container will bind directly to a port on the host.

`Performance Consideration:` Using the host network can sometimes provide better network performance since there is no network translation (NAT) overhead between the container and host.

`Use Cases:` The host network is useful in scenarios where low-latency access to the network or the actual host’s IP address is necessary, such as running certain monitoring services, or when you don’t want to map ports manually.

**Example**📄 

Let’s look at a practical example where we run an Nginx container with the host network:

```bash
docker run --network=host -d nginx
```
In this case:

The Nginx web server inside the container will be accessible directly at http://<host_ip>:80.

You won’t need to specify a -p (port mapping) option because the container is using the host’s network stack directly.

#### Important Considerations
`Port Conflicts:` Since the container is using the host's network, you need to ensure that no other services on the host are using the same ports. For example, if another service is already using port 80, starting an Nginx container using the host network will result in a port conflict.

`Security:` Using the host network eliminates Docker’s built-in network isolation between the host and containers, which may not be desirable from a security standpoint.

### Deep Dive: None Network🚫
The none network is exactly what it sounds like—it provides no networking for the container. When you run a container with the none network, it is completely isolated from any networks, including other containers, the host, and the external world.

#### How to use the none network
To run a container using the none network, you can use the --network=none flag in your docker run command:

```bash
docker run --network=none nginx
```

In this case, the container will not have any network interfaces, meaning:

It cannot communicate with other containers or the outside world.
It cannot access the internet or be accessed by any external service.
This creates a completely isolated environment.

#### Key Characteristics of None Network
`No Network Connectivity:` The container doesn’t get assigned an IP address or a network interface. It can only communicate with itself, but not with any other network.

`Use Cases:` The none network is useful for running containers where network access is either not required or not desired. For example, if you want to run a container to perform internal data processing without any need for communication with other systems.

📄 `Example`
Let’s run a simple Nginx container with the none network:

```bash
docker run --network=none nginx
```

In this case:
The Nginx web server inside the container won’t be accessible because the container isn’t connected to any network.
The container won’t be able to send or receive data from other containers, the host, or the internet.

#### `Important Considerations`
`Completely Isolated:` Since the container is completely disconnected from any network, you won’t be able to use any network services like HTTP or SSH within the container.

Use When No Networking is Needed: This is ideal for scenarios where you don’t need external communication, like containers doing background processing or performing isolated tasks.

