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

## Network Access Control Lists (NACLs)
- **Definition**: NACLs are like a firewall that controls traffic to and from subnets.
- **One NACL per Subnet**: Each subnet must have one NACL. New subnets are automatically assigned the default NACL.
- **NACL Rules**:
  - Rules are numbered from 1 to 32766, with lower numbers having higher precedence.
  - The first matching rule determines the traffic decision.
  - Example: If rule #100 is `ALLOW 10.0.0.10/32` and rule #200 is `DENY 10.0.0.10/32`, the IP address will be allowed because rule #100 has a higher precedence.
  - The last rule is an asterisk (`*`) and denies all traffic if no other rules match.
  - AWS recommends creating rules in increments of 100 for better organization.
- **Default Behavior**: Newly created NACLs deny all traffic by default.
- **Use Case**: NACLs are effective for blocking specific IP addresses at the subnet level.

## Security Groups
- **Definition**: Security groups act as virtual firewalls for individual instances, controlling traffic at the instance level.
- **Function**: They specify rules that allow traffic in or out of an instance.
- **Stateful**: Security groups are stateful, so if traffic is allowed in, the response traffic is automatically allowed out.
- **Instance-Level**: Security groups are applied directly to instances, providing more granular control.

## Key Differences
| **Feature**          | **NACL**                                   | **Security Group**                        |
|----------------------|--------------------------------------------|-------------------------------------------|
| **Level of Control** | Subnet-level                               | Instance-level                            |
| **State**            | Stateless                                  | Stateful                                  |
| **Rule Direction**   | Rules must be set for both inbound and outbound | Automatically allows responses for allowed traffic |
| **Rule Precedence**  | Lower-numbered rules have higher precedence | No rule numbering; all rules are evaluated |
| **Use Case**         | Additional layer of security, broader control, IP blocking | Primary control for instance traffic     |

NACLs and security groups work together to enhance network security within your VPC.

## What is Bastion

A **Bastion Host** acts as a secure bridge to connect to private instances within a VPC that do not have direct internet access. Here's how it works:

## Role of the Bastion Host
- It’s an intermediary server located in a public subnet with internet access. Users connect to this host to reach resources in private subnets, ensuring secure and controlled access.

## How It Enables Access
- Instead of exposing private instances to the public internet, you connect to the Bastion Host first. From there, you can securely access private servers. This maintains the privacy and security of the instances by restricting direct public access.

## Network Flow
- The user connects to the Bastion Host over the internet, and the Bastion Host connects internally to private instances using private IPs within the VPC. This ensures that private resources remain isolated from the external network.

# NAT Gateway

A **NAT Gateway**, or **Network Address Translation Gateway**, is a managed AWS service that allows instances in a **private subnet** to connect to the internet or other AWS services while ensuring that inbound internet traffic cannot reach them.

## How It Works:
- **Outbound Access**: Instances in private subnets can’t access the internet directly. The NAT Gateway acts as an intermediary that lets these instances send traffic out to the internet for tasks like software updates or API calls.
- **Inbound Protection**: While the NAT Gateway facilitates outbound internet connections, it blocks incoming traffic initiated from the internet, keeping private resources secure.
