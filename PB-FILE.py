import os, platform

os.system('git pull')

 

import requests

bit = platform.architecture()[0]

if bit == '64bit':

    from FILEV2 import dump

    dump()

elif bit == '32bit':

    from FILE import dump

    dump()
