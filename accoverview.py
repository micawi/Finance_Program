import pickle;
import os
from account import Account
from entry import Entry
from revenue import Revenue;
from expense import Expense;
from time import sleep;

ProgramVersion: str = "1.0";

class AccOverview:

    AccountList: list;

    Total: float;

    StartUp: bool;

    def __init__(self):
        self.AccountList = self.loadAccounts();
        self.Total = self.calcTotal();
        self.StartUp = True;
    
    def loadAccounts(self):
        cwd: str = os.getcwd();
        saveDir: str = cwd + "/accdata/";

        if(os.path.exists(saveDir)):
            os.chdir(saveDir);
            allAccs = os.listdir();
            self.AccountList = [];
            for accName in allAccs:
                with open(accName, "rb") as f:                        
                    currAcc = pickle.load(f);
                    self.AccountList.append(currAcc);
            os.chdir(cwd);
            return self.AccountList;
        else:
            return [];

    def saveAccount(self, account: Account):
        cwd: str = os.getcwd();
        saveDir: str = cwd + "/accdata/";
        accName: str = account.Name;
        accFileName: str = saveDir + accName + ".dat";

        if(os.path.exists(saveDir)):
            with open(accFileName, "wb") as f:
                pickle.dump(account, f);
        
        else:
            os.mkdir(saveDir);
            with open(accFileName, "wb") as f:
                pickle.dump(account, f);
    
    def calcTotal(self):
        acc: Account;
        self.Total = 0.00;
        for acc in self.AccountList:
            rev: Revenue;
            for rev in acc.Revenues:
                self.Total += rev.RevenueValue;
            exp: Expense;
            for exp in acc.Expenses:
                self.Total -= exp.ExpenseValue;
        return self.Total;
    
    def showAccount(self, accnumber: int):
        currAcc: Account = self.AccountList[accnumber - 1];
        allEntries: list = currAcc.Revenues + currAcc.Expenses;

        print("\n\n\nAccount name: " + currAcc.Name);
        print("\n\nBALANCE: " + str(currAcc.Total));

        sleep(1.5);

        print("\n\n\n1. Show All");
        print("\n\n2. Show Revenues");
        print("\n\n3. Show Expenses");
        print("\n\n4. Add Entry");
        print("\n\n5. REMOVE ACCOUNT");
        print("\n\n6. BACK");
        selection: str = input("\n\n");

        sleep(1);

        try:
            selection = int(selection);
        except:
            print("\nInvalid input.");
            self.showAccount(accnumber);
        
        if(selection == 1):
            for entry in allEntries:
                if(type(entry) == Revenue):
                    print("\nRevenue: " + entry.EntryName);
                    print("\nValue: " + str(entry.RevenueValue));
                    print("\n***************************");
                elif(type(entry) == Expense):
                    print("\nExpense: " + entry.EntryName);
                    print("\nValue: " + str(-abs(entry.ExpenseValue)));
                    print("\n***************************");
            self.showAccount(accnumber);
        elif(selection == 2):
            for rev in allEntries:
                if(type(rev) == Revenue):
                    print("\nRevenue: " + rev.EntryName);
                    print("\nValue: " + str(rev.RevenueValue));
                    print("\n***************************");
            self.showAccount(accnumber);
        elif(selection == 3):
            for exp in allEntries:
                if(type(exp) == Expense):
                    print("\nExpense: " + exp.EntryName);
                    print("\nValue: " + str(-abs(exp.ExpenseValue)));
                    print("\n***************************");
            self.showAccount(accnumber);

        elif(selection == 4):
            currAcc.addEntry();
            self.saveAccount(currAcc);
            self.calcTotal();
            self.showAccount(accnumber);
        
        elif(selection == 5):
            self.deleteAccount(currAcc);
            return;
        
        elif(selection == 6):
            return;
        
        else:
            print("\n\nFALSE INPUT.");
            self.showAccount(accnumber);
        
        sleep(1);

    def mainMenu(self):
        if(self.StartUp):
            print("\n\nWelcome to Finance Program v. " + ProgramVersion);
            self.StartUp = False;
            sleep(1);
        
        print("\n\nYou have " + str(len(self.AccountList)) + " Accounts registered.");
        sleep(1);
        print("\nTOTAL BALANCE: " + str(self.Total));

        sleep(1);
        
        counter: int = 1;
        acc: Account;
        print("\n\nOPTIONS:\n");
        print("\n0. ADD ACCOUNT");
        for acc in self.AccountList:
            print("\n" + str(counter) + ". Show " + acc.Name);
            counter += 1;
        print("\n\n\n" + str(counter) + ". EXIT PROGRAM");
        selection: str = input("\n");

        try:
            selection = int(selection);
        except:
            print("\n\nINVALID INPUT");
            self.mainMenu();
        
        if((selection >= 0) & (selection <= len(self.AccountList) + 1)):
            if(selection == 0):
                print("\n\nAdding new account...");
                sleep(1);
                self.addAccount();
            elif(selection <= len(self.AccountList)):
                print("\n\nShowing account " + self.AccountList[selection - 1].Name);
                sleep(1);
                self.showAccount(selection);
            else:
                print("\n\nSee you next time.");
                sleep(2);
                for acc in self.AccountList:
                    self.saveAccount(acc);
                exit();
        else:
            print("\n\nINVALID INPUT");
            self.mainMenu();
        
        self.mainMenu();
    
    def addAccount(self):
        print("\n\nName of new account: ");
        newAccName: str = input("\n");
        newAcc: Account = Account(newAccName);
        self.AccountList.append(newAcc);
    
    def deleteAccount(self, acc: Account):
        sleep(1);
        print("\n\n0. CANCEL");
        print("\n\n1. CONFIRM DELETION");
        sleep(1);
        selection: str = input("\n");

        try:
            selection = int(selection);
        except:
            sleep(1);
            print("\n\nINVALID INPUT");
            self.deleteAccount();
        
        if(selection in {0, 1}):
            if(selection == 0):
                return;
            else:
                self.AccountList.remove(acc);

                cwd: str = os.getcwd();
                saveDir: str = cwd + "/accdata/";
                os.chdir(saveDir);
                os.remove(saveDir + acc.Name + ".dat");
                os.chdir(cwd);
                self.Total = self.calcTotal();
                return;
        else:
            sleep(1);
            print("\n\nWRONG INPUT");
            self.deleteAccount(acc);