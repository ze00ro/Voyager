import os
from voyager import Voyager

openai_api_key = ""

# seed 1392041844
# https://github.com/MineDojo/Voyager/issues/77


mc_port = 62528

# new
voyager = Voyager(
    mc_port=mc_port,
    openai_api_key=openai_api_key,
)

# resume
# voyager = Voyager(
#     mc_port=mc_port,
#     openai_api_key=openai_api_key,
#     ckpt_dir="./ckpt-160",
#     resume=True,
#     max_iterations=1000,
# )

# start lifelong learning
voyager.learn()



