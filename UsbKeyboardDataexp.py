# 说明
# 若显示的是 HID Data
#  -e usbhid.data 
# 若显示的是 Leftover Capture Data
#  -e usb.capdata 

import sys, argparse, os


def tshark_do(pcapfile, filterfield, fieldvalue, datafile):
    if os.name == "nt":
        if filterfield is not None:
            command = f"tshark -r {pcapfile} -Y {filterfield} -T fields -e {fieldvalue} > {datafile}"
        else:
            command = f"tshark -r {pcapfile} -T fields -e {fieldvalue} > {datafile}"
        try:
            os.system(command)
            print("tshark执行语句：" + command)
            print("[+] Found : tshark导出数据成功")
        except:
            print("tshark执行语句：" + command)
            print("[+] Found : tshark导出数据失败")
        
    elif os.name == "posix":
        #sed '/^\s*$/d' 主要是去掉空行
        if filterfield not in None:
            command = f"tshark -r {pcapfile} -Y {filterfield} -T fields -e {fieldvalue} | sed '/^\s*$/d' > {datafile}"
        else:
            command = f"tshark -r {pcapfile} -T fields -e {fieldvalue} | sed '/^\s*$/d' > {datafile}"
        
        try:
            os.system(command)
            print("tshark执行语句：" + command)
            print("[+] Found : tshark导出数据成功")
        except:
            print("tshark执行语句：" + command)
            print("[+] Found : tshark导出数据失败")

def jiemi(DataFile):
    print("\n-----开始解密Tshark导出的键盘数据-----\n")
    # 读取数据z
    with open(DataFile, "r") as f:
        for line in f:
            presses.append(line[0:-1]) #去掉末尾的\n
    # 开始处理
    result = []
    for press in presses:
        if press == '':
            continue
        #thark版本原因，导出数据格式不同
        if ':' in press:
            Bytes = press.split(":")
        else:
            #两两分组
            Bytes = [press[i:i+2] for i in range(0, len(press), 2)]
            # print(Bytes)
        if Bytes[0] == "00":
            if Bytes[2] != "00" and normalKeys.get(Bytes[2]):
                result.append(normalKeys[Bytes[2]])
                # print(result)
        elif int(Bytes[0],16) & 0b10 or int(Bytes[0],16) & 0b100000: # shift key is pressed.
            if Bytes[2] != "00" and normalKeys.get(Bytes[2]):
                 result.append(normalKeys[Bytes[2]])
        else:
            print("[-] Unknow Key : %s" % (Bytes[0]))
    print("[+] USB_Found : %s" % (result))
    # print(type(result))

    flag = 0
    for i in range(len(result)):
        try:
            a = result.index('<DEL>')
            del result[a]
            del result[a - 1]
        except:
            pass

    for i in range(len(result)):
        try:
            if result[i] == "<CAP>":
                flag += 1
                result.pop(i)
                if flag == 2:
                    flag = 0
            if flag != 0:
                result[i] = result[i].upper()
        except:
            pass
    
    print('\n[+] 键盘数据output :' + "".join(result))

    # 删除提取数据文件
    rm_stat = eval(input(f"-----是否删除tshark导出的文件 \"{datafile}\", 1 or 0-----\n"))
    if rm_stat == 1:
        os.remove(DataFile)



if __name__ == "__main__":

    argobject = argparse.ArgumentParser(prog="UsbKeyboardExp", description="""This is a tool for decrypt UsbKeyboardData
    """)

    argobject.add_argument('-f', "--pcapfile", required=True, help="here is your capturedata file")
    argobject.add_argument('-e', "--fieldvalue", required=True, help="here is your output_format")
    argobject.add_argument('-Y', "--filterfield", help="here is your filter")

    arg = argobject.parse_args()    

    #Keyboard Traffic Dictionary
    normalKeys = {"04":"a", "05":"b", "06":"c", "07":"d", "08":"e", "09":"f", "0a":"g", "0b":"h", "0c":"i", "0d":"j", "0e":"k", "0f":"l", "10":"m", "11":"n", "12":"o", "13":"p", "14":"q", "15":"r", "16":"s", "17":"t", "18":"u", "19":"v", "1a":"w", "1b":"x", "1c":"y", "1d":"z","1e":"1", "1f":"2", "20":"3", "21":"4", "22":"5", "23":"6","24":"7","25":"8","26":"9","27":"0","28":"<RET>","29":"<ESC>","2a":"<DEL>", "2b":"\t","2c":"<SPACE>","2d":"-","2e":"=","2f":"[","30":"]","31":"\\","32":"<NON>","33":";","34":"'","35":"<GA>","36":",","37":".","38":"/","39":"<CAP>","3a":"<F1>","3b":"<F2>", "3c":"<F3>","3d":"<F4>","3e":"<F5>","3f":"<F6>","40":"<F7>","41":"<F8>","42":"<F9>","43":"<F10>","44":"<F11>","45":"<F12>"}

    #Press shift 
    shiftKeys = {"04":"A", "05":"B", "06":"C", "07":"D", "08":"E", "09":"F", "0a":"G", "0b":"H", "0c":"I", "0d":"J", "0e":"K", "0f":"L", "10":"M", "11":"N", "12":"O", "13":"P", "14":"Q", "15":"R", "16":"S", "17":"T", "18":"U", "19":"V", "1a":"W", "1b":"X", "1c":"Y", "1d":"Z","1e":"!", "1f":"@", "20":"#", "21":"$", "22":"%", "23":"^","24":"&","25":"*","26":"(","27":")","28":"<RET>","29":"<ESC>","2a":"<DEL>", "2b":"\t","2c":"<SPACE>","2d":"_","2e":"+","2f":"{","30":"}","31":"|","32":"<NON>","33":"\"","34":":","35":"<GA>","36":"<","37":">","38":"?","39":"<CAP>","3a":"<F1>","3b":"<F2>", "3c":"<F3>","3d":"<F4>","3e":"<F5>","3f":"<F6>","40":"<F7>","41":"<F8>","42":"<F9>","43":"<F10>","44":"<F11>","45":"<F12>"}

    #我的vscode工作区的原因，需要切换到当前目录
    pwd = os.path.dirname(__file__)
    os.chdir(pwd)


    #tshark导出文件
    datafile="usbdatafile.txt"
    presses= []
    
    # tshark导出数据，存储在usbdatafile.txt内
    tshark_do(pcapfile=arg.pcapfile, filterfield=arg.filterfield, fieldvalue=arg.fieldvalue, datafile=datafile)

    #解密流量文件
    jiemi(DataFile=datafile)  
