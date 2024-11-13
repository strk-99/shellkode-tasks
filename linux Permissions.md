# Linux Permissions
## Understand the Linux permissions - Read/Write/Execute
 - Users and groups
 - Try changing the file owner user/group
 - Change the permission for a file/folder
 - Create a folder called myfol and create 2 files inside that folder
     - Assing read only permissions for user and group for the myfol folder, and that permission should be applied to those files as well.
     - Change the owner and group for that folder, and it should be applied for those files as well inside the folder.
## Users
- users are individual accounts that can log into the system
## Groups
- groups are collections of users that can be managed together
## Try changing the file owner user/group
- We can change file owner user/group by usiing following command
```sh
chown name(user):name(group) filename.txt
```
## Change the permission for a file/folder
- We can change permission for a file/folde by usiing following command
```sh
chmod rwx-wx-rx file/
```

- r=read = 4  
- w=write = 2
- x=execute = 1
- we can use numeric also like
- (rwx) = 4+2+1 = 7
- (rw-) = 4+2+0 = 6
- (r-x) = 4+0+1 = 5
- (r--)  = 4+0+0 = 4
- (-wx) = 0+2+1 = 3
- (-w-) =0+2+0 = 2
- (- - x) = 0+0+0=0

for example
```sh
drwxrwxr-x 5 ec2-user ec2-user 198 may 22 13:20 media
```
- here d represents file type
- first rwx for user
- second rwx for group
- third r-x for write 
- ec2-user for user
- ec2-user for group
- may 22 13:20 is time of file
- media is file

##
we use 
"touch" to create file 
"cp" to copy file 
"mv" to move file

