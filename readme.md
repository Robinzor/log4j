goto https://log4shell.huntress.com/

click on "view connections"

copy the supplied check_url string:
${jndi:ldap://log4shell.huntress.com:1389/xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx}

goto scan.py replace the "check_url" with yours.

fill "targets.txt" per line with:
ip:port 

run it with:
python3 scan.py

view the Huntress Log4Shell Vulnerability Results
and look if you got a hit on a IP-address.

