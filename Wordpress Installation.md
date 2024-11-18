## Wordpress installation
Install Wordpress on EC2 instance
  - Launch EC2 instance(Ubuntu OS)
  - Install Lamp stack
  - Create database wordpress
  - Edit wp-config.php file to add database details
  - Run wordpress website
## Launch an EC2 Instance
- Log In to AWS Management Console
- Visit the AWS Management Console.
- Log in with your credentials.
- Launch a New EC2 Instance
- In the AWS (Amazon Web Services) Management Console, navigate to Services > EC2.
- Click on Launch Instance.
- Choose an Amazon Machine Image (AMI). Elect Ubuntu Server 20.04 LTS (HVM), SSD (Solid State Drive) Volume Type.
- Choose an instance type. For this tutorial, the t2.micro (free tier eligible) is sufficient.
- Click Next: Configure Instance Details and configure as needed. Defaults are usually fine for a basic setup.
- Click Next: Add Storage and configure the storage. A least of 10 GB is recommended.
- Click Next: Add Tags to add tags (optional).
- Click Next: Configure Security Group. Make a new security group with the following rules:
HTTP: Port 80 (Anywhere)
HTTPS: Port 443 (Anywhere)
SSH: Port 22 (Your IP or Anywhere, but restricting to your IP is more secure)
- Review your configuration and click Launch.
- When prompted, create a new key pair or use an existing one. Download the key pair (a .pem file) and keep it secure.
## Connect to Your Instance
- Open your terminal (or order Prompt in Windows).
- Navigate to the indicative where your key pair .pem file is located.
- Connect to your EC2 instance using SSH:
```sh
ssh -i "your-key-pair.pem" ubuntu@your-ec2-public-dns
```

## Install LAMP Stack

To run WordPress, you need a web server, database server, and PHP. The LAMP stack (Linux, Apache, MySQL, PHP) is a common choice.

- Update and Upgrade Packages
```sh
sudo apt update
sudo apt upgrade
```

- Install Apache
```sh
sudo apt install apache2

#Verify Apache is running:

sudo systemctl status apache2
```
- Install MySQL
```sh
sudo apt install mysql-server

Run the security script to secure MySQL:

sudo mysql_secure_installation
```


- Install PHP
```sh
sudo apt install php libapache2-mod-php php-mysql

#Restart Apache

sudo systemctl restart apache2
```
- Configure MySQL for WordPress
- Log In to MySQL
```sh
sudo mysql -u root -p

Create a Database and User for WordPress

CREATE DATABASE wordpress;

CREATE USER 'wpuser'@'localhost' IDENTIFIED BY 'password';

GRANT ALL PRIVILEGES ON wordpress.* TO 'wpuser'@'localhost';

FLUSH PRIVILEGES;

EXIT;
```
Replace password with a hard password of your choice.

## Install WordPress
- Download WordPress
- Navigate to the Apache root directory and download WordPress:

```sh
cd /var/www/html
sudo wget https://wordpress.org/latest.tar.gz

#Extract WordPress

sudo tar -xvzf latest.tar.gz
```
- Set Permissions
```sh
sudo chown -R www-data:www-data /var/www/html/wordpress
sudo chmod -R 755 /var/www/html/wordpress
```
- Configure Apache for WordPress
- Create an Apache configuration file for WordPress:

```sh
sudo nano /etc/apache2/sites-available/wordpress.conf

#Add the following content:

apache  Copy code
<VirtualHost *:80>
ServerAdmin admin@example.com
DocumentRoot /var/www/html/wordpress
ServerName example.com
ServerAlias www.example.com
<Directory /var/www/html/wordpress/>
Options FollowSymLinks
AllowOverride All
Require all granted
</Directory>
ErrorLog ${APACHE_LOG_DIR}/error.log
CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
Replace example.com with your domain name. Save and close the file (Ctrl+O, Enter, Ctrl+X).
```

Enable the new configuration & the rewrite module:

```sh
sudo a2ensite wordpress.conf
sudo a2enmod rewrite
sudo systemctl restart apache2
```

- Configure WordPress

- Navigate to the WordPress directory:
```sh
cd /var/www/html/wordpress
```
- Create a WordPress configuration file from the sample file:
```sh
sudo cp wp-config-sample.php wp-config.php
```
Edit the WordPress configuration file:
```sh
sudo nano wp-config.php
# Update the database details in wp-config.php:
# PHP Copy code
define('DB_NAME', 'wordpress');
define('DB_USER', 'wpuser');
define('DB_PASSWORD', 'password');
define('DB_HOST', 'localhost');
Save and close the file (Ctrl+O, Enter, Ctrl+X).
```
## Complete WordPress Installation
Access WordPress Web Interface
Open your web browser and navigate to http://your-ec2-public-dns. You should follow the WordPress installation page.

Complete the Setup
Select your language and click Continue.
Fill in the site information (site title, username, password, email).
Click Install WordPress.

Reference websites:
"https://blog.oudel.com/install-wordpress-on-aws-ec2-ubuntu-a-comprehensive-guide/#:~:
"https://medium.com/@DeployMaster/setting-up-wordpress-on-ubuntu-instance-in-aws-a-comprehensive-guide-63fa886afb5a"


