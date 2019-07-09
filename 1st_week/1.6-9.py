class LoggableList(list, Loggable):
    def append(self, item):
        super().append(item)
        self.log(item)
