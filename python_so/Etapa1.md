# Módulo OS

```py
import os
import time
```

```py
print(dir()) # return the names in the current scope
print(os.name)
print(os.getlogin())
print(os.environ["HOMEDRIVE"])  # return driver name where system is
os.environ.get('ENV_VAR') # same as above
print(os.getcwd())  # return current working directory
os.chdir("dir")  # change directory
print(os.getpid())  # return the current process id
os.mkdir("python_so")  # create top level directory
os.makedirs("dis/subdir")  # create dir and sub dirs !use this
os.rename("exemplo", "exemplo1")  # rename directories
os.rmdir("exemplo1/exemplo2")  # removes last dir !use this
os.removedirs("exemplo1/exemplo2")  # remove recursively dirs
print(os.listdir("."))  # show all inside directory
os.path.exists("some_dir")  # return a boolean if path exists or not
os.path.isfile("main.py")  # check if is a file
os.path.basename("path/file")  # return the name of a file at the end of a path
os.path.dirname("path/file")  # return the path for a file
os.path.abspath("file_name")  # return absolute path for the file
os.path.split("path_for_file")  # splits the path and the file nito a tuple
os.path.join("drive", "path", "path", "file")  # create a path
os.path.splitext("path") # split the root path and the file extension
os.stat("path")  # return file status e.g.: creation and modification date
modf = os.stat("file")
time.ctime(modf.st_mtime)  # return human date/time format
# return the current directory and all of its files and directories, doing it for all subdirs
os.walk("path")

# PROCESSES MANAGEMENT
os.abort()  # kill the current process
os.times()  # return process timing info
os.spawnl(p.NOWAIT, "file.exe", " ")  # executes a process
os.startfile("path")
os.system("calc")
```