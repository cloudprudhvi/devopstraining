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
