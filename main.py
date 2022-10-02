# coding: utf-8
# Author：quzard
from leave import *
import sys, os
from time import sleep
from numpy import random
import argparse

# if "USERNAME" in os.environ:
#     username = os.environ["USERNAME"]
# else:
#     print("未找到 ID")
#     sys.exit(1)

# if "PASSWORD" in os.environ:
#     password = os.environ["PASSWORD"]
# else:
#     print("未找到 PASSWORD")
#     sys.exit(1)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Test for argparse')
    parser.add_argument('--user', '-u', help='一卡通号', default='')
    parser.add_argument('--password', '-p', help='密码', default='')
    args = parser.parse_args()
    if args.user != '' and args.password != '':
        username = args.user
        password = args.password
    else:
        print("未找到 ID and PASSWORD")
        sys.exit(1)
    try:
        sleep(random.uniform(5, 15))
        leave = Leave(username, password, "./")
        res = leave.do_report()
        print(res)
        if "请假成功" not in res:
            sys.exit(1)
    except Exception as e:
        print(str(e))
        sys.exit(1)
