# ActiveOrNot

## 有什么用
* 用于处理 oneforall 等子域名扫描工具的结果去重 + 主机存活扫描

## 没什么用
* 参数
```
-f   --file       指定存放ip或子域名的文件，默认 ip.txt
-t   --thread     设置线程数，默认 50

python3 ActiveOrNot.py -f ip.txt -t 12
```
