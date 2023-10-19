import logging
import aiohttp

from vehicle import Vehicle
from velocitas_sdk.vehicle_app import VehicleApp, subscribe_topic


class DriverAnalyticsApp(VehicleApp):
    """
    The DriverAnalyticsApp subscribes to VehicleDataBroker for updates
    in gyro and accelerometer data.This data is sent to a remote machine
    learning as HTTP request and response is published to MQTT broker
    """

    def __init__(self, vehicle_client: Vehicle):
        super().__init__()
        self.Vehicle = vehicle_client
