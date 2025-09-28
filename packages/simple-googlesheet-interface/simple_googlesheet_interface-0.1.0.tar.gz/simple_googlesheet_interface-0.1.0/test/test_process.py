# -*- coding: utf-8 -*-

# ====== IMPORTS ===============

from _test_settings_ import USE_INSTALLED_PACKAGE
from _google_sheet_configuration_settings_ import SHEET_ID, SERVICE_ACCOUNT_FILE

if USE_INSTALLED_PACKAGE :
    from simple_googesheet_interface import GoogleSheetInterface
else:
    import sys
    sys.path.append('.')
    from src.simple_googesheet_interface import GoogleSheetInterface

# ===== TEST =======

interface = GoogleSheetInterface(SHEET_ID, SERVICE_ACCOUNT_FILE)

read = interface.read('A1:B5')

print(read)

values = [
            ["hello", "world"],
            ["hola", "mundo"],
            ["hola", "mundo"],
            ["hola", "mundo"],
            ["hola", "=max(9,6)"]
]  

write = interface.write('A1:B5',values)

print(write)

clear = interface.clear("A1:B2")

print(clear)