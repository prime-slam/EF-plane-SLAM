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
import open3d as o3d


class IclTumCompatLoader:
    def __init__(self, camera):
        self.camera = camera
        self.color_to_plane_id = {}
        self.id_counter = 0

    def load_point_cloud(self, depth_path, label_path):
        color_raw = o3d.io.read_image(str(label_path))
        depth_raw = o3d.io.read_image(str(depth_path))
        rgbd_image = o3d.geometry.RGBDImage.create_from_color_and_depth(
            color_raw,
            depth_raw,
            convert_rgb_to_intensity=False,
            depth_scale=self.camera.scale,
            depth_trunc=100
        )

        intrinsic = o3d.camera.PinholeCameraIntrinsic()
        intrinsic.width, intrinsic.height = self.camera.width, self.camera.height
        intrinsic.intrinsic_matrix = [
            [float(self.camera.fx), 0, float(self.camera.cx)],
            [0, float(self.camera.fy), float(self.camera.cy)],
            [0, 0, 1],
        ]

        point_cloud = o3d.geometry.PointCloud()
        point_cloud = point_cloud.create_from_rgbd_image(rgbd_image, intrinsic).transform(np.asarray([
            [1, 0, 0, 0], 
            [0, 1, 0, 0], 
            [0, 0, 1, 0], 
            [0, 0, 0, 1]]))
        
        return point_cloud
