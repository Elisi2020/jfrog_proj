## Jfrog

##### CLI for JFrog Artifactory 

Created by Eli Siese

#### Overview
This page describes how to use JFrog CLI with JFrog Artifactory.
Code is writen in python

#### Installation
```sh 
sudo pip3 install jfrogELISI  --index https://bob:'Bob123456&'@esiesel.jfrog.io/artifactory/api/pypi/pypi-local/simple
```


Create config.properties (You will be prompt for the file path)
```shell script
[CONFIG]
artifactory = <your-artifactory-path>
```
#### Usage
After installation the script can run as a script(Please see the sample below), 
on windows you will get  jfrog_cli.exe
```sh
Usage: jfrog_cli.py [OPTIONS] COMMAND [ARGS]...

Options:
  --configfile TEXT  Prompt: Please insert configuration file location if
                     other then default

  --username TEXT    Prompt Value
  --password TEXT    Prompt Value
  --help             Show this message and exit.

Commands:
  create-user
  delete-user
  get-storage-info
  system-ping
  system-version
```
### sample

##### Create User
````buildoutcfg
vagrant@master-2:~$ jfrog_cli create_user
Configfile [config.properties]:
Username [admin]:
Password:
New user: kuku
Email [sample@sample.com]:
Password [password]:
 User kuku was created successfully
````

##### Delete User
````buildoutcfg
vagrant@master-2:~$ jfrog_cli delete_user
Configfile [config.properties]:
Username [admin]:
Password:
User to delete: kuku
status code = 200 text =The user: 'kuku' has been removed successfully.

````
##### Get Storage Info
````buildoutcfg
vagrant@master-2:~$ jfrog_cli get_storage_info
Configfile [config.properties]:
Username [admin]:
Password:
status code = 200 text ={"binariesSummary":{ // etc....
````

### Todos

 - Configuration validation
 - Improve security
 - Write MORE Tests
 
### Contact Information
 please fill free to send your comments to eli.siesel@gmail.com
 
 ###### Thanks
 
 ###### Eli