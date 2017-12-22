# This is for not seeing the useless warnings. START
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
# For the useless warnings. END
import tensorflow as tf

# a=tf.random_normal((100,100))
# b=tf.random_normal((100,500))
# c=tf.matmul(a,b)
# sess=tf.InteractiveSession()
# sess.run(c)
hello = tf.constant('Hello ,TensorFlow')
sess1 = tf.Session()
print(sess1.run(hello))