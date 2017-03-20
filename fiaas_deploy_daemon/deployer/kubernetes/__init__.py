#!/usr/bin/env python
# -*- coding: utf-8
from __future__ import absolute_import

import pinject

from .adapter import K8s
from .service import ServiceDeployer
from .deployment import DeploymentDeployer
from .ingress import IngressDeployer
from .autoscaler import AutoscalerDeployer


class K8sAdapterBindings(pinject.BindingSpec):
    def configure(self, bind):
        bind("adapter", to_class=K8s)
        bind("service_deployer", to_class=ServiceDeployer)
        bind("deployment_deployer", to_class=DeploymentDeployer)
        bind("ingress_deployer", to_class=IngressDeployer)
        bind("autoscaler", to_class=AutoscalerDeployer)
