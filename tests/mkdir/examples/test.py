#!/usr/bin/env python
import os
import mkdir

path = "/tmp/folder/folder2/folder3"
mkdir.mkdir(path)
assert os.path.exists(path) is True
