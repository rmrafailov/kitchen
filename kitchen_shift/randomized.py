import numpy as np
import matplotlib.pyplot as plt

microwave_positions = ['closer', 
                       'closer_angled']
kettle_positions = ['top_right',
                    'bot_right',
                    'bot_right_angled',
                    'bot_left_angled']

cabinet_textures = ['wood1', 
                    'wood2', 
                    'metal1', 
                    'metal2', 
                    'marble1', 
                    'tile1']

lighting_options = ['cast_left',
                    'cast_right',
                    'brighter',
                    'darker']

counter_textures = ['white_marble_tile2',
                    'tile1',
                    'wood1',
                    'wood2',
                    ]

floor_textures = ['white_marble_tile',
                  'marble1',
                  'tile1',
                  'wood1',
                  'wood2',
                  'checker',
                  ]      


domain_parameters = [('change_camera', 2)]

microwave_idx = np.random.choice(5)
if microwave_idx < 4:
    domain_parameters.append(('change_microwave', microwave_idx))


kettle_idx = np.random.choice(7)
if kettle_idx < 6:
    domain_parameters.append(('change_kettle', kettle_idx))


microwave_position = np.random.choice(3)
if microwave_position < 2:
    domain_parameters.append(('change_objects_layout', 'microwave', microwave_positions[microwave_position]))


kettle_position = np.random.choice(5)
if kettle_position < 4:
    domain_parameters.append(('change_objects_layout', 'kettle', kettle_positions[kettle_position]))


hinge_texture = np.random.choice(7)
if hinge_texture < 6:
    domain_parameters.append(('change_hinge_texture', cabinet_textures[hinge_texture]))


slide_texture = np.random.choice(7)
if slide_texture < 6:
    domain_parameters.append(('change_slide_texture', cabinet_textures[slide_texture]))

#
#lighting_option = np.random.choice(5)
#if lighting_option < 4:
#    domain_parameters.append(('change_lighting', lighting_options[lighting_option]))


counter_texture = np.random.choice(5)
if counter_texture < 4:
    domain_parameters.append(('change_counter_texture', counter_textures[counter_texture]))


floor_texture = np.random.choice(7)
if floor_texture < 6:
    domain_parameters.append(('change_floor_texture', floor_textures[floor_texture]))


# 4. Apply domain shifts to env
env.reset_domain_changes()
for p in domain_parameters:
    fn = getattr(env, p[0])
    fn(*p[1:])

env.reset(reload_model_xml=True)

obs = env.render(mode='rgb_array')
plt.imshow(obs)