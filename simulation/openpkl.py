# 两种方法都能打开
import pickle
import numpy as np

f = open('E:/home/botong/iclr2021_data/1667_2_2_2_4_2_3_lrelu_lacim_d_num_cluster_3_original_1667/final.pkl','rb')
data = pickle.load(f)
print(data)