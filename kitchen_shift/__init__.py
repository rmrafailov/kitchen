from gym.envs.registration import register

try:
    from .kitchen_v0 import Kitchen_v0

    register(
        id='kitchen-v0',
        entry_point='kitchen_shift.kitchen_v0:Kitchen_v0',
        max_episode_steps=280,
    )
except:
    pass

try:
    from .kitchen_v1 import Kitchen_v1

    register(
        id='kitchen-v1',
        entry_point='kitchen_shift.kitchen_v1:Kitchen_v1',
        max_episode_steps=280,
    )
except:
    pass


#try:
#    from .randomized_kitchen import Randomized_Kitchen
#
#    register(
#        id='randomized_kitchen-v1',
#        entry_point='kitchen_shift.randomized_kitchen:Randomized_Kitchen',
#        max_episode_steps=280,
#    )
#except:
#    pass

from .randomized_kitchen import Randomized_Kitchen

register(
        id='randomized_kitchen-v1',
        entry_point='kitchen_shift.randomized_kitchen:Randomized_Kitchen',
        max_episode_steps=1000,
        )
from .mujoco.worldgen import MujocoWorldgenKitchenEnvWrapper
