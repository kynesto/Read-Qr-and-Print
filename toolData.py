import datetime

class Tool():
    def put(self, ToolInfo):
        self.Customer = ToolInfo[13]
        self.MaterialNr= ToolInfo[12]
        self.DrawingNr = ToolInfo[6]
        self.dateTimeInstance = datetime.datetime.now()
        self.Kw = self.dateTimeInstance.isocalendar()[1]
        self.Year = self.dateTimeInstance.isocalendar()[0]
        self.KwDate = F"{self.Kw}/{self.Year}"
        self.FA = ToolInfo[1]
