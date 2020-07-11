from threading import Thread
from queue import Queue
import requests
from time import time
import argparse

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
}


def ping(url, new_ip):
    url = url.strip()
    if (not url.startswith('http://')) and (not url.startswith('https://')):
        url = 'http://' + url
    try:
        req = requests.get(url, headers=headers, timeout=2)
        new_ip.put(url + '  --  ' + str(req.status_code))
        print("%s 存活" % url)
    except:
        print("%s 不存活" % url)


def new_list(file):
    with open(file, 'r') as f:
        new_ip = []
        ip_list = f.readlines()
        for ip in ip_list:
            # print(ip)
            ip = ip.strip().replace('http://', '').replace('https://', '')
            # print(ip)
            if ip:
                if not (ip in new_ip):
                    new_ip.append(ip)
        return new_ip


def main(file, th):
    begin_time = time()
    new_ip = Queue()
    ip_list = new_list(file)
    j = 0
    length = len(ip_list)
    print(length)
    while j < length:
        print(j)
        threads = []
        for i in range(th):
            t = Thread(target=ping, args=(ip_list[j], new_ip))
            t.start()
            threads.append(t)
            j += 1
            if j == length:
                break
        for thread in threads:
            thread.join()
    with open('NewIP.txt', 'a+') as nf:
        while not new_ip.empty():
            nf.write(new_ip.get()+'\n')
    end_time = time()
    run_time = end_time - begin_time
    print("总共耗时 %s 秒"% run_time)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='generate payload of gopher attack mysql')
    parser.add_argument("-f", "--file", help="指定文件", default='testip.txt')
    parser.add_argument("-t", "--thread", help="设置线程", default=50)
    args = parser.parse_args()
    file = args.file
    th = args.thread
    main(file, th)
