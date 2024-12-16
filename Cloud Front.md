# Amazon CloudFront Documentation

## General
Amazon CloudFront is a Content Delivery Network (CDN) service that delivers data, videos, applications, and APIs to users with low latency and high transfer speeds. It leverages a network of globally distributed edge locations to cache and serve content closer to users, improving performance and reducing load on origin servers.

### Key Features
- **Global Edge Network**: Over 450+ edge locations and regional edge caches.
- **Static and Dynamic Content Delivery**: Optimized for static (images, videos) and dynamic (APIs, personalized content) data.
- **Integration**: Works seamlessly with other AWS services like S3, EC2, and Lambda@Edge.
- **Cost-Efficiency**: Reduces bandwidth costs and improves application performance.

### CloudFront Overview
Amazon CloudFront is a Content Delivery Network (CDN) service provided by AWS. It securely delivers data, videos, applications, and APIs to customers globally, with low latency and high transfer speeds.

#### What is CloudFront?
- A CDN that caches and distributes content through a network of data centers called edge locations.
- It accelerates the delivery of both static content (images, CSS, JS, etc.) and dynamic content (APIs, live video streams).
- Integrated with other AWS services (like S3, EC2, Lambda@Edge).

#### Why Use CloudFront?
- **Low Latency and High Speed**: Delivers content closer to users by serving from the nearest edge location.
- **Global Reach**: Ensures users worldwide experience fast response times.
- **Improved Performance**: Reduces the load on origin servers by caching content.
- **Enhanced Security**: Supports AWS Shield, Web Application Firewall (WAF), and HTTPS connections.
- **Scalability**: Handles varying traffic demands without manual intervention.
- **Cost-Effective**: Reduces data transfer costs by optimizing traffic routes and caching.
- **Customizability**: Supports Lambda@Edge for executing code at the edge.

#### When to Use CloudFront?
- **Static Content Distribution**: For websites, images, or downloadable files hosted on S3 or other origins.
- **Dynamic Content Acceleration**: For APIs and personalized data with low latency requirements.
- **Streaming Media**: Live or on-demand video and audio streaming.
- **Global Applications**: Applications serving users in multiple regions.
- **Security Requirements**: Enabling features like TLS encryption, DDoS protection, and custom WAF rules.

#### Where is CloudFront Used?
- **E-Commerce Websites**: Ensures fast, reliable access to product pages and checkout flows.
- **Media and Entertainment**: For live and on-demand streaming.
- **Gaming Applications**: Reduces latency for gamers worldwide.
- **Corporate Portals**: Delivers internal resources securely and quickly.
- **Mobile and Web Applications**: Speeds up content delivery for global users.

#### How to Use CloudFront?
1. **Set Up an Origin**: Configure an origin server like S3, EC2, or an on-premise server.
2. **Create a CloudFront Distribution**: Define the content origin and behavior (e.g., caching rules, SSL, and allowed HTTP methods).
3. **Configure Settings**: Choose edge locations, pricing tiers, and caching durations.
4. **Integrate with DNS**: Use Route 53 or another DNS provider to route traffic through CloudFront.
5. **Monitor and Optimize**: Use AWS CloudWatch, reports, and logs to track performance and make adjustments.

---

## Security
CloudFront provides robust security features to protect applications and content from cyber threats.

### Key Security Features
1. **TLS/SSL Encryption**:
   - Delivers content over HTTPS for secure connections.
   - Supports custom SSL certificates.

2. **AWS Shield**:
   - Built-in DDoS protection at no additional cost.

3. **Web Application Firewall (AWS WAF)**:
   - Protects against common web exploits like SQL injection and cross-site scripting.
   - Allows custom security rules.

4. **Access Control**:
   - Geo-restrictions to block or allow content based on location.
   - Signed URLs and cookies for controlling access to private content.

5. **Integration with IAM**:
   - Role-based access for secure distribution management.

---

## Origins
Origins are the source of the content that CloudFront delivers.

### Types of Origins
- **Amazon S3**: For storing and distributing static files.
- **HTTP/HTTPS Servers**: Custom origin servers like EC2 instances or on-premises data centers.
- **AWS Media Services**: For live and on-demand video streaming.

### Configuration
- **Origin Settings**:
  - Specify the origin domain name and path.
  - Configure origin protocols (HTTP or HTTPS).

- **Origin Groups**:
  - Set up multiple origins for high availability and failover.

---

## Behaviors
Behaviors control how CloudFront processes requests and interacts with origins.

### Key Configuration Options
1. **Path Pattern**:
   - Define URL patterns to route specific requests to different origins.

2. **Cache Settings**:
   - Specify TTL (Time to Live) for objects in the cache.
   - Enable or disable cache key customizations (e.g., based on query strings, headers).

3. **Allowed HTTP Methods**:
   - Control supported request methods (e.g., GET, POST).

4. **Lambda@Edge**:
   - Run custom logic at edge locations, such as request/response manipulation or authentication.

5. **Redirects and Rewrites**:
   - Define URL redirects or rewrites to simplify request handling.

---

## Error Pages
Custom error pages improve user experience by providing meaningful messages during issues.

### Configuration
1. **Customize Error Responses**:
   - Configure custom error pages for HTTP errors (e.g., 404 Not Found, 500 Internal Server Error).

2. **Error Caching**:
   - Set TTL for caching error responses.

---

## Invalidations
Invalidations clear cached content from edge locations, ensuring users receive updated content.

### Usage
- **Manual Invalidation**:
  - Specify object paths (e.g., `/index.html`, `/assets/*`) for invalidation.

- **Automation**:
  - Use AWS CLI, SDKs, or APIs to automate invalidation processes.

- **Costs**:
  - First 1,000 invalidation paths per month are free; additional requests incur charges.

---

## Tags
Tags enable the organization and management of CloudFront distributions for tracking and cost allocation.

### Usage
- Add key-value pairs as tags during or after distribution creation.
- Use tags to filter resources in AWS Cost Explorer or Resource Groups.

---

## Logging
CloudFront supports logging to monitor and analyze distribution performance and usage.

### Types of Logs
1. **Standard Logs**:
   - Logs HTTP/S requests to Amazon S3.
   - Includes details like request time, IP address, and user agent.

2. **Real-Time Logs**:
   - Provides near-instantaneous logging for analysis.
   - Integrates with AWS Kinesis for real-time processing.

### Configuration
- Enable logging via the CloudFront console or APIs.
- Choose an S3 bucket to store logs.


