import tensorflow as tf
a=tf.constant([[3.,3.]])
b=tf.constant([[2.],[2.]])
p=tf.matmul(a,b)
print(p)
sess=tf.Session()
result=sess.run(p)
print(result)
sess.close()

with tf.Session() as sess:
     re=sess.run(p)
     print(re)




