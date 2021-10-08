import os

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
        print(".config file contains a not valid value") 
        os._exit(1)
    except:
        print("an unexpected error has been found")
        os._exit(1)
    finally:
        print(configParameters)

if __name__ == "__main__":
    main()