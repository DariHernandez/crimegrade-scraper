import PySimpleGUI as sg
import globals
import config
import log
import sniim_run
from gui_manager import gui

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
          sg.Button("Run", size=(33,1), key="run"),  
        ],
        [
            sg.Button("Theme", size=(8,1), key="Theme"), 
            sg.Button("Settings", size=(12,1), key="config"),  
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
                    
    # End window
    window.close()
    
    # Reopen window after changes
    if reopen: 
        main()
        
def config_gui (): 
    """ Update crdentials and user options
    """
    
    # Get theme from config file
    theme = config.get_credential("theme")
                
    # Set theme
    sg.theme(theme)
    
    # Main screed layout
    layout = [
        [
            sg.Text ("CREDENTIALS", size=(20,1)),  
        ],
        [
            sg.Text ("", size=(20,1)),  
        ],
        [
            sg.Button ("Save", key="save"),  
        ],
    ]
        
    # Create window
    window = sg.Window("Configuración", layout, no_titlebar=False)
    
    while True:
        
        
        reopen = False
    
        event, values = window.read()
        
        # RUN BUTTONS                 
        
        # End program when close windows
        if event == sg.WIN_CLOSED or event == 'Quit':
            
            # Restart last credentials
    
            break
        
        if event == "save": 
            
            # Update credentials
            
            break     
                    
    # End window
    window.close()
    
    # Reopen window after changes
    if reopen: 
        config_gui()

if __name__ == "__main__":
    main()