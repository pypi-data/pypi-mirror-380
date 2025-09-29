# Default Python Libraries
import logging
from concurrent.futures import ThreadPoolExecutor

from .client_service import AristaFlowClientService
from .configuration import Configuration
from .rest_helper import RestPackageRegistry
from .service_provider import ServiceProvider


class AristaFlowClientPlatform(object):
    """Entry point to the AristaFlow Python Client framework."""

    # thread pool for async requests
    __thread_pool: ThreadPoolExecutor = None

    def __init__(self, configuration: Configuration):
        self.configuration = configuration
        self.__client_services: [str, AristaFlowClientService] = {}
        self.__rest_package_registry = RestPackageRegistry(configuration)
        # we replace each pool used by each service by a central thread pool executor
        # the api clients will call join and close during shutdown, the thread pool
        # executor doesn't have these methods, and its shutdown is done within this class
        # => add these methods to the TPE doing nothing
        self.__thread_pool = ThreadPoolExecutor()
        def noop():
            pass
        self.__thread_pool.close = noop
        self.__thread_pool.join = noop

    def get_client_service(self, user_session: str = "python_default_session"):
        """
        :return: AristaFlowClientService The client service for the given user session
        """
        if user_session in self.__client_services:
            return self.__client_services[user_session]
        cs = AristaFlowClientService(
            self.configuration,
            user_session,
            ServiceProvider(
                self.__rest_package_registry, self.__thread_pool
            ),
        )
        self.__client_services[user_session] = cs
        return cs

    def disconnect(self):
        try:
            for user_session in self.__client_services:
                self.__client_services[user_session].disconnect()
            # shutdown thread pool
            self.__thread_pool.shutdown(wait=False, cancel_futures=True)
        except BaseException as ex:
            logging.warning('Exception on disconnect', ex)
