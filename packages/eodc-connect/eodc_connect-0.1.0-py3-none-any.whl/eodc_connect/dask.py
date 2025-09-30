import logging
from typing import Optional

from dask_gateway import Gateway, GatewayCluster
from eodc_connect import auth, settings
from distributed.utils import LoopRunner

logger = logging.getLogger(__name__)


class EODCDaskGateway(Gateway):
    def __init__(self, username: str = None) -> None:
        self.authenticator = auth.DaskOIDC(username=username)
        super().__init__(
            address=settings.DASK_URL,
            proxy_address=settings.DASK_URL_TCP,
            auth=self.authenticator,
        )

    @classmethod
    def from_token(cls, token: str, auth_extra: str = None):
        instance = cls.__new__(cls)
        instance.auth = auth.DaskOIDC.from_token(token, auth_extra)
        instance.address = settings.DASK_URL
        instance.proxy_address = settings.DASK_URL_TCP
        instance._public_address = instance.address
        instance._asynchronous = False
        instance._loop_runner = LoopRunner(
            loop=None, asynchronous=instance.asynchronous
        )
        instance._loop_runner.start()
        return instance

    def __new__(cls, *args, **kwargs):
        """There should only ever be one Gateway object instantiated -> singleton."""
        if not hasattr(cls, "instance"):
            cls.instance = super().__new__(cls)
        return cls.instance


class EODCCluster(GatewayCluster):
    def __init__(self, image: Optional[str] = None):
        self.gateway = EODCDaskGateway()

        cluster_options = self.gateway.cluster_options(use_local_defaults=False)
        if image is not None:
            cluster_options.image = image
        logger.info(f"Provisioning Dask cluster from {self.gateway.address}")

        super().__init__(
            address=self.gateway.address,
            cluster_options=cluster_options,
            shutdown_on_close=True,
        )
        logger.info(f"Initialised Dask Cluster at {self.scheduler_address}")
