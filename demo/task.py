import os
from voyager import Voyager

openai_api_key = ""

# seed? 1392041844
# https://github.com/MineDojo/Voyager/issues/77

# 怎么看
# /gamemode spectator
# /spectate bot
# https://github.com/MineDojo/Voyager/issues/19
# https://github.com/MineDojo/Voyager/issues/115

mc_port = 51787

voyager = Voyager(
    mc_port=mc_port,
    openai_api_key=openai_api_key,
    skill_library_dir="./skill_library/trial1",  # Load a learned skill library.
    ckpt_dir="./tmp/ckpt4",
    resume=False,
)

task = "make 2 craft table then drop them on the ground"
sub_goals = voyager.decompose_task(task=task)

voyager.inference(sub_goals=sub_goals)


