clear; clc
global x y;  % 将x和y定义为全局变量（方便在子函数中直接调用，要先声明）
load data_x_y  % 数据集内里面有x和y两个变量
narvs = 2;
% 使用粒子群算法，不需要指定初始值，只需要给定一个搜索的范围
lb = [-10 -10];  ub = [10 10];  
[k, fval] = particleswarm(@Obj_fun,narvs,lb,ub) 

% 使用粒子群算法后再利用fmincon函数混合求解
options = optimoptions('particleswarm','HybridFcn',@fmincon);
[k,fval] = particleswarm(@Obj_fun,narvs,lb,ub,options)


% % 注意：代码文件仅供参考，一定不要直接用于自己的数模论文中
% % 国赛对于论文的查重要求非常严格，代码雷同也算作抄袭
% % 视频中提到的附件可在售后群（购买后收到的那个无忧自动发货的短信中有加入方式）的群文件中下载。包括讲义、代码、我视频中推荐的资料等。
% % 关注我的微信公众号《数学建模学习交流》，后台发送“软件”两个字，可获得常见的建模软件下载方法；发送“数据”两个字，可获得建模数据的获取方法；发送“画图”两个字，可获得数学建模中常见的画图方法。另外，也可以看看公众号的历史文章，里面发布的都是对大家有帮助的技巧。
% % 购买更多优质精选的数学建模资料，可关注我的微信公众号《数学建模学习交流》，在后台发送“买”这个字即可进入店铺(我的微店地址：https://weidian.com/?userid=1372657210)进行购买。
% % 视频价格不贵，但价值很高。单人购买观看只需要58元，三人购买人均仅需46元，视频本身也是下载到本地观看的，所以请大家不要侵犯知识产权，对视频或者资料进行二次销售。
% % 如何修改代码避免查重的方法：https://www.bilibili.com/video/av59423231（必看）