from pathlib import Path  
import os  


def sortFiles(): 
	for i in p.iterdir(): #Iterate over every item
		if i.is_file(): #and check it is a file and clasificate it
			if i.suffix in clasification.keys():
				moveFile(i.name, clasification[i.suffix])#move to destiny
			elif i.suffix != ".py": #ignore python file
				moveFile(i.name, "Others")


def createFolders(): #function that check for item in directory
 	for item in p.iterdir(): 
 		if item.is_dir() and item.name in folders: #if it is directory and already
 			folders.remove(item.name)#exist in destiny eliminate from list
 	for f in folders:		
	 	os.system('mkdir '+ f) #create destiny directories
 		print("Directory ", f, " create")
 	print("Created destiny directories")

def moveFile(file, destiny):
	new_direction = "mv '"+file+"' "+destiny
	os.system(new_direction)
	print("file "+file+" moved to "+destiny)

#-------------------------------------------------------------------------------
#variable declaration

p = Path('.') #Directory where every file is gonna be organized
folders = ["Images", "PDFs", "Documents", "Music", "Videos", "Otros", "Comprimidos",
			"Software"]#destination directories
clasification = {".jpg":"Images", ".png":"Images", ".gif":"Images",
				 ".pdf":"PDFs", ".txt":"Documents", ".docx":"Documents",
				 ".mp3":"Music", ".avi":"Videos", ".mp4":"Videos", 
				 ".jpeg": "Images", ".zip": "Comprimidos", ".rar":"Comprimidos",
				 ".iso":"Imagen de disco", ".img":"Imagen de disco",
				 ".deb":"Software", ".jar":"Software", ".xls":"Documents",
				 ".tar":"Comprimidos", ".pptx":"Documents", ".apk":"Software" }
				 #Relationship between files and directories

#-------------------------------------------------------------------------------
#  script

createFolders()
print("---------------------")
sortFiles()


