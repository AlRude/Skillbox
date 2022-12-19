import platform
import sys

info = 'OS info is \n{}\n\n Python is {} {}'.format(
    platform.uname(), sys.version, platform.architecture())

print(info)

with open('os_info.txt', 'w') as file:
    file.write(info)