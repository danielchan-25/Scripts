import hmac
import hashlib
import base64
import urllib.parse
import requests
import json
import time
import psutil
import logging

# ------------------------------------- #
# 日期：2023-08-01
# 作者：陈某
# 功能：检测某些进程是否运行，通过钉钉告警
# ------------------------------------- #

api_url = 'https://oapi.dingtalk.com/robot/send?access_token='  # 钉钉机器人access_token
api_secret = ''  # 钉钉机器人加签
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger()


def get_timestamp_sign():
    timestamp = str(round(time.time() * 1000))
    secret = api_secret
    secret_enc = secret.encode('utf-8')
    string_to_sign = '{}\n{}'.format(timestamp, secret)
    string_to_sign_enc = string_to_sign.encode('utf-8')
    hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
    sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
    return timestamp, sign

def get_signed_url():
    timestamp, sign = get_timestamp_sign()
    webhook = api_url + "&timestamp=" + timestamp + "&sign=" + sign
    return webhook

def get_webhook(mode):
    if mode == 0: 
        webhook = api_url
    elif mode == 1 or mode == 2:
        webhook = get_signed_url()
    else:
        webhook = ""
        print("error! mode:   ", mode, "  webhook :  ", webhook)
    return webhook

def get_message(text, user_info):
    # 和类型相对应，具体可以看文档 ：https://ding-doc.dingtalk.com/doc#/serverapi2/qf2nxq
    message = {
        "msgtype": "text",
        "text": {
            "content": text
        },
        "at": {
            "atMobiles": [
                user_info,
            ],
            "isAtAll": False
        }
    }
    return message

def send_ding_message(text, user_info):
    webhook = get_webhook(1)
    header = {
        "Content-Type": "application/json",
        "Charset": "UTF-8"
    }
    message = get_message(text, user_info)
    message_json = json.dumps(message)
    info = requests.post(url=webhook, data=message_json, headers=header).json()
    code = info["errcode"]
    errmsg = info["errmsg"]

def check_process(process_name):
    for process in psutil.process_iter(['pid', 'cmdline']):
        cmdline = process.info.get('cmdline')
        if cmdline is not None and process_name in cmdline:
            return True
    return False

if __name__ == "__main__":
    user_info = ''  # 钉钉绑定的手机号码
    process_names = ["py.py"]  # 进程名
    while True:
        for process_name in process_names:
            if check_process(process_name):
                logger.info(f"进程 {process_name} 正在运行.")
            else:
                text = f"进程 {process_name} 未运行."
                logger.error(f"进程 {process_name} 未运行.")
                send_ding_message(text, user_info)
        time.sleep(60)
