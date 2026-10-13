#! /usr/bin/env python3
"""sysinfo - print basic system details"""

import platform
import socket
import psutil
import argparse
import json


def get_basic_info():
    return {
        "Hostname": socket.gethostname(),
        "OS": platform.system(),
        "OS Release":platform.release(),
        "Architecture": platform.machine(),
        "Python Version": platform.python_version(),


    }

def get_cpu_info():
    return {
        "Physical cores": psutil.cpu_count(logical=False),
        "Logical cores": psutil.cpu_count(logical=True),
        "CPU usage": f"{psutil.cpu_percent(interval=1)}%"
    }

def get_disk_info():
    info = {}
    gb = 1024**3
    for part in psutil.disk_partitions():
        try:
            usage = psutil.disk_usage(part.mountpoint)
        except PermissionError:
            continue
        info[part.mountpoint]=(
            f"{usage.used / gb:.1f}/{usage.total / gb:.1f} GB ({usage.percent}%)" 
            )
    return info

def get_network_info():
    info = {}
    for name, addrs in psutil.net_if_addrs().items():
        for addr in addrs:
            if addr.family == socket.AF_INET:
                info[name]= addr.address
    return info

def collect_all():
    return {
        "System" : get_basic_info(),
        "CPU" : get_cpu_info(),
        "Memory" : get_disk_info(),
        "Network" : get_network_info(),
    
    }



def print_section(title,data):
    print(f"\n==={title}===")
    for key,value in data.items():
        print(f"{key:<16}: {value}")

def main():
    parser = argparse.ArgumentParser(description="Print system details")
    parser.add_argument("--json", action="store_true" , help= "output JSON")
    args= parser.parse_args()

    data = collect_all()
    if args.json:
        print(json.dumps(data,indent=2))

    else:
        for title,section in data.items():
            print_section(title,section)
   # print_section("System",get_basic_info())
    #print_section("CPU",get_cpu_info())
    #print_section("Disks",get_disk_info())
    #print_section("Networks",get_network_info())
    



if __name__=="__main__":
     main()        