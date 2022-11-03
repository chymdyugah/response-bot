#imports
from haystack import Document
import pandas as pd

def predict(query:list, model, context):
    '''
    This function predicts the answer to question passed as query
    Arguments:
    query: This is/are the question you intend to ask
    model: This is the model for the prediction
    context: This is the data from which the model will find it's answers
    '''
    
    result = model.run_batch(queries=query,
                            documents=[Document(content=context)])
    response = convert_to_dict(result['answers'], query)
    return response

def convert_to_dict(res:list, query:list):
    '''
    This function takes the question, answer and context using pandas
    it creates a dataframe and convert to dictionary
    argument:
    res: list that contains the details for our answer
    query: list of questions
    '''
    response = []
    comment = []
    confidence = []
    for i in range(len(res)):
        min_response = []
        min_comment = []
        min_confidence = []
        for j in range(len(res[i][0])):
            min_response.append(res[i][0][j].__dict__['answer'])
            min_comment.append(res[i][0][j].__dict__['context'])
            min_confidence.append(res[i][0][j].__dict__['score']*100)

        response.append(min_response)
        comment.append(min_comment)
        confidence.append(min_confidence)
    
    #convert to DataFrame
    answer_df = pd.DataFrame()
    answer_df['Question'], answer_df['Response'], answer_df['Comment'], answer_df['Confidence'] = query,response,comment,confidence
    
    #convert DataFrame to dict
    answer_dict = answer_df.to_dict()
    
    return answer_dict


