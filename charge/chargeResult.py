#-*-coding:utf-8-*-

class ChargeResult(object):
    def __init__(self):
        self.all_assets = 100000
        self.max_lost = 0
        self.max_get = 0
        self.lost_time = 0
        self.get_time = 0
        self.total_lost = 0
        self.total_get = 0
        self.asset_array = []

    def clearResult(self):
        self.all_assets = 100000
        self.max_lost = 0
        self.max_get = 0
        self.lost_time = 0
        self.get_time = 0
        self.total_lost = 0
        self.total_get = 0

    def printResult(self):
        print "all_assets = %.2f" %self.all_assets
        print "max_get = %.2f"%self.max_get + "%"
        print "max_lost = %.2f"%self.max_lost + "%"
        print "get_time = %.f" %self.get_time
        print "lost_time = %.f" %self.lost_time
        print "total_get = %.2f" %self.total_get + "%"
        print "total_lost = %.2f" %self.total_lost + "%"
        print "average_get = %.2f" %(self.total_get/self.get_time) + "%"
        print "average_lost = %.2f" % (self.total_lost/ self.lost_time) + "%"