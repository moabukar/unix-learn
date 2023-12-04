# SSH not working

## Scenario

You are a DevOps Engineer working on a remote server infrastructure. Recently, you've encountered an issue where you cannot establish an SSH connection to one of your critical servers. This server hosts several key applications and its inaccessibility is causing operational delays. You suspect a few potential issues but need to systematically troubleshoot to identify the root cause.

## Question 

As a DevOps Engineer, you are tasked with resolving an SSH connectivity issue to a critical server. Your initial attempts to connect via SSH have failed, and you need to diagnose and fix the problem to regain access. What do you do and where do you start?

## Example Solution

Click the right arrow to view the answers

<details>
<summary>Solution</summary>

1) **Check the network connection**: Make sure that the server is connected to the network and that it has an active internet connection.<br><br>

2) **Check the SSH service**: Make sure that the SSH service is running on the server. You can check the status of the SSH service using the following command:
**systemctl status ssh**<br><br>


3. Check the firewall: Make sure that the firewall on the server is not blocking incoming SSH connections. You can check the firewall rules using the following command:
**iptables -L**<br><br>

4. **Check the IP address**: Make sure that you are using the correct IP address or hostname to connect to the server. You can check the server's IP address using the ifconfig command.<br><br>

5) **Check the SSH configuration**: Make sure that the SSH configuration on the server is set up correctly. You can check the SSH configuration file (usually located at /etc/ssh/sshd_config) for any issues.<br><br>

6) **Check the log files**: The log files (usually located in the /var/log directory) can often provide valuable information about why an SSH connection is not working. Look for any error messages related to SSH in the log files.<br><br>

7) **Disk was full so user could not use it**<br><br>

8) **ran out of inodes (cant allocation anymore due to disk full)**<br><br>

</details>
