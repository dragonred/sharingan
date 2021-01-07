#!/usr/bin/python3

import os
import sys
import time
sys.path.append('__init__')
import get_ip as ad
import file_mg as file 
from art import *
from termcolor import colored

SEC_PATH = "/usr/bin/"


def main():
	try:	
		os.system(" xterm -fg white -bg black -e 'echo Warning !!!  Website scan result information saved in a directory reports && sleep 20'  ")
		url =input("Please enter the URL : ")
		path_dir ="reports/" + url
		file.create_dir(path_dir)
		ip = ad.get(url)
		print('The IP Address is :',ip)
		os.system(" xterm -fg white -bg black -e 'whatweb "+url+" && sleep 10'" )
		os.system(' xterm -fg white -bg black -e whatweb -v '+url+' ')
		os.system(SEC_PATH  + 'xterm -fg white -bg black -e "nmap -A '+ip+' -o '+path_dir+'/nmap.txt  && bash"') 
		os.system(SEC_PATH  + 'xterm -fg white -bg black -e "nikto +h '+url+' -output '+path_dir+'/nikto.txt &&  bash" ')
		os.system(" xterm -fg white -bg black -e 'python3 .okadminfinder.py -u "+url+" && sleep 10 ' ")
		os.system(" xterm -fg white -bg black -e 'wafw00f "+url+" && sleep 10' ")
		os.system(" xterm -fg white -bg black -e 'python3 .dirsearch.py -u  "+url+" && sleep 10' ")
	except ValueError as e:
		print(e)
	except:
		print("unknow error")
	
	


if __name__ == '__main__':

	if sys.version_info.major < 3 :
		exit(0)
	main()
