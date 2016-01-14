import tensorflow as tf
import numpy as np
a=tf.placeholder(tf.float32)
b=tf.placeholder(tf.float32)
c=tf.mul(a,b)

with tf.Session() as sess:
     print sess.run([c],feed_dict={a:[3.],b:[40.]})




