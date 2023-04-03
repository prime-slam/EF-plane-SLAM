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

from typing import List

import numpy as np

from scripts.enough_planes.Pcd import Pcd
from scripts.enough_planes.Plane import Plane


class EnoughPlanesDetector:
    @staticmethod
    def has_enough_planes(pcd: Pcd) -> bool:
        return abs(EnoughPlanesDetector.__check_planes(pcd.planes)) > 0.1

    @staticmethod
    def __check_planes(planes: List[Plane]):
        matrix = []
        for plane in planes:
            matrix.append(plane.equation[:-1])
        matrix = np.asarray(matrix)
        covarience = matrix.T @ matrix
        eigvals, eigvects = np.linalg.eig(covarience)
        det = np.linalg.det(eigvects * eigvals)
        print("Det was {}".format(det))
        return det
