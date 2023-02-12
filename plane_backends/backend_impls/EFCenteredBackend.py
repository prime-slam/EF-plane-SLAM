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

from plane_backends.BaseBackend import BaseBackend


class EFCenteredBackend(BaseBackend):
    def _add_node_to_graph(self):
        return self.graph.add_eigen_factor_plane_center()

    def _register_observation(self, observation, pose_id, plane_id, graph_plane_id):
        self.graph.eigen_factor_plane_add_points_array(
            planeEigenId=graph_plane_id,
            nodePoseId=pose_id,
            pointsArray=observation[plane_id],
            W=1.0
        )
