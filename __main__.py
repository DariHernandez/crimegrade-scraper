import os
import log
import config
import globals
import subprocess
import PySimpleGUI as sg
from gui_manager import gui
from database.postgresql import PostgreSQL

def main (): 
    """Main function of the project with gui
    """
    
    # Get theme from config file
    theme = config.get_credential("theme")
    
    # Create json file if it doesn't exist
    if not theme: 
        
        config_data = {
            "theme": "Dark2",
            "rows": 3, 
            "db_server": "", 
            "db_name": "",
            "db_user": "", 
            "db_password": "",
        }
        
        theme = config_data["theme"]
        
        config.create_config(config_data)
                
    # Set theme
    sg.theme(theme)

    # Main screedn layout
    layout = [
        [
          sg.Button("Run", size=(43,1), key="run"),  
        ],
        [
            sg.Button("Theme", size=(8,1), key="Theme"), 
            sg.Button("Database", size=(10,1), key="database"),  
            sg.Button("Zip Codes", size=(10,1), key="zipcodes"),  
            sg.Button("Exit", size=(8,1), key="Quit"),
        ]
    ]
    
    # Create window
    window = sg.Window("Program name", layout, no_titlebar=False)
    
    while True:
        
        
        reopen = False
    
        event, values = window.read()
        
        # RUN BUTTONS                 
                   
        # End program when close windows
        if event == sg.WIN_CLOSED or event == 'Quit':
            break
            
        if event == "Theme": 
            
            # Select new theme
            gui.theme_selector()
            
            # Update theme in current window
            theme = config.get_credential("theme")
            sg.theme(theme)
            reopen = True
            break  
        
        if event == "run": 
            
            # Show loading status and run main function in thread
            
            # gui.loading(sniim_run.run)            
            # gui.show_status("Programa terminado. Estatus final:")
            print ("Running...")
            
        if event == "config":
            
            log.info ("Credentials and options updated")
            
            # Show config gui
            config_gui()
            
        if event == "database": 
            
            # Update credentials
            gui.database(PostgreSQL)
            
            # table = "table_2"
            # columns = ["usuario", "contraseña"]
            # data = [["d", "a"]]
            
            # globals.db_manager.insert_rows (table, columns, data)
            
            
        if event == "zipcodes": 
            
            zipcodes_file = os.path.join (os.path.dirname(__file__), "zipcodes.txt")
            subprocess.Popen(zipcodes_file, shell=True)
            
                    
    # End window
    window.close()
    
    # Reopen window after changes
    if reopen: 
        main()

if __name__ == "__main__":
    main()