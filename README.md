# TimeMachine

##  Setting up

-change the default location for both the config.dat file under the variable config in the script.
-change the path in the config.dat file

## Handling cron

-To schedule the task carry out the following command :
		-Give the absolute path for python: /usr/bin/python3  
 
		-Give the abolute path for the python program: /home/dan/Desktop/dante/timemachine.py 

		-open the crontab from the terminal: crontab

		-pass in both commands when they are concaneted: * * * * * /usr/bin/python3 /home/dan/Desktop/	   dante/timemachine.py

-This will run the program every minute.

			



##  important links
-About  `subprocess.call()` https://docs.python.org/2/library/subprocess.html

-About `yaml` http://pyyaml.org/wiki/PyYAMLDocumentation

-About `argpaser`  https://docs.python.org/3/library/argparse.html


