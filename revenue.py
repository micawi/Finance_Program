from entry import Entry;


class Revenue(Entry):

    RevenueValue: float;

    def __init__(self, entryName, entryDate, revenueValue):
        self.RevenueValue = revenueValue;
        super().__init__(entryName, entryDate);