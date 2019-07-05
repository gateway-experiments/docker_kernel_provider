"""Provides support for launching and managing kernels within Docker or Docker Swarm clusters."""

from remote_kernel_provider import RemoteKernelProviderBase


class DockerKernelProvider(RemoteKernelProviderBase):
    id = 'docker_swarm'  # 'docker' as id already used here: https://github.com/takluyver/jupyter_docker_kernels
    kernel_file = 'docker_kernel.json'
    lifecycle_manager_classes = ['docker_kernel_provider.docker_swarm.DockerSwarmKernelLifecycleManager',
                                 'docker_kernel_provider.docker_swarm.DockerKernelLifecycleManager']
