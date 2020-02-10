import requests
import robobrowser
import re
import os
from requests import Session
from termcolor import colored

def inicio():


	print ("")
	print ("")
	print ("--------------------------------")
	print (colored("Prevent Facebook login blocking.","blue"))
	print ("--------------------------------")
	print ("")
	print ("")


os.system("clear")
inicio()
x= True


while True:

	facebook = "https://m.facebook.com"

	facebook_email = "https://m.facebook.com/settings/email/add?souce_added=m_settings&gfid=AQBTAMFn1y4T2Zh2"

	url = (facebook)

	loggedin_title = 'Facebook'

	print (colored("Remova a parte AppleWebKit/537.36 do User-Agent","red"))
	print ("")
	useragent = input(colored("Digite o User-Agent: ","blue"))

	os.system("clear")

#  Configurações para uso de proxies
#	session = Session()
#	session.verify = False
#	session.proxies = {"https":"159.89.245.69:3128"}
#	browser = robobrowser.RoboBrowser(history=True, parser='html.parser', user_agent=useragent, session=session)

	browser = robobrowser.RoboBrowser(History=True, parser="html.parser", user_agent=useragent)
	browser.open(url)
	print ("")
	print (colored("Voce esta conectado em: "+ browser.url, "yellow"))
	print ("")
	username = input("\033[34m"+"Digite o email: "+"\033[0;0m")
	password = input("\033[34m"+"Digite a senha: "+"\033[0;0m")
	os.system("clear")
	form = browser.get_form(id="login_form")
	form["email"].value = (username)
	form["pass"].value = (password)

	browser.submit_form(form, submit=form["login"])

	redirect_title = re.compile("<title>(.*?)</title>").search(str(browser.parsed)).group(1)

	if redirect_title == loggedin_title:
		print (colored("[+] SUCESSO NA CONEXÂO","green"))
		print ("")
		print ("")
		print (colored("Conectado com Email: "+form["email"].value+"\nConectado com Senha: "+form["pass"].value,"yellow"))
		browser.open(facebook_email)
	else:
		print ("[-] LOGIN FAILED")
		x = False
	break
if x == True:

	form1 = browser.get_form(id="m-settings-form")

	print ("")

	m = input("\033[34m"+"Email para recuperação: "+"\033[0;0m")

	form1["email"].value = (m)  

	browser.submit_form(form1, submit=form1["email"])

	os.system("clear")

	# substituir email da variavel facebook_confirme por seu email
	# trocar @ por %40
	# exemplo https://m.facebook.com/entercode.php?cp=MEUEMAIL123%40GMAIL.COM&source_verified=m_settings&refid=74

	facebook_confirme = "https://m.facebook.com/entercode.php?cp=meuemail123%40gmail.com&source_verified=m_settings&refid=74"

	browser.open(facebook_confirme)

	c = browser.get_form(method="post")

	codigo = input(colored("Digite o Codigo: ","blue"))

	c["code"].value = (codigo)

	browser.submit_form(c, submit=c["code"])

	print ("--------------------")


