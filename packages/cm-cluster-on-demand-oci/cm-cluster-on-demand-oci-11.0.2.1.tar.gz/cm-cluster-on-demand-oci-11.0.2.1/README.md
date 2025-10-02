# Cluster on Demand - Oracle Cloud Infrastructure

This guide explains how to set up and use Cluster on Demand (COD) with Oracle Cloud Infrastructure (OCI).

## Setting up your OCI account
* Go to https://dlrequest/, and request to join the following groups:
  * `access-oci-ngcnonprod-bcm-admin`
  * `access-oci-nvidiamain-bcm-admin`
* You can inform Teun Docter or Martijn de Vries about your request. Note that it may take up to one hour for the groups to be synchronized after your account has been added to the group.
* Go to https://www.oracle.com/cloud/sign-in.html and use the Cloud Account name `nvidiangcnonprd`. Click "Next".
* Select the `Default` identity domain. Click "Next".
* Do _not_ use a username/password, click on `Sign in with nvidiaprimary` below instead.
* You should now be logged in to the OCI console with tenancy `nvidiangcnonprd`.
* Select `Netherlands Northwest (Amsterdam)` as your region.

## Setting up `cm-cod-oci`
Add the section below to your configuration ini file (in addition to the [general config file settings](/README.md#creating-a-minimal-config-file)).
* For detailed configuration steps, refer to section 2.2.3 of the [Cloudbursting Manual](https://support.brightcomputing.com/manuals/11/cloudbursting-manual.pdf#page=13). It will guide you through the OCI ini creation and credentials setup. It will also enable you to fill in the values below.

**Important:** The `image_compartment_id` may differ from your main OCI compartment ID. BCM developers should use images from the `nvidiangcnonprd/bcmnonprod/ci` compartment. The correct OCID can be found in [`krusty.ini`](../cluster-on-demand/clusterondemand/krusty.ini#lines-202). If you previously ran the `make use-bcm-cfgs` command, this should already be configured for you.
```ini
[oci.cluster.common]
oci_compartment_id=XYZ

[oci.credentials]
oci_user=XYZ
oci_fingerprint=XYZ
oci_tenancy=XYZ
oci_region=eu-amsterdam-1
oci_key_file=/path/to/your/key.pem

[oci.images.find]
image_compartment_id=XYZ
```

You should now be good to go. Try creating an OCI cluster with `cm-cod-oci cc --name test`.

## Serial Console Access
* Log in to the OCI console: https://cloud.oracle.com/
* Search for the compute instance you want to have serial console access to
* After selecting the instance, go to the `OS Management` tab
* Scroll down. Under `Console connection`, click on `Create local connection`.
* Upload/paste your public key and click on `Create console connection`
* After the connection has been created (is in `Active` state), click on the three dots on the right side and select `Copy serial console for Linux/Mac` from the menu
* You should be able to connect to the serial console using the copied `ssh` command string.
* *Troubleshooting*: Should the command fail with an error like this:
  ```
  Unable to negotiate with UNKNOWN port 65535: no matching host key type found. Their offer: ssh-rsa
  ```
  append the following options to your command `-o HostKeyAlgorithms=+ssh-rsa -o PubkeyAcceptedAlgorithms=+ssh-rsa`.

### Useful keystrokes when connected to the serial console
After successfully connecting via SSH to the serial console, usual control sequences like `ctrl+c` or `ctrl+d` do not work. Instead, you need to press `<return>`, followed by `~` and one of the control characters below to control the console.
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

## Additional Resources

- [OCI CLI Documentation](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/cliconcepts.htm)
- [OCI IAM Documentation](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/overview.htm)
