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

from plane_backends.backend_impls.BaregBackend import BaregBackend
from plane_backends.backend_impls.EFBackend import EFBackend
from plane_backends.backend_impls.EFCenteredBackend import EFCenteredBackend
from plane_backends.backend_impls.LandmarkBackend import LandmarkBackend
from plane_backends.backend_impls.PiFBackend import PiFBackend

solvers = {
    'ef': EFBackend,
    'ef-centered': EFCenteredBackend,
    'bareg': BaregBackend,
    'pi-factor': PiFBackend,
    'landmark': LandmarkBackend,
}


def create_solver_by_name(solver_name, iterations_count):
    return solvers[solver_name](iterations_count)
