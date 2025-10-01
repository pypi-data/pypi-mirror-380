import os
import asyncio
from typing import Optional, Any

from ironflock.CrossbarConnection import CrossbarConnection, Stage, getSerialNumber


class IronFlock:
    """Convenience class for easy-to-use message publishing in the IronFlock platform.

    Example:

        async def main():
            while True:
                publication = await ironflock.publish("test.publish.pw", 1, "two", 3, foo="bar")
                print(publication)
                await asyncio.sleep(3)


        if __name__ == "__main__":
            ironflock = IronFlock(mainFunc=main)
            await ironflock.run()
    """

    def __init__(self, serial_number: str = None, mainFunc=None) -> None:
        """Creates IronFlock Instance

        Args:
            serial_number (str, optional): serial_number of device.
            Defaults to None, in which case the environment variable DEVICE_SERIAL_NUMBER is used.
            mainFunc (callable, optional): Main function to run after connection is established.
        """
        self._serial_number = getSerialNumber(serial_number)
        self._device_name = os.environ.get("DEVICE_NAME")
        self._device_key = os.environ.get("DEVICE_KEY")
        self._connection = CrossbarConnection()
        self.mainFunc = mainFunc
        self._main_task = None
        self._is_configured = False

    @property
    def connection(self) -> CrossbarConnection:
        """The CrossbarConnection instance

        Returns:
            CrossbarConnection
        """
        return self._connection

    @property
    def is_connected(self) -> bool:
        """Check if the connection is established

        Returns:
            bool: True if connected, False otherwise
        """
        return self._connection.is_open

    async def _configure_connection(self):
        """Configure the CrossbarConnection with environment variables"""
        if self._is_configured:
            return
            
        swarm_key = int(os.environ.get("SWARM_KEY", 0))
        app_key = int(os.environ.get("APP_KEY", 0))
        env_value = os.environ.get("ENV", "DEV").upper()
        
        # Map environment string to Stage enum
        stage_map = {
            "DEV": Stage.DEVELOPMENT,
            "PROD": Stage.PRODUCTION
        }
        stage = stage_map.get(env_value, Stage.DEVELOPMENT)
        
        await self._connection.configure(
            swarm_key=swarm_key,
            app_key=app_key,
            stage=stage,
            serial_number=self._serial_number
        )
        self._is_configured = True

    async def publish(self, topic: str, *args, **kwargs) -> Optional[Any]:
        """Publishes to the IronFlock Platform Message Router

        Args:
            topic (str): The URI of the topic to publish to, e.g. "com.myapp.mytopic1"
            *args: Positional arguments to publish
            **kwargs: Keyword arguments to publish

        Returns:
            Optional[Any]: Object representing a publication
            (feedback from publishing an event when doing an acknowledged publish)
        """
        if not self.is_connected:
            print("cannot publish, not connected")
            return None

        # Add device metadata to kwargs
        device_metadata = {
            "DEVICE_SERIAL_NUMBER": self._serial_number,
            "DEVICE_KEY": self._device_key,
            "DEVICE_NAME": self._device_name,
        }
        
        # Merge device metadata with user kwargs
        combined_kwargs = {**device_metadata, **kwargs}
        
        # Use acknowledged publish
        options = {"acknowledge": True}
        
        try:
            pub = await self._connection.publish(
                topic, 
                args=list(args), 
                kwargs=combined_kwargs,
                options=options
            )
            return pub
        except Exception as e:
            print(f"Publish failed: {e}")
            return None
            
    async def set_device_location(self, long: float, lat: float):
        """Update the location of the device registered in the platform
        
        This will update the device's location in the master data of the platform.
        The maps in the device or group overviews will reflect the new device location in realtime.
        The location history will not be stored in the platform. 
        If you need location history, then create a dedicated table for it.
        
        Args:
            long (float): Longitude coordinate
            lat (float): Latitude coordinate
        """
        if not self.is_connected:
            print("cannot set location, not connected")
            return None

        payload = {
            "long": long,
            "lat": lat
        }
        
        extra = {
            "DEVICE_SERIAL_NUMBER": self._serial_number,
            "DEVICE_KEY": self._device_key,
            "DEVICE_NAME": self._device_name
        }
        
        try:
            res = await self._connection.call(
                'ironflock.location_service.update', 
                args=[payload], 
                kwargs=extra
            )
            return res
        except Exception as e:
            print(f"Set location failed: {e}")
            return None
    
    async def register_function(self, topic: str, func):
        """Registers a function to be called when a message is received on the given topic.
        
        Args:
            topic (str): The URI of the topic to register the function for, e.g. "example.mytopic1".
            func (callable): The function to call when a message is received on the topic.
        """
        if not self.is_connected:
            print("cannot register function, not connected")
            return None
            
        swarm_key = os.environ.get("SWARM_KEY")
        app_key = os.environ.get("APP_KEY")
        env_value = os.environ.get("ENV")
        
        full_topic = f"{swarm_key}.{self._device_key}.{app_key}.{env_value}.{topic}"
        
        try:
            # Note: CrossbarConnection doesn't support force_reregister option directly
            # but it handles resubscription automatically on reconnect
            registration = await self._connection.register(full_topic, func)
            return registration
        except Exception as e:
            print(f"Register function failed: {e}")
            return None

    async def call(self, device_key: str, topic: str, args: list = None, kwargs: dict = None):
        """Calls a remote procedure on the IronFlock platform.

        Args:
            device_key (str): The key of the device to call the procedure on.
            topic (str): The URI of the topic to call, e.g. "com.myprocedure".
            args (list): The arguments to pass to the procedure.
            kwargs (dict): The keyword arguments to pass to the procedure.

        Returns:
            The result of the remote procedure call.
        """
        if not self.is_connected:
            print("cannot call, not connected")
            return None
            
        swarm_key = os.environ.get("SWARM_KEY")
        app_key = os.environ.get("APP_KEY")
        env_value = os.environ.get("ENV")
        
        full_topic = f"{swarm_key}.{device_key}.{app_key}.{env_value}.{topic}"
        
        try:
            result = await self._connection.call(
                full_topic, 
                args=args or [], 
                kwargs=kwargs or {}
            )
            return result
        except Exception as e:
            print(f"Call failed: {e}")
            return None

    async def publish_to_table(
        self, tablename: str, *args, **kwargs
    ) -> Optional[Any]:
        """Publishes Data to a Table in the IronFlock Platform. This is a convenience function.
        
        You can achieve the same results by simply publishing a payload to the topic
        [SWARM_KEY].[APP_KEY].[your_table_name]
        
        The SWARM_KEY and APP_KEY are provided as environment variables to the device container.
        The also provided ENV variable holds either PROD or DEV to decide which topic to use, above.
        This function automatically detects the environment and publishes to the correct table.
        
        Args:
            tablename (str): The table name of the table to publish to, e.g. "sensordata"
            *args: Positional arguments to publish
            **kwargs: Keyword arguments to publish

        Returns:
            Optional[Any]: Object representing a publication
            (feedback from publishing an event when doing an acknowledged publish)
        """

        if not tablename:
            raise Exception("Tablename must not be None or empty string!")

        swarm_key = os.environ.get("SWARM_KEY")
        app_key = os.environ.get("APP_KEY")

        if swarm_key is None:
            raise Exception("Environment variable SWARM_KEY not set!")

        if app_key is None:
            raise Exception("Environment variable APP_KEY not set!")

        topic = f"{swarm_key}.{app_key}.{tablename}"

        pub = await self.publish(topic, *args, **kwargs)
        return pub

    async def start(self):
        """Start the connection and run the main function if provided"""
        await self._configure_connection()
        await self._connection.start()
        
        if self.mainFunc:
            self._main_task = asyncio.create_task(self.mainFunc())
        
    async def stop(self):
        """Stop the connection and cancel the main task if running"""
        if self._main_task and not self._main_task.done():
            self._main_task.cancel()
            try:
                await self._main_task
            except asyncio.CancelledError:
                pass
            self._main_task = None
            
        await self._connection.stop()

    async def run(self):
        """Start the connection and keep it running"""
        await self.start()
        
        try:
            # Keep running until manually stopped
            if self._main_task:
                await self._main_task
            else:
                # If no main function, just wait indefinitely
                while self.is_connected:
                    await asyncio.sleep(1)
        except KeyboardInterrupt:
            print("Shutting down...")
        finally:
            await self.stop()

    def run_sync(self):
        """Synchronous wrapper to run the IronFlock instance (for backward compatibility)"""
        asyncio.run(self.run())
