from decimal import Decimal

from .service_deploy import Deploy
from .service_credential_spec import CredentialSpec
from .compose_element import ComposeElement


class Service(ComposeElement):
    elements = {
        "image": (str,
                  "https://github.com/compose-spec/compose-spec/blob/master/spec.md#image"),
        "container_name": (str,
                           "https://github.com/compose-spec/compose-spec/blob/master/spec.md#container_name"),
        "cpu_count": (Decimal,
                      ""),
        "command": (str,
                    ""),
        "deploy": (Deploy.from_parsed_yaml,
                   ""),
        "ports": (str,
                  ""),
        "cpus": (Decimal,
                 ""),
        "credential_spec": (CredentialSpec.from_parsed_yaml,
                            ""),
        "blkio_config": (None,
                         "https://github.com/compose-spec/compose-spec/blob/master/spec.md#blkio_config"),
        "cpu_percent": (None,
                        "https://github.com/compose-spec/compose-spec/blob/master/spec.md#cpu_percent"),
        "cpu_shares": (None,
                       "https://github.com/compose-spec/compose-spec/blob/master/spec.md#cpu_shares"),
        "cpu_period": (None,
                       "https://github.com/compose-spec/compose-spec/blob/master/spec.md#cpu_period"),
        "cpu_quota": (None,
                      "https://github.com/compose-spec/compose-spec/blob/master/spec.md#cpu_quota"),
        "cpu_rt_runtime": (None,
                           "https://github.com/compose-spec/compose-spec/blob/master/spec.md#cpu_rt_runtime"),
        "cpu_rt_period": (None,
                          "https://github.com/compose-spec/compose-spec/blob/master/spec.md#cpu_rt_period"),
        "cpuset": (None,
                   "https://github.com/compose-spec/compose-spec/blob/master/spec.md#cpuset"),
        "build": (None,
                  "https://github.com/compose-spec/compose-spec/blob/master/build.md"),
        "cap_add": (None,
                    "https://github.com/compose-spec/compose-spec/blob/master/spec.md#cap_add"),
        "cap_drop": (None,
                     "https://github.com/compose-spec/compose-spec/blob/master/spec.md#cap_add"),
        "cgroup_parent": (None,
                          "https://github.com/compose-spec/compose-spec/blob/master/spec.md#cgroup_parent"),
        "configs": (None,
                    "https://github.com/compose-spec/compose-spec/blob/master/spec.md#configs"),
    }
