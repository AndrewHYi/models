# Copyright 2018 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import subprocess
import sys
import unittest


PYTHON_CMD = "python2" if sys.version_info[0] == 2 else "python3"
ROOT = os.getcwd()


def run(args):
  p = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE)
  output, err = p.communicate()
  returncode = p.returncode
  if returncode != 0:
    raise OSError("Run failed:\nStdout:\n{}\n\nStderr:\n{}".format(
        output.decode("utf-8"), err.decode("utf-8")
    ))


class BaseTest(unittest.TestCase):
  def test_cifar(self):
    run([PYTHON_CMD, os.path.join(ROOT, "cifar10_main.py"), "--model_dir",
         "/tmp/cifar10_testing", "--train_epochs", "1", "--use_synthetic_data"])


if __name__ == "__main__":
  unittest.main()
