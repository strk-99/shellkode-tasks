## Linux authentication
- Enable password auth in linux
  - Launch EC2 instance (amazon linux OS)
  - Create an user called admin
  - Add this user into sudoers (to make this user as super user)
  - Set password for this user
  - Edit SSH config file to allow login with password
 Output: login without any key file and it'll ask password, once you entered the password, it should login
 Subtask - Login as root user
  - Set password for the user ROOT
  - Allow login as root with password
 Output: while login, give the username as root and enter the password, it should login


## Enable Password Authentication for a User
- Launch EC2 Instance
- Launch an Amazon Linux EC2 instance from the AWS Management Console.
- Ensure the instance has SSH access via port 22 (check the security group settings).
- Connect to the Instance
- Use your SSH key file to connect to the instance:
```sh
ssh -i "your-key.pem" ec2-user@<public-ip>
```
- Switch to the Root User to Gain all access:
```sh
sudo su
```
- Create the admin User
- Add a new user named admin:
```sh
adduser admin
```
- Set a password for the admin user:
```sh
passwd admin
```
-After Adding users we need to give access to user to modify file by using sudoers by adding to wheel group
```sh 
usermod -aG wheel user
```

- Add admin to Sudoers
Open the sudoers file for editing:
```sh
visudo
```
Add the following line to grant admin sudo privileges:

```sh
admin    ALL=(ALL)       ALL
```
## Enable Password Authentication
- Open the SSH configuration file:
```sh
vi /etc/ssh/sshd_config
```
- Locate and modify the following parameters:
```sh
PasswordAuthentication yes
PermitRootLogin yes
```
- Save and exit the file.
- Restart the SSH service to apply changes:
```sh
systemctl restart sshd
```
## Test Login
- Disconnect from the current session.
- SSH into the instance using the admin user and password:
```sh
ssh admin@<public-ip>

Enter the password you set earlier.
```
## Allow Root Login with Password
- Set Root Password
- Switch to the root user 
```sh
sudo su
```
- Set a password for the root user:
```sh
passwd
```
- Update SSH Configuration
- Verify the following in /etc/ssh/sshd_config:
- plaintext
```sh
PermitRootLogin yes
```
Save and exit the file (if any changes were made).
- Restart the SSH service again:
```sh
systemctl restart sshd
```
-exit and retry to login as root user
```sh
ssh root@<public-ip>

Enter the root password you set earlier.
```
- Outputs
- For admin: When logging in, it prompts for the admin user's password and logs in successfully.
- For root: When logging in, it prompts for the root user's password and logs in successfully.