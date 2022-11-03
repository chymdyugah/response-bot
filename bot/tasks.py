from model.QA_Model import predict
from django.conf import settings
import requests, json
from celery import shared_task

@shared_task()
def upload_to_ai(questions:list, user_info:str, merchant:str, user_id:int):
    model_predictions = predict(questions, settings.MODEL, user_info)
    predictions = {'Question':{}, 'Response':{},'Confidence':{}}
    for a in predictions:
        if a == 'Question':
            predictions[a].update({'Organizational Information Security':dict(list(model_predictions['Question'].items())[0:9])})
            predictions[a].update({'General security':dict(list(model_predictions['Question'].items())[9:27])})
            predictions[a].update({'Network security':dict(list(model_predictions['Question'].items())[27:34])})
            predictions[a].update({'Security Monitoring':dict(list(model_predictions['Question'].items())[34:45])})
            predictions[a].update({'Business Continuity / Disaster Recovery':dict(list(model_predictions['Question'].items())[45:50])})
            predictions[a].update({'Incident Response':dict(list(model_predictions['Question'].items())[50:56])})
            predictions[a].update({'Risk Management/Auditing /Regulatory Compliance':dict(list(model_predictions['Question'].items())[56:100])})
        if a == 'Response':
            predictions[a].update(model_predictions['Response'])
        if a == 'Confidence':
            predictions[a].update(model_predictions['Confidence'])
    requests.post("http://localhost:8000/api/compliance/submit_predictions/", data={"predictions": json.dumps(predictions), "merchant": merchant, "user": user_id})
    return
