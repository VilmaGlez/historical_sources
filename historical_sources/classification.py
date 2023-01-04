import stanza
from allennlp_models import pretrained
import string
import re

allenslr=pretrained.load_predictor('structured-prediction-srl-bert')
nlp = stanza.Pipeline(lang='en', processors='tokenize')

#extraccion de las oraciones de un documento. 
def extract_sentences(data):
    """
    from a string use CoreNLP to extrac sentences
    
    Arguments
        data :: str
    Returns:
        lista :: list 
    """
    doc = nlp(data)
    lista=[sentence.text for sentence in doc.sentences]
    return lista

#extraccion del sujeto predicado y objeto 
def extract_triplets(sentence,iden):
    """
    from a sentence use AllenNLP SRLtool to extrac (subject-object, predicate) tuples
    
    Arguments
        sentence :: str
        iden :: str
    
    Returns:
        If possible
        (str, str, str, str, str) list of list
        Else
        None
    """
    remove='!"#$%&()*+,-./:;<=>?@[\]^_`{|}~'
    input=sentence.translate(str.maketrans('', '', remove))
    triplets=[]                                        # num de palabras sin anotar por verbo
    output=allenslr.predict(input)

    if len(output['verbs'])==0:                     # Ningun verbo anotado
        print("ERROR: Ningún verbo anotado")
        return None
    else: 
        for i in range(len(output['verbs'])):                  
            tags=output['verbs'][i]['tags']             # Valida el etiquetado
            if bool(re.search('ARG[0-5]', string) for string in tags):
                tuple=create_tuples(output,sentence,iden,i)             # Extracción de información
                triplets.append(tuple)
        return triplets


def create_tuples(output, sentence, iden, index=0):
    """
    Create a tuple from PropBank Anotations

    Arg:
    output :: Dict create with AllenNLP SLR
    sentence :: str 
    iden :: str
    index :: int to acces to the correct labeling 
    
    Returns:
    (id, sent, sj, prd, oj) list
    """
    S=[]
    P=[]
    O=[]
    tags=output['verbs'][index]['tags']
    words=output['words']
    for a in range(0,5):
        if any('ARG'+str(a) in string for string in tags):
            for i in range(len(tags)):
                if bool(re.search('ARG[2-5]', tags[i])):
                    O.append(words[i])
                elif bool(re.search('ARG[0-1]', tags[i])):
                    S.append(words[i])
                elif not 'O' in tags[i]:
                    P.append(words[i])
            break
    S=" ".join(S)
    P=" ".join(P)
    O=" ".join(O)
    return [iden,sentence,P,S,O]
