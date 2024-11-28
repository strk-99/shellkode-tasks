## Domain Name Mapping

  - Go to godddy.com and buy a website for you(try to buy .in because its cheaper)
  - Launch EC2 instance and install apache2
  - Edit the index.html file and add your own simple html content
  - Map your domain name to this EC2 instance
  - Output: if we hit the domain name then it should return the website that your added explain every step in detail

## Buy a Domain from GoDaddy
- godaddy.com > login >search for domain >purchase domain 
- Domain Management: After purchase, go to My Products in your GoDaddy account to manage your domain.
## Launch an EC2 Instance on AWS
- Log in to AWS: 
- Open the AWS Management Console.Navigate to EC2 under the "Compute" section.
Click on Launch Instance.Choose an Amazon Machine Image (AMI):
Select Amazon Linux 2 Select a free tier-eligible type like t2.micro.
- Configure Instance Details:Leave defaults or customize as per requirements.
- Add Storage: Leave default (8GB is enough).
- Add Tags: Optionally, add a name tag (e.g., MyWebsite).
- Configure Security Group: Allow HTTP (port 80) and SSH (port 22) in the inbound rules.
- Launch and Connect:

- Click Launch, and select or create a key pair for SSH access.
- After the instance starts, note its Public IPv4 Address.
- Connect to the instance via SSH:
```sh
ssh -i "your-key.pem" ec2-user@<Public-IP>
```
## Install Apache2 Web Server
Update Packages:
```sh
sudo yum update -y  
```
- Install Apache2:
```sh
sudo yum install httpd -y  
```
- Start the Web Server:
```sh
sudo systemctl start httpd  
```
- Enable on Boot:
```sh
sudo systemctl enable httpd  
```

- Visit http://<Public-IP> in your browser. You should see the Apache default page.
- Edit the index.html File
- Navigate to the Web Root Directory:

```sh
cd /var/www/html
```

- Edit index.html:
```sh
sudo nano index.html
```
- Add simple HTML content:
html
Copy code
<!DOCTYPE html>
<html>
<head>
    <title>title</title>
</head>
<body>
    <h1>content</h1>
    <p>content</p>
    <h1>content</h1>
    <p>content</p>
    <h1>content</h1>
    <p>content</p>
</body>
</html>
- Save and Exit:

- Press CTRL + O to save and CTRL + X to exit.
- Refresh http://<Public-IP> in your browser. You should see your custom content.
## Map the Domain to the EC2 Instance
- copy public ip of instance and Go to GoDaddy Domain Settings:

- In your GoDaddy account, open the Domain Manager for your purchased domain.
Update DNS Records:
- Find the DNS Management section.
- Add or edit the A Record: Type: A , Name: @ Value: Your EC2 Public IP 
TTL: 600 seconds (default).
- Save the DNS configuration. Propagation may take a few minutes.
## Verify Domain Setup
- Open a browser and visit http://yourdomain.in.
- You should see the website hosted on your EC2 instance.
## Output
If configured correctly:

- Entering http://yourdomain.in in the browser will display the HTML content you added to the index.html file.
