#+TITLE:R专题讲座
#+AUTHOR:汤银才
#+STARTUP: inlineimages

* 文学化编程


#+BEGIN_SRC python :results output :exports both
import pandas as pd

data = pd.read_csv('./auto.csv')
print(data.head(10))
#+END_SRC

#+RESULTS:
#+begin_example
            make  price  mpg  rep78  headroom  trunk  weight  length  turn  \
0    AMC Concord   4099   22    3.0       2.5     11    2930     186    40   
1      AMC Pacer   4749   17    3.0       3.0     11    3350     173    40   
2     AMC Spirit   3799   22    NaN       3.0     12    2640     168    35   
3  Buick Century   4816   20    3.0       4.5     16    3250     196    40   
4  Buick Electra   7827   15    4.0       4.0     20    4080     222    43   
5  Buick LeSabre   5788   18    3.0       4.0     21    3670     218    43   
6     Buick Opel   4453   26    NaN       3.0     10    2230     170    34   
7    Buick Regal   5189   20    3.0       2.0     16    3280     200    42   
8  Buick Riviera  10372   16    3.0       3.5     17    3880     207    43   
9  Buick Skylark   4082   19    3.0       3.5     13    3400     200    42   

   displacement  gear_ratio   foreign  
0           121        3.58  Domestic  
1           258        2.53  Domestic  
2           121        3.08  Domestic  
3           196        2.93  Domestic  
4           350        2.41  Domestic  
5           231        2.73  Domestic  
6           304        2.87  Domestic  
7           196        2.93  Domestic  
8           231        2.93  Domestic  
9           231        3.08  Domestic  
#+end_example


#+BEGIN_SRC python :results file :exports both
import matplotlib 
matplotlib.use('Agg') #必要
import matplotlib.pyplot as plt
plt.figure()
plt.plot([3, 4.5, 5])
plt.savefig('session-fig.png')# 必要
return 'session-fig.png'# 必要
#+END_SRC

#+RESULTS:
[[file:session-fig.png]]


#+BEGIN_SRC python :results output
# import pandas as pd

def a(x):
    if x > 0:
        return 1
    else:
        return -1

print a(1)
print(a(-1))
#+END_SRC

#+RESULTS:
: 1
: -1

[[file:1.jpg]]

#+BEGIN_SRC python :results output
import platform
print platform.python_version()
#+END_SRC

#+RESULTS:
: 2.7.13

** 由来
*《R for Data Science》*
数据分析师成长过程:
1. console write
2. edit run
3. code blocks and notebook --> rmarkdown

交流与编程共存
- 与自己交流
- 与其他分析师交流
- 与大众交流

** 含义
- 文章应该是有文本与代码组成的流构成
- 数据与代码自动更新
- 未来趋势:数据的统计分析报告自动智能生成

** 实现
环境
- markdown
- rmarkdown/knitr
- R
- tex/mathkax
- rstudio/RTVS

工具
- beaker
- jupyter
- rmd

** 动态交互式图表

- shiny
- Recharts
- leaflet

** 工具

#+BEGIN_SRC R
library(broom)
library(kableExtra)
#+END_SRC

** 导出beamer

** 幻灯片
- xaringan


* python

# blank lines not OK in indented blocks, and don't use return()
# Source block is passed directly to interactive python;
# value is value of _ at end.
#+begin_src python :session
def foo(x):
  if x>0:
    return x+1
  else:
    return x-1

print(foo(1))
#+end_src

#+RESULTS:




