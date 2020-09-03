from fabric.operations import local 
import os

DIR=r"C:\Users\Owner\Downloads"
DIRNEW=r"C:\Users\Owner\Downloads\New folder"

def mving():
    for r in os.listdir(DIR):
        if r.lower().endswith(".mp4") or r.lower().endswith(".wmv"):

        
            try:
                local(f'move "{os.path.join(DIR,r)}" "{os.path.join(DIRNEW,r)}"')
            except:
                pass
mving()