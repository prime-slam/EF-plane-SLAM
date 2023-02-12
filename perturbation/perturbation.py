# Copyright (c) 2022, Dmitrii Iarosh, Anastasiia Kornilova
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


class Perturbation:
    def __init__(self, rotation_shift, translation_shift):
        self.rotation_shift = rotation_shift
        self.translation_shift = translation_shift

    def __str__(self):
        return f"{self.rotation_shift}_{self.translation_shift}"


def generate_uniform_vector(r):
    theta = np.random.uniform(0, 2 * np.pi)
    phi = np.random.uniform(0, np.pi)
    x = r * np.sin(phi) * np.cos(theta)
    y = r * np.sin(phi) * np.sin(theta)
    z = r * np.cos(phi)
    return np.array([x, y, z])


def generate_random_pose_shift(rotation_shift, translation_shift):
    shift_se3 = np.hstack([generate_uniform_vector(rotation_shift), generate_uniform_vector(translation_shift)])
    return mrob.geometry.SE3(shift_se3).T()