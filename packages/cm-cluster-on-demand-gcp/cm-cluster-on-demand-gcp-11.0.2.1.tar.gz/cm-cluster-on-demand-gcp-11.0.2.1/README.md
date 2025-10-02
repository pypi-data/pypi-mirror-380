# Cluster on Demand - Google Cloud Platform

This guide explains how to set up and use Cluster on Demand (COD) with Google Cloud Platform (GCP).

## Setting up your GCP account
* Request your own account via [NVIDIA Security Portal](https://securityportal.nvidia.com) under Cloud OS
* Request access to the shared dev account by joining these groups via [DL Request](https://dlrequest/):
   * `access-bright-dev-gcp-admin`
   * `access-bright-dev-gcp-engineer`
* Verify that you have access to the BCM COD-GCP project by performing the following steps:
   * Open the [GCP console page](https://console.cloud.google.com/).
   * On the top left (right of the "Google Cloud" logo), click on the `Project Picker` (symbol with three dots).
   * Select the organization `nvidia.com` and search for the project `BCM COD-GCP`. Alternatively, you can use the project ID `nv-bcmcodgcp-20240216`.
   * Verify by listing COD compute instances [here](https://console.cloud.google.com/compute/instances).
* Install the GCP CLI on your dev machine for authentication, following the steps described [here](https://cloud.google.com/sdk/docs/install).

## Setting up `cm-cod-gcp`
* Authenticate with GCP:
   ```bash
   # Login with your credentials
   gcloud auth application-default login

   # Set the project
   gcloud config set project nv-bcmcodgcp-20240216

   # Set quota project
   gcloud auth application-default set-quota-project nv-bcmcodgcp-20240216
   ```
   Note: Authentication tokens expire within 24 hours. You'll need to re-run `gcloud auth application-default login` when this happens.

* Add the section below to your configuration ini file (in addition to the [general config file settings](/README.md#creating-a-minimal-config-file)).
   ```ini
   [gcp.common]
   project_id = "nv-bcmcodgcp-20240216"
   # This is the storage bucket which contains the BCM images
   image_blob_uri = "gs://nv-bcm-images-dev"

   [gcp.cluster.create]
   # Cost-optimized machine types, sufficient for daily tasks. More information here:
   # https://cloud.google.com/compute/docs/general-purpose-machines#e2_machine_types
   head_node_type = e2-medium
   node_type = e2-medium
   # europe-west4 is in the Netherlands
   head_node_zone = europe-west4-c
   ```
You should now be good to go. Try creating a GCP cluster with `cm-cod-gcp cc --name test`.

## Serial console access
The serial console can be accessed using the following `gcloud` command (assuming `head_node_zone=europe-west4-c` here, update accordingly):
```
gcloud compute --project=nv-bcmcodgcp-20240216 connect-to-serial-port <head-node-name> --zone=europe-west4-c
```
You can retrieve the head node name for your cluster by running `cm-cod-gcp cluster list`.

### Useful keystrokes when connected to the serial console
After successfully connecting to the serial console, usual control sequences like `ctrl+c` or `ctrl+d` do not work. Instead, you need to press `<return>`, followed by `~` and one of the control characters below to control the console.
```
<hostname> login: ~?
Supported escape sequences:
 ~.   - terminate connection (and any multiplexed sessions)
 ~B   - send a BREAK to the remote system
 ~R   - request rekey
 ~V/v - decrease/increase verbosity (LogLevel)
 ~^Z  - suspend ssh
 ~#   - list forwarded connections
 ~&   - background ssh (when waiting for connections to terminate)
 ~?   - this message
 ~~   - send the escape character by typing it twice
(Note that escapes are only recognized immediately after newline.)
```

## Create Clusters in Existing Network Infrastructure
It is possible to create clusters sharing the same GCP network and subnet.
Use the following cluster creation options for that:
```
--gcp-network-name MY_NETWORK
--gcp-subnet-name MY_SUBNET
```
Deletion of such clusters will only affect resources belonging to the cluster, i.e. won't delete the network/subnet.


## Additional Resources

- [Google Cloud SDK Documentation](https://cloud.google.com/sdk/docs)
- [GCP IAM Documentation](https://cloud.google.com/iam/docs)
