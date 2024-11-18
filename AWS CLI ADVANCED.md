## AWS CLI Advanced
 - Upload files to S3 using AWS CLI
 - Launch EC2(any OS)
  - Create two S3 bucket
       - Bucket 1 name : sk-learns3
       - Bucket 2 name: sk-learns3-1
  - Install AWS CLI on EC2
  - Create IAM User(User name: s3admin) and attach S3 full access permission
  - Create keys for the IAM user
  - Create another IAM user(User name: s3limit) and attach an inline policy. Inline policy permissions below.
  - Inline permission --> Read and Write access to only sk-learns3-1 bucket
  - Configure AWS CLI with the s3admin user's keys --> AWS CLI Profile name: s3admin
  - Configure AWS CLI with the s3limit user's keys --> AWS CLI Profile name: s3limit
  - Create a file with some random text(1 line)
  - Upload that file first S3 bucket using CLI profile s3admin(output: upload success)
  - Upload the same file to 2nd bucket using CLI profile s3limit(output: upload success)
  - Upload the same file to the 1st bucket using CLI profile s3limit(output: upload failed)

## Launching EC2 instance using AWS CLI
Connecting to cli through cloud shell
```sh
sudo yum update -y && sudo yum install aws-cli -y 
```

- Create a Key Pair 
```sh
aws ec2 create-key-pair --key-name demo_key-pair --query "keyMaterial" --output Text > demo_key_pair.pem
```
- creating security group
```sh
-aws ec2 create-security-group --group-name demo_sg --description "my security group"
-aws ec2 authorize-security-group-ingress --group-name "demo-sg" --protocol tcp --port 22 --cidr 0.0.0.0/0
```
- launch ec2 Instance 
```sh
-aws ec2 run-instances --image-id "ami- o53b..." --instance-type t2 micro --eyname demo-key-pair --security-group-ids sg --tags key=Name,valuw = Demoinstance
```
- Create S3 Buckets
```sh
aws s3 mb s3://sk-learns3
aws s3 mb s3://sk-learns3-1
```

## Create IAM User s3admin and Attach S3 Full Access Permission
- In the AWS Management Console:
- Go to IAM > Users > Add users.
Username: s3admin
- Access type: Programmatic access
Permissions: Attach the AmazonS3FullAccess policy.
Save the Access Key ID and Secret Access Key for s3admin.
## Create IAM User s3limit and Attach Inline Policy
- In IAM > Users, create another user:
Username: s3limit
Access type: Programmatic access
Inline Policy:
Go to Permissions for s3limit.
Add an Inline Policy:
```sh
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": ["s3:PutObject", "s3:GetObject"],
      "Resource": "arn:aws:s3:::sk-learns3-1/*"
    }
  ]
}
```
Save the Access Key ID and Secret Access Key for s3limit.
## Configure AWS CLI for s3admin and s3limit Profiles
- Configure s3admin profile:
```sh
aws configure --profile s3admin
# Enter Access Key ID for `s3admin`
# Enter Secret Access Key for `s3admin`
# Set default region and output format
Configure s3limit profile:
```
```sh
aws configure --profile s3limit
# Enter Access Key ID for `s3limit`
# Enter Secret Access Key for `s3limit`
# Set default region and output format
```
## Create a File with Random Text
```sh
echo "This is a test file for S3 upload" > testfile.txt
```
## Upload File to sk-learns3 Bucket Using s3admin Profile
```sh
aws s3 cp testfile.txt s3://sk-learns3 --profile s3admin
```
Output: upload success

## Upload File to sk-learns3-1 Bucket Using s3limit Profile
```sh
aws s3 cp testfile.txt s3://sk-learns3-1 --profile s3limit
```
Expected Output: upload success

## Attempt to Upload File to sk-learns3 Using s3limit Profile
```sh
aws s3 cp testfile.txt s3://sk-learns3 --profile s3limit
```


