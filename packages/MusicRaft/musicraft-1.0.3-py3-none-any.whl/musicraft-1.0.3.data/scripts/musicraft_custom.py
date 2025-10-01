#!python
"""
This in example of how to customise the (default) settings of musicraft.
The script name reflects the fact that the primary customisation in effect
concerns "Timidity", but several other possibilities are shown, some of
 them in 'commented out' form.
Copyright 2020 Larry Myerscough
"""
import musicraft
print(f"!using musicraft from {musicraft.__file__}!")
# -----------------------------------------------------------------------------
# import the code of the plugins we intend to launch 'on the raft':
from musicraft.abcraft import AbcRaft
from musicraft.pyraft import PyRaft
# -----------------------------------------------------------------------------
# import the code to start 'the raft':
from musicraft.__main__ import MusicMain
# -----------------------------------------------------------------------------
# but first let's do some tweaking (customisation)...

# -----------------------------------------------------------------------------
# select a specific MIDI output port name (this is useful for my ubuntu setup)
#from musicraft.abcraft.midiplayer import MidiPlayer
#MidiPlayer.outputPort = 'TiMidity:TiMidity port 0 128:0'
#  comment the above two lines out if you want to stick with default midi output.

# -----------------------------------------------------------------------------
# The overrules below would probably unnecessary if I'd' been more rigorous with encoding matters:
# Overrule text encoding to use when creating PDF
# (The underlying problem disappears if I use the 7-bit ASCII sequences for accented characters
# as described in the abc plus manual... but that oughtn't to be necesary in this day and age!)
#
from musicraft.raft import External
External.encoding = 'latin1'

# Produce PDFs both via the svg and postscript route and make it clear which is which.
# This is particularly handy when using special ps or svg definitions in fmt files.
#
from musicraft.abcraft.external import Ps2PDF, Svg2PDF
import datetime
Ps2PDF.exec_file = None  # use ghostscript internally
# N.B. time stamped into pdf name is start-up time of musicraft, not derivation time of PDF
Ps2PDF.fmtNameOut = f'%s-{datetime.date.today().strftime("%d_%b_%Y")}.pdf'

# enable the following line to also create PDFs via the 'svg' route at every explicit save.
Svg2PDF.fmtNameOut = '%s-svg.pdf' # currently this only works under Linux.

# -----------------------------------------------------------------------------
# enable the following lines to select a different directory for the abc2midi program.
# from musicraft.abcraft.external import Abc2midi
# Abc2midi.exec_dir = '/usr/local/bin/'
# # ... and maybe tweak the way musicraft parses the output of abc2mdi ...
# Abc2midi.reMsg = r'.*in\s+line-char\s(\d+)\-(\d+).*'
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# # enable the following lines to select a different docking scheme
# # for the various components of 'the raft'.
# from musicraft import QtCore, EditBook, StdBook, DisplayBook
# EditBook.whereToDock = QtCore.Qt.RightDockWidgetArea
# StdBook.whereToDock = QtCore.Qt.RightDockWidgetArea
# DisplayBook.whereToDock = QtCore.Qt.LeftDockWidgetArea


# -----------------------------------------------------------------------------
# 'PyRaft' works but is not needed for general use. Disable this if you wish!
# FreqRaft is currently disabled because it is (forever?) unfinished.
#
MusicMain().main(
    Plugins=(AbcRaft,
             PyRaft,
           #  FreqRaft,
             )
)
