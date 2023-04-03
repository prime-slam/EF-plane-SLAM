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


def extract_planes_from_pcd_colors(point_cloud):
    points = np.asarray(point_cloud.points)
    colors = np.asarray(point_cloud.colors)

    colors_unique = np.unique(colors, axis=0)
    unique_colors_without_black = list(
        filter(lambda x: (x != [0, 0, 0]).all(axis=0), colors_unique)
    )

    color_to_points = {}

    for color in unique_colors_without_black:
        indices = np.where((colors == color).all(axis=1))[0]
        if len(indices) > 1000:
            color_to_points[tuple(color)] = points[indices]

    return color_to_points
