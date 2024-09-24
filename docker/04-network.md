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

If you want to create custom networks like overlay or macvlan, you can use specific commands. However, for most cases, Docker’s pre-installed networks are all you need!
