import os
import winreg as reg

def addtostartup(filename,filepath=os.path.dirname(os.path.realpath(__file__))):

	if os.path.splitext(filename)[1] == '':
		print(os.error("Error: file extension is not provided inside filename"))
		return False
	pth = filepath
	# print(pth)
	program_name = filename.split(".")[0]
	
	# # name of the python file with extension
	s_name=filename	
	
	address=os.path.join(pth,s_name) 
	
	key_path = r"Software\\Microsoft\\Windows\\CurrentVersion\\Run"
	existing_key = reg.OpenKey(reg.HKEY_CURRENT_USER, key_path, 0, reg.KEY_WRITE)
	

    # Set the value of the "Pathname" entry

	reg.SetValueEx(existing_key,program_name, 0, reg.REG_SZ, address)	
	# Close the key
	reg.CloseKey(existing_key)
	

if __name__ == "__main__":
	addtostartup("passgen.exe")
	os.system("python main.py")




