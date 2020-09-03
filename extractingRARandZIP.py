# unrar every rar in Downloads
from fabric.operations import local 
import os
import re

DIR=r"C:\Users\Owner\Downloads"
PATTERN=re.compile(r"part\d{1,3}.rar$")
# unrar.
# You can add part1 only function
def extracting():
    for r in os.listdir(DIR):
        if r.lower().endswith(".rar"):
        
            if re.search(PATTERN,r):
                if r.lower().endswith("part1.rar") or r.lower().endswith("part01.rar") or r.lower().endswith("part001.rar"):
                    local(f"cd {DIR} && unrar x {r}")

            else:
                local(f"cd {DIR} && unrar x {r}")

        if r.lower().endswith(".zip"):        
            local(f'cd {DIR} && powershell -command "Expand-Archive {r}"')



# move the original rar to trashbin
def to_trashbin():
    for r in os.listdir(DIR):
        if r.lower().endswith(".rar") or r.lower().endswith(".zip"):
            # Added double quotes so that space won't intermeddle.
            local(f'cd {DIR} && trash "{r}"')

extracting()
to_trashbin()