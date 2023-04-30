import os, platform

os.system('git pull')

 

import requests

bit = platform.architecture()[0]

if bit == '64bit':

    from FILEV2 import approval

    dump()

elif bit == '32bit':

    from FILE import approval

    dump()
