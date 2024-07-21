import time
import subprocess
from dingbot import dingbot_notice

# 日期：2024年7月10日
# 功能：通过跳板机，获取指定服务器的IPV6地址，并通过钉钉告警提醒。
# 注意事项：需要在跳板机上运行这个程序，以下变量是[需要获取IPV6地址的服务器]的信息，而非跳板机信息；跳板机需要先安装 sshpass 命令。


host = '192.168.2.12'
username = 'admin'
password = 'NPw4ks5SP4pdrxdzK9Gc'


def get_ipaddress():
    ''' 获取 IPV6 地址 '''
    command = ["sshpass", "-p", password, "ssh", f"{username}@{host}", "curl", "-s", "test.ipw.cn"]
    # 完整命令：sshpass -p NPw4ks5SP4pdrxdzK9Gc ssh admin@192.168.2.12 curl -s icanhazip.com
    try:
        result = subprocess.check_output(command, stderr=subprocess.STDOUT, universal_newlines=True)
        ip_address = result.strip()
    except subprocess.CalledProcessError as e:
        ip_address = f"Error executing command: {e.output}"
    return ip_address


if __name__ == '__main__':
    old_ip = get_ipaddress()
    while True:
        new_ip = get_ipaddress()
        if new_ip != old_ip:
            dingbot_notice(f'{time.strftime("%Y-%m-%d %H:%M:%S")} - IPV6：{new_ip}')
        time.sleep(60)
