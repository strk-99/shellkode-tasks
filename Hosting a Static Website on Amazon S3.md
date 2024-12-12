# **Hosting a Static Website on Amazon S3**

Amazon S3 allows you to host static websites containing HTML, CSS, JavaScript, and other static assets. This guide walks through setting up a static website hosted on S3 and accessing it via the managed public URL.

---

## **Create an S3 Bucket**

1. Go to the [S3 Console](https://console.aws.amazon.com/s3/).
2. Click **Create Bucket**.
3. Provide a **Bucket Name** (e.g., `my-static-website`) and select a region.
4. Uncheck the **Block All Public Access** option:
   - Confirm the warning when prompted.
5. Click **Create Bucket**.

---

## **Upload Website Files**

1. Click on your newly created bucket.
2. Go to the **Objects** tab.
3. Click **Upload** and:
   - Add your website files (e.g., `index.html`, `styles.css`, etc.).
   - Click **Upload** to store them in the bucket.

---

## **Enable Static Website Hosting**

1. Go to the **Properties** tab of the bucket.
2. Scroll down to **Static Website Hosting** and click **Edit**.
3. Select **Enable**.
4. Configure the following:
   - **Index Document**: Enter the name of the main file (e.g., `index.html`).

5. Save the changes.
6. We will get url to access web page in properties static webhosting section

---

## Make Public using ACL

1. Go to the **objects** tab.
2. Under **actions**, click **Make Public Using ACL**.
3. click make public
---
## **output**

- click the url ijn properties we will get content in index.html page in browser