import tensorflow as tf
import numpy as np
x=np.float32(np.random.rand(2,500))

y_=np.dot([0.100,0.500],x)+0.300

b=tf.Variable(tf.zeros([1]))
w=tf.Variable(tf.random_uniform([1,2],-1.0,1.0))
y=tf.matmul(w,x)+b
loss=tf.reduce_mean(tf.square(y-y_))
optimizer=tf.train.GradientDescentOptimizer(0.5)
train=optimizer.minimize(loss)

init=tf.initialize_all_variables()
with tf.Session() as sess:
     sess.run(init)
     for i in xrange(0,501):
        sess.run(train)
        if i%50==0:
           print(str(i)+','+str(sess.run(w))+','+str(sess.run(b)))




