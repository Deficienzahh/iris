# IRIS
Iris is a virtual assistant that can help you to simplify some pc action

## Prerequisites
It works on MacOS and Linux (not tested) but you have to install all the dependencies with this commands:
``` bash
pip install keyboard
pip install pynput
pip install psutil
pip install secrets
pip install requests
```
## Installation
To install Iris you can simply download this repository and modify some files to make it work

In file "main.py" modify the first variables
```python
access_code = ''#insert the password you would use to access to iris
psw_def_lenght = 12 #The default lenght of the random password you can generate
weather_api_key = '' #Your API key on openweather website
```
You can also add it to .zshrc file in your terminal as an alias to start it everywhere 

## Contributing
You can contact me for bug fixes or to become a beta tester on [Telegram](https://t.me/lorehh_ric)
