# -*- coding: utf-8 -*-
"""
Provides a connector to the Nakala research repository.

:copyright: The pyHeimdall contributors.
:licence: Afero GPL, see LICENSE for more details.
:SPDX-License-Identifier: AGPL-3.0-or-later
"""  # nopep8: E501


from .objects import (
    PROD_URL, TEST_URL,
    Uploadable, Collection, Data, File,
    _exception,  # TODO remove
    )
from .create import upload
from .read import getDatabase, update_presets, ITEM_EID, FILE_EID


__version__ = '0.9.2'
__all__ = [
        'getDatabase', 'upload', 'update_presets',
        'Uploadable', 'Collection', 'Data', 'File',
        'PROD_URL', 'TEST_URL',
        '__version__',  '__copyright__', '__license__',
        '_exception',  # TODO remove
    ]
__copyright__ = "Copyright the pyHeimdall contributors."
__license__ = 'AGPL-3.0-or-later'
