# IRIS
Iris is a virtual assistant that can help you to simplify some pc action

## Prerequisites
It works on macOS and Linux (not tested) but you have to install all the dependencies.
First install python from [here](https://www.python.org/downloads/).
Next install HomeBrew because some dependencies we needs are already into it
``` bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)
```

Now install the other dependencies:
``` bash
pip install keyboard
pip install pynput
pip install psutil
pip install secrets
pip install requests
```
## Installation
To install Iris you can simply download this repository with git clone or in a .zip file and modify some files to make it work

Create a file named 'config.json' in this folder, copy this code and write your preferences.
You can obtain the weather api key on openweather website
``` json
{
    "access_code": " ", 
    "weather_api_key": " ",
    "psw_def_length": 12,
    "debug": true 
}
```
You can also add iris to .zshrc file with 'nano ~/.zshrc' in your terminal as an alias to start it everywhere 
Example:
``` bash
alias iris="cd (path of iris folder) && python3 cli.py" #cli file start iris on terminal 
alias iris_server="cd (path of iris folder) && python3 server.py" #server file start iris on self-hosted server to use it web browser 
```
## Iris won't work properly?
The web version is work in progress. Some features like weather doesn't work properly on the web version.
## Contributing
You can contact me for bug fixes or to become a beta tester on [Telegram](https://t.me/lorehh_ric)
