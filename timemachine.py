import yaml
import logging

from logging.handlers import RotatingFileHandler

config = './config.dat'
log = './logfile.log'
rotating_handler = RotatingFileHandler(log,
				    maxBytes=10000000,
				    backupCount=3)

logger = logging.getLogger('dante')
logger.setLevel(logging.DEBUG)
logger.addHandler(rotating_handler)


def read_config_file():
    config_Location = input('Please input the location of the config file to read from? ')

    if config_Location == '':
        logger.debug('Config location is ./config.dat')
    else:
        logger.debug('Config location is '+ config_Location)

    copies_Location = input('Please input the location of the file to store the copies of file? ')

    if copies_Location == '':
        logger.debug('Copies location is /copiesDir/data.txt')
    else:
        logger.debug('Copies location is '+ copies_Location)

    if config_Location != '':
        try:
            logger.debug('Reading data from '+ config_Location)
            with open (config_Location,'r') as f:
                file= yaml.load(f)
                print (file)
                for i in file:
                    if copies_Location == '':
                        logger.debug('Writting data to ./copiesDir/data.txt')
                        with open('./copiesDir/data.txt', 'w') as c:
                            for data in file[i]:

                                with open (data,'r') as x:
                                    value = yaml.load(x)
                                    print(value)

                                    dump = yaml.dump(value , c , default_flow_style=False)
                    else:
                        logger.debug('Writting data to '+ copies_Location)
                        with open(copies_Location, 'w') as c:
                            for data in file[i]:

                                with open (data,'r') as x:
                                    value = yaml.load(x)
                                    print(value)

                                    dump = yaml.dump(value , c , default_flow_style=False)

        except FileNotFoundError:
            logger.debug('specified file location was incorrect')
            print('There was a problem loading config file, It appears the path specified is not correct!!')
    else:
        try:
            logger.debug('Reading data from '+ config)
            with open (config,'r') as f:
                file= yaml.load(f)
                print (file)
                for i in file:
                    if copies_Location == '':
                        logger.debug('Writting data to ./copiesDir/data.txt')
                        with open('./copiesDir/data.txt', 'w') as c:
                            for data in file[i]:

                                with open (data,'r') as x:
                                    value = yaml.load(x)
                                    print(value)

                                    dump = yaml.dump(value , c , default_flow_style=False)
                    else:
                        logger.debug('Writting data to '+ copies_Location)
                        with open(copies_Location, 'w') as c:
                            for data in file[i]:

                                with open (data,'r') as x:
                                    value = yaml.load(x)
                                    print(value)

                                    dump = yaml.dump(value , c , default_flow_style=False)      
        except FileNotFoundError:
            logger.debug('specified file location was incorrect')
            print('There was a problem loading config file, It appears the path specified is not correct!!')

   

def check_for_change():
    with open (config,'r') as f:
        file = yaml.load(f)
        
    with open('./copiesDir/data.txt', 'w') as c:
        file2 = yaml.load(c)
        print(file2)

    
execute = read_config_file()
#execute2 = checkForChange()
