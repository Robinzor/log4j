Requirements:
- curl
- python3 

##### 1. Go to https://log4shell.huntress.com/

##### 2. Click on "view connections"

##### 3. Copy the supplied check_url string:
${jndi:ldap://log4shell.huntress.com:1389/xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx}

##### 4. Goto scan.py replace the "check_url" with yours.

##### 5. Fill "targets.txt" per line with:
ip:port 

##### 6. run it with:

(txt file import)\
**python3 scan.py**

(commandline args)\
**python3 scan.py 192.168.0.1:80**

**python3 scan.py 192.168.0.1:80 - 254**

View the Huntress Log4Shell Vulnerability Results
and look if you got a hit on a IP-address.

