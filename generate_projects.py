#!/usr/bin/env python
import os
import sys
import fnmatch
import shutil

script_dir = os.path.abspath(os.path.dirname(__file__))

if __name__ == '__main__':
    sys.path.append(os.path.join(script_dir, 'vendor', 'gyp', 'pylib'))
    import gyp

    os.putenv("PYTHONDONTWRITEBYTECODE", "1")
    gyp_file = os.path.join(script_dir, "SinchService.gyp")

    gyp_args = []    
    gyp_args += ['--depth', script_dir]
    gyp_args += ['-D', "OS=ios"]
    gyp_args += ['-f', "xcode"]
    gyp_args += [gyp_file]

    status = gyp.main(gyp_args)
    sys.stdout.flush()
    sys.exit(status)
