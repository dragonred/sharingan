#!/usr/bin/python

import os
import sys, traceback

os.system ("sudo apt install catimg -y")
os.system ("clear")
os.system("catimg -w 50 .sharingan.jpg")
def main():
	try:
		print ('''
\033[1;91m  _____ __ __   ____  ____   ____  ____    ____   ____  ____  \033[1;m
\033[1;91m / ___/|  |  | /    ||    \ |    ||    \  /    | /    ||    \ \033[1;m
\033[1;91m(   \_ |  |  ||  o  ||  D  ) |  | |  _  ||   __||  o  ||  _  |\033[1;m
\033[1;91m \__  ||  _  ||     ||    /  |  | |  |  ||  |  ||     ||  |  |\033[1;m
\033[1;91m /  \ ||  |  ||  _  ||    \  |  | |  |  ||  |_ ||  _  ||  |  |\033[1;m
\033[1;91m \    ||  |  ||  |  ||  .  \ |  | |  |  ||     ||  |  ||  |  |\033[1;m
\033[1;91m  \___||__|__||__|__||__|\_||____||__|__||___,_||__|__||__|__|\033[1;m  < a vulnerability scanning and information lookup tool !!!>
                                                              

\033[1;32mWeb search engine automatically finds security vulnerabilities by developer Long Hoang !!!!\033[1;m
\033[1;45mThanks Nguyen Tuyet for helping me regain the main motivation\033[1;m
\033[1;91mContact me at this github address {https://github.com/longhoang-j2009e}\033[1;m
\033[1;50mContact me at this email address [longhoangdevelopergithub@gmail.com]\033[1;m
\033[1;45mHow to use :\033[1;m
\033[1;42mPress CTL + C to exit
You just have to choose the options available and enjoy\033[1;m

		''')
		def inicio1():
			while True:
				print ('''
1) Install the necessary tools 
2) Upgrade tools to the latest version
3) Start conducting website information investigation

			''')

				opcion0 = raw_input("\033[1;36mlonghoang@j2009e \033[1;m")
			
				while opcion0 == "1":
					print ('''
1) Help the operating system using the apt installation package ( Ubuntu , Debian , Kalilinux ....)
2) Help the operating system using the pacman installation package ( Arch , Manjaro , Deppin ....)


					''')
					repo = raw_input("\033[1;32mWhat do you want to do ?> \033[1;m")
					if repo == "1":
						os.system("clear")
						os.system("sudo apt install python3-pip -y")
						os.system("sudo apt install gnupg -y ")
						os.system("sudo apt-key adv --keyserver pool.sks-keyservers.net --recv-keys ED444FF07D8D0BF6")
						os.system("sudo apt update  ")
						os.system(" bash .install.sh  ")
						os.system("clear ")
					elif repo == "2":
						os.system("pacman -Syu")
						os.system("clear")
						os.system("pacman -S  nmap nikto xterm whatweb  python3-pip wafw00f")
						os.system("pip3 install art  ")
                                                os.system("pip3 install -r requirements.txt ")
                                                os.system("pip3 install termcolor netifaces idna")
                                                os.system("clear ")

					elif repo == "back":
						inicio1()
					elif repo == "gohome":
						inicio1()
					
					else:
						print ("\033[1;31mSorry, that was an invalid command!\033[1;m") 					
						

				if opcion0 == "3":
					print (''' 
Are you sure you want to scan your website wisely (note this tool is written to look for vulnerabilities, not to commit crimes)
''')
					repo = raw_input("\033[1;32mPress y to confirm your consent ? [y/n]> \033[1;m")
					if repo == "y":
						cmd = os.system("clear")
						cmd = os.system("python3 .sharingan.py")

				def inicio():
					while opcion0 == "2":
						print ('''
\033[1;36m**************************** Start Update Tools !!!! *****************************\033[1;m

			 ''')
						print ("\033[1;32mPress (0) to update the tool\n\033[1;m")

						opcion1 = raw_input("\033[1;36mlonghoang@j2009e \033[1;m")
						if opcion1 == "back":
							inicio1()
						elif opcion1 == "gohome":
							inicio1()
						elif opcion1 == "0":
							os.system("cd")
							cmd = os.system("git clone https://github.com/longhoang-j2009e/sharingan")
						
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
							
							print ("\033[1;31mSorry, that was an invalid command!\033[1;m")

				inicio()
		inicio1()
	except KeyboardInterrupt:
		os.system("clear")
		print ("Shutdown requested...Goodbye...")
	except Exception:
		traceback.print_exc(file=sys.stdout)
	sys.exit(0)

if __name__ == "__main__":
    main()
