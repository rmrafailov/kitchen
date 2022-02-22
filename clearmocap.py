import gym
import copy
import h5py
import kitchen_shift
import os
import time

import numpy as np
import matplotlib.pyplot as plt

from pyquaternion import Quaternion
from oculus_reader.reader import OculusReader
from kitchen_shift.mujoco.rotations import euler2quat, mat2euler, quat2euler, mat2quat, quat_mul


reader = OculusReader()

env = gym.make('randomized_kitchen-v1', ctrl_mode='mixmocapik')
obs = env.reset()

    path = '/home/rafael/IRIS/vd5rl/HDF.h5'
    f = h5py.File(path, "a")
    datasets = dict()
    for k in obs.keys():
        datasets[k] = f.create_dataset(k, (1, env._max_episode_steps, *obs[k].shape), 
                maxshape=(None, env._max_episode_steps, *obs[k].shape), dtype=obs[k].dtype)
    
    for j in range(3):
        
        time.sleep(3)
        obs = env.reset()
        episode = dict()
        
        for k, v in obs.items():
            episode[k] = np.zeros(shape = [env._max_episode_steps + 1] + list(v.shape), dtype = v.dtype)
            episode[k][0] = copy.deepcopy(v)
        episode['action'] = np.zeros(shape = [env._max_episode_steps + 1, env.env.N_DOF_ROBOT])
        episode['reward'] = np.zeros(shape = [env._max_episode_steps + 1])
        episode['done'] = np.zeros(shape = [env._max_episode_steps + 1])
        
        d = copy.deepcopy(env.domain)
        episode['domain'] = copy.deepcopy(d)
                
        
        
        init = reader.get_transformations_and_buttons()
        m = init[0]['r'][:3, :3]
        e_init = mat2euler(m).copy()
        
        pos_old = init[0]['r'][:3, -1]
        init_sim_quat = env.solver_sim.data.mocap_quat.copy()[0]
        init_sim_e = quat2euler(init_sim_quat)
        
        for i in range(1, env._max_episode_steps + 1):
            
            out = reader.get_transformations_and_buttons()
            rot_matrix = out[0]['r'][:3, :3]
            
            e = mat2euler(rot_matrix).copy()
            angles = e.copy()
            angles[0] = -(e[0] - e_init[0]) + init_sim_e[0]
            angles[1] = (e[1] - e_init[1]) + init_sim_e[1]
            angles[2] = -(e[2] - e_init[2]) + init_sim_e[2]
            
            
            pos = out[0]['r'][:3, -1]
            pos_ctrl = pos - pos_old
            pos_old = pos.copy()
            
            gripper = 1.0 * out[1]['RTr']
            
            control = np.zeros(9)
            control[0] =- 200 * pos_ctrl[0]
            control[1] = 200 * pos_ctrl[2]
            control[2] = 200 * pos_ctrl[1]
            control[3:7] = euler2quat(angles)
            
            if gripper > 0:
                control[7:] = -1.0
            else:
                control[7:] = 1.0
                
            
        
            obs, rew, done, info = env.step(control)
            for k,v in obs.items():
                episode[k][i] = copy.deepcopy(v)
            episode['action'][i] = copy.deepcopy(info['action'])
            episode['reward'][i] = copy.deepcopy(rew)
            episode['done'][i] = copy.deepcopy(done)
            env.render()
            
        for k in obs.keys():
            datasets[k][j] = episode[k]
            datasets[k].resize(datasets[k].shape[0] + 1, axis = 0)
        