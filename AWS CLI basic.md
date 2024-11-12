# AWS CLI Basic
## Upload files to S3 using AWS CLI
  - Launch EC2(any OS)
  - Create S3 bucket
  - Install AWS CLI on EC2
  - Create IAM User and attach S3 full access permission
  - Create keys for the IAM user
  - Configure AWS CLI with access and secret keys
  - Create a file with some random text(1 line)
  - Upload that file to S3 using CLI_

## 1. Launch Ec2 instance on any Os

 - After login to our AWS console go to Search bar and type EC2 , Search bar will show tabs which is related to ec2 
 - Select ec2 in search bar and it will navigate to ec2 
 - In ec2 section go to resources dialog box
 - In resources you will find instances (not instances running) select that icon and it will navigate to instances page
 - In instances page you will get launch instances icon click on launch instances icon 
 - It will redirect to the page where we can able to create instances
 - in this page select name, tags of our instance, select required amazon machine image for instance according to our requirement 
 - Check the architecture, Instance type
 - Create new key pair for the Instance
In the key pair we need to give name for the key pair, key pair type, private key pair format and create key pair
  -- After creating key pair select network settings

- Create security group or select excisting security group, allow security access like ssh and https and allow to access anywhere 
-- Configure storage settings required for instances
-- Click on launch instance
- After selecting Launch Instance, Instance will be loaded
- To Check Weather instance is loaded go to Instance running and check weather our instance is launched or not, By selecting our instance we can stop/start/terminate our instance by given settings in instances dialog box
## Create IAM User and attach S3 full access permission
- Go to Search bar and type IAM , Search bar will show tabs which is related to IAM
 - Select IAM in search bar and it will navigate to IAM 
 - In dashboard go to users in access management
 - After selecting users you will navigate to users page
 - In users Page Select Create User to Create new user
 - Mention User details and we can proide access to the user,
 - in console password select Autogenerate Password if we need system to generate password and we can give option to change password or we can give custom password.
 - After selecting next we need to set permisions for iam user
 - Permissions are like adduser to group, copy permissions and Attach policies directly 
 - In this we need to give all s3 Full access to IAM user so select Attach Policies Directly
 - It will show Permission Policies Dialogue box in that go to search bar and type S3 and we will get options related to S3, In that select AmazonS3FullAcess and select Create Policy
 - It will Redirect to Retrive Password section Download .csv file to get credentials of iam user that created.
 - We can check in the Users section to get user details ike username, permissions given.
## Create keys for the IAM user
 - We can create access key to iam user by selecting user and go to access key in summary dialogue box
 - By Selecting Access Key We can able to generate access keys and download it
 
## Create S3 bucket
 - Go to Search bar and type S3 , Search bar will show tabs which is related to S3 
 - Select S3 in search bar and it will navigate to S3 
 - In S3 section go to general purpose buckets and select create bucket
 - Give Bucket name and select create bucket
 - We can check our bucket in general purose buckets section
 
## Install AWS CLI on EC2
- To install Install AWS CLI on EC2 We already have pem file that downloaded while installing/launching the instance we can directly launch our instance by selecting connect instance in aws portal or we can use command prompt 
- In AWS portal we can Directly Connect to the instance 
- If we want to connect in other way we can connect remotely using pem file that we have downloaded go to pem file and type cmd in location of pem file and command prompt will be opened 
- if we already have ssh active we can connect to instance by typing this command
```sh
ssh -i keypair ec2-user@ip_addressofinstance
```
- By selecting this command we can connect with EC2 Instance

## Configure AWS CLI with access and secret keys
- To Configure AWS CLI with access and secret keys we need to give command 
```sh
aws configure
```
- Then we need to give details like 
--AWS Access Key ID
--AWS Secret Access
--Default Region Name
--Default output Format
to configure Aws Cli with Acesss and Secret keys
##Create a file with some random text(1 line)
- To create file we need to use "touch command"
```sh 
touch file.txt
```
- to write data on the file we can use "vim "
```sh
vim file.txt
```
- To instert data press "i"
- "esc" to read only mode or command mode
- ":wq" to save and exit from the file
- If we need to check data we can use "cat command
```sh
cat file.txt
```

## Upload that file to S3 using CLI

- We can upload file by using this command
```sh
aws s3 cp ./file.txt s3://bucketname/
```
- we can get file conformation like uploaded
- s3 cp: The AWS CLI command to copy files.
- ./testfile.txt: The local path to your file (assuming it’s in the current directory).
- s3://file.txt s3://bucketname/: The S3 bucket and path where the file will be stored.


 