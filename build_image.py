#!/usr/bin/env python3
import glob
import os
from pathlib import Path


uml = glob.glob("**/**/*.pu")

for u in uml:
    path = Path(u)
    os.system("cd {} && plantweb {} --format svg".format(path.parent,path.name))
    os.system("cd {} && rsvg-convert -f pdf -o {}.pdf {}.svg".format(path.parent,path.stem,path.stem))
    os.system("cd {} && rm {}.svg".format(path.parent,path.stem))
