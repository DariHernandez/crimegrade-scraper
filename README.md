<div><a href='https://github.com/darideveloper/crimegrade-scraper/blob/master/LICENSE' target='_blank'>
            <img src='https://img.shields.io/github/license/darideveloper/crimegrade-scraper.svg?style=for-the-badge' alt='MIT License' height='30px'/>
        </a><a href='https://www.linkedin.com/in/francisco-dari-hernandez-6456b6181/' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=LinkedIn&color=0A66C2&logo=LinkedIn&logoColor=FFFFFF&label=' alt='Linkedin' height='30px'/>
            </a><a href='https://t.me/darideveloper' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=Telegram&color=26A5E4&logo=Telegram&logoColor=FFFFFF&label=' alt='Telegram' height='30px'/>
            </a><a href='https://github.com/darideveloper' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=GitHub&color=181717&logo=GitHub&logoColor=FFFFFF&label=' alt='Github' height='30px'/>
            </a><a href='https://www.fiverr.com/darideveloper?up_rollout=true' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=Fiverr&color=222222&logo=Fiverr&logoColor=1DBF73&label=' alt='Fiverr' height='30px'/>
            </a><a href='https://discord.com/users/992019836811083826' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=Discord&color=5865F2&logo=Discord&logoColor=FFFFFF&label=' alt='Discord' height='30px'/>
            </a><a href='mailto:darideveloper@gmail.com?subject=Hello Dari Developer' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=Gmail&color=EA4335&logo=Gmail&logoColor=FFFFFF&label=' alt='Gmail' height='30px'/>
            </a></div><div align='center'><br><br><img src='https://github.com/darideveloper/crimegrade-scraper/blob/master/imgs/logo.jpg?raw=true' alt='Crimegrade Scraper' height='80px'/>

# Crimegrade Scraper

Extract data from different zip codes, in page: crimegrade.org. Save output data in PostgreSQL database.

Project with GUI

Project type: **client**

</div><br><details>
            <summary>Table of Contents</summary>
            <ol>
<li><a href='#buildwith'>Build With</a></li>
<li><a href='#media'>Media</a></li>
<li><a href='#install'>Install</a></li>
<li><a href='#settings'>Settings</a></li>
<li><a href='#run'>Run</a></li></ol>
        </details><br>

# Build with

<div align='center'><a href='https://www.python.org/' target='_blank'> <img src='https://cdn.svgporn.com/logos/python.svg' alt='Python' title='Python' height='50px'/> </a><a href='https://www.pysimplegui.org/en/latest/' target='_blank'> <img src='https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/Logo%20with%20text%20for%20GitHub%20Top.png' alt='PySimpleGUI' title='PySimpleGUI' height='50px'/> </a><a href='https://www.postgresql.org/' target='_blank'> <img src='https://cdn.svgporn.com/logos/postgresql.svg' alt='PostgreSQL' title='PostgreSQL' height='50px'/> </a><a href='https://www.selenium.dev/' target='_blank'> <img src='https://cdn.svgporn.com/logos/selenium.svg' alt='Selenium' title='Selenium' height='50px'/> </a></div>

# Install

## Tird party modules

Install all modules from pip: 

``` bash
$ pip install -r requirements.txt
```

## Programs

To run the project, the following programs must be installed:: 

* [Google Chrome](https://www.google.com/intl/es/chrome) last version

# Settings

## Home

![Config screen 1](https://github.com/darideveloper/crimegrade-scraper/blob/master/imgs/home.PNG?raw=true)

On the home screen, you must **write the name of the table** where the **scraping data** will be **saved**.
If the **table does not exist** in the database, **the program will create it**.

### DATABASE

![Config screen 2](https://github.com/darideveloper/crimegrade-scraper/blob/master/imgs/database.PNG?raw=true)

To configure the database, we need to set our credentials:
* **Server**
* **Database name**
* **User**
* **Password**

## config.json

All **configurations** are saved in the **config.json file**, so **you can edit it manually** without the graphical interface.

# Run

## GUI

For **start** the program with **graphic interface**, **run** the file **__ main__.py** with you **python 3.9** interpreter.

The graphical interface, in addition to allowing you to run the program, will make it easier for you to configure it (more details in the configuration section).

![Home](https://github.com/darideveloper/crimegrade-scraper/blob/master/imgs/home.PNG?raw=true)

## Terminal

To **start** the program **in terminal** / without interfaz, **run** the **crimegrade_scraper.py** file with your **python 3.9** interpreter.

Executing the program in this way **it will not be possible to update the configurations** and it will be executed with the **last configuration** (more details in the next).

Ejecutando el programa de esta forma **no se podrán actualizar las configuraciones** y se ejecutará con la **última configuración establecida** (mas detalles en la sección de configuración).

