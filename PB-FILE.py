import os, platform

os.system('git pull')

 

import requests

bit = platform.architecture()[0]

if bit == '64bit':

    import FILEV2

elif bit == '32bit':

    import FILE
