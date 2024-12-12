## CLOUDFRONT

## What is CloudFront?

Amazon CloudFront is a content delivery network (CDN) service provided by AWS. It is designed to deliver data, videos, applications, and APIs to customers globally with low latency and high transfer speeds. CloudFront works by caching your content in multiple edge locations around the world, making it faster for users to access content.

### Why Use CloudFront?
- **Improved Performance:** Delivers content with low latency and high transfer speeds.
- **Global Distribution:** Distributes content to users from the nearest edge location.
- **Scalability:** Handles traffic ups and downs efficiently.
- **Security:** Offers features like AWS WAF, and HTTPS for secure delivery.
- **Cost Optimization:** Reduces load on your origin server by caching content at edge locations.transfers content quickly.

---


# Connecting an S3 `index.html` to CloudFront

---

## Step 1: Set Up the S3 Bucket

1. **Create an S3 Bucket**:
   - Go to the [S3 Console](https://aws.amazon.com/s3/).
   - Click `Create bucket`.
   - Use unique bucket name as S3 is Global Service.
   - Select the desired AWS region.
   - Click `Create`.

2. **Upload `index.html` to the S3 Bucket**:
   - Open the newly created bucket.
   - Click `Upload`.
   - Add your `index.html` file.
   - Click `Upload`.

3. **Enable Static Website Hosting**:
   - Go to the `Properties` tab of the bucket.
   - Scroll down and go to `Static website hosting`.
   - Enable the option.
   - Set the `index document` to `index.html`.
   - Copy the URL that enabled from static webhosting section and paste it in url
   - it will show 403 error because we didnot enabled public access.

4. **Set Bucket Policy for Public Access**:
   - Go to the `Permissions` tab.
   - Click `Bucket policy`.
   - Add the following policy:
     ```json
     {
       "Version": "2012-10-17",
       "Statement": [
         {
           "Sid": "PublicReadGetObject",
           "Effect": "Allow",
           "Principal": "*",
           "Action": "s3:GetObject",
           "Resource": "arn:aws:s3:::your-bucket-name/*"
         }
       ]
     }
     ```
   - Replace `your-bucket-name` with the actual bucket name.
   - Click `Save changes`.

---

## Step 2: Create a CloudFront Distribution

1. **Go to the CloudFront Console**:
   - Navigate to the [CloudFront Console](https://aws.amazon.com/cloudfront/).

2. **Create a Distribution**:
   - Click `Create Distribution`.
   - Under `Origin domain`, select your S3 bucket from the dropdown.
   - Set the `Origin access control settings` to:
     - `Public` if your bucket allows public access.
     - `Restrict bucket access` if you want CloudFront to be the sole accessor.
   - Click `Create`.

3. **Set Default Root Object**:
   - In the `Distribution Settings`, specify `index.html` as the `Default Root Object`.

4. **Update S3 Bucket Permissions** (if access is restricted):
   - Add a bucket policy to allow CloudFront to access your S3 bucket.
   - Example policy:
     ```json
     {
    "Version": "2008-10-17",
    "Id": "PolicyForCloudFrontPrivateContent",
    "Statement": [
        {
            "Sid": "AllowCloudFrontServicePrincipal",
            "Effect": "Allow",
            "Principal": {
                "Service": "cloudfront.amazonaws.com"
            },
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::strk-bucket1/*",
            "Condition": {
                "StringEquals": {
                    "AWS:SourceArn": "arn:aws:cloudfront::343218219875:distribution/E1Y43ZD952C3GQ"
                }
            }
        }
    ]
}
     ```

---

## Step 3: Test the CloudFront Distribution

1. **Get the CloudFront Domain Name**:
   - Go to the `Distributions` list.
   - Copy the `Domain Name` of your distribution (e.g., `https://d8ouh2iiqjdm1.cloudfront.net/index.html`).

2. **Access the Website**:
   - Open a browser and go to `https://d8ouh2iiqjdm1.cloudfront.net/index.html`.
   - Verify that the `index.html` file is displayed.


