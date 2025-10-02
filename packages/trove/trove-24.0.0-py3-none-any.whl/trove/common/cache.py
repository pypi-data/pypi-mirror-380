# Copyright 2021 Catalyst Cloud
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

"""The code related to integration between oslo.cache module and trove."""

from oslo_cache import core
from oslo_config import cfg


PORTS_CACHE_GROUP = cfg.OptGroup('instance_ports_cache')
PORTS_CACHE_OPTS = [
    cfg.IntOpt('expiration_time', default=86400,
               help='TTL, in seconds, for any cached item in the '
                    'dogpile.cache region used for caching of the '
                    'instance ports.'),
    cfg.BoolOpt("caching", default=True,
                help='Toggle to enable/disable caching when getting trove '
                     'instance ports. Please note that the global toggle '
                     'for oslo.cache(enabled=True in [cache] group) '
                     'must be enabled to use this feature.')
]


def register_cache_configurations(conf):
    """Register all configurations required for oslo.cache.

    The procedure registers all configurations required for oslo.cache.
    It should be called before configuring of cache region
    """
    core.configure(conf)

    conf.register_group(PORTS_CACHE_GROUP)
    conf.register_opts(PORTS_CACHE_OPTS, group=PORTS_CACHE_GROUP)

    return conf


# variable that stores an initialized cache region for trove
_REGION = None


def get_cache_region():
    global _REGION
    if not _REGION:
        _REGION = core.configure_cache_region(
            conf=register_cache_configurations(cfg.CONF),
            region=core.create_region())
    return _REGION
