# -*- coding: utf-8 -*-

#Heracles Project
from PIL import Image, ImageOps
import math
import os
import sys
import cv2
import numpy
import subprocess
숫자넘버 = 1

#전체 스크롤을 하고 세이프 에리어 있는 버전.

width = 640
height = 480
fourcc = cv2.VideoWriter_fourcc(*'LJPG')
video = cv2.VideoWriter("innet.mkv", fourcc, 59.94,(width,height))

바이미지 = cv2.imread('data/bar.png')

for i in range(1, 901): #시작이미지
    video.write(바이미지)
    숫자넘버 = 숫자넘버 + 1
                            
dirname="./in"
#try:
filenames = os.listdir(dirname)
풀가로길이 = 0
풀세로길이 = 0
가로스위치 = 0
첫스위치 = 0
가로싱글스위치 = 0
for filename in filenames:
    full_filename = os.path.join(dirname, filename)
    if os.path.isdir(full_filename):
        search(full_filename)
    else:
        ext = os.path.splitext(full_filename)[-1]
        if ext == '.png' or ext == '.jpg' or ext == '.jpeg' or ext == '.PNG' or ext == '.JPG' or ext == '.JPEG': 
            rtx=full_filename
            print(rtx)
            초기파일위치 = os.getcwd()
            파일경로가제거된파일명 = os.path.basename(rtx)
            적당히잘린파일명 = os.path.splitext(파일경로가제거된파일명)
            확장자가제거된파일명 = 적당히잘린파일명[0]
                
            잘라질이미지 = Image.open(rtx) 
            가로길이 = 잘라질이미지.size[0]
            세로길이 = 잘라질이미지.size[1]
            print(str(가로길이)+'/'+str(세로길이))
            진짜잘라질이미지=잘라질이미지
            
            if 세로길이 // 가로길이 < 1 and 가로길이 >= 640:  # 가로 모드
                if 가로스위치 == 2 : # 중간 세로처리
                    print('중간세로사진커팅중')
                    뉴뉴세로길이 = round(풀세로길이+64)   
                    풀세로길이 = 뉴뉴세로길이
                    댕강댕강이미지=ImageOps.pad(풀이미지, (576,풀세로길이), 5, 'black') #상하 세이프존 설정
                    뉴댕강댕강이미지=ImageOps.pad(댕강댕강이미지, (640,풀세로길이), 5, 'black') #좌우 세이프존 설정
                    잘라질이미지 = 뉴댕강댕강이미지
                    
                    if 첫스위치 != 0 :
                        이것도가로길이 = 잘라질이미지.size[0]
                        이것도세로길이 = 잘라질이미지.size[1]
                        캔버스 = Image.new('RGB', (640, 이것도세로길이+448), 'black')
                        캔버스.paste(잘라질이미지, (0,448))
                        캔버스.paste(이전잘린이미지, (0, 0))
                        잘라질이미지=캔버스
                        풀세로길이=풀세로길이+448  
  
                    if math.ceil((풀세로길이-478)/2) < 0 :
                        한번더=ImageOps.pad(잘라질이미지, (640,480), 5, 'black')
                        for i in range(1, 121):
                            video.write(cv2.cvtColor(numpy.array(한번더), cv2.COLOR_RGB2BGR))
                            숫자넘버 = 숫자넘버 + 1
                    elif 풀세로길이 > 550 :
                        반복을시작하지=range(1,math.ceil((풀세로길이-478)/2+1)) #가운대 2개 int의 합이 480이 될것
                        for 반복함수 in 반복을시작하지:
                            윗컷팅함수=반복함수*2-2 #int의 합이 0이 될것
                            아랫커팅함수=반복함수*2+478 #int의 합이 480이 될것
                            if 아랫커팅함수 >= 풀세로길이:
                                윗컷팅함수 = 풀세로길이-480
                                아랫커팅함수 = 풀세로길이
                                잘린이미지=잘라질이미지.crop((0, 윗컷팅함수, 640, 아랫커팅함수))
                                이전잘린이미지=잘린이미지
                                video.write(cv2.cvtColor(numpy.array(잘린이미지), cv2.COLOR_BGR2RGB))
                                숫자넘버 = 숫자넘버 + 1
                            elif 윗컷팅함수 == 0 and 첫스위치 == 0:
                                잘린이미지=잘라질이미지.crop((0, 윗컷팅함수, 640, 아랫커팅함수))
                                for i in range(1, 61):
                                    video.write(cv2.cvtColor(numpy.array(잘린이미지), cv2.COLOR_BGR2RGB))
                                    숫자넘버 = 숫자넘버 + 1                            
                            elif 윗컷팅함수 == 0:
                                잘린이미지=잘라질이미지.crop((0, 윗컷팅함수, 640, 아랫커팅함수))
                                video.write(cv2.cvtColor(numpy.array(잘린이미지), cv2.COLOR_BGR2RGB))
                                숫자넘버 = 숫자넘버 + 1
                            else :
                                잘린이미지=잘라질이미지.crop((0, 윗컷팅함수, 640, 아랫커팅함수))
                                video.write(cv2.cvtColor(numpy.array(잘린이미지), cv2.COLOR_BGR2RGB))
                                숫자넘버 = 숫자넘버 + 1
                    else :
                        한번더=ImageOps.pad(잘라질이미지, (640,480), 5, 'black')
                        for i in range(1, 121):
                            video.write(cv2.cvtColor(numpy.array(한번더), cv2.COLOR_RGB2BGR))
                            숫자넘버 = 숫자넘버 + 1                       
                    풀가로길이 = 0
                    풀세로길이 = 0
                    
                    
                    가가로길이 = 풀이미지.size[0]
                    세세로길이 = 풀이미지.size[1]
                    앞이미지 = 풀이미지.crop((0, 세세로길이-480, 640, 세세로길이))
                    첫스위치=첫스위치+1 
                    
                가로스위치 = 1
                
                잘라질이미지 = 진짜잘라질이미지
                뉴가로길이 = round(가로길이*(416/세로길이))
                뉴세로길이 = 416
                
                print(str(뉴가로길이)+'/'+str(뉴세로길이))

                if 세로길이 >= 416 :
                    잘라질이미지.thumbnail((뉴가로길이,416))
                else :
                    커진이미지 = 잘라질이미지.resize((뉴가로길이,416),5)
                    잘라질이미지 = 커진이미지               
                canvas = Image.new('RGB', (풀가로길이+뉴가로길이+10, 416), 'black')
                
                
                if 풀가로길이 == 0 :
                    canvas.paste(잘라질이미지, (0, 0))
                    풀가로길이 = 뉴가로길이
                else   :
                    canvas.paste(풀이미지, (뉴가로길이+10, 0))
                    canvas.paste(잘라질이미지, (0, 0))
                    풀가로길이 = 풀가로길이 + 뉴가로길이 + 10 
                풀이미지 = canvas
                가로싱글스위치 = 가로싱글스위치+1
            
            else :    # 세로 모드
                if 가로스위치 == 1 : # 중간 가로처리
                    print('중간가로사진커팅중')
                    뉴뉴가로길이 = round(풀가로길이+64)   
                    풀가로길이 = 뉴뉴가로길이
                    댕강댕강이미지=ImageOps.pad(풀이미지, (풀가로길이,416), 5, 'black') #상하 세이프존 설정
                    뉴댕강댕강이미지=ImageOps.pad(댕강댕강이미지, (풀가로길이,480), 5, 'black') #좌우 세이프존 설정
                    잘라질이미지 = 뉴댕강댕강이미지 
                    
                    if 첫스위치 != 0 :
                        이것도가로길이 = 잘라질이미지.size[0]
                        이것도세로길이 = 잘라질이미지.size[1]
                        캔버스 = Image.new('RGB', (608 + 이것도가로길이, 480), 'black')
                        캔버스.paste(잘라질이미지, (0,0))
                        캔버스.paste(이전잘린이미지, (이것도가로길이-32, 0))
                        풀가로길이=풀가로길이+608
                        잘라질이미지=캔버스
                    if 가로싱글스위치 == 1 :
                        나도가로길이 = 잘라질이미지.size[0]
                        나도세로길이 = 잘라질이미지.size[1]
                        캔버스1 = Image.new('RGB', (5 + 나도가로길이, 480), 'black')
                        캔버스1.paste(잘라질이미지, (5,0))
                        잘라질이미지=캔버스1
                    #잘라질이미지.save(str(숫자넘버)+'longtest22.png', "PNG")
                    반복을시작하지=range(math.ceil((풀가로길이-638)/2+1),1,-1) #가운대 2개 int의 합이 640이 될것
                    for 반복함수 in 반복을시작하지:
                        윗컷팅함수=반복함수*2-2-2 #int의 합이 0이 될것?
                        아랫커팅함수=반복함수*2+638-2 #int의 합이 640이 될것
                        #print(str(윗컷팅함수)+'x'+str(아랫커팅함수))
                        if 윗컷팅함수 == 0 :
                            잘린이미지=잘라질이미지.crop((윗컷팅함수, 0, 아랫커팅함수, 480))
                            이전잘린이미지=잘린이미지
                            #이전잘린이미지.save(str(숫자넘버)+'longtest30.png', "PNG")
                            video.write(cv2.cvtColor(numpy.array(잘린이미지), cv2.COLOR_BGR2RGB))
                            숫자넘버 = 숫자넘버 + 1
                        elif 윗컷팅함수 == 반복을시작하지 and 첫스위치 == 0:
                            잘린이미지=잘라질이미지.crop((윗컷팅함수, 0, 아랫커팅함수, 480))
                            for i in range(1, 61):
                                video.write(cv2.cvtColor(numpy.array(잘린이미지), cv2.COLOR_BGR2RGB))
                                숫자넘버 = 숫자넘버 + 1
                        elif 윗컷팅함수 == 반복을시작하지 :
                            잘린이미지=잘라질이미지.crop((윗컷팅함수, 0, 아랫커팅함수, 480))
                            video.write(cv2.cvtColor(numpy.array(잘린이미지), cv2.COLOR_BGR2RGB))
                            숫자넘버 = 숫자넘버 + 1                                
                        else :
                            잘린이미지=잘라질이미지.crop((윗컷팅함수, 0, 아랫커팅함수, 480))
                            video.write(cv2.cvtColor(numpy.array(잘린이미지), cv2.COLOR_BGR2RGB))
                            숫자넘버 = 숫자넘버 + 1
                    풀가로길이 = 0
                    풀세로길이 = 0
                    가가로길이 = 풀이미지.size[0]
                    세세로길이 = 풀이미지.size[1]
                    앞이미지 = 풀이미지.crop((가가로길이-480, 0, 가가로길이, 480))
                    첫스위치=첫스위치+1
                    가로싱글스위치=0
                가로스위치 = 2
                잘라질이미지 = 진짜잘라질이미지
                뉴가로길이 = 576
                뉴세로길이 = round(세로길이*(576/가로길이))
                
                print(str(뉴가로길이)+'/'+str(뉴세로길이))

                if 가로길이 >= 576 :
                    잘라질이미지.thumbnail((576,뉴세로길이))
                else :
                    커진이미지 = 잘라질이미지.resize((576,뉴세로길이),5)
                    잘라질이미지 = 커진이미지
                canvas = Image.new('RGB', (576, 풀세로길이+뉴세로길이+10), 'black')
                if 풀세로길이 == 0 :
                    canvas.paste(잘라질이미지, (0, 0))
                    풀세로길이 = 뉴세로길이
                else   :
                    canvas.paste(풀이미지, (0, 0))
                    canvas.paste(잘라질이미지, (0, 풀세로길이+10))
                    풀세로길이 = 풀세로길이 + 뉴세로길이 + 10 
                풀이미지 = canvas         

if 가로스위치 == 1 :
    print('최종가로사진커팅중')
    뉴뉴가로길이 = round(풀가로길이+64)   
    풀가로길이 = 뉴뉴가로길이
    댕강댕강이미지=ImageOps.pad(풀이미지, (풀가로길이,416), 5, 'black') #상하 세이프존 설정
    뉴댕강댕강이미지=ImageOps.pad(댕강댕강이미지, (풀가로길이,480), 5, 'black') #좌우 세이프존 설정
    잘라질이미지 = 뉴댕강댕강이미지 
    #잘라질이미지.save(str(숫자넘버)+'longtest23.png', "PNG")
    if 첫스위치 != 0 :
        이것도가로길이 = 잘라질이미지.size[0]
        이것도세로길이 = 잘라질이미지.size[1]
        캔버스 = Image.new('RGB', (608 + 이것도가로길이, 480), 'black')
        캔버스.paste(잘라질이미지, (0,0))
        캔버스.paste(이전잘린이미지, (이것도가로길이-32, 0))
        풀가로길이=풀가로길이+608
        잘라질이미지=캔버스
    if 가로싱글스위치 == 1 :
        나도가로길이 = 잘라질이미지.size[0]
        나도세로길이 = 잘라질이미지.size[1]
        캔버스1 = Image.new('RGB', (5 + 나도가로길이, 480), 'black')
        캔버스1.paste(잘라질이미지, (5,0))
        잘라질이미지=캔버스1
    반복을시작하지=range(math.ceil((풀가로길이-638)/2+1),1,-1) #가운대 2개 int의 합이 640이 될것
    for 반복함수 in 반복을시작하지:
        윗컷팅함수=반복함수*2-2-2 #int의 합이 0이 될것
        아랫커팅함수=반복함수*2+638-2 #int의 합이 640이 될것
        if 윗컷팅함수 == 0 :
            잘린이미지=잘라질이미지.crop((윗컷팅함수, 0, 아랫커팅함수, 480))
            video.write(cv2.cvtColor(numpy.array(잘린이미지), cv2.COLOR_BGR2RGB))
            숫자넘버 = 숫자넘버 + 1
            이전잘린이미지=잘린이미지
        elif 윗컷팅함수 == 반복을시작하지 and 첫스위치 == 0:
            잘린이미지=잘라질이미지.crop((윗컷팅함수, 0, 아랫커팅함수, 480))
            for i in range(1, 61):
                video.write(cv2.cvtColor(numpy.array(잘린이미지), cv2.COLOR_BGR2RGB))
                숫자넘버 = 숫자넘버 + 1
        elif 윗컷팅함수 == 반복을시작하지 :
            잘린이미지=잘라질이미지.crop((윗컷팅함수, 0, 아랫커팅함수, 480))
            video.write(cv2.cvtColor(numpy.array(잘린이미지), cv2.COLOR_BGR2RGB))
            숫자넘버 = 숫자넘버 + 1 
        else :
            잘린이미지=잘라질이미지.crop((윗컷팅함수, 0, 아랫커팅함수, 480))
            video.write(cv2.cvtColor(numpy.array(잘린이미지), cv2.COLOR_BGR2RGB))
            숫자넘버 = 숫자넘버 + 1
    첫스위치 = 첫스위치+1    
elif 가로스위치 == 2 :
    print('최종세로사진커팅중')
    뉴뉴세로길이 = round(풀세로길이+64)   
    풀세로길이 = 뉴뉴세로길이
    댕강댕강이미지=ImageOps.pad(풀이미지, (576,풀세로길이), 5, 'black') #상하 세이프존 설정
    뉴댕강댕강이미지=ImageOps.pad(댕강댕강이미지, (640,풀세로길이), 5, 'black') #좌우 세이프존 설정
    잘라질이미지 = 뉴댕강댕강이미지
    
    if 첫스위치 != 0 :
        이것도가로길이 = 잘라질이미지.size[0]
        이것도세로길이 = 잘라질이미지.size[1]
        캔버스 = Image.new('RGB', (640, 이것도세로길이+448), 'black')
        캔버스.paste(잘라질이미지, (0,448))
        캔버스.paste(이전잘린이미지, (0, 0))
        잘라질이미지=캔버스
        풀세로길이=풀세로길이+448
    
    if math.ceil((풀세로길이-478)/2) < 0 :
        한번더=ImageOps.pad(잘라질이미지, (640,480), 5, 'black')
        for i in range(1, 121):
            video.write(cv2.cvtColor(numpy.array(한번더), cv2.COLOR_RGB2BGR))
            숫자넘버 = 숫자넘버 + 1
    elif 풀세로길이 > 550 :
        
        
        반복을시작하지=range(1,math.ceil((풀세로길이-478)/2+1)) #가운대 2개 int의 합이 480이 될것
        for 반복함수 in 반복을시작하지:
            윗컷팅함수=반복함수*2-2 #int의 합이 0이 될것
            아랫커팅함수=반복함수*2+478 #int의 합이 480이 될것
            if 아랫커팅함수 >= 풀세로길이:
                윗컷팅함수 = 풀세로길이-480
                아랫커팅함수 = 풀세로길이
                잘린이미지=잘라질이미지.crop((0, 윗컷팅함수, 640, 아랫커팅함수))
                video.write(cv2.cvtColor(numpy.array(잘린이미지), cv2.COLOR_BGR2RGB))
                숫자넘버 = 숫자넘버 + 1
                이전잘린이미지=잘린이미지
            elif 윗컷팅함수 == 0 and 첫스위치 == 0:
                잘린이미지=잘라질이미지.crop((0, 윗컷팅함수, 640, 아랫커팅함수))
                for i in range(1, 61):
                    video.write(cv2.cvtColor(numpy.array(잘린이미지), cv2.COLOR_BGR2RGB))
                    숫자넘버 = 숫자넘버 + 1                            
            elif 윗컷팅함수 == 0:
                잘린이미지=잘라질이미지.crop((0, 윗컷팅함수, 640, 아랫커팅함수))
                video.write(cv2.cvtColor(numpy.array(잘린이미지), cv2.COLOR_BGR2RGB))
                숫자넘버 = 숫자넘버 + 1
            else :
                잘린이미지=잘라질이미지.crop((0, 윗컷팅함수, 640, 아랫커팅함수))
                video.write(cv2.cvtColor(numpy.array(잘린이미지), cv2.COLOR_BGR2RGB))
                숫자넘버 = 숫자넘버 + 1
    else :
        한번더=ImageOps.pad(잘라질이미지, (640,480), 5, 'black')
        for i in range(1, 121):
            video.write(cv2.cvtColor(numpy.array(한번더), cv2.COLOR_RGB2BGR))
            숫자넘버 = 숫자넘버 + 1   
    첫스위치 = 첫스위치+1

print('사진커팅완료')

for i in range(1, 61): #종료이미지
    video.write(cv2.cvtColor(numpy.array(이전잘린이미지), cv2.COLOR_BGR2RGB))
    숫자넘버 = 숫자넘버 + 1

for i in range(1, 301): #종료이미지
    video.write(바이미지)
    숫자넘버 = 숫자넘버 + 1

video.release()

#subprocess.call('ffmpeg.exe -i innet.mkv -c:v libx264 -r 59.94 -crf 19 -preset faster -profile:v high -pix_fmt yuv420p out_super3fix.mkv')
#os.remove('innet.mkv')