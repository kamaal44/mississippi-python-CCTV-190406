import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

# ******
# mining
# *****
mnist = input_data.read_data_sets('./mnist/data/', one_hot=True)
# ******
# modeling
# *****
# 옵션
learning_rate = 0.01
total_epoch = 30 # 총 회전수
batch_size = 128 # 한번에 입력받는 갯수

n_input = 28 # 가로픽셀
n_step = 28 # 세로픽셀
n_hidden = 128
n_class = 10 # 10단계

X = tf.placeholder(tf.float32, [None, n_step, n_input])
Y = tf.placeholder(tf.float32, [None, n_class])
W = tf.Variable(tf.random_normal([n_hidden, n_class]))
# b = tf.Variable()
