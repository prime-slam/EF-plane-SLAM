# Copyright (c) 2022, Gonzalo Ferrer, Dmitrii Iarosh, Anastasiia Kornilova
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import mrob
import numpy as np


def rpe(traj_gt, traj_est):
    dT_traj_gt = [np.linalg.inv(traj_gt[i]) @ traj_gt[i + 1] for i in range(len(traj_gt) - 1)]
    dT_traj_est = [np.linalg.inv(traj_est[i]) @ traj_est[i + 1] for i in range(len(traj_est) - 1)]
    dTs = [np.linalg.inv(dT_traj_gt[i]) @ dT_traj_est[i] for i in range(len(dT_traj_gt))]

    transl_err = []
    rot_err = []
    for dT in dTs:
        transl_err.append(mrob.geometry.SE3(dT).distance_trans() ** 2)
        rot_err.append(mrob.geometry.SE3(dT).distance_rotation() ** 2)
    return np.mean(transl_err) ** 0.5, np.mean(rot_err) ** 0.5