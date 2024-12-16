

## **Networking Basics**

### **IP Addresses**
**An IP address is a unique identifier assigned to devices in a network. AWS VPCs use private and public IP addresses for communication.**
  - **Public IP**: Accessible over the internet.
  - **Private IP**: Restricted to internal communication within a VPC.

- We use ip address to uniquely identify and route traffic to resources.

-  IP address is Assigned to resources such as EC2 instances, NAT gateways, and load balancers.

- We use IP address is To ensure that resources can communicate efficiently within and outside the network.

- **Example**:
  - A private IP for a backend server: `10.0.1.25`
  - A public IP for a web server: `54.32.12.5`

### **CIDR (Classless Inter-Domain Routing)**
-CIDR is a method for defining IP address ranges for efficient allocation and routing.
  - Example: `10.0.0.0/16` specifies an IP address range of `10.0.0.0` to `10.0.255.255`.

- CIDR is Used to design VPCs and subnets by specifying IP ranges.

- CIDR is Applied in VPC and subnet creation to define address spaces.

- CIDR is used  To segment and allocate IP addresses efficiently within a network.

- **Example**:
  - CIDR for a VPC: `10.0.0.0/16`
  - CIDR for a subnet: `10.0.1.0/24`

## 1. **VPCs**
=
- Virtual Private Clouds (VPCs) allow you to provision logically isolated networks in the AWS cloud.
- Provides control over network settings, IP address ranges, subnets, route tables, and gateways.
- When setting up an isolated environment for your applications or workloads.
- When you need specific network configurations for compliance or performance.
- VPC is Located within a single AWS region but can span multiple Availability Zones (AZs).
-We use VPC To ensure security by isolating resources, control over traffic.

---

## 2. **Subnets**

- Subnets are subdivisions of a VPC's IP address range and can be public or private.
- We use Subnets When segregating workloads based on access levels or functionality.

### **Where**
- Each subnet is mapped to a single Availability Zone.

### **Why**
- To separate public-facing resources (e.g., web servers) from private resources (e.g., databases).

### **Example**
- Create a public subnet for web servers with an associated internet gateway and a private subnet for backend servers.

---

## 3. **Route Tables**
### **What**
- Route tables define how traffic is routed within a VPC and outside it.

### **When**
- When configuring routing rules for specific destinations (e.g., internet, peering connections).

### **Where**
- Associated with subnets or a VPC.

### **Why**
- To ensure proper routing of data packets within the network.

### **Example**
- Configure a route table to direct all traffic (0.0.0.0/0) to an internet gateway for public subnets.

---

## 4. **Internet Gateways**
### **What**
- A horizontally scaled, redundant component that allows VPC resources to connect to the internet.

### **When**
- When you need public internet access for EC2 instances or other resources.

### **Where**
- Attached to a VPC.

### **Why**
- To enable outbound and inbound internet traffic for resources in the VPC.

### **Example**
- Attach an internet gateway to a VPC and update the route table to allow traffic to and from the internet.

---

## 5. **Egress-Only Internet Gateways**
### **What**
- Allows IPv6-enabled resources in a VPC to access the internet but blocks inbound traffic.

### **When**
- When using IPv6 resources that only require outbound internet access.

### **Where**
- Attached to a VPC.

### **Why**
- To maintain security by preventing inbound connections while allowing outbound access.

### **Example**
- Create an egress-only internet gateway and configure route tables for IPv6 traffic.

---


## 6. **Elastic IPs**
### **What**
- Static, public IPv4 addresses that you can allocate to your AWS resources.

### **When**
- When you need a fixed public IP address for an EC2 instance or NAT gateway.

### **Where**
- Associated with resources in a VPC.

### **Why**
- To maintain a consistent IP address even if the associated resource is stopped or restarted.

### **Example**
- Allocate an Elastic IP and associate it with an EC2 instance to ensure a persistent public IP.

---

## 7. **Managed Prefix Lists**
### **What**
- Collections of CIDR blocks that you can reference in security groups and route tables.

### **When**
- When managing complex network configurations with multiple CIDR blocks.

### **Where**
- Applied in route tables or security groups.

### **Why**
- To simplify and standardize network management.

### **Example**
- Create a managed prefix list for corporate IP ranges and reference it in security groups.

---

## 8. **NAT Gateways**
### **What**
- Allows instances in a private subnet to connect to the internet or other AWS services while remaining inaccessible from the internet.

### **When**
- When private resources need outbound internet access.

### **Where**
- Deployed in a public subnet.

### **Why**
- To enable secure, outbound internet connectivity for private resources.

### **Example**
- Launch a NAT gateway in a public subnet and update the route table for private subnets.

---

## 9. **Peering Connections**
### **What**
- Enables networking between two VPCs to allow resource sharing.

### **When**
- When you need to connect VPCs in the same or different AWS accounts or regions.

### **Where**
- Configured between two VPCs.

### **Why**
- To facilitate communication without using public internet or VPNs.

### **Example**
- Establish a VPC peering connection to allow applications in one VPC to access databases in another.

---

## 10. **Security**
### **What**
- Measures to protect resources in your VPC, such as security groups and network ACLs.

### **When**
- Always applied to control access to and from resources.

### **Where**
- Defined at the subnet and instance levels.

### **Why**
- To protect resources from unauthorized access or attacks.

### **Example**
- Implement a security group allowing only SSH access from specific IP ranges.

---

## 11. **Network ACLs**
### **What**
- Stateless, subnet-level rules for inbound and outbound traffic control.

### **When**
- When setting broad network-level security rules.

### **Where**
- Applied at the subnet level.

### **Why**
- To provide an additional layer of security.

### **Example**
- Configure a network ACL to block all inbound traffic except HTTP and HTTPS.

---

## 12. **Security Groups**
### **What**
- Stateful, instance-level firewalls that control inbound and outbound traffic.

### **When**
- When setting specific access rules for individual instances.

### **Where**
- Associated with EC2 instances or other services.

### **Why**
- To tightly control traffic to and from specific resources.

### **Example**
- Create a security group to allow only MySQL access from a specific application server.

---

## 13. **Endpoints**
### **What**
- Enable private connectivity between VPC resources and AWS services without traversing the internet.

### **When**
- When accessing AWS services like S3 or DynamoDB privately from a VPC.

### **Where**
- Configured within a VPC.

### **Why**
- To enhance security and reduce latency by avoiding internet traffic.

### **Example**
- Set up an S3 VPC endpoint to allow private access to S3 buckets from a VPC.

---

