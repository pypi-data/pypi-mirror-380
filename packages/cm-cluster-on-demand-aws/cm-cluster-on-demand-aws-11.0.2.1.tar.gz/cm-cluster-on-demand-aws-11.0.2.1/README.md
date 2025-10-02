# Cluster on Demand - AWS

This guide explains how to set up and use Cluster on Demand (COD) with Amazon Web Services (AWS).

## Setting up your AWS account
* Go to https://dlrequest/, search for the group `access-bright-aws-mddev-engineer` and request to join the group.
* You can inform Piotr Wachowicz, Teun Docter or Martijn de Vries about your request. Note that it may take up to one hour for the groups to be synchronized after your account has been added to the group.
* Go to https://www.microsoft365.com/apps/; if required, sign in with NVIDIA SSO.
* Search for `AWS NVIDIA Accounts` and click on the entry. It should forward you to the AWS console home. You can also bookmark [the underlying URL](https://account.activedirectory.windowsazure.com/applications/signin/4fb1a2be-e2a1-4b13-9cca-740ce090659f?tenantId=43083d15-7273-40c1-b7db-39efd9ccc17a) for directly accessing the AWS console.
* Make sure that you see `AWSOS-AD-Engineer/<your-username> @ bright-dev` on the top right
* Select `eu-west-1` (Europe/Ireland) as your region.

## Setting up `cm-cod-aws`
Add the section below to your configuration ini file (in addition to the [general config file settings](/README.md#creating-a-minimal-config-file)).
* You can get the corresponding IDs and password by logging in to [krusty](https://krusty.nvidia.com) and checking out `/cm-setup-configs/trunk.conf`.
* Please be mindful when using the credentials, as those are shared between all BCM engineering team members.
* The `image_owner` field determines which BCM images are available to the cluster. The value is the AWS account ID. There are two account IDs which can be set up here:
  * `137677339600` (default if not set by the user): This is the productive account. It contains all productive images and official BCM releases
  * `197943594779`: This is the development account. It contains `trunk` and `-dev` images. This is what COD developers will likely want to use.
```ini
[aws.credentials]
aws_region=eu-west-1
aws_access_key_id=XYZ
aws_secret_key=XYZ

[aws.cluster.create]
image_owner=197943594779
```
You should now be good to go. Try creating an AWS cluster with `cm-cod-aws cc --name test`.

## Serial Console Access
To access the serial console:
* Go to https://console.aws.amazon.com
* Select the top left menu icon next to AWS and go to "Compute"|"E2C".
* Select "Running instances" and search for your instance. You can then right-click on the entry and select "Monitor and troubleshoot"|"E2C Serial Console".
* In the next dialog, click on "Connect" and you should be presented with a Browser serial console.


## Additional Resources

- [AWS CLI Documentation](https://docs.aws.amazon.com/cli/)
- [AWS IAM Documentation](https://docs.aws.amazon.com/IAM/)
