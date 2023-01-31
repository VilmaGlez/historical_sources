from historical_sources.transformer_modules import *
import matplotlib.pyplot as plt
from collections import defaultdict
import pandas as pd
import string, re, os
import math, random
import logging
import sysconfig
import argparse

from pdb import set_trace as st
cwd = str(sysconfig.get_paths()["purelib"]) + '/historical_sources'
config_file = cwd + '/predictor_configuration.json'
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p')

def make_prediction(val_pair, n_demo, out_dir):
    if not (n_demo < 0 or isinstance(n_demo, str)):
        # Create duplicates of the same input query to make multiple predictions
        val_pairs = [val_pair] * n_demo
        save_predictions(pairs=val_pairs,
                    to_file_path=out_dir + 'val_predictions.csv')

        logging.info("KBC FOR VALIDATION SET WRITTEN TO {}".format(
                    out_dir + 'val_predictions.csv'))
        return None
    else:
        # Get a unique prediction for the imput query, and 
        inp = val_pair[0]
        return decode_sequence(inp)

(dataset_name,
n_epochs,
stack_size,
sequence_length,
max_features,
batch_size,
key_dim,
model_dim,
latent_dim,
num_heads,
out_dir) = get_config(config_file)

#n_demo = 10
n_demo = -1

if os.path.isdir(out_dir):
    logging.info("Loading Vectorizers")
else:
    logging.error("NO model trained and directory with specified parameters"
        " exists in: {}".format(config_file))
    exit()


es_callback = tf.keras.callbacks.EarlyStopping(monitor='val_loss',
                                                patience=10,
                                                min_delta=0.005,
                                                mode='auto',
                                                restore_best_weights=True,
                                                verbose=1)
#logging.info("OBTAINING PREDICTION FOR INPUT QUERY...")

"""
The inputs 'Subject_Predicate' and 'Object' should be provided by a function
implementing the Allen AI's Semantic Role Labeling method. I set their values
for testing purposes:
"""
def predictor(val_pair):
	global n_demo, out_dir
	return make_prediction(val_pair, n_demo, out_dir)

def train(default=True,dataFile=None):
    if default is True:
        exampleFile=cwd+ '/datasets/results200.tsv'
        with open(exampleFile) as f:
            train_text = f.readlines()
        with open(exampleFile) as f:
            test_text = f.readlines()
    else:
        with open(dataFile) as f:
            train_text = f.readlines()
        with open(dataFile) as f:
            test_text = f.readlines()

    train_pairs = list(
        map(functools.partial(
            prepare_data), train_text))
    test_pairs= list(
        map(functools.partial(
            prepare_data), test_text))
    train_in_texts = [pair[0] for pair in train_pairs]
    train_out_texts = [pair[1] for pair in train_pairs]

    input_vectorizer = layers.experimental.preprocessing.TextVectorization(
        output_mode="int", max_tokens=max_features,
        # ragged=False, # only for TF v2.7
        output_sequence_length=sequence_length,
        standardize=custom_standardization)

    output_vectorizer = layers.experimental.preprocessing.TextVectorization(
        output_mode="int", max_tokens=max_features, # ragged=False,
        output_sequence_length=sequence_length+1,
        standardize=custom_standardization)

    input_vectorizer.adapt(train_in_texts)
    output_vectorizer.adapt(train_out_texts)
    #saving the vectorizers also
    save_vectorizer(
        vectorizer=input_vectorizer, to_file=out_dir+'in_vect_model')
    save_vectorizer(
        vectorizer=output_vectorizer, to_file=out_dir+'out_vect_model')
    train_ds = make_dataset(train_pairs)
    test_ds = make_dataset(test_pairs)
    logging.info("Training Transformer Semantic EncoDec")
    history = transformer.fit(train_ds,
        epochs=n_epochs,
        validation_data=test_ds,
            callbacks=[ #cp_callback,
                        es_callback])
    logging.info("TRAINED!!")
    rdf = pd.DataFrame(history.history)
    rdf.to_csv(out_dir + "history.csv")
    fig, axes = plt.subplots(2, 1)
    rdf[sort_cols(rdf.columns)].iloc[:, :2].plot(ax=axes[0])
    axes[0].grid(b=True,which='major',axis='both',linestyle='--')
    rdf[sort_cols(rdf.columns)].iloc[:, 2:].plot(ax=axes[1])
    axes[1].grid(b=True,which='major',axis='both',linestyle='--')
    plt.savefig(out_dir + 'history_plot.pdf')
    """ Notes about saving the model weights:
    - must be the same paramers when you load the model
    - if you specify a directory, you will save them without a prefix
    """
    logging.info("Saving learned weights to {}\n".format(
        out_dir+'transformer_model_weights/model'))
    transformer.save_weights(out_dir+'transformer_model_weights/model')

