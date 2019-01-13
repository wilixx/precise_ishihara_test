# The funny journey
Everything starts with an ambicous goal as well as a funny plan, though we hardly ultimately get it done. --Allen Guo
xxx的方法相对最具有启发意义，借助于现有的黑白数字图像、卡通人物图像为底版，绘制大量半径随机不等的圆形，这些圆形的填充色彩主要在预先选取的前景色集合与背景色集合中选取，填充位置则依据图像中前景背景的分割情况。具体过程如下：

前景色彩集合与背景色彩集合产生器的设计。其中考虑因素有以下内容：

色盲类型：3种或者4种
色彩集合的丰富度，总共有1种或者2种颜色，即每个颜色集合的颜色数目。

二、实验任务划分

初步任务：输入一个前景图片、产生一组具有针对特定色盲类别的ishihara测试图、并对产生的图片进行优化。图片需要有说服力，能精确地鉴别出不同色盲类型。
初步任务优化：深入探究这项任务的实际实施方法；实际应用领域可以让医生手写、体检者在另一面查看。还可以嵌入到手机当中进行使用。

进一步任务：不输入前景图片，自动产生包含数字、有意义字符的针对特定色盲类别的ishihara测试图。

下一步任务：交给别人、让别人继续探讨并研究。。。


三、具体任务

任务划分：
任意选定一种色盲类型，随机产生一对混淆色，（origin_color, sim_color）
将颜色填充到

约束条件：图像必须为 (n x n x 3)形式的图片

1.随机颜色集合产生器的编写，默认前景色3种，背景色3种；调用3次即可，方法不受限。
return dict {
foreground: [( ), ( ), ( )]
background:[( ), ( ), ( )]
}

2.对输入图片进行定量quanlization处理，初步处理为6种颜色，构建一对一map关系图：

foreground[0]------>color[0]
foreground[1]------>color[1]
foreground[2]------>color[2]


background[0]------>color[4]
background[1]------>color[5]
background[2]------>color[6]

当然也可以一对多映射。

3.圆形绘制算法，产生最终图案。




