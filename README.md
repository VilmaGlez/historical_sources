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

### Example to create a training set. 

```sh 
from historical_sources import set_train_modules

set_train_modules.set_train(your-document-path)

```

The results are a document called "setTrain.tsv".

### Example to train the neural network

```sh
from historical_sources import transformer_predictor

transformer_predictor.train()

```

### Example to make a inference.

```python
>>> from historical_sources import transformer_predictor
>>> Subject_Predicate = "Teuliztaca falls"
>>> Object = "between the south and the west"
>>> prediction = transformer_predictor.predictor((Subject_Predicate, Object))
>>> prediction = prediction.replace("[start] ", '').replace(" [end]", '')
>>> print(f"Given sentence: {Subject_Predicate} {Object}")
Given sentence: Teuliztaca falls between the south and the west
>>> print(f"Generated sentence: {Subject_Predicate} {prediction}")
Generated sentence: Teuliztaca falls to the south
 
```
 
```python
>>> from historical_sources import transformer_predictor
>>> Subject_Predicate = "the grain that grows in this land as referred to from its seeds is"
>>> Object = "corn, chili, beans and pumpkins (where the seeds are obtained), and sweet potatoes and yucca sweet potato, and anonas and tomatoes, and chia (in the form of zargatona), which is a seed that, ground and toasted, with stirred toasted corn, is a good concoction to drink; and the natives drink it, and consider it a very healthy and fresh thing."
>>> prediction = transformer_predictor.predictor((Subject_Predicate, Object))
>>> prediction = prediction.replace("[start] ", '').replace(" [end]", '')
>>> print(f"Given sentence: {Subject_Predicate} {Object}")
Given sentence: the grain that grows in this land as referred to from its seeds is corn, chili, beans and pumpkins (where the seeds are obtained), and sweet potatoes and yucca sweet potato, and anonas and tomatoes, and chia (in the form of zargatona), which is a seed that, ground and toasted, with stirred toasted corn, is a good concoction to drink; and the natives drink it, and consider it a very healthy and fresh thing.
>>> print(f"Generated sentence: {Subject_Predicate} {prediction}")
Generated sentence: the grain that grows in this land as referred to from its seeds is corn beans chili peppers and beans and chili and other legumes that they use for the rest
 
```
```python
>>> from historical_sources import transformer_predictor
>>> Subject_Predicate = "The weapons they used were"
>>> Object = "bows and arrows and clubs, in which they put knives and flint and some stones, which clubs served as weapon axes"
>>> prediction = transformer_predictor.predictor((Subject_Predicate, Object))
>>> prediction = prediction.replace("[start] ", '').replace(" [end]", '')
>>> print(f"Given sentence: {Subject_Predicate} {Object}")
Given sentence: The weapons they used were bows and arrows and clubs, in which they put knives and flint and some stones, which clubs served as weapon axes
>>> print(f"Generated sentence: {Subject_Predicate} {prediction}")
Generated sentence: The weapons they used were bows and arrows and clubs
 
```




