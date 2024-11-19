## Increase Root and Data disk volume size
  - Launch EC2 instance (Ubuntu OS)
  - Attach 1GB EBS volume to the ec2 and mount it in /mnt - FileSystem EXT4
  - Increase the Data disk size (1GB disk) to 2GB (output: lsblk should show 2GB) explain each inndetail like you you explain to 15 years old 
  - Increase the root volume to 10GB (output: lsblk should show 10GB)
  - Launch EC2 Instance with amazon linux OS - FileSystem XFS
  - Increse the Root volume size to 12GB(output: lsblk should show 12GB)

## Launch an EC2 Instance
- Launch an Ubuntu EC2 instance using the AWS Management Console.
- Attach a 1GB EBS volume to this instance:
- Go to the EC2 Dashboard → Volumes.
- Create a 1GB volume and attach it to the instance.

## Connect to the Instance
SSH into the instance:
```sh
ssh -i "your-key.pem" ubuntu@Public_IP
```

- Format and Mount the EBS Volume
- Check the available disks:

```sh
lsblk
```
- You should see the attached volume (e.g., /dev/xvdf).

- Format the volume as EXT4:

```sh
sudo mkfs.ext4 /dev/xvdf
```
- Create a mount point and mount the volume:

```sh
sudo mkdir /mnt
sudo mount /dev/xvdf /mnt
```
- Verify the mount:
```sh
df -h
```
You should see /dev/xvdf mounted on /mnt.

## Increase Data Disk Size
- Resize the EBS volume to 2GB:

- Go to the AWS Management Console → Volumes.
- Select the volume attached to the instance and click Modify Volume.
- Change the size to 2GB and confirm.
- Verify the new size:

- On the instance, use:
```sh
lsblk
```
- The disk size will still show as 1GB initially.
- Resize the file system:

```sh
sudo growpart /dev/xvdf 1
```
- Expand the file system:
```sh
sudo resize2fs /dev/xvdf
```
- Verify the new size:
```sh
lsblk
```
- You should see 2GB for /dev/xvdf.

## Increase Root Volume to 10GB
- Resize the root EBS volume:

- Go to the AWS Management Console → Volumes.
- Select the root volume of the instance and click Modify Volume.
- Change the size to 10GB and confirm.
- Inform the system about the size change:
```sh
sudo growpart /dev/xvda 1
```
- Resize the file system:

- Expand the file system:
```sh
sudo resize2fs /dev/xvda1
```

- Verify the new size:

```sh
lsblk
```

- The root volume should now show as 10GB.

## Amazon Linux Instance - Root Volume
## Launch an Amazon Linux EC2 Instance
- Launch an Amazon Linux EC2 instance using the AWS Management Console.
- Increase Root Volume Size to 12GB
- Resize the root EBS volume:

- Go to the AWS Management Console → Volumes.
- Select the root volume of the instance and click Modify Volume.
- Change the size to 12GB and confirm.
- Connect to the instance:

```sh
ssh -i "your-key.pem" ec2-user@Public_IP
```

- Inform the system about the size change:

```sh
sudo growpart /dev/xvda 1
```
- Resize the file system (XFS):

- For Amazon Linux, the root file system is typically XFS:
```sh
sudo xfs_growfs /
```
- Verify the new size:
```sh
lsblk
```
The root volume should now show as 12GB.

