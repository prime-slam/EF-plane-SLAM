# Copyright (c) 2024, Gonzalo Ferrer, Dmitrii Iarosh, Anastasiia Kornilova
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

from plane_backends.EFBackend import EFBackend


class EFAlternatingBackend(EFBackend):
    def _add_node_to_graph(self):
        return self.graph.add_eigen_factor_plane_alternating()

    def _optimize(self):
        return self.graph.solve(mrob.LM_ELLIPS, self.iterations_count)
