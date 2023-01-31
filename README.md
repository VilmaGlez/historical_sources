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

```python
from historical_sources import downloads (do not specify the link if you want our pretrained model, which url is specified by default).

downloads.download_results(default=True)

```
Note: the above step only needs to be done once after the package installation.

If you need to modify the download link from google drive, just add the folder to your google drive repository and copy the link from the folder (make sure it is a public link) and paste it as shown below:

Example:
```python
from historical_sources import downloads

downloads.download_results(default=False,
    link="https://drive.google.com/drive/folders/1vPt_QbACi960J8Ocy6iIWfUcd76a7Vrr?usp=share_link")

```

## Usage 

### Train a model. 

If you need to train a new model do the following:

Create a folder with the files you want to use for training (the input directory). To create the dataset for training, do the following, and add the path of the created folder:

Example:
```python 
>>> from historical_sources import set_train_modules

>>> set_train_modules.create_training_set("vilma/documentos/entrenamiento", common_sense_data="cn_kb.csv")

```
The results will be saved in a file called "setTrain.tsv". This file is stored in the current working directory.

Notice that at the moment, we have not ehabled hyperparameters of the Transformer model. We alctualy keep them fixed according to what it is known to work the best. Only the training data changes ("setTrain.tsv" cintains ConceptNet + <triplets from files in the input directory>).

In the case the pretrained model does not fit your requirements, the next step would be to start training the network, do the following and add the path where your training set is located:

Example:
```python
>>> from historical_sources import transformer_predictor

>>> transformer_predictor.train(default=False, "setTrain.tsv")

```
The training usually lasts some time according to the amount of data and computing power used, be patient, when finished you will be notified and you will have your new training model (from several hours to days).

### Inference.

If you would like to try the previously downloaded (trained) model, here you can find some examples of use:



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
If you want to perform different tests:
Specify your subject-predicate and object.
Finally do the following:

```python
>>> from historical_sources import transformer_predictor
>>> Subject_Predicate = "your-subject-and-predicate"
>>> Object = "your-object"
>>> prediction = transformer_predictor.predictor((Subject_Predicate, Object))
>>> prediction = prediction.replace("[start] ", '').replace(" [end]", '')
>>> print(f"Given sentence: {Subject_Predicate} {Object}")
>>> print(f"Generated sentence: {Subject_Predicate} {prediction}")
```
Note: you can get more subject-predicates and objects, from the "setTrain.tsv" file.





