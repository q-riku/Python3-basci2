class OrderingFood:
    ordering_food_name = ['酸菜鱼','红烧排骨','红烧茄子','香肠套餐'] #套餐的清单
    ordering_food_price = [64,18,15,14]
    order_list = [] #清单列表（打印）
    #初始化方法
    def __init__(self):
        self.do_order_food()
    #欢迎界面
    def welcome(self):
        print("================================")
        print("    欢迎来到编程狮点餐系统")
        print("  1、套餐类")
        print("  2、结账")
        print("  3、退出")
        print("================================")
    #打印清单的方法
    def order_list_(self,b=2):
        total_price = 0.0  # 总价
        if b==1:
            #如果结账完成，直接把清单放在order.txt文件；
            f = open('./order.txt','a',encoding='UTF-8')
            import time
            f.write("===========================================\n")
            f.write("订单打印时间：" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"\n")
            for v in self.order_list:
                value = v.split("@@")
                f.write(value[0] + "\t" + value[1] + "份\t" + value[2] + '元\n')
                total_price = float(total_price) + float(value[2])
            f.write("\t\t\t\t总价：" + str(total_price)+"\n")
            f.write("===========================================\n")
            f.close()
            return total_price
        else:
            import time
            print("订单打印时间：" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            for v in self.order_list:
                value = v.split("@@")
                print(value[0] + "\t" + value[1] + "份\t" + value[2] + '元')
                total_price = float(total_price) + float(value[2])
            print("\t\t\t\t总价：" + str(total_price))
            return total_price
    #执行点餐的方法
    def do_order_food(self):
        while True:
            self.welcome()
            num = input("请选择：")
            index = 0 #为了列表的序号从1开始；
            if num=="1":
                print("-----------套餐清单-----------------")
                ordering_food_len = self.ordering_food_name.__len__() #获取列表的长度；
                for k in range(ordering_food_len):
                    index = index + 1
                    print(str(index)+"、"+str(self.ordering_food_name[k])+"\t\t"+str(self.ordering_food_price[k])+"元")
                print("-----------------------------------")
                food_index = int(input("请选择套餐："))
                food_index = food_index - 1  #列表的下标是从0开始；

                if food_index >= 0 and food_index < ordering_food_len:
                    order_list_index = -1  # 获取订单可能有相同下标的值
                    b = True #去重（修改），如没有相同商品时，重新添加，如果有，则修改；
                    for each in self.order_list:
                        order_list_index = order_list_index + 1
                        food_name = self.ordering_food_name[food_index] #获取到商品名称
                        food_name_len = food_name.__len__() #商品的长度；
                        if food_name == each[0:food_name_len]:
                            b = False
                            break
                    f = input("请输入购买份数：") #请输入购买份数
                    if b:
                        price = float(self.ordering_food_price[food_index] * int(f))
                        print("您选择了：" + self.ordering_food_name[food_index] + "\t" + f + "份\t总价：" + str(price) + "元")
                        self.order_list.append(self.ordering_food_name[food_index] + "@@" + str(f) + "@@" + str(price))
                        print(self.order_list)
                    else:
                        list = self.order_list[order_list_index].split('@@')
                        sum = int(list[1]) + int(f) #已有列表的份数+新购买的份数=new
                        price = float(self.ordering_food_price[food_index] * sum)
                        self.order_list[order_list_index] = self.ordering_food_name[food_index] + "@@" + str(sum) + "@@" + str(price)
                        print("您选择了：" + self.ordering_food_name[food_index] + "\t" + f + "份\t总价：" + str(price) + "元")

                else:
                    print('没有该商品')
            elif num=="2":
                print("-----------------清单列表--------------------")
                total_price = self.order_list_()
                print("--------------------------------------------")
                while True:
                    if self.order_list:
                        money = input("请输入金额支付：")
                        import re
                        res = re.match(r'\d+', money)
                        if res:
                            if int(money)>=total_price:
                                print('支付成功，找您' + str(float(money) - float(total_price)) + '元，欢迎再次光临！')
                                self.order_list_(1)
                                self.order_list = [] #清空列表
                                break
                            else:
                                print("金额不够，请重新支付！")
                        else:
                            print("您这不是RMB，看不懂！-^-")
                    else:
                        print("没有购买清单，无法结账！")
                        break

            elif num=='3':
                exit()
            else:
                print('请重新输入！')

of = OrderingFood()