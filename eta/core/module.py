'''
Core module infrastructure.

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

from eta.core import log
from eta.core.config import Config
from eta.core.pipeline import PipelineConfig


def setup(module_config, pipeline_config_path=None):
    '''Perform module setup.

    If a pipeline config is provided, it overrides any applicable values in
    the module config.

    Args:
        module_config: a Config instance derived from BaseModuleConfig
        pipeline_config_path: an optional path to a PipelineConfig
    '''
    # Set/override module config settings
    if pipeline_config_path:
        pipeline_config = PipelineConfig.from_json(pipeline_config_path)
        module_config.logging_config = pipeline_config.logging_config

    # Setup logging
    log.custom_setup(module_config.logging_config)


class BaseModuleConfig(Config):
    '''Base module configuration settings.'''

    def __init__(self, d):
        self.logging_config = self.parse_object(
            d, "logging_config", log.LoggingConfig,
            default=log.LoggingConfig.default())