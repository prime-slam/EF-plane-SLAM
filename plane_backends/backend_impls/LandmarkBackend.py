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

import numpy as np

from plane_backends.BaseBackend import BaseBackend


class LandmarkBackend(BaseBackend):
    def _add_node_to_graph(self):
        return self.graph.add_node_plane_4d(np.array([1, 0, 0, 0]))

    def _register_observation(self, observation, pose_id, plane_id, graph_plane_id):
        w_z = np.identity(4)
        plane_equation = self.__get_plane_equation(observation[plane_id])
        self.graph.add_factor_1pose_1plane_4d(
            plane_equation, pose_id, graph_plane_id, w_z
        )

    @staticmethod
    def __get_plane_equation(points):
        c = np.mean(points, axis=0)
        A = np.array(points) - c
        eigvals, eigvects = np.linalg.eig(A.T @ A)
        min_index = np.argmin(eigvals)
        n = eigvects[:, min_index]

        d = -np.dot(n, c)
        normal = int(np.sign(d)) * n
        d *= np.sign(d)
        return np.asarray([normal[0], normal[1], normal[2], d])
