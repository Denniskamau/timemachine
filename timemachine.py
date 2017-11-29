import yaml
import argparse
import logging

from logging.handlers import RotatingFileHandler


parser = argparse.ArgumentParser(description="Create copies of specified files and watch for changes ")
parser.add_argument('-a' ,'--add', default=None, action="store_true",
                    help='Add a file to the list of files to be observed')

parser.add_argument('-r' , '--remove',default=None,action="store_true",
                    help='Remove a file from the list of files to be observed')

parser.add_argument('-l','--list', action="store_true",
                    help='Print a list of the file being observed')


config = './config.dat'
log = './logfile.log'
rotating_handler = RotatingFileHandler(log,
				    maxBytes=10000000,
				    backupCount=3)

logger = logging.getLogger('dante')
logger.setLevel(logging.DEBUG)
logger.addHandler(rotating_handler)

"""
-function to read the config file data
-Gives the user an option to give the location of the config file if none is provided then the default value of 
config file in ./config.dat
-Gives the user an option to give the location of where the files are to be copied to ,if none is given then the
default location will be in the copies Directory

-Copies the content of the file given in the config.dat to a file in the copies Directory
"""
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


"""
-A function to watch for changes in the original file and compare them to the copies created.
"""
   

def check_for_change():
    with open (config,'r') as f:
        file = yaml.load(f)
        
    with open('./copiesDir/data.txt', 'w') as c:
        file2 = yaml.load(c)
        print(file2)


# Check for all the files in config.dat
def list_all_files():
    print('checking for files')
    try:
        with open(config, 'r') as f:
            files = yaml.load(f)
            print (files)
    except FileNotFoundError:
        print("Config file {0} not found".format(filename), file=sys.stderr)
        sys.exit(1)

#Add a file to config.dat
def add_file_to_config(filename):
    print('adding file to list of observable files')
    
    try:
        with open(config, 'w') as f:
            new_file = yaml.dump(filename,f.files,default_flow_style=False)
            print(file+ "has been added to the list of observable files")
    except FileNotFoundError:
        print("Specified file {0} not found".format(filename), file=sys.stderr)
        sys.exit(1)


#Delete a file from config.dat
def delete_file_from_config():
     print('removing file from list of observable files')
    



def main():
    args =parser.parse_args() 
    if args.list:
        list_all_files()
    elif args.add:
        add_file_to_config()
    elif args.remove:
        delete_file_from_config()
    else:
        execute = read_config_file()

    



run=main()
