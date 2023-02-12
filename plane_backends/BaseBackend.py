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

import abc
import datetime
import mrob
import numpy as np


class BaseBackend(abc.ABC):
    def __init__(self, iterations_count):
        self.graph = mrob.FGraph()
        self.iterations_count = iterations_count
    
    def solve(self, observations, Ts_init=None):
        if Ts_init is None:
            Ts_init = [np.eye(4) for _ in observations]
            
        self._init_poses(Ts_init)
        self.__add_observations(observations)
        timestamp_before_optimization = datetime.datetime.now()
        used_iterations_count = self.__optimize()
        timestamp_after_optimization = datetime.datetime.now()
        return (
            self.__get_trajectory(),
            used_iterations_count,
            (timestamp_after_optimization - timestamp_before_optimization).microseconds
        )

    def _init_poses(self, Ts_init):
        # Add nodes for poses
        for i, Ts in enumerate(Ts_init):
            node_mode = mrob.NODE_ANCHOR if i == 0 else mrob.NODE_STANDARD
            self.graph.add_node_pose_3d(mrob.geometry.SE3(Ts), node_mode)
            
    def __optimize(self):
        return self.graph.solve(mrob.LM_ELLIPS, self.iterations_count)
        
    def __get_trajectory(self):
        return self.graph.get_estimated_state()

    def __add_observations(self, observations):
        label_id_to_graph_id = {}
        for pose_id, observation in enumerate(observations):
            for plane_id in observation:
                if plane_id in label_id_to_graph_id:
                    # This landmark already exists in the graph
                    graph_plane_id = label_id_to_graph_id[plane_id]
                else:
                    # This landmarks doesn't exist in the graph
                    graph_plane_id = self._add_node_to_graph()
                    label_id_to_graph_id[plane_id] = graph_plane_id

                self._register_observation(observation, pose_id, plane_id, graph_plane_id)

    @abc.abstractmethod
    def _add_node_to_graph(self):
        pass

    @abc.abstractmethod
    def _register_observation(self, observation, pose_id, plane_id, graph_plane_id):
        pass
