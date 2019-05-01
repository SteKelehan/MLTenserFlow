TenserFLow in Python (NN)
=============

Overview
-------

![alt text](https://www.researchgate.net/publication/320270458/figure/download/fig1/AS:551197154254848@1508427050805/Mathematical-model-of-artificial-neuron.png "Artificial Neural Network")

1. Start with your input data
2. These input values are passed along, each of these input values are weighted
3. They are then sumed together
4. There is then a threshold/activation function (normaly a sigmod).
5. This then produces an output that is a function of the vectors $\vec{x}$ and $\vec{w}$. 


$$
Y(\vec{x}) = f(\vec{x}\vec{{w}})
$$


![alt text](https://camo.githubusercontent.com/82b7fff72d1c4da37e0c4474bfd0cdd06b1a6a75/687474703a2f2f74656c656772612e70682f66696c652f3137356133343032346263343536353164306265362e706e67 "Neural Network exposing hidden layers")

1. All off your inputs are connected (IN the most basic model)
2. In the image above there are 3 hidden layers
3. This is know as a deep neural network as it has more then one hidden layer
4. In a deep neural network the optimaisation is a lot more difficult

The reason the deep neural networks are more difficult to train is they are very interdependent. Thus if you change one weight in one layer it could drastically effect the other layers. 

How it works
-------

TenserFlow
-------
### Installing TenserFlow

1. If you dont already have pip install pip.

#### Own Mac/Lunix

The bellow installation is made for CPU usasage only

```bash
sudo pip3 install -U virtualenv
pip install tensorflow
pip install tf-nightly
```

##### Create a virtual environment

1. Make a ./venv to hold the VM

```bash
virtualenv --system-site-packages -p python3 ./venv
```

2. Activate virtual environment

```bash
source ./venv/bin/activatev
```

3. To exit VM 

```bash
deactivate
```


#### Docker Container

Docker has its own image

```bash
docker pull tensorflow/tensorflowarkup
```

To run it with a jupyter notebook:

```bash
docker run -it -p 8888:8888 tensorflow/tensorflow
```


TensorFlow is just a large libary of functions that milipulate arrays/matrix's

A tensor is just an array or a matrix

Contributing
------------

See [Contributing](CONTRIBUTING.md).