import os
import pandas as pd
from historical_sources.classification import extract_sentences
from historical_sources.classification import extract_triplets 
import sysconfig

cwd = str(sysconfig.get_paths()["purelib"]) + '/historical_sources/datasets/'

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
def tsv_set_train(r,e,common_sense_data):
    """
    create a set train archive from a dataframe
    
    Arguments
        r,e :: list
    Returns:
        setTrain.tsv
        erroresSetTrain.tsv 
    """
    commonFile = cwd + common_sense_data
    df = pd.DataFrame (r, columns = ['id','sentence','subject','predicate','object'])
    df = df.sample(frac=0.7).reset_index(drop=True)
    df2 = pd.read_csv(commonFile,sep='\t')
    frames = [df,df2]
    trainFile = pd.concat(frames)
    trainFile=trainFile.sample(frac=1).reset_index(drop=True)
    trainFile.to_csv('setTrain.tsv',index=False,sep='\t')
    df1 = pd.DataFrame (e, columns = ['id','sentence','subject','predicate','object'])
    df1.to_csv('erroresSetTrain.tsv',index=False,sep='\t')

def create_training_set(input_path,common_sense_data="csd.tsv"):
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
            ruta=input_path + '/' + fichero.name
            data=open_source_file(ruta)
            sentences=extract_sentences(data)
            for sentence in sentences:
                output=extract_triplets(sentence,fichero.name)
                if output != None:
                    for i in range(len(output)):
                        if output[i][0] != "" and output[i][1] != "" and output[i][2] != "" and output[i][3] != "" and output[i][4] != "":
                            st.append(output[i]) 
                        else:
                            errors.append(output[i])
            print("Done",fichero.name)
    tsv_set_train(st,errors,common_sense_data)




