# -*- coding: utf-8 -*-
"""
simple_gsheet_interface: Module to work with the most simple version with Google Sheets: READ, WRITE and CLEAR data from an existing spreadsheet of Google
"""
__author__  = "Robert Rijnbeek"
__email__   = "robert270384@gmail.com"
__version__ = "0.1.0"

# ============ IMPORTS =============

from typing import Callable
from functools import wraps

from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build, Resource

# ========= BASE PARAMETERS ========

SCOPES = ["https://spreadsheets.google.com/feeds"]

# == GOOGLE SHEET INTERFACE CLASS ==
class GoogleSheetInterface():
    """
    Class that allow you to interact with an Google spreadsheet in the form of:

    * READ: Read information from an Google spreadsheet.
    * WRITE: Write information to an Google spreadsheet.
    * CLEAR: Clear information to an Google spreadsheet.
    """
    def __init__(self,SheetID: str, service_account_file_location: str) -> None:
        # Make it possible to read, write and clear information from an spreadsheet
        self.SCOPES = SCOPES 
        # Needed parameters to acces to an epecific Google spreadsheet
        self.SERVICE_ACCOUNT_FILE = service_account_file_location
        self.SHEET_ID = SheetID
        # Internal parameters of the class
        self.active = False
        self.CREDENTIALS = None
        self.SERVICE = None
        self.SHEET= None
        # Initialize method that put it active if the acces parameters are right
        self.__initialize()

    # ===== INITIALIZE FUNCTION =====

    def __initialize(self) -> bool:
        """
        Method that make access to the Google spreadsheet document. And if the access is correct it activate the class to be used.
        """
        try: 
            self.CREDENTIALS = Credentials.from_service_account_file(self.SERVICE_ACCOUNT_FILE, scopes = self.SCOPES)
            self.SERVICE: Resource = build("sheets", "v4", credentials=self.CREDENTIALS)
            self.SHEET = self.SERVICE.spreadsheets()
            self.active = True
            print("GoogleSheetInterface() is now active and operational")
            return True
        except Exception as exc:
            print(f"ERROR: Problems initializing GoogleSheetInterface()\n\n {exc}")
            return False
    
    # ====== DECORATOR =======

    @staticmethod
    def __is_active_method(func: Callable) -> Callable:
        """
        Decorator method that virify if GoogleSheetInterface() Class is active. 
        * If it is active it allow you to use the method. 
        * If it is not active. Than it rais al exception error when you usig it
        """
        @wraps(func)
        def new_func(self, *args, **kwargs):
            if not self.active:
                raise Exception("ERROR: Class is inactive")
            return func(self, *args, **kwargs)
        return new_func

    
    # ===== CLASS METHODS =====

    @__is_active_method
    def read(self, RANGE: str, **kwargs) -> list[list]:
        """
        Class method that read information from Google spreadsheet defined in the 'RANGE'
        """
        try:
            sheet_read = self.SHEET.values().get(spreadsheetId=self.SHEET_ID ,range=RANGE, **kwargs).execute()
            return sheet_read.get("values", [])
        except Exception as exc:
            print(f"ERROR: {exc}")
            return False
    
    
    @__is_active_method
    def write(self, RANGE: str, VALUES: list[list], valueInputOption: str ='USER_ENTERED', **kwargs) -> dict:
        """
        Class method that write information from Google spreadsheet defined in the 'RANGE' and 'VALUES'
        """
        try:
            body = {"values": VALUES}
            return self.SHEET.values().update(spreadsheetId=self.SHEET_ID, range=RANGE, body=body, valueInputOption=valueInputOption, **kwargs).execute() #RAW
        except Exception as exc:
            print(f"ERROR: {exc}")
            return False
        
    
    @__is_active_method
    def clear(self, RANGE: str, **kwargs) -> dict:
        """
        Class method that clear information from Google spreadsheet difined in the 'RANGE'
        """
        try:
            return self.SHEET.values().clear(spreadsheetId=self.SHEET_ID ,range=RANGE, **kwargs).execute()
        except Exception as exc:
            print(f"ERROR: {exc}")
            return False

    # =============== EXECUTE TEST CODE ==============

if __name__ == "__main__":

    pass
    