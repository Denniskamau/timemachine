import yaml

config = './config.dat'


def readConfigFile():
    config_Location = input('Please input the location of the config file to read from? ')
    copies_Location = input('Please input the location of the file to store the copies of file? ')
    
    if config_Location != '':
        try:
            with open (config_Location,'r') as f:
                file= yaml.load(f)
                print (file)
                for i in file:
                    if copies_Location == '':
                        with open('./copiesDir/data.txt', 'w') as c:
                            for data in file[i]:

                                with open (data,'r') as x:
                                    value = yaml.load(x)
                                    print(value)

                                    dump = yaml.dump(value , c , default_flow_style=False)
                    else:
                        with open(copies_Location, 'w') as c:
                            for data in file[i]:

                                with open (data,'r') as x:
                                    value = yaml.load(x)
                                    print(value)

                                    dump = yaml.dump(value , c , default_flow_style=False)

        except FileNotFoundError:
            print('There was a problem loading config file, It appears the path specified is not correct!!')
    else:
        try:
            with open (config,'r') as f:
                file= yaml.load(f)
                print (file)
                for i in file:
                    if copies_Location == '':
                        with open('./copiesDir/data.txt', 'w') as c:
                            for data in file[i]:

                                with open (data,'r') as x:
                                    value = yaml.load(x)
                                    print(value)

                                    dump = yaml.dump(value , c , default_flow_style=False)
                    else:
                        with open(copies_Location, 'w') as c:
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
#execute2 = checkForChange()
