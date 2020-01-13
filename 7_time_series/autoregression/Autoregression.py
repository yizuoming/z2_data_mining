# -*- coding: utf-8 -*-
"""
回归模型（例如线性回归）基于输入值的线性组合对输出值进行建模
因为回归模型在之前的时间步骤使用来自相同输入变量的数据，所以它被称为自回归

自回归模型假设先前时间步骤的观察对于预测下一时间步的值是有用的
变量之间的这种关系称为相关性，自回归模型变量就是自相关性
如果所有滞后变量与输出变量显示低或无相关性，则表明时间序列问题可能无法预测

ARIMA是AutoRegressive Integrated Moving Average的缩写

AR：自回归。一种模型，它使用观察与一些滞后观察之间的依赖关系
I：综合。使用原始观察的差分（例如，从前一时间步骤的观察中减去观察值）以使时间序列静止
MA：移动平均线。使用应用于滞后观察的移动平均模型中的观察和残差之间的依赖关系的模型

ARIMA模型的参数定义如下：
p：模型中包含的滞后观察数，也称为滞后顺序。
d：原始观测值的差异次数，也称为差分程度。
q：移动平均窗口的大小，也称为移动平均值的顺序

"""