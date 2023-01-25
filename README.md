# Historical Sources
## Description

Data extraction and treatment package from historical sources from the 16th century through the use of neural networks.

## Installation

### Installing Conda

First of all you must install [Conda](https://www.anaconda.com/products/distribution).

Once installed open your terminal and type:
```sh
conda create --name python3-env python
```
To change between environments type:

```sh
conda activate [name-of-your-environment]
```
### Installing AllenNLP

To avoid errors in AllenNLP installation, first do the following:

```sh
conda install -c conda-forge jsonnet
```
Now, install AllenNLP and models: 
 
```sh

pip install allennlp==2.2.0

```

```sh
pip install allennlp-models==2.2.0
```
### Installing TensorFlow

Install TensorFlow 2.6
```sh
pip install tensorflow==2.6.0
```
And install Keras 2.6
```sh
pip install keras==2.6.0
```
### Installing historical_sources package

Next step, for package installation open your terminal and type:

```sh 
pip install git+https://github.com/VilmaGlez/historical_sources.git
```
### Download a trained model

Finally, you must download the trained model by executing the following:

```sh

from historical_sources import downloads

```
Note: the above step only needs to be done once after the package installation.
## Usage 

1.- Example to create a training set. 

```sh 
from historical_sources import set_train_modules

set_train_modules.set_train(your-document-path)

```

The results are a document called "setTrain.tsv".

2.-Example to train the neural network

```sh
from historical_sources import transformer_predictor

transformer_predictor.train(your-file)

```

3.- Example to make a inference.

```sh 
from historical_sources import transformer_predictor

Subject_Predicate = "The women bring a garment that they make from"

Object = "the cotton blanket itself"

prediction = transformer_predictor.predictor((Subject_Predicate, Object))

prediction = prediction.replace("[start] ", '').replace(" [end]", '')

print(f"\n\n\n\nGiven sentence: {Subject_Predicate} {Object}")

print(f"Generated sentence: {Subject_Predicate} {prediction}")

```



