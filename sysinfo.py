#! /usr/bin/env python3
"""sysinfo - print basic system details"""

import platform
import socket
import psutil

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

def print_section(title,data):
    print(f"\n==={title}===")
    for key,value in data.items():
        print(f"{key:<16}: {value}")

def main():
    print_section("System",get_basic_info())
    print_section("CPU",get_cpu_info())
    print_section("Disks",get_disk_info())
    



if __name__=="__main__":
     main()        