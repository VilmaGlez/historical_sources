import os
import pandas as pd
from historical_sources.classification import extract_sentences
from historical_sources.classification import extract_triplets 
import sysconfig

cwd = str(sysconfig.get_paths()["purelib"]) + '/historical_sources/datasets/p/'

#abrir archivo traducido
def open_source_file(name):
    """
    opens each input file from which the knowledge base is extracted

    Arguments
        name :: file
    Returns:
        data :: string 
    """
    with open(name, 'r') as file:
        data = file.read().rstrip()
    return data

#crear los tsv
def tsv_set_train(r,e):
    """
    create a set train archive from a dataframe
    
    Arguments
        r,e :: list
    Returns:
        setTrain.tsv
        erroresSetTrain.tsv 
    """
    df = pd.DataFrame (r, columns = ['id','sentence','subject','predicate','object'])
    df.to_csv('setTran.tsv',index=False,sep='\t')
    df1 = pd.DataFrame (e, columns = ['id','sentence','subject','predicate','object'])
    df1.to_csv('erroresSetTrain.tsv',index=False,sep='\t')

def create_training_set(input_path=cwd):
    """
    from a directory create a set train
    
    Arguments
        input_path :: str
    Returns:
        r :: list 
        e :: list 
    """
    st=[]
    errors=[]
    with os.scandir(input_path) as ficheros:
        for fichero in ficheros:
            ruta=input_path+fichero.name
            data=open_source_file(ruta)
            sentences=extract_sentences(data)
            for sentence in sentences:
                output=extract_triplets(sentence,fichero.name)
                if output != None:
                    for i in range(len(output)):
                        if output[i][2] != "" and output[i][4] != "":
                            st.append(output[i]) 
                        else:
                            errors.append(output[i])
            print("Done",fichero.name)
    tsv_set_train(st,errors)




