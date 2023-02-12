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

from plane_backends.BaseBackend import BaseBackend


class PiFBackend(BaseBackend):
    def _add_node_to_graph(self):
        return self.graph.add_node_plane_4d(np.array([1, 1, 1, 1]))

    def _register_observation(self, observation, pose_id, plane_id, graph_plane_id):
        S = mrob.registration.estimate_matrix_S(observation[plane_id])
        self.graph.add_pi_factor_plane_4d(
            S, pose_id, graph_plane_id
        )
