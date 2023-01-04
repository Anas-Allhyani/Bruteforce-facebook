#created by Anas Allhyani
#Brute force facebook
import os,sys
logo ="""
\033[1;91m             ##     ##    ##    ## #### ##    ##  ######\033[1;0m
\033[1;91m            ###   ###    ##   ##   ##  ###   ## ##    ##\033[1;0m
\033[1;97m           #### ####    ##  ##    ##  ####  ## ##\033[1;0m
\033[1;97m          ## ### ##    #####     ##  ## ## ## ##   ####\033[1;0m
\033[1;91m         ##     ##    ##  ##    ##  ##  #### ##    ## \033[1;0m
\033[1;91m        ##     ##    ##   ##   ##  ##   ### ##    ##\033[1;0m
\033[1;97m       ##     ##    ##    ## #### ##    ##  ######\033[1;0m
\033[1;97m--------------------------------------------------
\033[1;91m Author      : Anas Allhyani
\033[1;91m GitHub      : https://github.com/Anas-Allhyani
\033[1;91m Facebook    : https://www.facebook.com/Asdfrew90
\033[1;97m--------------------------------------------------
"""
print(logo)
print("\033[1;32m[1]\033[0;93m b-Api[soon]")
print("\033[1;32m[2]\033[0;93m free[best]")
xx = input("\033[1;34m[+] chose method brute force : \033[0;93m")
if xx in ["1", "01"]:
	os.system("python b-api-brute.py")
if xx in ["2", "02"]:
	os.system("python free-brute.py")
