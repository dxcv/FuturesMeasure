#-*-coding:utf-8-*-
from plot.plot import Plot
class ChargeResult(object):
    def __init__(self,total_day):
        self.all_assets = 100000
#最大获利最小获利
        self.max_lost = 0
        self.max_get = 0
        self.lost_time = 0
        self.get_time = 0
        self.total_lost = 0
        self.total_get = 0
        self.asset_array = []
        self.gap = 0
        self.gapArray = []
        self.gap_lost_array = []
        self.big_get_time = 0
        self.big_get = 0
        self.distant_bigGet = 0
        self.big_array = []
        self.total_day = total_day
        self.continue_lost = 0         # 当前连续失败次数

        # 计算最大回撤
        self.max_rollback = 0          # 最大回撤
        self.max_assets = 100000
        self.min_assets = 100000

    def clearResult(self):
        self.all_assets = 100000
        self.max_lost = 0
        self.max_get = 0
        self.lost_time = 0
        self.get_time = 0
        self.total_lost = 0
        self.total_get = 0

    # 获取中值
    def get_median(self,data):
        if len(data)==0: return 0
        data.sort()
        half = len(data) // 2
        avg = sum(data)/len(data)
        return (data[half] + data[~half]) / 2 + avg/2

    def printResult(self,nodeStat):
        mid_lost_time = self.get_median(self.gap_lost_array)
        self.big_get_time = 1 if self.big_get_time==0 else self.big_get_time
        print "年均收益 %.2f " %((self.total_get+self.total_lost)*200/self.total_day)+"%"
        print "最大获利比例 = %.2f" % self.max_get + "%"
        print "最大损失比例 = %.2f" % self.max_lost + "%"
        print "总获利次数 = %.f 次" %self.get_time
        print "总损失次数 = %.f 次" %self.lost_time
        print "获利次数比例 = %.f " % (self.get_time * 100 / (self.get_time+self.lost_time)) + "%"
        print "大涨次数 = %.f 次" % self.big_get_time
        print "大涨次数比例 = %.f " % (self.big_get_time*100/self.get_time) +"%"
        print "平均每次大涨比例 = %.2f" % (self.big_get / self.big_get_time) + "%"
        print "平均每次获利比例 = %.2f" %(self.total_get/self.get_time) + "%"
        print "平均每次损失比例 = %.2f" % (self.total_lost/ self.lost_time) + "%"
        print "大涨间隔 = %s " % self.gapArray
        print "平均大涨间隔 = %.f 天" % (self.gap/self.big_get_time)
        print "距离上次大涨天数 = %.f 天" % self.distant_bigGet
        print "大涨间平均失败次数 = %.f 次" % mid_lost_time
        print "当前连续失败次数 = %d 次"%self.continue_lost
        print "是否可以交易  ： %s" %("是" if self.continue_lost>mid_lost_time else "否")
        print "资金总额 = %.2f 元" % self.all_assets
        print "总获利比例 = %.2f" % self.total_get + "%"
        print "总损失比例 = %.2f" % self.total_lost + "%"
        print "最大回撤 = %.2f" % (self.max_rollback*100) + "%"
        if nodeStat:
            print "大幅信息".center(50,"-")
            for charge in self.big_array:
                print "大幅：" + charge

    def printStrategy(self):
        min_lost_time = self.get_median(self.gap_lost_array)
        self.big_get_time = 1 if self.big_get_time == 0 else self.big_get_time
        print "年均收益 %.2f " % ((self.total_get + self.total_lost) * 244 / self.total_day) + "%"
        print "平均每次大涨比例 = %.2f" % (self.big_get / self.big_get_time) + "%"
        print "平均每次获利比例 = %.2f" % (self.total_get / self.get_time) + "%"
        print "平均每次损失比例 = %.2f" % (self.total_lost / self.lost_time) + "%"
        print "总获利比例 = %.2f" % self.total_get + "%"
        print "总损失比例 = %.2f" % self.total_lost + "%"
        print "资金总额 = %.2f 元" % self.all_assets

    def resultJson(self):
        return {'profile_year' :float(((self.total_get + self.total_lost) * 200 / self.total_day)),
                'key':'年均收益'}
                # "最大获利比例 " : self.max_get + "%",
                # "最大损失比例 " : self.max_lost + "%",
                # "总获利次数 " : self.get_time}
    # 绘图
    def plot(self):
        Plot.plot(self.asset_array,'name')