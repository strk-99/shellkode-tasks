# Amazon EC2: Comprehensive Guide

## What is EC2?
Amazon Elastic Compute Cloud (EC2) provides resizable compute capacity in the cloud, enabling users to run virtual servers efficiently.

### Key Features:
- Broad choice of instance types.
- Auto-scaling to meet demand.
- Flexible pricing models (On-Demand, Reserved, Spot).

---

## Instances

### What are Instances?
Instances are virtual servers running on AWS EC2, forming the foundation for deploying applications and workloads.

### Why use Instances?
- To host applications in a scalable environment.
- To handle varying workloads with different instance types.
- To ensure reliability with features like Elastic IPs and auto-recovery.

### When to use Instances?
- When hosting web applications or databases.
- For batch processing and data analysis.
- During the development and testing of software.

### Where are Instances used?
- Across Availability Zones within an AWS Region.
- In hybrid cloud setups using AWS Outposts.

### Key Properties:
- **Instance ID**: A unique identifier for each instance.
- **State**: Indicates if the instance is running, stopped, or terminated.
- **Elastic IPs**: Static IP addresses for consistent access.
- **Public and Private DNS**: Hostnames for instance communication.
- **Tags**: Metadata labels for organizing and identifying resources.

---

## Instance Types

### What are Instance Types?
Instance types define the hardware specifications of EC2 instances, such as CPU, memory, and storage.

### Why choose specific Instance Types?
- To optimize costs based on workload requirements.
- To ensure performance for CPU, memory, or storage-intensive tasks.

### When to use specific Instance Types?
- **General Purpose**: For web servers and app development.
 -- Instance Family: T, M, A, Mac
 -- Use Cases: Balanced workloads like web servers, application servers, and small databases
-- Key Features: Balanced CPU, memory, and networking. Offers burstable performance (T family).
- **Compute Optimized**: For gaming, machine learning, or HPC.
 -- Instance Family: C
-- Use Cases: Compute-intensive applications like HPC, gaming, ML inference, and real-time analytics
-- Key Features: High-performance processors with low latency and optimized compute power.
- **Memory Optimized**: For in-memory databases like Redis.
 -- Instance Family: R, X, Z, High Memory
-- Use Cases: Memory-intensive applications like in-memory databases, big data analytics, and real-time caches
-- Key Features:  High memory-to-CPU ratio for applications needing large amounts of memory.
- **Storage Optimized**: For big data processing.
 -- Instance Family:I, D, H
-- Use Cases: Data-intensive applications like NoSQL databases, big data analytics, and log processing
-- Key Features: High, sequential read and write access with low latency; NVMe SSDs or HDD storage options.
- **Accelerated Computing**: For GPU-based tasks like rendering.
 -- Instance Family: P, G, F, Inf, VT, DL
-- Use Cases: Graphics, machine learning training/inference, FPGA-based workloads, and video transcoding
-- Key Features: Leverages GPUs, FPGAs, or AWS-designed Inferentia chips for specialized hardware acceleration.

### Where are Instance Types used?
- Across all AWS Regions and Availability Zones.
- In VPC environments for isolated workloads.

---

## Launch Templates

### What are Launch Templates?
Launch Templates store configuration details for launching EC2 instances.

### Why use Launch Templates?
- To streamline and standardize instance launches.
- To enable versioning for configuration updates.
- To simplify Auto Scaling Group configurations.

### When to use Launch Templates?
- For environments requiring multiple instances with similar settings.
- When using Spot Instances or Auto Scaling.

### Where are Launch Templates used?
- In the EC2 console or AWS CLI.
- As part of CI/CD pipelines for automated deployments.

---

## Spot Requests

### What are Spot Requests?
Spot Requests allow users to access unused EC2 capacity at reduced costs.

### Why use Spot Requests?
- To save up to 90% on EC2 costs.
- For non-critical, fault-tolerant workloads.

### When to use Spot Requests?
- For batch jobs, containerized workloads, or testing environments.
- When workload interruptions can be tolerated.

### Where are Spot Requests used?
- Across all regions where Spot capacity is available.
- In scenarios requiring flexible compute resources.

---

## Savings Plans

### What are Savings Plans?
Savings Plans offer flexible pricing based on consistent EC2 usage.

### Why use Savings Plans?
- To reduce compute costs by up to 72%.
- To maintain flexibility in switching instance families.

### When to use Savings Plans?
- When running consistent workloads for 1 or 3 years.
- To optimize costs for both EC2 and AWS Fargate.

### Where are Savings Plans applied?
- Globally across all AWS Regions.
- Automatically applied to eligible resources.

---

## Reserved Instances

### What are Reserved Instances (RIs)?
RIs are pre-purchased compute capacity for long-term usage.

### Why use Reserved Instances?
- To secure discounts for predictable workloads.
- To ensure capacity availability in specific zones.

### When to use Reserved Instances?
- For steady-state applications such as databases.
- In environments with predictable traffic patterns.

### Where are Reserved Instances used?
- Within specific AWS Regions and Availability Zones.
- In setups requiring guaranteed capacity.

---

## Dedicated Hosts

### What are Dedicated Hosts?
Dedicated Hosts provide physical servers reserved for exclusive use.

### Why use Dedicated Hosts?
- To meet compliance and licensing requirements.
- To run workloads requiring physical server isolation.

### When to use Dedicated Hosts?
- For Bring Your Own License (BYOL) software.
- To run high-security workloads.

### Where are Dedicated Hosts used?
- Across regulated industries such as healthcare or finance.
- In private or hybrid cloud architectures.

---

## Capacity Reservations

### What are Capacity Reservations?
Capacity Reservations guarantee EC2 capacity in specific Availability Zones.

### Why use Capacity Reservations?
- To ensure instance availability during peak demand.
- For compliance with internal or external requirements.

### When to use Capacity Reservations?
- For high-priority applications.
- In disaster recovery scenarios.

### Where are Capacity Reservations used?
- In regions requiring guaranteed compute resources.
- Across multiple Availability Zones for redundancy.

---

## Images and AMIs

### What are AMIs?
Amazon Machine Images (AMIs) are preconfigured templates for launching EC2 instances.

### Why use AMIs?
- To standardize application configurations.
- To speed up deployment processes.

### When to use AMIs?
- When creating new instances with pre-installed software.
- For replicating environments across regions.

### Where are AMIs used?
- Across all AWS Regions and accounts.
- For on-premise deployments using AWS Outposts.

---

## Elastic Block Store (EBS) 

### What is EBS?
EBS provides block-level storage volumes for EC2 instances.

### Why use EBS?
- To store persistent data independent of instances.
- To back up critical data with snapshots.

### When to use EBS?
- For databases requiring low-latency storage.
- For applications needing high IOPS or throughput.

### Where is EBS used?
- Across all AWS Regions.
- In hybrid environments for extended storage.

---
## what is snapshot?
- Snapshot is backup for volume which contains information till on point.

## why we use Snapshots?
- We can use snapshot to create volumes, AMIs and can share amis.

## when we use Snapshots?
- We can use snapshot when we accidentally deleted volumes or instances.
- as abackup we can use snapshot

## where to use snapshot?
- Within the EBS console.
- Across multi-region architectures to standardize backups.
---
## Lifecycle Manager

### What is Lifecycle Manager?
Lifecycle Manager automates the creation and management of EBS snapshots.

### Why use Lifecycle Manager?
- To ensure regular backups of critical data.
- To meet compliance and data retention policies.

### When to use Lifecycle Manager?
- For automating snapshot schedules.
- When managing large volumes requiring backup policies.

### Where is Lifecycle Manager used?
- Within the EBS console.
- Across multi-region architectures to standardize backups.

---
## LOAD BALANCER
### What is Load Balancer?
- loadbalancer is a service provided by aws which helps to distribute traffic to the servers and reduce risk of getting servers go down
 
### why use Load Balancer?
 
- load balancer conducts continuos health checks by sending api calls to the servers regularly and sends taffic to the server which responds to regular ealth checks conducted by aws load balancer
- We use Load Balancer for improved performance, scalability, fault tolerance, security, High Availability.

### when to use Load Balancer?
- A Load Balancer is used when you need to distribute incoming network traffic across multiple servers or resources to ensure optimal performance, availability, and fault tolerance. It is a critical component for scalable, high-availability applications and is often deployed in systems requiring redundancy and seamless user experiences.

### where to use load balancers?
- In Front of Web Applications:
-- Distribute HTTP/HTTPS requests across multiple servers or instances.
--Example: E-commerce platforms or SaaS applications.
- In API Gateways:
-- Manage incoming API requests for backend microservices.
- In Multi-Tier Architectures:
--Distribute requests between application servers, database servers, or caching layers.
- In Multi-Region Deployments:
--Direct users to the nearest server to minimize latency.
--Example: Global content delivery or disaster recovery setups.
In Hybrid Environments:

- Balance traffic between on-premises data centers and cloud environments.

### Types Of Load Balancers
### Based on Layer:
- Application Load Balancer (ALB):
--Operates at Layer 7 (HTTP/HTTPS).
--Best for routing based on content, URLs, or headers.

- Network Load Balancer (NLB):
--Operates at Layer 4 (TCP/UDP).
--Best for low-latency, high-throughput applications.

- Classic Load Balancer (CLB):
--Operates at both Layers 4 and 7.
--Basic load balancing for older applications.


### How Does a Load Balancer Work?
- Receiving Requests:
-- The Load Balancer acts as the single entry point for all incoming traffic.
- Distributing Traffic:
-- Based on predefined rules or algorithms, it routes traffic to backend servers or instances.
- Health Checks:
-- Continuously monitors the health of backend servers and only routes traffic to healthy ones.
- Scaling and Adaptation:
-- Automatically adjusts to handle dynamic traffic loads by integrating with auto-scaling services.
- Failover Mechanism:
-- If a server fails, traffic is seamlessly redirected to healthy servers without downtime.


