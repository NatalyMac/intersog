import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#dirname = os.path.dirname(os.path.dirname(__file__))
#realpath = os.path.dirname(os.path.realpath(__file__))
#abspath = os.path.dirname(os.path.abspath(__file__))
#mypath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#mypath = abspath = os.path.dirname(os.path.abspath(__file__))
#filecount = os.path.join(mypath, 'counter.txt')

print os.path.join(BASE_DIR, 'static')

