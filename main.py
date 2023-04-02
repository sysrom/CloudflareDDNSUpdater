import requests
import time
import CloudFlare
import datetime

Record_name=""#记录明加域 例如域是sysrom.xyz 记录名是test 此处就填test.sysrom.xyz
Cloudflare_Token=""#你觉得这是什么就是什么别问我
Cloudflare_Zone_ID=""#区域ID
IPAddress=""#填了就傻逼

def GetTime():
  return datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')

def main():
    IPAddress=requests.get("https://ifconfig.me/ip").text
    print(f"[Info][{GetTime()}]First Get IPAddr:{IPAddress}")
    if(Cloudflare_Token==None or Cloudflare_Token=="" or Cloudflare_Zone_ID==None or Cloudflare_Zone_ID==""):
        print("CloudFlare Token/ZoneID没填写初始化个毛线")
        exit(1)
    cf = CloudFlare.CloudFlare(token=Cloudflare_Token)
    while(True):
        Dns_Records = cf.zones.dns_records.get(Cloudflare_Zone_ID, params={'name': Record_name, 'type': 'A'})
        if len(Dns_Records) == 0:
            print(f"[Error][{GetTime()}]你妈妈的吻没这个记录")
            exit(1)
        Dns_Record = Dns_Records[0]
        Dns_Record_ID = Dns_Record['id']
        Dns_Record_Value = Dns_Record['content']
        if Dns_Record_Value != IPAddress:
            print(f"[Info][{GetTime()}]{Record_name}==>{IPAddress}")
            Dns_Record['content'] = IPAddress
            cf.zones.dns_records.put(Cloudflare_Zone_ID, Dns_Record_ID, data=Dns_Record)
        time.sleep(20)#呐 这里是每次检测IP的间隔 以秒为单位

if __name__ == '__main__':
    main()