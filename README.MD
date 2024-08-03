# IRIS
Iris is a virtual assistant that can help you to simplify some pc action

## Prerequisites
It works on macOS and Linux (not tested) but you have to install all the dependencies with this commands:
``` bash
pip install keyboard
pip install pynput
pip install psutil
pip install secrets
pip install requests
```
## Installation
To install Iris you can simply download this repository and modify some files to make it work

Create a file named 'config.json' in this folder, copy this code and write your preferences
```json
{
    "access_code": " ", 
    "weather_api_key": " ",
    "psw_def_length": 12,
    "debug": true 
}
```
The debug variable in 'config.json' can also be false, it is needed for some command in the program. 
You can also add it to .zshrc file in your terminal as an alias to start it everywhere 

## Contributing
You can contact me for bug fixes or to become a beta tester on [Telegram](https://t.me/lorehh_ric)
