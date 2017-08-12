# rootnotes

Python module for integrating ROOT plots into jupyter notebooks.

## Description

Helper module for displaying ROOT canvases in ipython notebooks

Usage example:
    # Save this file as rootnotes.py to your working directory.
    
    import rootnotes
    c1 = rootnotes.canvas()
    fun1 = TF1( 'fun1', 'abs(sin(x)/x)', 0, 10)
    c1.SetGridx()
    c1.SetGridy()
    fun1.Draw()
    c1

More examples: http://mazurov.github.io/webfest2013/

@author alexander.mazurov@cern.ch
@author andrey.ustyuzhanin@cern.ch
@date 2013-08-09

Developed more by Ryan Reece <ryan.reece@cern.ch>
@author ryan.reece@cern.ch
@date 2016-11-08

## Author

Ryan Reece  <ryan.reece@cern.ch>

## License

Copyleft 2009-2017 Ryan Reece     
License: GPL <http://www.gnu.org/licenses/gpl.html>

## TODOs

-   Explain things better.


**Created:** 2016-11-08
