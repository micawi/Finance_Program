from datetime import date;


class Entry:

    EntryName: str;

    EntryDate: date;

    def __init__(self, entryName, entryDate):
        self.EntryName = entryName;
        self.EntryDate = entryDate;