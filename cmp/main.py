from pathlib import Path
import logging as log
from PIL import Image
import numpy as np
import csv
import struct
import utils
import sys


if __name__=="__main__": 
    bsq = utils.read_BSQ_from_bin(Path(sys.argv[1]), 4, 24, 32)
    decompressed = utils.BSQ_to_mosaic(bsq)
    Image.fromarray(decompressed).show()   



