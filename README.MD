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

Create a file named 'config.json' in this folder, copy this code and write your preferences
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
alias iris="cd (path of iris folder) && python3 main.py"
```
## Do you see useless file?
In this repository I also uploaded 'main_ui.py', 'server.py' and 'voc_module.py' which are not used now because they are tests for functions that I will add in the future. If you want you can delete it.
## Contributing
You can contact me for bug fixes or to become a beta tester on [Telegram](https://t.me/lorehh_ric)
