import os
import time
from printer import termalPrint 
def readPath(path,fileExt):
    files=[]
    for root, __, files in os.walk(path):
      for file in files:
         if file.lower().endswith(fileExt):
            files.append(os.path.join(root, file))
    return(files)

def printFiles(files):
    termalPrint()
    
def searchToPrint(configParameters):
    files=readPath(configParameters['printer_path'], configParameters['file_extension'])

def main():
    configParameters ={"printer_path": "", "file_extension": ""}
    try:
        config = open('./.config')
        for line in config:
            name, value = line.split("=")
            value = value.strip()
            if value == '':
                raise ValueError
            configParameters[name] = value
        
    except OSError as exc:
        print(".config file doesnt exist") 
        os._exit(1)
    except ValueError as exc:
        print(".config file contains an invalid value") 
        os._exit(1)
    except:
        print("an unexpected error has been found")
        os._exit(1)
    finally:
        while True:
            searchToPrint(configParameters)
            time.sleep(3)


if __name__ == "__main__":
    main()