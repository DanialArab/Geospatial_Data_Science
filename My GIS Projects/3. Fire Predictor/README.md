
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

side note:
I could have approached the problem like a regression task because the data also includes, in addition to the fire size class, the fire size in acres.

Here are some notes:

+ I used Spark 
+ ...
