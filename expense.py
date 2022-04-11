from entry import Entry;


class Expense(Entry):

    ExpenseValue: float;

    def __init__(self, entryName, entryDate, expenseValue):
        self.ExpenseValue = expenseValue;
        super().__init__(entryName, entryDate);