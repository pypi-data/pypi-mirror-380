#!python
"""
This in example of how to customise the (default) settings of musicraft.
These partuclar customizations make sense t ome (Larry Myerscough) but are probably
of little or no interest to a wider world. They do, however, show how to add shortcuts,
additional to those defined in 'musicraft/abcraft/syntax.py'.
"""
import musicraft
print(f"!using musicraft from {musicraft.__file__}!")

from musicraft.abcraft.external import Ps2PDF, Svg2PDF
import datetime
Ps2PDF.exec_file = None  # use ghostscript internally
Ps2PDF.fmtNameOut = f'%s-cello-ps.pdf'
Svg2PDF.fmtNameOut = '%s-cello-svg.pdf'   # pdf via svg output is a fall-back if ever the pdf via ps route disappoints


# -----------------------------------------------------------------------------
# See 'musicraft_custom.py' for more customization options, better commented.
# This is a special customization to facilitate colouring note heads according to
# the assumed left hand position when playing the cello.

from musicraft.abcraft import AbcRaft
from musicraft.__main__ import MusicMain
from musicraft.abcraft.syntax import AbcHighlighter

AbcHighlighter.snippets.update(
    {
        '1=' : (r'"^$21="[I:voicecolor #000000]',),
        '1\\': (r'"^$21\\"[I:voicecolor #504000]',),
        '1/' : (r'"^$21/"[I:voicecolor purple]',),
        '2-' : (r'"^$22-"[I:voicecolor #008000]',),
        '3=' : (r'"^$23="[I:voicecolor #000080]',),
        '3/' : (r'"^$23/"[I:voicecolor #007070]',),
        '4\\': (r'"^$24\\"[I:voicecolor #800000]',),
    }
)
#
MusicMain().main(
    Plugins=(AbcRaft,
             )
)
