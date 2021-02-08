users = {}
status = ""

def displyMenu():
	status1 = input("bist du schon regestriert j/n drück q zum schließen")
	if status1 == "j":
		oldUser()
	else: 
		status1 == "n"
		newUser()

def newUser():
	createLogin = input("erstelle einen neuen benutzer: ")
	if creatLogin in users:
		print("\nnutzer Name schon vergeben\n")
	else:
		creatPasswort = input("erstelle ein Passwort")
		users[greatelogin] = creatPasswort1
		print("\nnutzer erstellt\n")

def oldUser():
	login = input("username")
	creatPasswort1 = input("passwort")

	if users in user[login] == creatPasswort1:
		print("\neingeloggtt\n")
	else:
		print("\nbenutzer exsistiert nicht oder falsches Passwort!\n")

while status != "q":
	displyMenu()
	break
