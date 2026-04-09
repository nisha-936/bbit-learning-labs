#Uncomment line above & run cell to save solution
#TODO Define class that implements portFolioInterface & allows for the management of a portfolio

from typing import Set, Iterable
from interfaces.portfolioInterface import portfolioInterface
from interfaces.accountInterface import accountInterface
from interfaces.securityInterface import securityInterface

class portfolio(portfolioInterface):
    def __init__(self, portfolioName: str, accounts: Set[accountInterface]) -> None:
        super().__init__(portfolioName, accounts)
        self.name = portfolioName
        self.accounts = dict()

        for a in accounts:
            self.accounts[a.getName()] = a

    def getAllAccounts(self) -> Iterable[accountInterface]:
        return list(self.accounts.values())

    def getAccounts(self, accountNamesFilter:Set[str], securitiesFilter:Set) -> Iterable[accountInterface]:
        if len(accountNamesFilter)==0 and len(securitiesFilter)==0:
            return self.getAllAccounts()

        filteredAccs = set()

        if len(accountNamesFilter) != 0:
            for a in accountNamesFilter:
                if a in self.accounts:
                    filteredAccs.add(self.accounts[a])
        else:
            filteredAccs = set(self.accounts.values())

        ret = set()

        if len(securitiesFilter) != 0:
            for a in filteredAccs:
                if len(a.getPositions(securitiesFilter)) > 0:
                    ret.add(a)
        else:
            ret = filteredAccs

        return ret


    def addAccounts(self, accounts: Set[accountInterface]) -> None:
        for a in accounts:
            self.accounts[a.getName()] = a

    def removeAccounts(self, accountNames: Set[str]) -> None:
        for a in accountNames:
            if a in self.accounts:
                self.accounts.pop(a)
