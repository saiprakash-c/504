#!/usr/bin/env python
'''
Generate clips from a video.

Copyright 2017, Voxel51, LLC
voxel51.com

Brian Moore, brian@voxel51.com
'''
# pragma pylint: disable=redefined-builtin
# pragma pylint: disable=unused-wildcard-import
# pragma pylint: disable=wildcard-import
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from builtins import *
# pragma pylint: enable=redefined-builtin
# pragma pylint: enable=unused-wildcard-import
# pragma pylint: enable=wildcard-import

import logging
import sys

from eta.core.config import Config, ConfigError
import eta.core.events as ev
import eta.core.module as mo
import eta.core.video as vd


logger = logging.getLogger(__name__)


def run(config_path):
    '''Run the clip_videos module.

    Args:
        config_path: path to a ClipConfig file
    '''
    clip_config = ClipConfig.from_json(config_path)
    mo.setup(clip_config)
    _clip_videos(clip_config)


def _clip_videos(clip_config):
    for data_config in clip_config.data:
        logger.info("Generating video clips for '%s'", data_config.input_path)
        with vd.VideoProcessor(
            data_config.input_path,
            frames=data_config.get_frames(),
            out_vidpath=data_config.output_path,
        ) as p:
            for img in p:
                p.write(img)


class ClipConfig(mo.BaseModuleConfig):
    '''Clip configuration settings.'''

    def __init__(self, d):
        super(ClipConfig, self).__init__(d)
        self.data = self.parse_object_array(d, "data", DataConfig)


class DataConfig(Config):
    '''Data configuration settings.'''

    def __init__(self, d):
        self.input_path = self.parse_string(d, "input_path")
        self.output_path = self.parse_string(d, "output_path")
        self.events_json_path = self.parse_string(
            d, "events_json_path", default=None)
        self.frames = self.parse_string(d, "frames", default=None)

    def get_frames(self):
        if self.events_json_path:
            return ev.EventSeries.from_json(self.events_json_path).to_str()
        elif self.frames:
            return self.frames
        else:
            raise ConfigError("Expected 'events_json_path' or 'frames'")


if __name__ == "__main__":
    run(sys.argv[1])
