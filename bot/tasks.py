from model.QA_Model import predict
import requests, json
from celery import shared_task
from bot.apps import BotConfig

@shared_task()
def upload_to_ai(questions:list, user_info:str, merchant:str, user_id:int):
    # for question in questions:
    #     answer = new_mod(question, user_info)
    #     print(answer)
    model_predictions = predict(questions, BotConfig.MODEL, user_info)
    # print(model_predictions)
    predictions = {'Question':{}, 'Response':{},'Confidence':{}}
    for a in predictions:
        if a == 'Question':
            predictions[a].update({'Organizational Information Security':dict(list(model_predictions['Question'].items())[0:9])})
            predictions[a].update({'General security':dict(list(model_predictions['Question'].items())[9:27])})
            predictions[a].update({'Network security':dict(list(model_predictions['Question'].items())[27:34])})
            predictions[a].update({'Security Monitoring':dict(list(model_predictions['Question'].items())[34:45])})
            predictions[a].update({'Business Continuity / Disaster Recovery':dict(list(model_predictions['Question'].items())[45:50])})
            predictions[a].update({'Incident Response':dict(list(model_predictions['Question'].items())[50:56])})
            predictions[a].update({'Risk Management/Auditing /Regulatory Compliance':dict(list(model_predictions['Question'].items())[56:])})
        if a == 'Response':
            predictions[a].update(model_predictions['Response'])
        if a == 'Confidence':
            predictions[a].update(model_predictions['Confidence'])
    requests.post("https://api.smartcomplyapp.com/api/compliance/submit_predictions/", data={"predictions": json.dumps(predictions), "merchant": merchant, "user": user_id})
    return

@shared_task()
def add():
    return 10
