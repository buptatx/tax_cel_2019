#! -*- coding:utf-8 -*-

class Tax():
    def __init__(self, salary, house, child, parent, edu, month):
        self.salary = salary
        self.house = house
        self.child = child
        self.parent = parent
        self.edu = edu
        self.month = month
        self.yanglao_rate = 0.08
        self.yiliao_rate = 0.02
        self.shiye_rate = 0.002
        self.gongjijin_rate = 0.12

    def cel_origin_tax(self):
        origin_nt_salary = (1 - self.yanglao_rate - self.yiliao_rate - self.shiye_rate \
            - self.gongjijin_rate) * self.salary - 3 - 5000
        if origin_nt_salary < 0:
            origin_tax = 0
        else:
            tax_rate, tax_deduction = self.get_tax_rate_and_deduction(origin_nt_salary)
            origin_tax = origin_nt_salary * tax_rate - tax_deduction
        return origin_tax

    def cel_deducate_tax(self):
        deducate_nt_salary = (1 - self.yanglao_rate - self.yiliao_rate - self.shiye_rate \
            - self.gongjijin_rate) * self.salary - 3 - 5000 - self.house - self.child \
            - self.parent - self.edu
        if deducate_nt_salary < 0:
            deducate_tax = 0
        else:
            tax_rate, tax_deduction = self.get_tax_rate_and_deduction(deducate_nt_salary)
            deducate_tax = deducate_nt_salary * tax_rate - tax_deduction
        return deducate_tax

    def get_tax_rate_and_deduction(self, nt_salary):
        if nt_salary <= 3000:
            return 0.03 ,0
        elif nt_salary > 3000 and nt_salary <= 12000:
            return 0.1 ,210
        elif nt_salary > 12000 and nt_salary <= 25000:
            return 0.2 ,1410
        elif nt_salary > 25000 and nt_salary <= 35000:
            return 0.25, 2660
        elif nt_salary > 35000 and nt_salary <= 55000:
            return 0.3, 4410
        elif nt_salary > 55000 and nt_salary <= 80000:
            return 0.35, 7160
        elif nt_salary > 80000:
            return 0.45, 15160

    def get_accumulated_tax(self, nt_salary, month):
        sum_nt_salary = nt_salary * month
        if sum_nt_salary <= 36000:
            return sum_nt_salary * 0.03 - 0
        elif sum_nt_salary > 36000 and sum_nt_salary <= 144000:
            return sum_nt_salary * 0.1 - 2520
        elif sum_nt_salary > 144000 and sum_nt_salary <= 300000:
            return sum_nt_salary * 0.2 - 16920
        elif sum_nt_salary > 300000 and sum_nt_salary <= 420000:
            return sum_nt_salary * 0.25 - 31920
        elif sum_nt_salary > 420000 and sum_nt_salary <= 660000:
            return sum_nt_salary * 0.30 - 52920
        elif sum_nt_salary > 660000 and sum_nt_salary <= 960000:
            return sum_nt_salary * 0.35 - 85920
        elif sum_nt_salary > 960000:
            return sum_nt_salary * 0.45 - 181920
        
    def cel_accumulated_tax(self, month):
        nt_salary_per_month = (1 - self.yanglao_rate - self.yiliao_rate - self.shiye_rate \
            - self.gongjijin_rate) * self.salary - 3 - 5000 - self.house - self.child \
            - self.parent - self.edu
        if nt_salary_per_month < 0:
            accumulated_tax = 0
        else:
            accumulated_tax = self.get_accumulated_tax(nt_salary_per_month, month)
        return accumulated_tax

    def get_tax(self):
        onts = self.cel_origin_tax()
        dnts = self.cel_deducate_tax()
        tax_in = "当前月份:%d 收入:%.2f 住房预扣:%.2f 子女预扣:%.2f 赡养预扣:%.2f 再教育预扣:%.2f" % \
            (self.month, self.salary, self.house, self.child, self.parent, self.edu)
        res_2018 = "2018年 原始应缴税额:%.2f 预扣税后应缴税额:%.2f 差值:%.2f 年总税额:%.2f" % (onts, dnts, onts-dnts, dnts*12)

        #nts = self.cel_accumulated_tax(self.month)
        tax_list = [self.cel_accumulated_tax(i) for i in range(1, 13)]
        idx = self.month - 1
        print(tax_list)
        if self.month == 1:
            nts = tax_list[idx]
        else:
            nts = tax_list[idx] - tax_list[idx-1]
        res_2019 = "2019年 预扣税后应缴税额:%.2f 新缴税额:%.2f 差值:%.2f 年总税额:%.2f" % (dnts, nts, dnts-nts, tax_list[-1])
        return tax_in, res_2018, res_2019


if __name__ == "__main__":
    tax = Tax(27000, 1000, 0, 0, 0, 12)
    tax.get_tax()
