#!python
"""
'run_muscraft.py' is practically equivalent to 'python -m musicraft', but may be more convenient in
some operational contexts.
"""

# -----------------------------------------------------------------------------
# import the code of the plugins we intend to launch 'on the raft':
from musicraft.abcraft import AbcRaft
from musicraft.pyraft import PyRaft
# -----------------------------------------------------------------------------
# import the code to start 'the raft':
from musicraft.__main__ import MusicMain

# -----------------------------------------------------------------------------
# # enable the following lines to select a different docking scheme
# # for the various components of 'the raft'.
# from musicraft import QtCore, EditBook, StdBook, DisplayBook
# EditBook.whereToDock = QtCore.Qt.RightDockWidgetArea
# StdBook.whereToDock = QtCore.Qt.RightDockWidgetArea
# DisplayBook.whereToDock = QtCore.Qt.LeftDockWidgetArea


# -----------------------------------------------------------------------------
# now call the 'raft' with the 'abcraft' plugin;
# 'PyRaft' works bu is not needed for general use. Disable this if you wish!
# FreqRaft is currently disabled because it is (forever?) unfinished.
#
MusicMain().main(
    Plugins=(AbcRaft,
             PyRaft,
           #  FreqRaft,
             )
)
