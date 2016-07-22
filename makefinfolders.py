"""

makefolders.py

--tkp

Makes financial folders for a given year.

Example usage:
python makefinfolders.py --root /root -y 2016 --prefix "FY "

/root
    /FY 2016
           /2016-01 Jan
           /2016-02 Feb

"""


import argparse
import os
from datetime import datetime
from time import strftime

if __name__ == "__main__":
    # Get arguments
    parser = argparse.ArgumentParser(prog='makefolders', 
                description='Create folders under root for months of the year.')
    parser.add_argument('--version', action='version', version='%(prog)s 1.0')
    parser.add_argument('-y', action='append', dest='years', type=int,
                default=[],
                help='Add years to process, e.g. -y 2014 -y 2015',
                )
    parser.add_argument('--root', action="store", dest="root", 
                default=os.getcwd(),
                help='Root path to start folders'
                )
    parser.add_argument('--prefix', action="store", dest="prefix", 
                default='',
                help='Name prefix for years, e.g. --prefix "Bank statements "'
                )
    args = parser.parse_args()
    i = 0
    years = args.years if len(args.years) > 0 else [datetime.now().year]
    for year in args.years:
        names = [strftime('%Y-%m %b', (year, month,1,0,0,0,0,0,0)) for month in range(1,13)]
        parent = os.path.join(args.root, "{}{}".format(args.prefix, str(year)))
        if not os.path.exists(parent):
            os.makedirs(parent)
        for name in names:
            try:
                os.mkdir(os.path.join(parent, name))
                i += 1
            except:
                print("Error creating folder {}".format(name))
                pass
    print("Created {} folders under {}".format(i, parent))
        
    


