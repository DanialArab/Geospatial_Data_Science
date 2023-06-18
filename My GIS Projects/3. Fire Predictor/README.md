
# 3. Fire Predictor

In this project, I trained ML model to predict US Wildfire size class, so my approach would be to perform classification task to predict the fire class size, which could be ope of the following:

|**number of acres within the final fire perimeter expenditures**|**Class ID** |
| -- | --| 
|0 - 0.25|A|
|0.26-9.9|B|
|10.0-99.9|C|
|100-299|D|
|300 to 999|E|
|1000 to 4999|F|
|5000 +|G|

So the problem is a multiclass classification.

side note:
I could have approached the problem like a regression task because the data also includes, in addition to the fire size class, the fire size in acres.

Here are some notes:

+ I used Spark 
+ ...

ML Ideas and some comments:

|**FIRE_SIZE_CLASS**|**count** | **normalized count (%)**|
| -- | --| --|
|              B|939376|49.95|
|              A|666919|35.46|
|              C|220077|11.703329|
|              D| 28427|1.511701|
|              E| 14107|0.750187|
|              F|  7786|0.414047|
|              G|  3773|0.200642|


|**STAT_CAUSE_CODE**|**count** | **normalized count (%)**|
| -- | --| --|
|            5.0|429028|22.81|
|            9.0|323805|17.21|
|            7.0|281455|14.96|
|            1.0|278468|14.80|
|           13.0|166723|8.86|
|            2.0|147612|7.84|
|            4.0| 76139|4.04|
|            8.0| 61167|3.25|
|            3.0| 52869|2.81|
|            6.0| 33455|1.77|
|           11.0| 14448|0.76|
|           10.0| 11500| 0.61|
|           12.0|  3796|0.20

