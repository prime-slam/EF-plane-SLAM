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

import open3d as o3d


class CameraParameters:
    def __init__(self, width, height, cx, cy, fx, fy, scale):
        self.width = width
        self.height = height
        self.cx = cx
        self.cy = cy
        self.fx = fx
        self.fy = fy
        self.scale = scale

    def to_o3d_intrinsics(self):
        intrinsics = o3d.camera.PinholeCameraIntrinsic()
        intrinsics.width, intrinsics.height = self.width, self.height
        intrinsics.intrinsic_matrix = [
            [self.fx, 0, self.cx],
            [0, self.fy, self.cy],
            [0, 0, 1],
        ]

        return intrinsics
