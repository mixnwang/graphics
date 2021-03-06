#Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""tensorflow_graphics module."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# pylint: disable=g-statement-before-imports,g-import-not-at-top
try:
  import tensorflow as tf
except ImportError:
  print("Warning: TensorFlow is not installed when you install TensorFlow"
        " Graphics. To use TensorFlow Graphics, please install TensorFlow, by"
        " following instructions at https://tensorflow.org/install or by using"
        " pip install tensorflow_graphics[tf] or"
        " pip install tensorflow_graphics[tf-gpu].")
# pylint: enable=g-statement-before-imports,g-import-not-at-top

from tensorflow_graphics import geometry
from tensorflow_graphics import image
from tensorflow_graphics import math
from tensorflow_graphics import nn
from tensorflow_graphics import notebooks
from tensorflow_graphics import rendering
from tensorflow_graphics import util
from tensorflow_graphics import version

__version__ = version.__version__

# API contains submodules of tensorflow_graphics.
__all__ = util.export_api.get_modules()
# Remove modules notebooks, util and version from API.
__all__.remove("notebooks")
__all__.remove("util")
__all__.remove("version")
