# KingCounty
美国King County房价预测训练赛 神经网络

这个题也是datacastle上面的一道练习题。由于之前并没有做过回归类问题。于是在网上先查了一些资料再做的。
最早使用的是GDBR和RF，效果都很差，于是借鉴了网上的做法，用深度神经网络。训练了5w次，效果很好。
最后的平方损失只有9100+

题目链接：http://www.pkbigdata.com/common/cmpt/%E7%BE%8E%E5%9B%BDKing%20County%E6%88%BF%E4%BB%B7%E9%A2%84%E6%B5%8B%E8%AE%AD%E7%BB%83%E8%B5%9B_%E7%AB%9E%E8%B5%9B%E4%BF%A1%E6%81%AF.html

运行步骤：
先执行feature.py，这个作用是把原始数据中的年月日拆开，然后根据房屋的建造年份和修复年份计算一下售出时已经过了多少年，这样特征维数有17维

然后执行predict.py，用keras搭建了一个2层的神经网络，激活函数都用的relu。训练五万轮后，预测结果。

