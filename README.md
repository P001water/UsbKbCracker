# readme
把tshark的`-e`（导出协议字段）放在了python 命令行参数里，适用下面两种情况灵活选择

若显示的是 HID Data

 -e usbhid.data 
 
若显示的是 Leftover Capture Data

 -e usb.capdata 


![image.png](https://cdn.nlark.com/yuque/0/2022/png/22999319/1666406713922-5845c661-5110-4db9-9f1f-20d9ba4ecc2c.png#clientId=u78cc44cc-1f9a-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=123&id=uaae84650&margin=%5Bobject%20Object%5D&name=image.png&originHeight=184&originWidth=1427&originalType=binary&ratio=1&rotation=0&showTitle=false&size=7127&status=done&style=none&taskId=uaa8bf6e7-6cd7-48d5-ae4c-ec635a02290&title=&width=951.3333333333334)
![image.png](https://cdn.nlark.com/yuque/0/2022/png/22999319/1666406758507-3a7f0d00-5239-4ec4-a2d5-37d46d43be33.png#clientId=u78cc44cc-1f9a-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=89&id=u1ccdf4d3&margin=%5Bobject%20Object%5D&name=image.png&originHeight=133&originWidth=1414&originalType=binary&ratio=1&rotation=0&showTitle=false&size=6979&status=done&style=none&taskId=ueee1e5ce-399e-46e7-8ea9-5ba43997344&title=&width=942.6666666666666)

# Usage

- windows下使用把wireshark文件夹下的tshark放在环境变量里，起码这样

![image.png](https://cdn.nlark.com/yuque/0/2022/png/22999319/1666019085482-971c800f-9b78-465b-a227-48389c87e7a7.png#clientId=u89c5a77b-7f55-4&crop=0&crop=0&crop=1&crop=1&errorMessage=unknown%20error&from=paste&height=231&id=Sh36P&margin=%5Bobject%20Object%5D&name=image.png&originHeight=453&originWidth=959&originalType=binary&ratio=1&rotation=0&showTitle=false&size=191036&status=error&style=none&taskId=u3b7169c6-0109-4700-855a-9ff894fdb63&title=&width=488.3333740234375)

- linux下别忘了`sudo apt-get install tshark`，安装tshark

```
Usage : 
        python UsbKeyboardDataexp.py -f pcapfile -e fieldvalue [-Y "xxx"]
        `-f` 流量文件
        `-Y` 过滤器条件[选项可选]
        `-e` 导出协议字段
```

# example
example里面是三个样本，ez_usb是一道题目，其他两个名文件名分别是`-e`导出协议字段名的选项
`-Y`就是wireshark里的过滤器的过滤条件
```python
python .\UsbKeyboardDataexp.py -f .\example\ez_usb.pcapng -e usbhid.data -Y "usb.src==2.8.1"
其他同理
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/22999319/1666407584389-fa87f236-2458-4bb5-85ec-183d602d6858.png#clientId=u78cc44cc-1f9a-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=369&id=u4d64997f&margin=%5Bobject%20Object%5D&name=image.png&originHeight=1167&originWidth=1918&originalType=binary&ratio=1&rotation=0&showTitle=false&size=953266&status=done&style=none&taskId=uae6cea18-04fe-4d8e-acee-547e04c9974&title=&width=607)


# Acknowledgment
@WangYihang
