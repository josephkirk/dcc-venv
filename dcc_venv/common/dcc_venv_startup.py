import os
import sys
import inspect

def startup():

    sys.stdout.write("#"*50)
    sys.stdout.write("\n dcc_venv setup\n")
    
    
    # Add site-packages to sys.path
    CURRENT_DIR = os.path.dirname(inspect.getfile(inspect.currentframe()))
    
    if CURRENT_DIR not in sys.path:
        sys.path.append(CURRENT_DIR)
    
    
    
    # Adding Egg Links that might be in site-packages
    site_paths = []
    for f in os.listdir(CURRENT_DIR):
        if f.endswith('.egg-link'):
        
            egg_link_path = os.path.join(CURRENT_DIR, f)
            
            with open(egg_link_path, "r") as fp:
                for path in fp.read().splitlines():
                    if path == ".":
                        continue
                        
                    site_paths.append(os.path.abspath(path))

    if site_paths:
        sys.stdout.write("\nDEV site-setup\n")
                        
        for site_path in site_paths:
            if not site_path in sys.path:
                print("DEV - adding to sys.path {}".format(site_path))
                sys.path.append(site_path)
            
            
            
            
    # startup complete
    sys.stdout.write("#"*50)

    
if __name__ == "__startup__":
    startup()