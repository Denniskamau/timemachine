import yaml

config = './config.dat'


def readConfigFile():
    try:
        with open (config,'r') as f:
            file= yaml.load(f)
            print (file)
            for i in file:
                with open('./copiesDir/data.txt', 'w') as c:
                    for data in file[i]:
                        
                        with open (data,'r') as x:
                            value = yaml.load(x)
                            print(value)
                            
                            dump = yaml.dump(value , c , default_flow_style=False)         
    except FileNotFoundError:
        print('There was a problem loading config file, It appears the path specified is not correct!!')

   

def checkForChange():
    with open (config,'r') as f:
        file = yaml.load(f)
        
    with open('./copiesDir/data.txt', 'w') as c:
        file2 = yaml.load(c)
        print(file2)

    
execute = readConfigFile()
execute2 = checkForChange()
