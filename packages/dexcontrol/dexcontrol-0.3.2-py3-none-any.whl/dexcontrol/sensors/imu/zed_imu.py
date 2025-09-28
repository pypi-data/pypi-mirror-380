# Copyright (C) 2025 Dexmate Inc.
#
# This software is dual-licensed:
#
# 1. GNU Affero General Public License v3.0 (AGPL-3.0)
#    See LICENSE-AGPL for details
#
# 2. Commercial License
#    For commercial licensing terms, contact: contact@dexmate.ai

"""ZED IMU sensor implementation using Zenoh subscriber."""

import numpy as np

from dexcontrol.comm import create_imu_subscriber


class ZedIMUSensor:
    """ZED IMU sensor using Zenoh subscriber.

    This sensor provides IMU data from ZED cameras including acceleration, angular velocity,
    orientation quaternion, and magnetometer data using the IMUSubscriber for efficient data handling.
    The ZED IMU typically provides 9-axis data (accelerometer, gyroscope, magnetometer) with
    quaternion orientation.
    """

    def __init__(
        self,
        configs,
    ) -> None:
        """Initialize the ZED IMU sensor.

        Args:
            configs: Configuration object containing topic, name, and other settings.
        """
        self._name = configs.name


        self._subscriber = create_imu_subscriber(
            topic=configs.topic,
        )

    def shutdown(self) -> None:
        """Shutdown the ZED IMU sensor."""
        self._subscriber.shutdown()

    def is_active(self) -> bool:
        """Check if the ZED IMU sensor is actively receiving data.

        Returns:
            True if receiving data, False otherwise.
        """
        data = self._subscriber.get_latest()
        return data is not None

    def wait_for_active(self, timeout: float = 5.0) -> bool:
        """Wait for the ZED IMU sensor to start receiving data.

        Args:
            timeout: Maximum time to wait in seconds.

        Returns:
            True if sensor becomes active, False if timeout is reached.
        """
        msg = self._subscriber.wait_for_message(timeout)
        return msg is not None

    def get_obs(self, obs_keys: list[str] | None = None) -> dict[str, np.ndarray] | None:
        """Get observation data for the ZED IMU sensor.

        Args:
            obs_keys: List of observation keys to retrieve. If None, returns all available data.
                     Valid keys: ['ang_vel', 'acc', 'quat', 'mag', 'timestamp']

        Returns:
            Dictionary with observation data including all IMU measurements.
            Keys are mapped as follows:
            - 'ang_vel': Angular velocity from 'gyro'
            - 'acc': Linear acceleration from 'acc'
            - 'quat': Orientation quaternion from 'quat'
            - 'mag': Magnetometer from 'mag' (if available)
            - 'timestamp_ns': Timestamp from 'timestamp'
        """
        if obs_keys is None:
            obs_keys = ['ang_vel', 'acc', 'quat']

        data = self._subscriber.get_latest()
        if data is None:
            return None

        obs_out = {}

        # Add timestamp if available
        if 'timestamp' in data:
            obs_out['timestamp_ns'] = data['timestamp']

        for key in obs_keys:
            if key == 'ang_vel':
                obs_out[key] = data.get('gyro', np.zeros(3))
            elif key == 'acc':
                obs_out[key] = data.get('acc', np.zeros(3))
            elif key == 'quat':
                obs_out[key] = data.get('quat', np.array([1.0, 0.0, 0.0, 0.0]))
            elif key == 'mag' and 'mag' in data:
                obs_out[key] = data['mag']
            elif key == 'timestamp' and 'timestamp' in data:
                obs_out['timestamp_ns'] = data['timestamp']

        return obs_out

    def get_acc(self) -> np.ndarray | None:
        """Get the latest linear acceleration from ZED IMU.

        Returns:
            Linear acceleration [x, y, z] in m/s² if available, None otherwise.
        """
        data = self._subscriber.get_latest()
        return data.get('acc') if data else None

    def get_gyro(self) -> np.ndarray | None:
        """Get the latest angular velocity from ZED IMU.

        Returns:
            Angular velocity [x, y, z] in rad/s if available, None otherwise.
        """
        data = self._subscriber.get_latest()
        return data.get('gyro') if data else None

    def get_quat(self) -> np.ndarray | None:
        """Get the latest orientation quaternion from ZED IMU.

        Returns:
            Orientation quaternion [w, x, y, z] if available, None otherwise.
            Note: dexcomm uses [w, x, y, z] quaternion format.
        """
        data = self._subscriber.get_latest()
        return data.get('quat') if data else None

    def get_mag(self) -> np.ndarray | None:
        """Get the latest magnetometer reading from ZED IMU.

        Returns:
            Magnetic field [x, y, z] in µT if available, None otherwise.
        """
        data = self._subscriber.get_latest()
        if not data or not isinstance(data, dict):
            return None
        return data.get('mag', None)

    def has_mag(self) -> bool:
        """Check if the ZED IMU has magnetometer data available.

        Returns:
            True if magnetometer data is available, False otherwise.
        """
        data = self._subscriber.get_latest()
        if not data or not isinstance(data, dict):
            return False
        return 'mag' in data and data['mag'] is not None


    # Backward compatibility aliases
    get_acceleration = get_acc
    get_angular_velocity = get_gyro
    get_orientation = get_quat
    get_magnetometer = get_mag
    has_magnetometer = has_mag

    @property
    def name(self) -> str:
        """Get the ZED IMU name.

        Returns:
            IMU name string.
        """
        return self._name
