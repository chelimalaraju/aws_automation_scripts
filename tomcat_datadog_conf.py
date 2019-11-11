import subprocess

grepResults = subprocess.check_output(['ps -ef | grep tomcat'], shell=True).split()
print(grepResults)
