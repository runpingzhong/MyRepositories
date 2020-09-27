%% SA 模拟退火: 求解函数y = 11*sin(x) + 7*cos(5*x)在[-3,3]内的最大值(动画演示）
tic
clear; clc

%% 绘制函数的图形
x = -3:0.1:3;
y = 11*sin(x) + 7*cos(5*x);
figure
plot(x,y,'b-')
hold on  % 不关闭图形，继续在上面画图

%% 参数初始化
narvs = 1; % 变量个数
T0 = 100;   % 初始温度
T = T0; % 迭代中温度会发生改变，第一次迭代时温度就是T0
maxgen = 200;  % 最大迭代次数
Lk = 100;  % 每个温度下的迭代次数
alfa = 0.95;  % 温度衰减系数
x_lb = -3; % x的下界
x_ub = 3; % x的上界

%%  随机生成一个初始解
x0 = zeros(1,narvs);
for i = 1: narvs
    x0(i) = x_lb(i) + (x_ub(i)-x_lb(i))*rand(1);    
end
y0 = Obj_fun1(x0); % 计算当前解的函数值
h = scatter(x0,y0,'*r');  % scatter是绘制二维散点图的函数（这里返回h是为了得到图形的句柄，未来我们对其位置进行更新）

%% 定义一些保存中间过程的量，方便输出结果和画图
max_y = y0;     % 初始化找到的最佳的解对应的函数值为y0
MAXY = zeros(maxgen,1); % 记录每一次外层循环结束后找到的max_y (方便画图）

%% 模拟退火过程
for iter = 1 : maxgen  % 外循环, 我这里采用的是指定最大迭代次数
    for i = 1 : Lk  % 内循环，在每个温度下开始迭代
        y = randn(1,narvs);  % 生成1行narvs列的N(0,1)随机数
        z = y / sqrt(sum(y.^2)); % 根据新解的产生规则计算z
        x_new = x0 + z*T; % 根据新解的产生规则计算x_new的值
        % 如果这个新解的位置超出了定义域，就对其进行调整
        for j = 1: narvs
            if x_new(j) < x_lb(j)
                r = rand(1);
                x_new(j) = r*x_lb(j)+(1-r)*x0(j);
            elseif x_new(j) > x_ub(j)
                r = rand(1);
                x_new(j) = r*x_ub(j)+(1-r)*x0(j);
            end
        end
        x1 = x_new;    % 将调整后的x_new赋值给新解x1
        y1 = Obj_fun1(x1);  % 计算新解的函数值
        if y1 > y0    % 如果新解函数值大于当前解的函数值
            x0 = x1; % 更新当前解为新解
            y0 = y1;
        else
            p = exp(-(y0 - y1)/T); % 根据Metropolis准则计算一个概率
            if rand(1) < p   % 生成一个随机数和这个概率比较，如果该随机数小于这个概率
                x0 = x1; % 更新当前解为新解
                y0 = y1;
            end
        end
        % 判断是否要更新找到的最佳的解
        if y0 > max_y  % 如果当前解更好，则对其进行更新
            max_y = y0;  % 更新最大的y
            best_x = x0;  % 更新找到的最好的x
        end
    end
    MAXY(iter) = max_y; % 保存本轮外循环结束后找到的最大的y
    T = alfa*T;   % 温度下降
    pause(0.01)  % 暂停一段时间(单位：秒)后再接着画图
    h.XData = x0;  % 更新散点图句柄的x轴的数据（此时解的位置在图上发生了变化）
    h.YData = Obj_fun1(x0); % 更新散点图句柄的y轴的数据（此时解的位置在图上发生了变化）
end

disp('最佳的位置是：'); disp(best_x)
disp('此时最优值是：'); disp(max_y)

pause(0.5)
h.XData = [];  h.YData = [];  % 将原来的散点删除
scatter(best_x,max_y,'*r');  % 在最大值处重新标上散点
title(['模拟退火找到的最大值为', num2str(max_y)])  % 加上图的标题

%% 画出每次迭代后找到的最大y的图形
figure
plot(1:maxgen,MAXY,'b-');
xlabel('迭代次数');
ylabel('y的值');
toc

% % 注意：代码文件仅供参考，一定不要直接用于自己的数模论文中
% % 国赛对于论文的查重要求非常严格，代码雷同也算作抄袭
% % 视频中提到的附件可在售后群（购买后收到的那个无忧自动发货的短信中有加入方式）的群文件中下载。包括讲义、代码、我视频中推荐的资料等。
% % 关注我的微信公众号《数学建模学习交流》，后台发送“软件”两个字，可获得常见的建模软件下载方法；发送“数据”两个字，可获得建模数据的获取方法；发送“画图”两个字，可获得数学建模中常见的画图方法。另外，也可以看看公众号的历史文章，里面发布的都是对大家有帮助的技巧。
% % 购买更多优质精选的数学建模资料，可关注我的微信公众号《数学建模学习交流》，在后台发送“买”这个字即可进入店铺(我的微店地址：https://weidian.com/?userid=1372657210)进行购买。
% % 视频价格不贵，但价值很高。单人购买观看只需要58元，三人购买人均仅需46元，视频本身也是下载到本地观看的，所以请大家不要侵犯知识产权，对视频或者资料进行二次销售。
% % 如何修改代码避免查重的方法：https://www.bilibili.com/video/av59423231（必看）