""" =================================================
# Copyright (c) MyoSuite Authors
Authors  :: Sherwin Chan (sherwin.chan@ntu.edu.sg), J-Anne Yow (janne.yow@ntu.edu.sg), Chun Kwang Tan (cktan.neumove@gmail.com), Vikash Kumar (vikashplus@gmail.com), Vittorio Caggiano (caggiano@gmail.com), Pierre Schumacher (schumacherpier@gmail.com)
================================================= """

import collections
from myosuite.utils import gym
import numpy as np
import os
from enum import Enum
from typing import Optional, Tuple

import pink

from myosuite.envs.myo.base_v0 import BaseV0
from myosuite.envs.myo.myobase.walk_v0 import WalkEnvV0
from myosuite.utils.quat_math import quat2euler, euler2mat, euler2quat

class GoalKeeper:
    """
    GoalKeeper for the Soccer Track of the MyoChallenge 2025.
    Manages the goalkeeper's behaviour, including randomized movement speed
    and probabilities of blocking the goal.
    Contains several different policies. For the final evaluation, an additional
    non-disclosed policy will be used.
    """
    FIXED_X_POS = 50  # Initial position for the goalkeeper
    Y_MIN_BOUND = -3.3
    Y_MAX_BOUND = 3.3
    P_GAIN = 5.0
    
    def __init__(self,
                 sim,
                 rng,
                 random_vel_range: Tuple[float],
                 probabilities=(0.1, 0.35, 0.55),
                 dt=0.01,):
        """
        Initialize the GoalKeeper class.
        :param sim: Mujoco sim object.
        :param rng: np_random generator.
        :param probabilities: Probabilities for the different policies, (block_ball, random, stationary).
        :param random_vel_range: Range of velocities for the block_ball policy. Clipped.
        :param dt: Simulation timestep.
        """
        self.dt = dt
        self.sim = sim
        self.goalkeeper_probabilities = probabilities
        self.random_vel_range = random_vel_range
        self.rng = rng

        self.block_velocity = self.rng.uniform(self.random_vel_range[0], self.random_vel_range[1])
        self.reset_goalkeeper(rng=rng)

    def reset_noise_process(self):
        self.noise_process = pink.ColoredNoiseProcess(beta=2, size=(2, 10), scale=self.block_velocity, rng=self.rng)

    def get_goalkeeper_pose(self):
        """
        Get goalkeeper Pose
        :return: The  pose.
        :rtype: list -> [x, y, angle]
        """
        angle = quat2euler(self.sim.data.mocap_quat[0, :])[-1]
        return np.concatenate([self.sim.data.mocap_pos[0, :2], [angle]])

    def set_goalkeeper_pose(self, pose: list):
        """
        Set goalkeeper pose directly.
        :param pose: Pose of the goalkeeper.
        :type pose: list -> [x, y, angle]
        """
        # Enforce goalkeeper limits
        pose[0] = self.FIXED_X_POS   
        pose[1] = np.clip(pose[1], self.Y_MIN_BOUND, self.Y_MAX_BOUND) 

        self.sim.data.mocap_pos[0, :2] = pose[:2]
        self.sim.data.mocap_quat[0, :] = euler2quat([0, 0, pose[-1]])

    def move_goalkeeper(self, vel: list):
        """
        This is the main function that moves the goalkeeper and should always be used if you want to physically move
        it by giving it a velocity. If you want to teleport it to a new position, use `set_goalkeeper_pose`.
        :param vel: Linear and rotational velocities in [-1, 1]. Moves goalkeeper
                  forwards or backwards and turns it. vel[0] is assumed to be linear vel and
                  vel[1] is assumed to be rotational vel
        :type vel: list -> [lin_vel, rot_vel].
        """
        self.goalkeeper_vel = vel
        assert len(vel) == 2

        lin_vel = vel[0]
        pose = self.get_goalkeeper_pose()
        pose[1] += self.dt * lin_vel
        
        self.set_goalkeeper_pose(pose)      # Enforce goalkeeper limits here
    
    def random_movement(self):
        """
        This moves the goalkeeper randomly in a correlated
        pattern.
        """
        return np.clip(self.noise_process.sample(), -self.block_velocity, self.block_velocity)
    
    def block_ball_policy(self):
        """
        Calculates the linear velocity along the Y-axis required for the goalkeeper to
        move towards and block the ball.
        The goalkeeper's orientation and X-position are fixed.
        The target Y for the goalkeeper is clipped to its valid movement range.
        """
        goalkeeper_pose = self.get_goalkeeper_pose()
        ball_pos = self.sim.data.body('soccer_ball').xpos[:3].copy()

        # Clip the target Y position to the goalkeeper's allowed range
        target_y = np.clip(ball_pos[1], self.Y_MIN_BOUND, self.Y_MAX_BOUND)
        current_y = goalkeeper_pose[1]

        displacement = target_y - current_y

        linear_vel_y = np.clip(displacement, -self.block_velocity, self.block_velocity)
        
        return np.array([linear_vel_y, 0.0])
        # return np.array([linear_vel_y * self.P_GAIN, 0.0])

    def sample_goalkeeper_policy(self):
        """
        Takes in three probabilities and returns the policies with the given frequency.
        """
        rand_num = self.rng.uniform()
        if rand_num < self.goalkeeper_probabilities[0]:
            self.goalkeeper_policy = 'block_ball'
        elif rand_num < self.goalkeeper_probabilities[0] + self.goalkeeper_probabilities[1]:
            self.goalkeeper_policy = 'random'
        elif rand_num < self.goalkeeper_probabilities[0] + self.goalkeeper_probabilities[1] + self.goalkeeper_probabilities[2]:
            self.goalkeeper_policy = 'stationary'

    def update_goalkeeper_state(self):
        """
        This function executes an goalkeeper step with
        one of the control policies.
        """
        if self.goalkeeper_policy == 'stationary':
            goalkeeper_vel = np.zeros(2,)

        elif self.goalkeeper_policy == 'random':
            goalkeeper_vel = self.random_movement()

        elif self.goalkeeper_policy == 'block_ball':
            goalkeeper_vel = self.block_ball_policy()
        else:
            raise NotImplementedError(f"This goalkeeper policy doesn't exist. Chose: stationary, random or block_ball. Policy was: {self.goalkeeper_policy}")
        self.move_goalkeeper(goalkeeper_vel)

    def reset_goalkeeper(self, rng=None):
        """
        Resets the goalkeeper's position, policy, and blocking speed.
        :rng: np_random generator
        """
        if rng is not None:
            self.rng = rng
            self.reset_noise_process()

        self.goalkeeper_vel = np.zeros((2,))
        self.sample_goalkeeper_policy()

        self.rng_loc = self.rng.uniform(self.Y_MIN_BOUND, self.Y_MAX_BOUND)

        initial_goalkeeper_pos = [self.FIXED_X_POS, self.rng_loc, 0]
        self.set_goalkeeper_pose(initial_goalkeeper_pos)
        self.goalkeeper_vel[:] = 0.0

        # Randomize the maximum linear speed for the 'block_ball' policy for this reset.
        # This value is used within the `block_ball_policy` to clip movement speed.
        self.block_velocity = self.rng.uniform(self.random_vel_range[0], self.random_vel_range[1])

class SoccerEnvV0(WalkEnvV0):
    DEFAULT_OBS_KEYS = [
        'internal_qpos',
        'internal_qvel',
        'grf',
        'torso_angle',
        'ball_pos',
        'model_root_pos',
        'model_root_vel',
        'muscle_length',
        'muscle_velocity',
        'muscle_force',
    ]

    # You can change reward weights here
    DEFAULT_RWD_KEYS_AND_WEIGHTS = {
        "goal_scored": 1000,
        "time_cost": -0.01,
        "act_reg": -100,
        "pain": -10,
    }

    # Goal dimensions based on Goalkeeper's fixed position and Y-bounds
    GOAL_X_POS = GoalKeeper.FIXED_X_POS # Ball must cross this X-coordinate
    GOAL_Y_MIN = GoalKeeper.Y_MIN_BOUND # Ball must be within this Y-range
    GOAL_Y_MAX = GoalKeeper.Y_MAX_BOUND
    GOAL_Z_MIN = 0.0 
    GOAL_Z_MAX = 2.2 

    # Joint overextension dict
    JNT_OVEREXT = ['hip_adduction_l', 'hip_adduction_r', 'hip_flexion_l', 'hip_flexion_r', 'hip_rotation_l', 'hip_rotation_r',
                'knee_angle_l', 'knee_angle_l_rotation2', 'knee_angle_l_rotation3',
                'mtp_angle_l', 'ankle_angle_l', 'subtalar_angle_l']

    def __init__(self, model_path, obsd_model_path=None, seed=None, **kwargs):
        # This flag needs to be here to prevent the simulation from starting in a done state
        # Before setting the key_frames, the model and goalkeeper will be in the cartesian position,
        # causing the step() function to evaluate the initialization as "done".
        self.startFlag = False

        # EzPickle.__init__(**locals()) is capturing the input dictionary of the init method of this class.
        # In order to successfully capture all arguments we need to call gym.utils.EzPickle.__init__(**locals())
        # at the leaf level, when we do inheritance like we do here.
        # kwargs is needed at the top level to account for injection of __class__ keyword.
        # Also see: https://github.com/openai/gym/pull/1497
        gym.utils.EzPickle.__init__(self, model_path, obsd_model_path, seed, **kwargs)

        # This two step construction is required for pickling to work correctly. All arguments to all __init__
        # calls must be pickle friendly. Things like sim / sim_obsd are NOT pickle friendly. Therefore we
        # first construct the inheritance chain, which is just __init__ calls all the way down, with env_base
        # creating the sim / sim_obsd instances. Next we run through "setup"  which relies on sim / sim_obsd
        # created in __init__ to complete the setup.
        BaseV0.__init__(self, model_path=model_path, obsd_model_path=obsd_model_path, seed=seed, env_credits=self.MYO_CREDIT)
        self._setup(**kwargs)

    def _setup(self,
               obs_keys: list = DEFAULT_OBS_KEYS,
               weighted_reward_keys: dict = DEFAULT_RWD_KEYS_AND_WEIGHTS,
               reset_type='none',
               min_agent_spawn_distance=1,
               random_vel_range=(1.0, 5.0),
               rnd_pos_noise=1.0,
               rnd_joint_noise=0.02,
               goalkeeper_probabilities=(0.1, 0.45, 0.45),
               max_time_sec=10,
               **kwargs,
               ):

        self._setup_convenience_vars()

        self.reset_type = reset_type
        self.rnd_pos_noise = rnd_pos_noise
        self.rnd_joint_noise = rnd_joint_noise
        self.max_time = max_time_sec # in seconds

        self.goalkeeper = GoalKeeper(sim=self.sim,
                                     rng=self.np_random,
                                     probabilities=goalkeeper_probabilities,
                                     random_vel_range=random_vel_range)

        self.grf_sensor_names = ['r_foot', 'r_toes', 'l_foot', 'l_toes']
        self.myo_joints = ['Abs_r3', 'Abs_t1', 'Abs_t2', 'L1_L2_AR', 'L1_L2_FE', 'L1_L2_LB', 'L2_L3_AR', 'L2_L3_FE', 'L2_L3_LB', 
                            'L3_L4_AR', 'L3_L4_FE', 'L3_L4_LB', 'L4_L5_AR', 'L4_L5_FE', 'L4_L5_LB', 
                            'ankle_angle_l', 'ankle_angle_r', 'axial_rotation', 'flex_extension', 'hip_adduction_l', 
                            'hip_adduction_r', 'hip_flexion_l', 'hip_flexion_r', 'hip_rotation_l', 'hip_rotation_r', 
                            'knee_angle_l', 'knee_angle_l_beta_rotation1', 'knee_angle_l_beta_translation1', 'knee_angle_l_beta_translation2',
                             'knee_angle_l_rotation2', 'knee_angle_l_rotation3', 'knee_angle_l_translation1', 'knee_angle_l_translation2',
                             'knee_angle_r', 'knee_angle_r_beta_rotation1', 'knee_angle_r_beta_translation1', 'knee_angle_r_beta_translation2', 
                             'knee_angle_r_rotation2', 'knee_angle_r_rotation3', 'knee_angle_r_translation1', 'knee_angle_r_translation2', 
                             'lat_bending', 'mtp_angle_l', 'mtp_angle_r', 'subtalar_angle_l', 'subtalar_angle_r']
       
        super()._setup(obs_keys=obs_keys,
                       weighted_reward_keys=weighted_reward_keys,
                       reset_type=reset_type,
                       **kwargs
                       )
        self.init_qpos[:] = self.sim.model.key_qpos[0]
        self.init_qvel[:] = 0.0
        self.startFlag = True
        self.assert_settings()
        self.goalkeeper.dt = self.sim.model.opt.timestep * self.frame_skip

        self.min_agent_spawn_distance = min_agent_spawn_distance


    def assert_settings(self):

        for prob in self.goalkeeper.goalkeeper_probabilities:
            assert 0 <= prob <= 1, "GoalKeeper probabilities should be between 0 and 1"
        assert np.isclose(np.sum(self.goalkeeper.goalkeeper_probabilities), 1.0), \
            "GoalKeeper probabilities should sum to 1.0"

        # Assertions for random_vel_range
        assert self.goalkeeper.random_vel_range[0] >= 0, \
            "GoalKeeper block_vel_range min must be greater than or equal to 0"
        assert self.goalkeeper.random_vel_range[0] <= self.goalkeeper.random_vel_range[1], \
            "GoalKeeper block_vel_range min must be less than or equal to max"


    def get_obs_dict(self, sim):
        obs_dict = {}

        # Time
        obs_dict['time'] = np.array([self.sim.data.time])

        # proprioception
        obs_dict['internal_qpos'] = self._get_joint_qpos()
        obs_dict['internal_qvel'] = self._get_joint_qvel() * self.dt
        obs_dict['grf'] = self._get_grf().copy()
        obs_dict['torso_angle'] = self.sim.data.body('torso').xquat.copy()
        obs_dict['pelvis_angle'] = self.sim.data.body('pelvis').xquat.copy()

        obs_dict['muscle_length'] = self.muscle_lengths()
        obs_dict['muscle_velocity'] = self.muscle_velocities()
        obs_dict['muscle_force'] = self.muscle_forces()

        obs_dict['r_toe_pos'] = self.sim.data.geom('r_bofoot').xpos.copy()
        obs_dict['l_toe_pos'] = self.sim.data.geom('l_bofoot').xpos.copy()

        if self.sim.model.na>0:
            obs_dict['act'] = self.sim.data.act[:].copy()

        # exteroception
        obs_dict['ball_pos'] = self.sim.data.body('soccer_ball').xpos[:3].copy()
        obs_dict['goal_bounds'] = np.array([[self.GOAL_X_POS, self.GOAL_Y_MIN, self.GOAL_Z_MIN], 
                                            [self.GOAL_X_POS, self.GOAL_Y_MAX, self.GOAL_Z_MIN], 
                                            [self.GOAL_X_POS, self.GOAL_Y_MIN, self.GOAL_Z_MAX], 
                                            [self.GOAL_X_POS, self.GOAL_Y_MAX, self.GOAL_Z_MAX]]).flatten()
        obs_dict['model_root_pos'] = self.sim.data.joint('root').qpos.copy()
        obs_dict['model_root_vel'] = self.sim.data.joint('root').qvel.copy()

        return obs_dict

    def get_reward_dict(self, obs_dict):
        """
        Rewards are computed from here, using the <self.weighted_reward_keys>.
        These weights can either be set in this file in the
        DEFAULT_RWD_KEYS_AND_WEIGHTS dict, or when registering the environment
        with gym.register in myochallenge/__init__.py
        """
        # act_mag = np.linalg.norm(self.obs_dict['act'], axis=-1)/self.sim.model.na if self.sim.model.na !=0 else 0
        act_mag = np.mean( np.square(self.obs_dict['act']) ) if self.sim.model.na !=0 else 0

        goal_scored = self._goal_scored_condition()
        time_limit_exceeded = self.obs_dict['time'] >= self.max_time
        fallen = self._get_fallen_condition()

        pain = self.get_jnt_limit_violation() # Joint limit violation torque as pain score
        done = bool(goal_scored or time_limit_exceeded or fallen)
        # ----------------------

        # Example reward, you should change this!
        distance = np.linalg.norm(obs_dict['model_root_pos'].flatten()[0:3] - obs_dict['ball_pos'].flatten())

        rwd_dict = collections.OrderedDict((
            # Perform reward tuning here --
            # Update Optional Keys section below
            # Update reward keys (DEFAULT_RWD_KEYS_AND_WEIGHTS) accordingly to update final rewards

            # Example: simple distance function

                # Optional Keys
                ('goal_scored', float(goal_scored)),
                ('time_cost', float(self.obs_dict['time'])),
                ('act_reg', act_mag),
                ('pain', pain),
                # Must keys
                ('sparse',  float(done)),
                ('solved',  float(goal_scored)),
                ('done',  float(self._get_done())),
            ))
        rwd_dict['dense'] = np.sum([wt*rwd_dict[key] for key, wt in self.rwd_keys_wt.items()], axis=0)
        # Success Indicator
        # self.sim.model.site_rgba[self.success_indicator_sid, :] = np.array([0, 2, 0, 0.2]) if rwd_dict['solved'] else np.array([2, 0, 0, 0])
        return rwd_dict

    def get_metrics(self, paths):
        """
        Evaluate paths and report metrics
        """
        # average sucess over entire env horizon
        score = np.mean([np.sum(p['env_infos']['rwd_dict']['solved']) for p in paths])
        points = np.mean([np.sum(p['env_infos']['rwd_dict']['sparse']) for p in paths])
        times = np.mean([np.round(p['env_infos']['obs_dict']['time'][-1],2) for p in paths])
        effort = np.mean([np.sum(p['env_infos']['rwd_dict']['act_reg']) for p in paths])
        pain = np.mean([np.sum(p['env_infos']['rwd_dict']['pain']) for p in paths])
        # average activations over entire trajectory (can be shorter than horizon, if done) realized

        metrics = {
            'score': score,
            'points': points,
            'times': times,
            'effort':effort,
            'pain':pain,
            }
        return metrics

    def step(self, *args, **kwargs):
        self.goalkeeper.update_goalkeeper_state()
        results = super().step(*args, **kwargs)
        return results

    def reset(self, **kwargs):
        # randomized initial state
        qpos, qvel = self._get_reset_state()
        self.robot.sync_sims(self.sim, self.sim_obsd)
        obs = super(WalkEnvV0, self).reset(reset_qpos=qpos, reset_qvel=qvel, **kwargs)
        self.goalkeeper.reset_goalkeeper(rng=self.np_random)
        self.sim.forward()
        return obs

    def _randomize_position_orientation(self, qpos, qvel):
        qpos[:2]  = self.np_random.uniform(-5, 5, size=(2,))
        orientation = self.np_random.uniform(0, 2 * np.pi)
        euler_angle = quat2euler(qpos[3:7])
        euler_angle[-1] = orientation
        qpos[3:7] = euler2quat(euler_angle)
        # rotate original velocity with unit direction vector
        qvel[:2] = np.array([np.cos(orientation), np.sin(orientation)]) * np.linalg.norm(qvel[:2])
        return qpos, qvel
    
    def _get_reset_state(self):
        if self.reset_type == 'random':
            qpos, qvel = self._get_randomized_initial_state()
            # return self._randomize_position_orientation(qpos, qvel)
            return qpos, qvel
        elif self.reset_type == 'init':
            return self.sim.model.key_qpos[0], self.sim.model.key_qvel[0]
        else:
            return self.sim.model.key_qpos[0], self.sim.model.key_qvel[0]

    def viewer_setup(self, *args, **kwargs):
       """
       Setup the default camera
       """
       distance = 5.0
       azimuth = 90
       elevation = -15
       lookat = None
       self.sim.renderer.set_free_camera_settings(
               distance=distance,
               azimuth=azimuth,
               elevation=elevation,
               lookat=lookat
       )
       render_tendon = True
       render_actuator = True
       self.sim.renderer.set_viewer_settings(
           render_actuator=render_actuator,
           render_tendon=render_tendon
       )

    def _get_randomized_initial_state(self):
        # Setting initial keypose values
        self.sim.data.qpos = self.sim.model.key_qpos[0].copy()
        self.sim.data.qvel = self.sim.model.key_qvel[0].copy()

        # Note: No randomization for ball, a goal kick ball position has to be fixed

        # Add some noise to the joints
        for jnt in self.myo_joints:
            self.sim.data.joint(jnt).qpos[0] += self.np_random.uniform(-np.abs(self.rnd_joint_noise), np.abs(self.rnd_joint_noise), size=(1,))

        # Body start position randomizations
        # Treatment for root joint is different
        self.sim.data.joint('root').qpos[0] += self.np_random.uniform(-np.abs(self.rnd_pos_noise), 0, size=(1,)) # Only allow body to move behind the ball, not in front
        self.sim.data.joint('root').qpos[1] += self.np_random.uniform(-np.abs(self.rnd_pos_noise), np.abs(self.rnd_pos_noise),size=(1,)) # Y-direction movement allowable

        return self.sim.data.qpos.copy(), self.sim.data.qvel.copy()

    def _setup_convenience_vars(self):
        """
        Convenience functions for easy access. Important: There will be no access during the challenge evaluation to this,
        but the values can be hard-coded, as they do not change over time.
        """
        self.actuator_names = np.array(self._get_actuator_names())
        self.joint_names = np.array(self._get_joint_names())
        self.muscle_fmax = np.array(self._get_muscle_fmax())
        self.muscle_lengthrange = np.array(self._get_muscle_lengthRange())
        self.tendon_len = np.array(self._get_tendon_lengthspring())
        self.musc_operating_len = np.array(self._get_muscle_operating_length())

        self.soccer_ball_id = self.sim.model.body_name2id('soccer_ball')

    def _get_done(self):
        if self._goal_scored_condition():
            return 1
        if (self.obs_dict['time'] >= self.max_time):
            return 1
        if self._get_fallen_condition():
            return 1
        return 0

    def _goal_scored_condition(self):
        """
        Checks if the ball has entered the goal.
        The ball must cross GOAL_X_POS and be within the GOAL_Y/Z bounds.
        """
        ball_pos = self.sim.data.body(self.soccer_ball_id).xpos.copy()

        is_x_past_goal = ball_pos[0] >= self.GOAL_X_POS
        is_y_in_bounds = self.GOAL_Y_MIN <= ball_pos[1] <= self.GOAL_Y_MAX
        is_z_in_bounds = self.GOAL_Z_MIN <= ball_pos[2] <= self.GOAL_Z_MAX

        return bool(is_x_past_goal and is_y_in_bounds and is_z_in_bounds)

    def _get_fallen_condition(self):
        """
        Checks if the agent has fallen by checking the if the height of the pelvis is too near to the ground
        """
        pelvis = self.sim.data.body('pelvis').xpos
        if pelvis[2] < 0.2:
            return 1
        else:
            return 0

    def get_jnt_limit_violation(self):
        """
        Normalized sum of the joint limit violation forces.
        """
        if not self.startFlag:
            return -1

        limit_score = 0
        for joint in self.JNT_OVEREXT:
            limit_score += np.abs(np.clip(self.get_limitfrc(joint).squeeze(), -1000, 1000)) / 1000
        return limit_score / len(self.JNT_OVEREXT)

    # Helper functions
    def _get_body_mass(self):
        """
        Get total body mass of the biomechanical model.
        :return: the weight
        :rtype: float
        """
        return self.sim.model.body('root').subtreemass

    def _get_body_pos(self):
        '''
        Return an array of body positions [X,Y,Z, Quaternion]
        '''
        return np.array()

    def _get_score(self, time):
        time = np.round(time, 2)
        return 1 - (time / self.max_time)

    def _get_muscle_lengthRange(self):
        return self.sim.model.actuator_lengthrange.copy()

    def _get_tendon_lengthspring(self):
        return self.sim.model.tendon_lengthspring.copy()

    def _get_muscle_operating_length(self):
        return self.sim.model.actuator_gainprm[:,0:2].copy()

    def _get_muscle_fmax(self):
        return self.sim.model.actuator_gainprm[:, 2].copy()

    def _get_grf(self):
        return np.array([self.sim.data.sensor(sens_name).data[0] for sens_name in self.grf_sensor_names]).copy()

    def _get_pelvis_angle(self):
        return self.sim.data.body('pelvis').xquat.copy()

    def _get_joint_names(self):
        '''
        Return a list of joint names according to the index ID of the joint angles
        '''
        return [self.sim.model.joint(jnt_id).name for jnt_id in range(1, self.sim.model.njnt)]

    def _get_joint_qpos(self):
        '''
        Return a list of joint qpos from the predefined list of joint names
        '''
        return np.array([self.sim.data.joint(jnt).qpos[0].copy() for jnt in self.myo_joints])
    
    def _get_joint_qvel(self):
        '''
        Return a list of joint qvel from the predefined list of joint names
        '''
        return np.array([self.sim.data.joint(jnt).qvel[0].copy() for jnt in self.myo_joints])

    def _get_actuator_names(self):
        '''
        Return a list of actuator names according to the index ID of the actuators
        '''
        return [self.sim.model.actuator(act_id).name for act_id in range(1, self.sim.model.na)]

    def get_limitfrc(self, joint_name):
        """
        Get the joint limit force for a given joint.
        """
        non_joint_limit_efc_idxs = np.where(self.sim.data.efc_type != self.sim.lib.mjtConstraint.mjCNSTR_LIMIT_JOINT)[0]
        only_jnt_lim_efc_force = self.sim.data.efc_force.copy()
        only_jnt_lim_efc_force[non_joint_limit_efc_idxs] = 0.0
        joint_force = np.zeros((self.sim.model.nv,))
        self.sim.lib.mj_mulJacTVec(self.sim.model._model, self.sim.data._data, joint_force, only_jnt_lim_efc_force)

        return joint_force[self.sim.model.joint(joint_name).dofadr]