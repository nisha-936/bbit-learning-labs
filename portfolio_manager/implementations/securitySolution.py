#Uncomment line above & run cell to save solution
#TODO Define class that implements securityInterface & allows for the management of a security

import os
import sys
module_path = os.path.abspath('..')
if module_path not in sys.path:
    sys.path.append(module_path)

from interfaces.securityInterface import securityInterface

class security(securityInterface):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.name = name

    def getName(self) -> str:
        return self.name

    def setName(self, name: str) -> None:
        self.name = name
