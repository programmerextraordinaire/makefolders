# makefolders
Python program to quickly make monthly folders for a given year or range of years.
The program defaults to the current year and current directory path.

Examples:

`python makefolders.py `

    /(current directory) 
        /2016 (current year) 
            /2016-01 Jan 
            /2016-02 Feb 
            ... 
            /2016-12 Dec
        

`python makefolders.py --root /root -y 2015 -y 2016 --prefix "Bills "`

    /root
        /Bills 2015
           /2015-01 Jan
           /2015-02 Feb
           ...
           /2015-12 Dec
        /Bills 2016
           /2016-01 Jan
           /2016-02 Feb
           ...
           /2016-12 Dec`
