"""Hive Camera Module."""

# pylint: skip-file


class HiveCamera:
    """Hive camera.

    Returns:
        object: Hive camera
    """

    cameraType = "Camera"

    def getCameraTemperature(self, device: dict):
        """Get the camera state.

        Returns:
            boolean: True/False if camera is on.
        """
        state = None

        try:
            data = self.session.data.devices[device["hiveID"]]
            state = data["props"]["temperature"]
        except KeyError as e:
            self.session.log.error(e)

        return state

    def getCameraState(self, device: dict):
        """Get the camera state.

        Returns:
            boolean: True/False if camera is on.
        """
        state = None

        try:
            data = self.session.data.devices[device["hiveID"]]
            state = True if data["state"]["mode"] == "ARMED" else False
        except KeyError as e:
            self.session.log.error(e)

        return state

    def getCameraImageURL(self, device: dict):
        """Get the camera image url.

        Returns:
            str: image url.
        """
        state = None

        try:
            state = self.session.data.camera[device["hiveID"]]["cameraImage"][
                "thumbnailUrls"
            ][0]
        except KeyError as e:
            self.session.log.error(e)

        return state

    def getCameraRecodringURL(self, device: dict):
        """Get the camera recording url.

        Returns:
            str: image url.
        """
        state = None

        try:
            state = self.session.data.camera[device["hiveID"]]["cameraRecording"]
        except KeyError as e:
            self.session.log.error(e)

        return state

    def setCameraOn(self, device: dict, mode: str):
        """Set the camera state to on.

        Args:
            device (dict): Camera device.

        Returns:
            boolean: True/False if successful.
        """
        final = False

        if (
            device["hiveID"] in self.session.data.devices
            and device["deviceData"]["online"]
        ):
            self.session.hiveRefreshTokens()
            resp = self.session.api.setState(mode=mode)
            if resp["original"] == 200:
                final = True
                self.session.getCamera()

        return final

    def setCameraOff(self, device: dict, mode: str):
        """Set the camera state to on.

        Args:
            device (dict): Camera device.

        Returns:
            boolean: True/False if successful.
        """
        final = False

        if (
            device["hiveID"] in self.session.data.devices
            and device["deviceData"]["online"]
        ):
            self.session.hiveRefreshTokens()
            resp = self.session.api.setState(mode=mode)
            if resp["original"] == 200:
                final = True
                self.session.getCamera()

        return final


class Camera(HiveCamera):
    """Home assistant camera.

    Args:
        HiveCamera (object): Class object.
    """

    def __init__(self, session: object = None):
        """Initialise camera.

        Args:
            session (object, optional): Used to interact with the hive account. Defaults to None.
        """
        self.session = session

    def getCamera(self, device: dict):
        """Get camera data.

        Args:
            device (dict): Device to update.

        Returns:
            dict: Updated device.
        """
        device["deviceData"].update(
            {"online": self.session.attr.onlineOffline(device["device_id"])}
        )
        dev_data = {}

        if device["deviceData"]["online"]:
            self.session.helper.deviceRecovered(device["device_id"])
            data = self.session.data.devices[device["device_id"]]
            dev_data = {
                "hiveID": device["hiveID"],
                "hiveName": device["hiveName"],
                "hiveType": device["hiveType"],
                "haName": device["haName"],
                "haType": device["haType"],
                "device_id": device["device_id"],
                "device_name": device["device_name"],
                "status": {
                    "temperature": self.getCameraTemperature(device),
                    "state": self.getCameraState(device),
                    "imageURL": self.getCameraImageURL(device),
                    "recordingURL": self.getCameraRecodringURL(device),
                },
                "deviceData": data.get("props", None),
                "parentDevice": data.get("parent", None),
                "custom": device.get("custom", None),
                "attributes": self.session.attr.stateAttributes(
                    device["device_id"], device["hiveType"]
                ),
            }

            self.session.devices.update({device["hiveID"]: dev_data})
            return self.session.devices[device["hiveID"]]
        else:
            self.session.log.errorCheck(
                device["device_id"], "ERROR", device["deviceData"]["online"]
            )
            return device
