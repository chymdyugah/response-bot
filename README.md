# response-bot
A question answering model wrapped in django.

**ENSURE YOU SET THESE ENVIRONMENT VARIABLES**\n
DEBUG\n
TOKENIZERS_PARALLELISM\n
SECRET_KEY\n
SUBMISSION_SERVER\n
MODEL_PATH (see https://huggingface.co/models?pipeline_tag=question-answering for available models)

To try this out; \n
start your server.
make a post repuest to this endpoint(/bot/run/) with a json body with these keys
questions: a list of string(questions you want answered)
user_info: a string containing the passage with answers to the questions
merchant: a string (can be anything, an empty string will suffice)
user_id: a int (can be any number)

OR

run your django shell(python manage.py shell) and run these commands:
from bot.tasks import upload_to_ai as ai
questions = ["who is chymdy?", "where did he live?", "where does beth live?"]  # your list of questions
user_info = "there is a man named chymdy, he is a smiley and an introvert. Beth lives in the far away west. in a land of hills and rocks. Chymdy on the other hand, stays in a cave."  # your passage containing answers to your questions
ai(questions, user_info)
