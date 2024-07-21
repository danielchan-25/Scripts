import paramiko
from datetime import datetime

# 日期：2024年7月12日
# 功能：下载远程服务器文件到本地

hostname = ''
port = 22
username = ''
password = ''


def main(remote_file_path):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=hostname, port=port, username=username, password=password)
        sftp = ssh.open_sftp()
        sftp.get(remote_file_path, f'./{remote_file_path.split("/", -1)[-1]}')
        sftp.close()
        print(f'{datetime.today().strftime("%Y-%m-%d %H:%M:%S")} - {i} 备份成功!')

    except Exception as e:
        print(f'{datetime.today().strftime("%Y-%m-%d %H:%M:%S")} - 连接出错：{e}')

    finally:
        ssh.close()


if __name__ == '__main__':
    print(f'{datetime.today().strftime("%Y-%m-%d %H:%M:%S")} 备份程序启动')

    today_date = datetime.today().strftime("%Y-%m-%d")
    remote_file_path = [f'/home/ecs-user/memos_{today_date}.tar.gz',
                        f'/home/ecs-user/valutwarden_{today_date}.tar.gz']  # 需要备份的文件

    for i in remote_file_path:
        main(f'{i}')
