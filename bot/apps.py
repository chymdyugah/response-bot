from django.apps import AppConfig
from django.apps import AppConfig
from haystack.nodes import FARMReader
from haystack import Pipeline
from decouple import config
import os

os.environ["TOKENIZERS_PARALLELISM"] = config("TOKENIZERS_PARALLELISM")  # do this to avoid problems with multiprocessing


class BotConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bot'
    model_path = config("MODEL_PATH")
    reader = FARMReader(model_name_or_path=model_path, top_k=3, use_gpu=False) # return_no_answer=True

    #model pipeline
    MODEL = Pipeline()
    MODEL.add_node(component= reader, name="Reader", inputs=["Query"])
