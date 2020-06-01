#from pytube import YouTube
import pytube 
import os,sys
from loguru import logger
#colors
LR = "\033[1;31m" # light red
LG = "\033[1;32m" # light green
LO = "\033[1;33m" # light orange
LB = "\033[1;34m" # light blue
LP = "\033[1;35m" # light purple
LC = "\033[1;36m" # light cyan
intro = """
                 _                     _         _          
 _ __  _   _  __| | _____      ___ __ | |_ _   _| |__   ___ 
| '_ \| | | |/ _` |/ _ \ \ /\ / / '_ \| __| | | | '_ \ / _ \'
| |_) | |_| | (_| | (_) \ V  V /| | | | |_| |_| | |_) |  __/
| .__/ \__, |\__,_|\___/ \_/\_/ |_| |_|\__|\__,_|_.__/ \___|
|_|    |___/  |   |    |  | | | | | | |   | |   |    |  |  |                      
| |    |   |  |   |    |  | | | | | | |   | |   |    |  |  |
| |    |   |  |   |    |  | | | | | | |   | |   |    |  |  |
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

"""
print(LG+intro)
print(LR+"                     by r00t.k@lih@ck3r")
logger.debug("pydowntube.service started!")
link = input("full-link ?> ")
logger.info("Downloading....")
pytube.YouTube(link).streams.get_highest_resolution().download()
logger.success("Video is downloaded! please check current directory")
