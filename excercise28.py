import os
import datetime as dt
cwd=os.getcwd()
cwdb=os.getcwdb()
print("current working directory",cwd,cwdb)

directory="StevenProjects"
directory2="StevenGraphics"
parent_dir = r"C:\Users\shivam\PycharmProjects\College-projects"
path = os.path.join(parent_dir,directory)
os.mkdir(path)
print(os.path.getsize(os.getcwd()))
print("last access time :",os.path.getatime(os.getcwd()))
print("last modification time :",os.path.getmtime(os.getcwd()))
# os.rename("StevenProjects","StevenGraphics")
# os.rmdir("StevenGraphics")
access_time=dt.datetime.fromtimestamp(os.path.getatime(os.getcwd())).strftime('%Y-%m-%d %I:%M %p')
print(access_time)
modification_time=dt.datetime.fromtimestamp(os.path.getmtime(os.getcwd())).strftime('%Y-%m-%d %I:%M %p')
print(modification_time)
print("Directory '%s' created" % directory)
import filecmp as fc
d = fc.dircmp(directory, directory2, ignore=None, hide=None)

print("comparison 1 :")
d.report()