
# 强大而精致的机器学习调参方法：贝叶斯优化


## 一、简介

**贝叶斯优化**用于机器学习调参由J. Snoek(2012)提出，主要思想是，给定优化的目标函数(广义的函数，只需指定输入和输出即可，无需知道内部结构以及数学性质)，通过不断地添加样本点来更新目标函数的后验分布(高斯过程**,直到后验分布基本贴合于真实分布。简单的说，就是**考虑了上一次参数的信息**，从而更好的调整当前的参数。

他与常规的网格搜索或者随机搜索的区别是：


- 贝叶斯调参采用高斯过程，**考虑之前的参数信息**，不断地更新先验；网格搜索未考虑之前的参数信息
- 贝叶斯调参**迭代次数少，速度快**；网格搜索速度慢,参数多时易导致维度爆炸
- 贝叶斯调参针对非凸问题依然**稳健**；网格搜索针对非凸问题易得到局部优最


## 二、理论


介绍贝叶斯优化调参，必须要从两个部分讲起：

- 高斯过程，用以拟合优化目标函数
- 贝叶斯优化，包括了“开采”和“勘探”，用以花最少的代价找到最优值

## 2.1 高斯过程

高斯过程可以用于非线性回归、非线性分类、参数寻优等等。以往的建模需要对 $p(y|X)$ 建模，当用于预测时，则是 

$$
p(y_{N+1} | X_{N+1})
$$

而高斯过程则， **还考虑了 $y_N$ 和 $y_{N+1}$ 之间的关系**，即：

$$
p(y_{N+1} | X_{N+1}, y_{N})
$$

高斯过程通过假设 $Y$ 值服从联合正态分布，来考虑 $y_N$ 和 $y_{N+1}$ 之间的关系，因此需要给定参数包括：均值向量和协方差矩阵，即：

$$
\begin{bmatrix}
y_1 \\
y_2 \\
... \\
y_n \\
\end{bmatrix} \sim
N( \mathbf{0}, \begin{bmatrix}
k(x_1, x_1) , k(x_1, x_2), ..., k(x_1, x_n) \\
k(x_2, x_1) , k(x_2, x_2), ..., k(x_2, x_n) \\
... \\
k(x_n, x_1) , k(x_n, x_2), ..., k(x_n, x_n) 
\end{bmatrix} )
$$


其中协方差矩阵又叫做 **核矩阵**, 记为 $\mathbf{K}$ ，仅和特征 $x$ 有关，和 $y$ 无关。

高斯过程的思想是： 假设 $Y$ 服从高维正态分布（先验），而根据训练集可以得到最优的核矩阵 ，从而得到后验以估计测试集 $Y*$

我们有后验：

$$
p(y_*| \mathbf{y} \sim N(K_* K^{-1} \mathbf{y}, ~  K_{**} - K_* K^{-1} K_*^T)
$$

其中，$K_*$为训练集的核向量，有如下关系：

$$
\begin{bmatrix}
\mathbf{y} \\
y_*
\end{bmatrix} \sim
N(\mathbf{0}, \begin{bmatrix}
K, K_*^T \\
K_*, K_{**} \\
\end{bmatrix})
$$

可以发现，在后验公式中，只有均值和训练集 $Y$ 有关，方差则仅仅和核矩阵，也就是训练集和测试集的 $X$ 有关，与训练集 $Y$ 无关

### 高斯过程的估计（训练）方法

假设使用平方指数核(Squared Exponential Kernel)，那么有：

$$
k(x_1, x_2) = \sigma^2_f exp(\frac{-(x_1 - x_2)^2}{2 l^2})
$$

那么所需要的确定的超参数 $\theta = [\sigma^2_f, l]$ ，由于 $Y$ 服从多维正态分布，因此似然函数为：

$$
L = log p(y| x, \theta) = - \frac{1}{2} log|\mathbf{K}| - \frac{1}{2} (y - \mu)^T \mathbf{K}^{-1} (y - \mu) - n*log(2\pi)/2
$$

由于 $K$ 是由 $\theta$ 决定的，所以通过梯度下降即可求出超参数 $\theta$，而根据核矩阵的计算方式也可以进行预测。

![](https://images2018.cnblogs.com/blog/998084/201807/998084-20180726204924171-1721363009.png)


上图是一张高斯分布拟合函数的示意图，可以看到，它只需要九个点，就可以大致拟合出整个函数形状（图片来自：https://github.com/fmfn/BayesianOptimization）


## 2.2 贝叶斯优化理论

贝叶斯优化是一种逼近思想，当计算非常复杂、迭代次数较高时能起到很好的效果，多用于超参数确定

### 基本思想

是基于数据使用贝叶斯定理估计目标函数的后验分布，然后再根据分布选择下一个采样的超参数组合。它充分利用了前一个采样点的信息，其优化的工作方式是通过对目标函数形状的学习，并找到使结果向全局最大提升的参数

**高斯过程** 用于在贝叶斯优化中对目标函数建模，得到其后验分布

通过高斯过程建模之后，我们尝试抽样进行样本计算，而贝叶斯优化很容易在局部最优解上不断采样，这就涉及到了开发和探索之间的权衡。

- 开发 (exploitation)：   根据后验分布，在最可能出现全局最优解的区域进行采样, 开发高意味着均值高
- 探索 (exploration):     在还未取样的区域获取采样点，   探索高意味着方差高


而如何高效的采样，即开发和探索，我们需要用到 **Acquisition Function**, 它是用来寻找下一个 x 的函数。


###  Acquistion Function

一般形式的Acquisition Funtion是关于x的函数，映射到实数空间R，表示改点的目标函数值能够比当前最优值大多少的概率，目前主要有以下几种主流的Acquisition Function


#### POI(probability of improvement)

$$
POI(X) = P(f(X) \ge f(X^+) + \xi) = \Phi(\frac{\mu(x) - f(X^+) - \xi}{\sigma(x)})
$$

其中， $f(X)$ 为X的目标函数值， $f(X^+)$ 为 **到目前为止** 最优的X的目标函数值， $\mu(x), \sigma(x)$ 分别是高斯过程所得到的目标函数的均值和方差，即 $f(X)$ 的后验分布。 $\xi$ 为trade-off系数,如果没有该系数，POI函数会倾向于取在 $X^+$ 周围的点，即倾向于exploit而不是explore，因此加入该项进行权衡。

而我们要做的，就是尝试新的X，使得 $POI(X)$ 最大，则采取该$X$ （因为$f(X)$的计算代价非常大），通常我们使用 **蒙特卡洛模拟** 的方法进行。

详细情况见下图（图片来自 Ref[5])

![](https://images2018.cnblogs.com/blog/998084/201807/998084-20180729210806816-1260397803.png)


#### Expected Improvement

POI是一个概率函数，因此只考虑了$f(x)$ 比 $f(x^+)$ 大的概率，而EI则是一个期望函数，因此考虑了 $f(x)$ 比 $f(x^+)$ 大多少。我们通过下式获取$x$

$$
x = argmax_x \ \  E(\max\{0, f_{t+1}(x) - f(X^+)\}| D_t)
$$

其中 $D_t$ 为前t个样本，在正态分布的假定下，最终得到:

$$
EI(x) = 
\begin{cases}
(\mu(x) - f(x^+)) \Phi(Z) + \sigma(x) \phi(Z), if \ \sigma(x) > 0 \\
0, if \ \sigma(x) = 0
\end{cases}
$$


 $$
 Z= \frac{\mu(x) - f(x^+)}{\sigma(x)}
 $$

#### Confidence bound criteria

$$
LCB(x) = \mu(x) - \kappa \sigma(x)
$$


$$
UCB(x) = \mu(x) + \kappa \sigma(x) 
$$




## 2.3 缺点和不足

- 高斯过程核矩阵不好选




# 三、例子

目前可以做贝叶斯优化的包非常多,光是python就有:

- [BayesianOptimization](https://github.com/fmfn/BayesianOptimization)
- [bayesopt](https://github.com/rmcantin/bayesopt)
- [skopt](https://github.com/scikit-optimize/scikit-optimize/tree/master/skop)
- ...

本文使用BayesianOptimization，以



# Reference

- [1] J. Snoek, H. Larochelle, and R. P. Adams, “Practical bayesianoptimization of machine learning algorithms,” in Advances in neural information processing systems, 2012, pp. 2951–2959.
- [2] 高斯过程：http://www.gaussianprocess.org/gpml/
- [3] 高斯过程：https://www.zhihu.com/question/46631426?sort=created
- [4] 高斯过程：http://www.360doc.com/content/17/0810/05/43535834_678049865.shtml
- [5] Brochu E, Cora V M, De Freitas N. A tutorial on Bayesian optimization of expensive cost functions, with application to active user modeling and hierarchical reinforcement learning[J]. arXiv preprint arXiv:1012.2599, 2010.
