import os
from voyager import Voyager

openai_api_key = os.environ['OPENAI_API_KEY']

mc_port = 62528

# 新学习
voyager = Voyager(
    mc_port=mc_port,
    openai_api_key=openai_api_key,
)

# 继续学习, 没啥效果, 因为你没有对方的世界进度, 所以可以用这个进度运行 task
# voyager = Voyager(
#     mc_port=mc_port,
#     openai_api_key=openai_api_key,
#     ckpt_dir="./ckpt-160",
#     resume=True,
#     max_iterations=1000,
# )

voyager.learn()



