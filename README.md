# Historical Sources
## Large-scale computational analysis of historical sources

Extraction and processing of data from historical sources of the 16th century.

## Please read this guide before try to run the application.


## Installation

Open your terminal and type:

```sh 
pip install git+https://github.com/VilmaGlez/historical_sources.git
```

## Use 

1.- Example to create a training set. 

```sh 
from historical_sources import set_train_modules

set_train_modules.set_train(your document path)

```

The results are a document called "setTrain.tsv".


2.- Example to make a prediction.

```sh 
from historical_sources import transformer_predictor

Subject_Predicate = "The cause of lung cancer can be"

Object = "DNA methylation"

prediction = transformer_predictor.predictor((Subject_Predicate, Object))

prediction = prediction.replace("[start] ", '').replace(" [end]", '')

print(f"\n\n\n\nGiven sentence: {Subject_Predicate} {Object}")

print(f"Generated sentence: {Subject_Predicate} {prediction}")

```



