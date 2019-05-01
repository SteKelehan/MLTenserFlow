#TODO

import tensorflow as tf
'''
input -> weights -> hiddin layer 1 (activation function) -> weights -> hidden layer 2 etc -> weights -> output layer

This is a feedforward network as we are feeding the data forward only

Compare output data with the intended output -> put that through a cost/loss function (cross entropy) This will determain how good or bad the network did

optimization function -> this will attemtped to minimize the cost (How nbad it did) ie. SGD

Backpropagation the occurs this is the correction of the weight with the optimazation function

One feedforward and a backprop is know as an epock (One cycle)

'''

from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("/tmp/data", one_hot=True)

# Numbers of nodes in each hidden layer
n_nodes_hl1 = 500
n_nodes_hl2 = 500
n_nodes_hl3 = 500

n_classes = 10
# Does it in groups of 100 features
batch_size = 100

# your input data x and your output data y
x = tf.placeholder('float', [None], 784)
y = tf.placeholder('float')


def neural_network_model(data):
    # Starting the weights off as random vaules -> giving ML model no help
    # input data * weights + biases
    # A biases is good if for example all the inputs where 0 adding a make them non 0 and that menas some neruons will fire
    hiddien_1_layer = {
        'weights': tf.Variable(tf.random_normal([784, n_nodes_hl1])),
        'biases': tf.Variable(tf.random_normal(n_nodes_hl1))
    }
    hiddien_2_layer = {
        'weights': tf.Variable(tf.random_normal([n_nodes_hl1, n_nodes_hl2])),
        'biases': tf.Variable(tf.random_normal(n_nodes_hl2))
    }
    hiddien_3_layer = {
        'weights': tf.Variable(tf.random_normal([n_nodes_hl2, n_nodes_hl3])),
        'biases': tf.Variable(tf.random_normal(n_nodes_hl3))
    }
    output_layer = {
        'weights': tf.Variable(tf.random_normal([n_nodes_hl3, n_classes])),
        'biases': tf.Variable(tf.random_normal(n_classes))
    }

    l1 = tf.add(
        tf.matmul(data, hidden_1_layer['weigthts'], hidden_1_layer['biases']))
    l1 = tf.nn.relu(l1)

    l2 = tf.add(
        tf.matmul(data, hidden_2_layer['weigthts'], hidden_2_layer['biases']))
    l2 = tf.nn.relu(l2)

    l3 = tf.add(
        tf.matmul(data, hidden_3_layer['weigthts'], hidden_3_layer['biases']))
    l3 = tf.nn.relu(l3)

    output = tf.matmul(l3, output_layer['weights']) + output_layer['biases']

    return output_layer


def train_neural_network(x):
    prediction = neural_network_model(x)
    cost = tf.reduce_mean(
        tf.nn.softmax_cross_entropy_with_logits(prediction, y))

    optimizer = tf.train.AdamOptimizer().minimize(cost)

    # How many times to train (do full cycle)
    hm_epochs = 10

    with tf.Session() as sess:
        sess.run(tf.initialize_all_variables())

        for epoch in range(hm_epochs):
            epoch_loss = 0
            for _ in range(int(mnist.train.num_examples / batch_size)):
                _x, _y = mnist.train.next_batch(batch_size)
                _, c = sess.run([optimizer, cost], feed_dict={x: _x, y: _y})
                epoch_loss += c
            print('Epoch', epoch, 'completed out of', hm_epochs, 'loss:',
                  epoch_loss)

        correct = tf.equal(tf.argmax(prediction, 1), tf.argmax(y, 1))
        accuracy = tf.reduce_mean(tf.cast(cottect, 'float'))
        print('Accuracy:',
              accuracy.eval({
                  x: mnist.test.images,
                  y: mnist.test.lables
              }))
