## AWS Priv Esc (UNUSED) 

Since the Captial One Breach that happened, AWS accounts have needed to be locked down more and more. In this challenge, a low level AWS will be turned into an administrator, in order to grab a flag.  

Most of this comes from a link that I found: https://rhinosecuritylabs.com/aws/aws-privilege-escalation-methods-mitigation/.   

### Ideas 
- Give the user the ability to edit IAM roles. Then, when they give themselves a policy in order to boost their permissions to view an S3 bucket. 
- Give the user the iam:CreateAccessKey permission. Then, force them to use an access key in order to pull data from the account. This would teach them to use the AWS CLI and priv esc stuff :) 
