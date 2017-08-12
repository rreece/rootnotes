"""
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
2016-11-08
"""

import ROOT
ROOT.gROOT.SetBatch()

import os
import tempfile
import base64
#from IPython.core import display
from IPython import display


#_______________________________________________________________________________
def canvas(name="icanvas", size=(800, 600)):
    """Helper method for creating canvas"""
    # Check if icanvas already exists
    c = ROOT.gROOT.FindObject(name)
    assert len(size) == 2
    if c:
        return c
    else:
        return ROOT.TCanvas(name, name, size[0], size[1])


#_______________________________________________________________________________
def _canvas_to_html(c):
    f = tempfile.NamedTemporaryFile(suffix=".png")
    fn = f.name
    c.SaveAs(fn)
    encoded_png = base64.b64encode(open(fn).read())
    html = '<img style="width: 100%%; margin: 0px; float: left; border: 1px solid gray;" src="data:image/png;base64,%s" />' % encoded_png
    return html


#_______________________________________________________________________________
def _display_canvas(c):
    html = _canvas_to_html(c)
    x = display.HTML(html)
    return x._repr_html_()


#_______________________________________________________________________________
def _display_any(obj):
    """
    obj can be any Draw()able ROOT type.
    """
    file = tempfile.NamedTemporaryFile(suffix=".png")
    obj.Draw()
    ROOT.gPad.SaveAs(file.name)
    ip_img = display.Image(filename=file.name, format='png', embed=True)
    return ip_img._repr_png_()


#_______________________________________________________________________________
def _display_list(_list):
    """
    _list entries must be of type dict or TCanvas.
    """
    htmls = list()
    for c in _list:
        if isinstance(c, dict):
            htmls.append( _dict_to_html(c) )
        elif isinstance(c, ROOT.TCanvas):
            htmls.append( _canvas_to_html(c) )
    if htmls:
        html = '\n'.join(htmls)
        x = display.HTML(html)
        return x._repr_html_()
    else:
        return repr(_list)


#_______________________________________________________________________________
def _dict_to_html(d):
    htmls = list()
    if d.has_key('canvas'):
        htmls.append( _canvas_to_html(d['canvas']) )
    if d.has_key('html'):
        htmls.append( d['html'] )
    if htmls:
        html = ''
        if htmls:
            html = '\n'.join(htmls)
        return html
    else:
        return repr(d)


#_______________________________________________________________________________
def _display_dict(d):
    html = _dict_to_html(d)
    x = display.HTML(html)
    return x._repr_html_()


#_______________________________________________________________________________
## register display function with PNG formatter:
png_formatter = get_ipython().display_formatter.formatters['image/png']  # noqa

## Register ROOT types in ipython
##
##   In  [1]: canvas = rootnotes.canvas()
##   In  [2]: canvas
##   Out [2]: [image will be here]
#png_formatter.for_type(ROOT.TCanvas, _display_canvas)
png_formatter.for_type(ROOT.TF1, _display_any)

html_formatter = get_ipython().display_formatter.formatters['text/html']
html_formatter.for_type(list, _display_list)
html_formatter.for_type(dict, _display_dict)
html_formatter.for_type(ROOT.TCanvas, _display_canvas)


