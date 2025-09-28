"""
This file is part of OpenSesame.

OpenSesame is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

OpenSesame is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with OpenSesame.  If not, see <http://www.gnu.org/licenses/>.
"""

__author__ = "Bob Rosbag"
__license__ = "GPLv3"

from libopensesame.py3compat import *
from libopensesame.item import Item
from libqtopensesame.items.qtautoplugin import QtAutoPlugin
from libopensesame.exceptions import OSException
from libopensesame.oslogging import oslogger


class RadboudboxInit(Item):

    def reset(self):
        self.var.dummy_mode = 'no'
        self.var.verbose = 'yes'
        self.var.id = 'autodetect'
        self.var.port = 'autodetect'
        self.var.extended_mode = 'yes'

    def prepare(self):
        super().prepare()
        self.verbose = 'yes'
        self.close()
        self._init_var()
        self._check_init()

        if self.dummy_mode == 'no':
            try:
                from rusocsci import buttonbox
                from rusocsci import extended
            except ImportError:
                self._show_message('The RuSocSci package could not be imported. Please install package.')
            try:
                if self.var.extended_mode == 'no':
                    self.experiment.radboudbox = buttonbox.Buttonbox(id=self.id,
                                                                     port=self.port)
                elif self.var.extended_mode == 'yes':
                    self.experiment.radboudbox = extended.Extended(id=self.id,
                                                                     port=self.port)
                self.clock.sleep(4000)
                self.experiment.cleanup_functions.append(self.close)
                # self.python_workspace['radboudbox'] = self.experiment.radboudbox
            except OSError:
                self._show_message('Could not access the Radboud Buttonbox')
        elif self.dummy_mode == 'yes':
            self._show_message('Dummy mode enabled, prepare phase')
        else:
            self._show_message(f'Error with dummy mode, dummy mode: {self.dummy_mode}')

    def run(self):
        self.set_item_onset()

    def close(self):
        if not hasattr(self.experiment, "radboudbox") or \
            self.experiment.radboudbox is None:
            self._show_message("No active radboudbox")
            return
        try:
            self.experiment.radboudbox.clearEvents()
            self.experiment.radboudbox.close()
            self.experiment.radboudbox = None
            self._show_message("Radboudbox closed")
        except:
            self._show_message("Failed to close radboudbox")

    def _check_init(self):
        if hasattr(self.experiment, 'radboudbox'):
            raise OSException('You should have only one instance of `radboudbox_init` in your experiment')

    def _init_var(self):
        self.dummy_mode = self.var.dummy_mode
        self.verbose = self.var.verbose
        self.experiment.radboudbox_extended_mode = self.var.extended_mode
        self.experiment.radboudbox_dummy_mode = self.var.dummy_mode
        self.experiment.radboudbox_verbose = self.var.verbose
        self.experiment.radboudbox_get_buttons_locked = 0
        self.experiment.radboudbox_get_buttons = None
        #self.experiment.radboudbox_get_buttons_wait = None
        #self.experiment.radboudbox_get_buttons_start = None

        if self.var.id == 'autodetect':
            self.id = 0
        else:
            self.id = self.var.id

        if self.var.port == 'autodetect':
            self.port = None
        else:
            self.port = self.var.port

    def _show_message(self, message):
        oslogger.debug(message)
        if self.verbose == 'yes':
            print(message)


class QtRadboudboxInit(RadboudboxInit, QtAutoPlugin):

    def __init__(self, name, experiment, script=None):
        RadboudboxInit.__init__(self, name, experiment, script)
        QtAutoPlugin.__init__(self, __file__)

