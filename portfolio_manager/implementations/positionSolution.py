#Uncomment line above & run cell to save solution
#TODO Define class that implements positionInterface & allows for the management of a position

import os
import sys
module_path = os.path.abspath('..')
if module_path not in sys.path:
    sys.path.append(module_path)

from interfaces.positionInterface import positionInterface
from interfaces.securityInterface import securityInterface
from implementations.securitySolution import security

class position(positionInterface):
    def __init__(self, securityIn, initialPosition: int) -> None:
        super().__init__(securityIn, initialPosition)

        if initialPosition < 0:
            raise Exception()

        self.positionVal = initialPosition

        if isinstance(securityIn, securityInterface):
            self.security = securityIn
        else:
            self.security = security(securityIn)

    def getSecurity(self) -> security:
        return self.security

    def getPosition(self) -> int:
        return self.positionVal

    def setPosition(self, inputValue: int) -> None:
        if inputValue < 0:
            raise Exception()
        self.positionVal = inputValue

    def addPosition(self, inputValue: int) -> None:
        if self.positionVal+inputValue < 0:
            raise Exception

        self.positionVal += inputValue
