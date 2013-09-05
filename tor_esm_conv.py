# -*- coding: cp949 -*-
import urllib2
import re
import sys
import datetime, time
 
def torGet():
    try:
        req = urllib2.Request('https://www.dan.me.uk/torlist/')
        req.add_header("Connection", "Keep-Alive")
        req.add_header('User-agent', "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36")
        req.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
        req.add_header('Accept-Language', 'ko-KR,ko;q=0.8,en-US;q=0.6,en;q=0.4')
        url = urllib2.urlopen(req, timeout=100)
        savedata = url.read()
        print savedata
        with open('torip.txt','w') as f:
            f.write(savedata)
        print "저장성공"
    except IOError as e:
        print "접속불가"
        pass
    time.sleep(3)

def getNowDate():
    now    = datetime.datetime.now()
    year   = now.year
    month  = now.month
    day    = now.day
    hour   = now.hour
    minute = now.minute
    nowDate = str(year)+"-"+str(month)+"-"+str(day)
    return nowDate

def saveLog(savedata):
    try:
        filename = str(getNowDate()).replace("-", "") + "_tor_ip.txt"
        with open(filename,'wb') as f:
          f.write(savedata)
          f.close()
    except Exception as inst:
        print inst
        pass

def savefiles():
    saveBlackList = "이름,IP,시작시간,종료시간,비고,블랙리스트 그룹 \n"
    try:
        ipcount = 0
        FH = open("torip.txt", 'r')
        today = str(getNowDate())
        nametor =  today.replace("-", "") + "_토르"
        for line in FH:
            savedata =  nametor +"_" +  str(ipcount) +"," + line.replace("\n", "") +","+ today +"," + "2999-12-31," + "토르IP," + "토르IP대역" + "\n"
            saveBlackList = saveBlackList + savedata
            ipcount = ipcount + 1
        FH.close
    except Exception as inst:
        print inst
        print "심각한 에러발생"
        
    return saveBlackList

if __name__ == '__main__':
    try:
        torGet()
        saveBlackList = savefiles()
        print saveBlackList
        saveLog(saveBlackList)
    except Exception as inst:
        pass
        

  
