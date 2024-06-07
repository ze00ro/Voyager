import os
from voyager import Voyager
import shutil

openai_api_key = os.environ['OPENAI_API_KEY']

mc_port = 50495

try:
    shutil.rmtree('./tmp')
except Exception as ex:
    print(f"delete failed with {ex}")
os.mkdir('./tmp')

voyager = Voyager(
    mc_port=mc_port,
    openai_api_key=openai_api_key,
    skill_library_dir="./skill_library/trial3",  # Load a learned skill library.
    ckpt_dir="./tmp",
    resume=False,
)

task = "kill three cows"
sub_goals = voyager.decompose_task(task=task)

voyager.inference(sub_goals=sub_goals)


