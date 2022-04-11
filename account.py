from datetime import date, timedelta;
from revenue import Revenue;
from expense import Expense;
from time import sleep;


class Account:

    Name: str;

    Revenues: list;

    Expenses: list;

    Total: float;

    def __init__(self, name):
        self.Name = name;
        self.Revenues = [];
        self.Expenses = [];
        self.Total = 0.00;

    def addEntry(self):
        isRevenue: bool = False;
        isExpense: bool = False;

        print("\nType of entry: \n");
        print("\n1. Revenue");
        print("\n2. Expense");
        print("\n3. CANCEL\n");

        sleep(1);

        selection = input();
        if(selection == "1"):
            isRevenue = True;
        elif(selection == "2"):
            isExpense = True;
        elif(selection == "3"):
            return;
        else:
            print("\n\nINVALID INPUT\n\n");
            self.addEntry();

        if(isRevenue):
            name = input("\nName of revenue: ");
            currDateRaw = date.today();
            currDate = currDateRaw.strftime("%d/%m/%Y");
            value = input("\nRevenue value €€.cc: ");

            try:
                value = float(value);
            except:
                print("\n\nInvalid input");
                self.addEntry();
            
            rev = Revenue(name, currDate, value);
            self.Revenues.append(rev);
            sleep(1);
            print("\nRevenue added.");
            self.Total += value;

        elif(isExpense):
            name = input("\nName of expense: ");
            currDateRaw = date.today();
            currDate = currDateRaw.strftime("%d/%m/%Y");
            value = input("\nExpense value €€.cc: ");

            try:
                value = float(value);
            except:
                print("\n\nInvalid input.");
                self.addEntry();
            
            exp = Expense(name, currDate, value);
            self.Expenses.append(exp);
            sleep(1);
            print("\nExpense added.");
            self.Total -= value;

    def removeEntry(self):
        isRevenue: bool;
        isExpense: bool;

        print("\n\nDelete entry: ");
        print("\n1. Delete revenue");
        print("\n2. Delete expense");
        print("\n3. CANCEL"); 

        sleep(1);                      

        selection: str = input();
        if(selection == "1"):
            isRevenue = True;
        elif(selection == "2"):
            isExpense = True;
        elif(selection == "3"):
            return;
        else:
            print("\n\nINVALID INPUT\n\n");
            self.removeEntry();
        
        if(isRevenue):
            counter: int = 1;

            print("\n\n0. CANCEL");
            for entry in reversed(self.Revenues):
                delta: timedelta = date.today() - entry.EntryDate;
                if(delta.days <= 90):
                    print("\n" + str(counter) + ". " + entry.EntryName);
                    print("\n   " + str(entry.EntryDate));
                    print("\n   " + str(entry.RevenueValue));
                counter += 1;
            
            sleep(1);
            
            selection: str = input("\n");
            last90Days: Revenue = [];
            for entry in reversed(self.Revenues):
                delta: timedelta = date.today() - entry.EntryDate;
                if(delta.days <= 90):
                    last90Days.append(entry);

            try: 
                selection = int(selection);
            except:
                print("\n\nInvalid input.");
                self.removeEntry();

            if((selection < 0) | len(last90Days) < selection):
                print("\n\nInvalid input");
                self.removeEntry();

            if(selection == 0):
                return;
            for entry in reversed(self.Revenues):
                if(entry == last90Days[selection - 1]):
                    self.Revenues.remove(entry);
                    self.Total -= entry.RevenueValue;
                    return; 
        
        if(isExpense):
            counter: int = 1;

            print("\n\n0. CANCEL");
            for entry in reversed(self.Expenses):
                delta: timedelta = date.today() - entry.EntryDate;
                if(delta.days <= 90):
                    print("\n" + str(counter) + ". " + entry.EntryName);
                    print("\n   " + str(entry.EntryDate));
                    print("\n   " + str(entry.ExpenseValue));
                counter += 1;
            
            sleep(1);
            
            selection: str = input("\n");
            last90Days: Revenue = [];
            for entry in reversed(self.Expenses):
                delta: timedelta = date.today() - entry.EntryDate;
                if(delta.days <= 90):
                    last90Days.append(entry);

            try: 
                selection = int(selection);
            except:
                print("\n\nInvalid input.");
                self.removeEntry();

            if((selection < 0) | len(last90Days) < selection):
                print("\n\nInvalid input");
                self.removeEntry();

            if(selection == 0):
                return;
            for entry in reversed(self.Expenses):
                if(entry == last90Days[selection - 1]):
                    self.Expenses.remove(entry);
                    self.Total += entry.ExpenseValue;
                    return;