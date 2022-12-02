#-----------------------------------------------------------------------------
# Copyright (c) 2005-2021, PyInstaller Development Team.
#
# Distributed under the terms of the GNU General Public License (version 2
# or later) with exception for distributing the bootloader.
#
# The full license is in the file COPYING.txt, distributed with this software.
#
# SPDX-License-Identifier: (GPL-2.0-or-later WITH Bootloader-exception)
#-----------------------------------------------------------------------------
from PyInstaller.utils.hooks.qt import pyqt5_library_info, \
    get_qt_binaries, get_qt_conf_file

# Only proceed if PyQt5 can be imported.
if pyqt5_library_info.version is not None:
    hiddenimports = [
        # PyQt5.10 and earlier uses sip in an separate package;
        'sip',
        # PyQt5.11 and later provides SIP in a private package. Support both.
        'PyQt5.sip'
    ]

    # Collect the ``qt.conf`` file.
    datas = get_qt_conf_file(pyqt5_library_info)

    # Collect required Qt binaries.
    binaries = get_qt_binaries(pyqt5_library_info)