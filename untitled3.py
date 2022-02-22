#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 09:24:37 2022

@author: rafael
"""

obs = env.reset()
env.perturb_camera_params()
plt.imshow(obs['rgb_array'])

env = MujocoWorldgenKitchenEnvWrapper()

obs = env.reset()
plt.imshow(obs['rgb_array'])



obs = env0.reset()
plt.imshow(obs['rgb_array'])



        
        mode = 'rgb_array'
        camera_id = None
        depth = False
        segmentation = False
        
        imgs = {}
        if 'rgb' in mode:
            if camera_id is None:
                camera_id = env.camera_id

            # TODO: cache camera? doesn't seem to affect performance that much
            # also use camera._scene.free()? though it will slow things down
            if camera_id is None:
                camera_id = env.camera_id
            camera = engine.MovableCamera(env.sim, height=128, width=128)
            if env.camera_params is None:
                camera.set_pose(**CAMERAS[camera_id])
            else:
                camera.set_pose(**env.camera_params)
                
            # http://www.mujoco.org/book/APIreference.html#mjvOption
            # https://github.com/deepmind/dm_control/blob/9e0fe0f0f9713a2a993ca78776529011d6c5fbeb/dm_control/mujoco/engine.py#L200
            # mjtRndFlag(mjRND_SHADOW=0, mjRND_WIREFRAME=1, mjRND_REFLECTION=2, mjRND_ADDITIVE=3, mjRND_SKYBOX=4, mjRND_FOG=5, mjRND_HAZE=6, mjRND_SEGMENT=7, mjRND_IDCOLOR=8, mjNRNDFLAG=9)
            if not (depth or segmentation):  # RGB
                img = camera.render(render_flag_overrides=dict(skybox=False, fog=False, haze=False))
            else:
                img = camera.render(depth=depth, segmentation=segmentation)
            imgs['rgb_array'] = img
            
            camera_gripper = engine.Camera(env.sim, height=128, width=128, camera_id='gripper_camera_rgb')
            gripper_img = camera_gripper.render()
            imgs['rgb_gripper'] = gripper_img
        plt.imshow(imgs['rgb_array'])
        
        
        imgs2 = {}
        if 'rgb' in mode:
            if camera_id is None:
                camera_id = env.camera_id

            # TODO: cache camera? doesn't seem to affect performance that much
            # also use camera._scene.free()? though it will slow things down
            if camera_id is None:
                camera_id = env.camera_id
            camera = engine.MovableCamera(env.solver_sim, height=128, width=128)
            if env.camera_params is None:
                camera.set_pose(**CAMERAS[camera_id])
            else:
                camera.set_pose(**env.camera_params)
                
            # http://www.mujoco.org/book/APIreference.html#mjvOption
            # https://github.com/deepmind/dm_control/blob/9e0fe0f0f9713a2a993ca78776529011d6c5fbeb/dm_control/mujoco/engine.py#L200
            # mjtRndFlag(mjRND_SHADOW=0, mjRND_WIREFRAME=1, mjRND_REFLECTION=2, mjRND_ADDITIVE=3, mjRND_SKYBOX=4, mjRND_FOG=5, mjRND_HAZE=6, mjRND_SEGMENT=7, mjRND_IDCOLOR=8, mjNRNDFLAG=9)
            if not (depth or segmentation):  # RGB
                img = camera.render(render_flag_overrides=dict(skybox=False, fog=False, haze=False))
            else:
                img = camera.render(depth=depth, segmentation=segmentation)
            imgs2['rgb_array'] = img
            
            camera_gripper = engine.Camera(env.sim, height=128, width=128, camera_id='gripper_camera_rgb')
            gripper_img = camera_gripper.render()
            imgs2['rgb_gripper'] = gripper_img
        plt.imshow(imgs2['rgb_array'])   
        