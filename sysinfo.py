#! /usr/bin/env python3
"""sysinfo - print basic system details"""

import platform
import socket

def get_basic_info():
    return {
        "Hostname": socket.gethostname(),
        "OS": platform.system(),
        "OS Release":platform.release(),
        "Architecture": platform.machine(),
        "Python Version": platform.python_version(),


    }

def main():
    print("====System Information====")
    for key, value in get_basic_info().items():
        print(f"{key:<16}: {value}")



if __name__=="__main__":
     main()        