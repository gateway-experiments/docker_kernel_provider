# Docker Kernel Provider

__NOTE: This repository is experimental and undergoing frequent changes!__

The Docker Kernel Provider package provides support necessary for launching and managing Jupyter kernels within Docker or Docker Swarm clusters.  This is accomplished via two classes:

1. [`DockerKernelProvider`](https://github.com/gateway-experiments/docker_kernel_provider/blob/master/docker_kernel_provider/provider.py) is invoked by the application to locate and identify specific kernel specificiations (kernelspecs) that manage kernel lifecycles within Docker configurations.
2. Either of [`DockerSwarmKernelLifecycleManager`](https://github.com/gateway-experiments/docker_kernel_provider/blob/master/docker_kernel_provider/docker_swarm.py) or [`DockerKernelLifecycleManager`](https://github.com/gateway-experiments/docker_kernel_provider/blob/master/docker_kernel_provider/docker_swarm.py) depending on the content of the `docker_kernel.json` file.  One of these classes is instantiated by the [`RemoteKernelManager`](https://github.com/gateway-experiments/remote_kernel_provider/blob/master/remote_kernel_provider/manager.py) to peform the kernel lifecycle management.  This class performs post-launch discovery of the kernel container and handles its termination via the [docker-py](https://github.com/docker/docker-py) python API.

## Installation
`DockerKernelProvider` is a pip-installable package:
```bash
pip install docker_kernel_provider
```

## Docker Kernel Specifications
Criteria for discovery of the kernel specification via the `DockerKernelProvider` is that a `docker_kernel.json` file exist in a sub-directory of `kernels`.  
