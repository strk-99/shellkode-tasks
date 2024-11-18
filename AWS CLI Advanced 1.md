## AWS CLI Advanced 1
 Create an EC2 instance with CLI
  - Create an IAM role(EC2 role) with EC2 full access
  - Create an EC2 instance and attch the above IAM role
  - Install AWS CLI on the EC2
  - Create an EC2 instance using CLI(take any AMI id from ec2 launch instance page)

## Create an IAM role(EC2 role) with EC2 full access
```sh
aws iam create-role --role-name test-role --assume-role-policy-document file://file.json
```
```sh
json 
{
  "Version":"2024-11-15",
  "Statement":[
    {
      "Effect":"Allow",
      "Principal":{
        "Service":"ec2.amazonaws.com"
      },
      "Action":"sts:AssumeRole"
    },
    {
      "Effect":"Allow",
      "Principal":{
        "Service":"sagemaker.amazonaws.com",
        "AWS":"*"
      },
      "Action":"sts:AssumeRole"
    }
  ]
}
```
```sh
aws iam attach-role-policy --policy-arn arn:"arn id" --role-name rolename
```
## configure aws
```sh
aws configure
```

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





