# Copyright (c) 2015 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import sys

import config_util  # pylint: disable=import-error


# This class doesn't need an __init__ method, so we disable the warning
# pylint: disable=no-init
class Breakpad(config_util.Config):
    @staticmethod
    def fetch_spec(props):
        url = 'https://chromium.googlesource.com/breakpad/breakpad.git'
        solution = {
            'name': 'src',
            'url': url,
            'managed': False,
            'custom_deps': {},
        }
        spec = {
            'solutions': [solution],
        }
        if props.get('target_os'):
            spec['target_os'] = props['target_os'].split(',')
        if props.get('target_os_only'):
            spec['target_os_only'] = props['target_os_only']
        return {
            'type': 'gclient_git',
            'gclient_git_spec': spec,
        }

    @staticmethod
    def expected_root(_props):
        return 'src'


def main(argv=None):
    return Breakpad().handle_args(argv)


if __name__ == '__main__':
    sys.exit(main(sys.argv))
