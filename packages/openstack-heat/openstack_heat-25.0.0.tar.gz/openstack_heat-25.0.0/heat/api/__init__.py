#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
import warnings

from oslo_config import cfg
import paste.urlmap

CONF = cfg.CONF


def root_app_factory(loader, global_conf, **local_conf):
    warnings.warn('root_app_facotry is deprecated. Use the built-in '
                  'urlmap application from the Paste library instead.',
                  DeprecationWarning)
    return paste.urlmap.urlmap_factory(loader, global_conf, **local_conf)


def pipeline_factory(loader, global_conf, **local_conf):
    """A paste pipeline replica that keys off of deployment flavor."""
    pipeline = local_conf[CONF.paste_deploy.flavor or 'default']
    pipeline = pipeline.split()
    filters = [loader.get_filter(n) for n in pipeline[:-1]]
    app = loader.get_app(pipeline[-1])
    filters.reverse()
    for filter in filters:
        app = filter(app)
    return app
