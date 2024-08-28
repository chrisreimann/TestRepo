import subprocess
test = subprocess.Popen(["pip", "install", "-r", "requirements.txt"], stderr=subprocess.STDOUT, stdout = subprocess.PIPE)
output = test.communicate()[0]

if test.returncode == 0:
    print(f"\n\
        ###################################################################\n\
        #                                                                 #\n\
        # Python Pakete fürs Rentenmodell wurden erfolgreich installiert! #\n\
        #                                                                 #\n\
        ###################################################################")

else:
    print(f"Setup failed! Output was: \n {output}")