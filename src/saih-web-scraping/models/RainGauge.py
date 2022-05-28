class RainGauge:
    '''
        Device that gather information about temperature and pluviometry.
    '''

    def __init__(self, place, urlPluviometry, urlTemperature):
            self.place = place
            self.urlPluviometry = urlPluviometry
            self.urlTemperature = urlTemperature