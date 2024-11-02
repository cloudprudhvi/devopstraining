## What is CIDR?
CIDR (Classless Inter-Domain Routing) is a technique for allocating IP addresses and managing IP routing efficiently. It simplifies IP addressing by pairing an IP address with a subnet mask.

## Components of a CIDR Block
A CIDR block is composed of:
- **Base IP Address**: The starting point of the IP range (e.g., `10.0.0.0`, `192.168.0.0`).
- **Subnet Mask**: Indicates how many bits represent the network portion, written as `/8`, `/24`, `/32`, etc.

## CIDR Subnet Mask Examples
| CIDR Notation | Subnet Mask        |
|---------------|--------------------|
| /8            | 255.0.0.0          |
| /16           | 255.255.0.0        |
| /24           | 255.255.255.0      |
| /32           | 255.255.255.255    |

## Subnet Mask Formula
To calculate the number of host addresses available within a subnet:
\[ \text{Number of host addresses} = 2^{(32 - \text{prefix length})} \]

### Example:
- **CIDR Block**: `10.0.0.0/24`
- **Number of host addresses**: \(2^{(32 - 24)} = 256\)

## Public vs. Private IP Addresses
### Private IP Ranges
These ranges are reserved for internal network use:
- **10.0.0.0/8**: For large enterprise networks.
- **172.16.0.0/12**: Commonly used for AWS default VPCs.
- **192.168.0.0/16**: Typically used in home or small business networks.

### Public IP Addresses
Addresses outside the private ranges are public and routable on the Internet.

## Subnet Calculation Examples
### Example 1: `192.168.1.0/24`
- **Subnet Mask**: `255.255.255.0`
- **Available hosts**: 254

### Example 2: `10.0.0.0/16`
- **Subnet Mask**: `255.255.0.0`
- **Available hosts**: 65,534

## VPC

An Amazon **VPC (Virtual Private Cloud)** is like a private, secure section of AWS where you can run your cloud resources, such as servers. It’s your own customizable network within the cloud, allowing you to control how these resources connect to each other and the internet. You can split it into subnets (smaller sections) for organizing resources and set up security groups and access control lists for traffic protection. Internet Gateways allow public access, while NAT Gateways let private parts access the internet without exposure. VPCs provide isolation, security, and flexibility for cloud infrastructure.

### Subnet
A subnet is a logical subdivision of an IP network within an Amazon VPC (Virtual Private Cloud). It partitions the VPC’s IP address range into smaller segments, allowing better organization and isolation of resources. Subnets help control where specific AWS resources, like EC2 instances, are launched and managed.
### 1. Public Subnets
- **Definition**: A subnet that is configured to allow resources to communicate directly with the internet.
- **Characteristics**:
  - **Route Table Configuration**: A public subnet has a route table with a route that directs traffic to an **Internet Gateway (IGW)**.
  - **Use Case**: Used for resources that need to be accessible from the internet, such as web servers.
  - **Accessibility**: Instances in public subnets have public IP addresses or Elastic IPs that facilitate direct internet access.

### 2. Private Subnets
- **Definition**: A subnet that is configured so that its resources do not have direct access to the internet.
- **Characteristics**:
  - **Route Table Configuration**: A private subnet has a route table that does **not** have a route to an Internet Gateway.
  - **Use Case**: Ideal for resources that should remain isolated from the public internet, such as databases or internal services.
  - **Accessibility**: Instances in private subnets may connect to the internet only through a **NAT Gateway** or **NAT Instance** for outbound traffic without exposing themselves to inbound internet traffic.

### What Makes a Subnet Public or Private?
The key factor that determines whether a subnet is public or private is the **route table and its rules**. 

### Route Table and Route Rules:
- **Public Subnet**:
  - Contains a route with a destination of `0.0.0.0/0` (or `::/0` for IPv6) that directs traffic to an Internet Gateway (IGW).
  - This configuration allows instances within the subnet to send and receive traffic from the internet.
- **Private Subnet**:
  - Lacks a direct route to an Internet Gateway.
  - Traffic destined for the internet is routed through a **NAT Gateway** or **NAT Instance** for outbound connections, preventing direct inbound access.

### Summary of Differences:
| **Feature**         | **Public Subnet**                          | **Private Subnet**                        |
|---------------------|--------------------------------------------|-------------------------------------------|
| **Internet Access** | Direct via Internet Gateway (IGW)          | Indirect via NAT Gateway/Instance         |
| **Route Table**     | Route to `0.0.0.0/0` through IGW           | No route to IGW                          |
| **Use Case**        | Web servers, public-facing resources       | Databases, internal applications         |
| **Inbound Traffic** | Allowed from the internet                  | Restricted from the internet             |
| **Outbound Traffic**| Direct outbound to the internet            | Outbound via NAT (no direct inbound)     |


### Internet Gateway (IGW)

An **Internet Gateway (IGW)** is a critical component of an Amazon VPC that allows resources within public subnets to communicate with the internet. It serves as a bridge between the VPC and the internet, enabling inbound and outbound traffic.

## Key Points about Internet Gateway:
- **Single IGW per VPC**: Each VPC can have only one Internet Gateway attached at a time.
- **Functionality**: An IGW allows instances in public subnets to access the internet and allows incoming traffic to those instances that have public IP addresses.
- **Attachment**: For an IGW to function, it must be explicitly attached to the VPC.
- **Route Table Configuration**: Public subnets require a route table that directs traffic to the IGW (typically using a `0.0.0.0/0` route) to facilitate internet connectivity.

### Route Table

A **route table** is like a set of instructions that tells your network where to send traffic. Each subnet in your VPC must be associated with a route table to control the flow of network traffic.

## Key Points about Route Tables:
- **Routes**: Each route table has a list of routes that specify the path for traffic. For example, traffic going to `0.0.0.0/0` can be directed to an **Internet Gateway (IGW)** for internet access.
- **Subnet Association**: A route table can be linked to one or more subnets, which determines how traffic is routed for those subnets.
- **Internet Access**: To make a subnet public, the route table must include a route that directs traffic to the IGW.
