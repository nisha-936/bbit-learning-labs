#Uncomment line above & run cell to save solution
#TODO Define class that implements accountInterface & allows for the management of an account

import os
import sys
module_path = os.path.abspath('..')
if module_path not in sys.path:
    sys.path.append(module_path)

from interfaces.accountInterface import accountInterface
from interfaces.positionInterface import positionInterface
from interfaces.securityInterface import securityInterface
from typing import Iterable, Set, Dict, Any

class account(accountInterface):
    def __init__(self, positions: set, name: str) -> None:
        self.name = name
        self.positions = dict()

        for position in positions:
            self.positions[position.getSecurity().getName()] = position

    def getName(self) -> str:
        return self.name

    def getAllPositions(self) -> Iterable[positionInterface]:
        return list(self.positions.values())

    def getPositions(self, securities: Set) -> Dict[Any, positionInterface]:
        ret = dict()

        for s in securities:
            if isinstance(s, securityInterface) and s.getName() in self.positions:
                ret[s] = self.positions[s.getName()]
            elif s in self.positions:
                ret[s] = self.positions[s]

        return ret

    def addPositions(self, positions: Set[positionInterface]) -> None:
        for p in positions:
            if p.getSecurity().getName() in self.positions:
                self.positions[p.getSecurity().getName()].setPosition(p.getPosition())
            else:
                self.positions[p.getSecurity().getName()] = p

    #Remove a number of positions from this account if they represent a security in a given input set
    def removePositions(self, securities: Set) -> None:
        for s in securities:
            if isinstance(s, securityInterface) and s.getName() in self.positions:
                self.positions.pop(s.getName())
            elif s in self.positions:
                self.positions.pop(s)
