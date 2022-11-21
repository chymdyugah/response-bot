from django.apps import AppConfig
from django.apps import AppConfig
from haystack.nodes import FARMReader
from haystack import Pipeline
import os

os.environ["TOKENIZERS_PARALLELISM"] = "false"


class BotConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bot'
    reader = FARMReader(model_name_or_path="deepset/roberta-base-squad2", top_k=3, use_gpu=False) # return_no_answer=True

    #model pipeline
    MODEL = Pipeline()
    MODEL.add_node(component= reader, name="Reader", inputs=["Query"])
