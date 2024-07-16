import wmi
import time

# 日期：2024-07-16
# 功能：磁盘 Smart 状态检测

if __name__ == "__main__":
    now_time = f'{time.strftime("%Y-%m-%d %H:%M:%S")}'
    device_data = wmi.WMI()
    for i in device_data.Win32_DiskDrive():
        print(f'{now_time} - {int(i.Size) / (1024 ** 3):.2f}GB 磁盘 Smart 状态：{i.Status}')
