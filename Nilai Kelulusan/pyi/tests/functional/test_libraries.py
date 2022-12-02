# -*- coding: utf-8 -*-
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

# Library imports
# ---------------
import os

# Third-party imports
# -------------------
import pytest
import py

# Local imports
# -------------
from PyInstaller.compat import is_win, is_darwin, is_linux
from PyInstaller.utils.tests import importorskip, xfail, skipif, requires

# :todo: find a way to get this from `conftest` or such
# Directory with testing modules used in some tests.
_MODULES_DIR = py.path.local(os.path.abspath(__file__)).dirpath('modules')
_DATA_DIR = py.path.local(os.path.abspath(__file__)).dirpath('data')


@importorskip('gevent')
def test_gevent(pyi_builder):
    pyi_builder.test_source(
        """
        import gevent
        gevent.spawn(lambda: x)
        """,
        # reduce footprint of the test (and avoid issued introduced by one of
        # these packages breaking)
        excludes=["PySide2", "PyQt5", "numpy", "scipy"])


@importorskip('gevent')
def test_gevent_monkey(pyi_builder):
    pyi_builder.test_source(
        """
        from gevent.monkey import patch_all
        patch_all()
        """,
        # reduce footprint of the test (and avoid issued introduced by one of
        # these packages breaking)
        excludes=["PySide2", "PyQt5", "numpy", "scipy"])


@xfail(is_darwin, reason='Issue #1895.')
def test_tkinter(pyi_builder):
    pyi_builder.test_script('pyi_lib_tkinter.py')


def test_pkg_resource_res_string(pyi_builder, monkeypatch):
    # Include some data files for testing pkg_resources module.
    datas = os.pathsep.join((str(_MODULES_DIR.join('pkg3', 'sample-data.txt')),
                             'pkg3'))
    pyi_builder.test_script('pkg_resource_res_string.py',
                            pyi_args=['--add-data', datas])


def test_pkgutil_get_data(pyi_builder, monkeypatch):
    # Include some data files for testing pkg_resources module.
    datas = os.pathsep.join((str(_MODULES_DIR.join('pkg3', 'sample-data.txt')),
                             'pkg3'))
    pyi_builder.test_script('pkgutil_get_data.py',
                            pyi_args=['--add-data', datas])


@xfail(
    reason='Our import mechanism returns the wrong loader-class for __main__.'
)
def test_pkgutil_get_data__main__(pyi_builder, monkeypatch):
    # Include some data files for testing pkg_resources module.
    datas = os.pathsep.join((str(_MODULES_DIR.join('pkg3', 'sample-data.txt')),
                             'pkg3'))
    pyi_builder.test_script('pkgutil_get_data__main__.py',
                            pyi_args=['--add-data', datas])


@importorskip('sphinx')
def test_sphinx(tmpdir, pyi_builder, data_dir):
    # Note that including the data_dir fixture copies files needed by this test
    pyi_builder.test_script('pyi_lib_sphinx.py')


@importorskip('pygments')
def test_pygments(pyi_builder):
    pyi_builder.test_source(
        """
        # This sample code is taken from http://pygments.org/docs/quickstart/.
        from pygments import highlight
        from pygments.lexers import PythonLexer
        from pygments.formatters import HtmlFormatter

        code = 'print "Hello World"'
        print(highlight(code, PythonLexer(), HtmlFormatter()))
        """)


@requires('zope.interface')
def test_zope_interface(pyi_builder):
    # Tests that `nspkg.pth`-based namespace package are bundled properly.
    # The `nspkg.pth` file is created by setuptools and thus changes
    # frequently. If this test fails most propably
    # _SETUPTOOLS_NAMESPACEPKG_PTHs in modulegraph needs to be updated.
    pyi_builder.test_source(
        """
        # Package 'zope' does not contain __init__.py file.
        # Just importing 'zope.interface' is sufficient.
        import zope.interface
        """)


@importorskip('idlelib')
def test_idlelib(pyi_builder):
    pyi_builder.test_source(
        """
        # This file depends on loading some icons, located based on __file__.
        try:
            import idlelib.TreeWidget
        except:
            import idlelib.tree
        """)


@importorskip('keyring')
@skipif(is_linux, reason="SecretStorage backend on linux requires active "
                         "D-BUS session and initialized keyring, and may "
                         "need to unlock the keyring via UI prompt.")
def test_keyring(pyi_builder):
    pyi_builder.test_source(
        """
        import keyring
        keyring.get_password("test", "test")
        """)


@importorskip('numpy')
def test_numpy(pyi_builder):
    pyi_builder.test_source(
        """
        import numpy
        from numpy.core.numeric import dot
        print('dot(3, 4):', dot(3, 4))
        """)


@importorskip('pytz')
def test_pytz(pyi_builder):
    pyi_builder.test_source(
        """
        import pytz
        pytz.timezone('US/Eastern')
        """)


@importorskip('requests')
def test_requests(tmpdir, pyi_builder, data_dir, monkeypatch):
    # Note that including the data_dir fixture copies files needed by this test.
    # Include the data files.
    datas = os.pathsep.join((str(data_dir.join('*')), os.curdir))
    pyi_builder.test_script('pyi_lib_requests.py',
                            pyi_args=['--add-data', datas])


@importorskip('urllib3.packages.six')
def test_urllib3_six(pyi_builder):
    # Test for pre-safe-import urllib3.packages.six.moves.
    pyi_builder.test_source("""
        import urllib3.connectionpool
        import types
        assert isinstance(urllib3.connectionpool.queue, types.ModuleType)
        """)


@importorskip('sqlite3')
def test_sqlite3(pyi_builder):
    pyi_builder.test_source(
        """
        # PyInstaller did not included module 'sqlite3.dump'.
        import sqlite3
        conn = sqlite3.connect(':memory:')
        csr = conn.cursor()
        csr.execute('CREATE TABLE Example (id)')
        for line in conn.iterdump():
             print(line)
        """)


# Note that @importorskip('scapy') isn't sufficient; this doesn't ask scapy to
# import its backend dependencies (such as pcapy or dnet). scapy.all does import
# the backends, skipping this test if they aren't installed.
@requires('scapy >= 2.0')
def test_scapy(pyi_builder):
    pyi_builder.test_source(
        """
        # Test-cases taken from issue #834
        import scapy.all
        scapy.all.IP

        from scapy.all import IP

        # Test-case taken from issue #202.
        from scapy.all import *
        DHCP # scapy.layers.dhcp.DHCP
        BOOTP # scapy.layers.dhcp.BOOTP
        DNS # scapy.layers.dns.DNS
        ICMP # scapy.layers.inet.ICMP
        """)


@requires('scapy >= 2.0')
def test_scapy2(pyi_builder):
    pyi_builder.test_source(
        """
        # Test the hook to scapy.layers.all
        from scapy.layers.all import DHCP
        """)


@requires('scapy >= 2.0')
def test_scapy3(pyi_builder):
    pyi_builder.test_source(
        """
        # Test whether
        # a) scapy packet layers are not included if neither scapy.all nor
        #    scapy.layers.all are imported.
        # b) packages are included if imported explicitly

        # This test-case assumes, that layer modules are imported only if
        NAME = 'hook-scapy.layers.all'
        layer_inet = 'scapy.layers.inet'

        def testit():
            try:
                __import__(layer_inet)
                raise SystemExit('Self-test of hook %s failed: package module found'
                                 % NAME)
            except ImportError, e:
                if not e.args[0].endswith(' inet'):
                    raise SystemExit('Self-test of hook %s failed: package module found'
                                    ' and has import errors: %r' % (NAME, e))

        import scapy
        testit()
        import scapy.layers
        testit()
        # Explicitly import a single layer module. Note: This module MUST NOT
        # import inet (neither directly nor indirectly), otherwise the test
        # above fails.
        import scapy.layers.ir
        """)


@importorskip('sqlalchemy')
def test_sqlalchemy(pyi_builder):
    pyi_builder.test_source(
        """
        # The hook behaviour is to include with sqlalchemy all installed database
        # backends.
        import sqlalchemy
        # This import was known to fail with sqlalchemy 0.9.1
        import sqlalchemy.ext.declarative
        """)


@importorskip('twisted')
def test_twisted(pyi_builder):
    pyi_builder.test_source(
        """
        # Twisted is an event-driven networking engine.
        #
        # The 'reactor' is object that starts the eventloop.
        # There are different types of platform specific reactors.
        # Platform specific reactor is wrapped into twisted.internet.reactor module.
        from twisted.internet import reactor
        # Applications importing module twisted.internet.reactor might fail
        # with error like:
        #
        #     AttributeError: 'module' object has no attribute 'listenTCP'
        #
        # Ensure default reactor was loaded - it has method 'listenTCP' to start server.
        if not hasattr(reactor, 'listenTCP'):
            raise SystemExit('Twisted reactor not properly initialized.')
        """)


@importorskip('pyexcelerate')
def test_pyexcelerate(pyi_builder):
    pyi_builder.test_source(
        """
        # Requires PyExcelerate 0.6.1 or higher
        # Tested on Windows 7 x64 SP1 with CPython 2.7.6
        import pyexcelerate
        """)


@importorskip('usb')
@pytest.mark.skipif(is_linux, reason='libusb_exit segfaults on some linuxes')
def test_usb(pyi_builder):
    # See if the usb package is supported on this platform.
    try:
        import usb
        # This will verify that the backend is present; if not, it will
        # skip this test.
        usb.core.find()
    except (ImportError, usb.core.NoBackendError):
        pytest.skip('USB backnd not found.')

    pyi_builder.test_source(
        """
        import usb.core
        # NoBackendError fails the test if no backends are found.
        usb.core.find()
        """)


@importorskip('zeep')
def test_zeep(pyi_builder):
    pyi_builder.test_source(
        """
        # Test the hook to zeep
        from zeep import utils
        utils.get_version()
        """)


@importorskip('PIL')
#@pytest.mark.xfail(reason="Fails with Pillow 3.0.0")
def test_pil_img_conversion(pyi_builder):
    datas = os.pathsep.join((str(_DATA_DIR.join('PIL_images')), '.'))
    pyi_builder.test_script(
        'pyi_lib_PIL_img_conversion.py',
        pyi_args=['--add-data', datas,
                  # Use console mode or else on Windows the VS() messageboxes
                  # will stall pytest.
                  '--console'])


@requires("pillow >= 1.1.6")
@importorskip('PyQt5')
def test_pil_PyQt5(pyi_builder):
    # hook-PIL is excluding PyQt5, but is must still be included
    # since it is imported elsewhere. Also see issue #1584.
    pyi_builder.test_source("""
    import PyQt5
    import PIL
    import PIL.ImageQt
    """)


@importorskip('PIL')
def test_pil_plugins(pyi_builder):
    pyi_builder.test_source(
        """
        # Verify packaging of PIL.Image.
        from PIL.Image import frombytes
        print(frombytes)

        # PIL import hook should bundle all available PIL plugins. Verify that plugins
        # are bundled.
        from PIL import Image
        Image.init()
        MIN_PLUG_COUNT = 7  # Without all plugins the count is usually 6.
        plugins = list(Image.SAVE.keys())
        plugins.sort()
        if len(plugins) < MIN_PLUG_COUNT:
            raise SystemExit('No PIL image plugins were bundled!')
        else:
            print('PIL supported image formats: %s' % plugins)
        """)


@importorskip('pandas')
def test_pandas_extension(pyi_builder):
    # Tests that the C extension ``pandas._libs.lib`` is properly bundled. Issue #1580.
    # See http://pandas.pydata.org/pandas-docs/stable/whatsnew.html#modules-privacy-has-changed.
    pyi_builder.test_source(
        """
        from pandas._libs.lib import is_float
        assert is_float(1) == 0
        """)


@importorskip('pandas')
@importorskip('jinja2')
def test_pandas_io_formats_style(pyi_builder):
    # pandas.io.formats.style requires jinja2 as hiddenimport, as
    # well as collected template file from pandas/io/formats/templates.
    # See #6008 and #6009.
    pyi_builder.test_source(
        """
        import pandas.io.formats.style
        """)


@importorskip('win32ctypes')
@pytest.mark.skipif(not is_win,
                    reason='pywin32-ctypes is supported only on Windows')
@pytest.mark.parametrize('submodule', ['win32api', 'win32cred', 'pywintypes'])
def test_pywin32ctypes(pyi_builder, submodule):
    pyi_builder.test_source("""
        from win32ctypes.pywin32 import {0}
        """.format(submodule))
