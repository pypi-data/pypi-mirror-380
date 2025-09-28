from dataclasses import dataclass
from enum import Enum
import pandas as pd
from pathlib import Path
from types import SimpleNamespace
import numpy as np

from . io import read_data, find_metadata
from .adjustments import get_neutral_bias_at_border, remove_ambient, apply_calibration, get_points_from_fraction, zfilter
from .detect import get_acceleration_start, get_acceleration_stop, get_nir_surface, get_nir_stop, get_sensor_start, get_ground_strike
from .depth import AccelerometerDepth, BarometerDepth
from .logging import setup_log
from .calibrations import Calibrations
import logging


setup_log()

LOG = logging.getLogger('study_lyte.profile')

@dataclass
class Event:
    name: str
    index: int
    depth: float # centimeters
    time: float # seconds

@dataclass
class GISPoint:
    x: float
    y: float


class Sensor(Enum):
    """Enum for various scenarios that come up with variations of data"""
    UNAVAILABLE = -1
    UNINTERPRETABLE = -2


class GenericProfileV6:
    def __init__(self, filename, surface_detection_offset=4.5, calibration=None,
             tip_diameter_mm=5):
        """
        Args:
            filename: path to valid lyte probe csv.
            surface_detection_offset: Geometric offset between nir sensors and tip in cm.
            calibration: Dictionary of keys and polynomial coefficients to calibration sensors
            tip_diameter_mm: diameter of the force tip in mm
        """
        self.filename = Path(filename)
        self.surface_detection_offset = surface_detection_offset
        self.tip_diameter_mm = tip_diameter_mm

        # Properties
        self._raw = None
        self._meta = None
        self._point = None
        self._serial_number = None
        self._calibration = calibration or None
        self.header_position = None

        # Dataframes
        self._depth = None  # Final depth series used for analysis
        self._acceleration = None  # No gravity acceleration
        self._cropped = None  # Full dataframe cropped to surface and stop
        self._force = None
        self._nir = None

        # Useful stats/info properties
        self._distance_traveled = None  # distance travelled while moving
        self._distance_through_snow = None  # Distance travelled while in snow
        self._avg_velocity = None  # avg velocity of the probe while in the snow
        self._resolution = None  # Vertical resolution of the profile in the snow
        self._datetime = None
        self._has_upward_motion = None  # Flag for datasets containing upward motion

        # Time series events
        self._start = None
        self._stop = None
        self._surface = None
        self._error = None
        self._ground = None

    def assign_event_depths(self):
        """" Enable depth assignment post depth realization """
        self.events
        for event in [self._start, self._stop, self._surface.nir, self._surface.force]:
            event.depth = self.depth.iloc[event.index]

    @property
    def serial_number(self):
        if self._serial_number is None:
            self._serial_number = self.metadata.get('Serial Num.')
            if self._serial_number is None:
                self._serial_number = 'UNKNOWN'
        return self._serial_number

    def set_calibration(self, ext_calibrations:Calibrations):
        """
        Assign new calibration using a collection of calibrations
        Args:
            ext_calibrations: External collection of calibrations
        """
        cal = ext_calibrations.from_serial(self.serial_number, date=self.datetime)
        self._calibration = cal.calibration

    @property
    def calibration(self):
        return self._calibration

    @classmethod
    def from_metadata(cls, filename, **kwargs):
        profile = cls(filename)
        if 'APP VERSION' in profile.metadata.keys():
            return ProcessedProfileV6(filename)
        else:
            return LyteProfileV6(filename)

    @property
    def raw(self):
        """
        Pandas dataframe hold the data exactly as it read in.
        """
        if self._raw is None:
            metadata = self.metadata
            self._raw, self._meta = read_data(str(self.filename), metadata, self.header_position)
            self._raw = self.process_df(self.raw)

        return self._raw

    @property
    def metadata(self):
        """
        Returns a dictionary of all data held in the header portion of the csv
        """
        if self._meta is None:
            self.header_position, self._meta = find_metadata(str(self.filename))

            # Manage misc naming of the acceleration range
            if 'ACC. Range' not in self._meta.keys():
                if "ACCRANGE" in self._meta.keys():
                    self._meta['ACC. Range'] = float(self._meta['ACCRANGE'])
                else:
                    self._meta['ACC. Range'] = 16

            else:
                self._meta['ACC. Range'] = float(self._meta['ACC. Range'])

            if 'ZPFO' in self._meta.keys():
                self._meta['ZPFO'] = int(self._meta['ZPFO'])

        return self._meta

    @property
    def nir(self):
        """
        Retrieve the Active NIR sensor with ambient NIR removed
        """
        if self._nir is None:
            self._nir = self.raw[["Sensor2", "Sensor3", "nir"]]
            self._nir['depth'] = self.depth.values
            end = self.stop.index if self.ground.index is None else self.ground.index
            if self.surface.nir.index < end:
                self._nir = self._nir.iloc[self.surface.nir.index:end].reset_index()
                self._nir = self._nir.drop(columns='index')
                self._nir['depth'] = self._nir['depth'] - self._nir['depth'].iloc[0]
            else:
                self._nir = Sensor.UNINTERPRETABLE
        return self._nir

    @property
    def force(self):
        """
        calibrated force and depth as a pandas dataframe cropped to the snow surface and the stop of motion
        """
        if self._force is None:
            # Default to raw data
            force = self.raw['Sensor1'].values
            if self.calibration is not None:
                if 'Sensor1' in self.calibration.keys():
                    force = apply_calibration(self.raw['Sensor1'].values, self.calibration['Sensor1'], minimum=0, maximum=15000)
                    force = force - np.nanmean(force[0:20])

            self._force = pd.DataFrame({'force': force, 'depth': self.depth.values})
            # prefer a ground index if available
            end = self.stop.index if self.ground.index is None else self.ground.index
            self._force = self._force.iloc[self.surface.force.index:end].reset_index()
            self._force = self._force.drop(columns='index')
            if not self._force.empty:
                self._force['depth'] = self._force['depth'] - self._force['depth'].iloc[0]

        return self._force

    @property
    def pressure(self):
        """ Force converted into pressure in kpa"""
        if 'pressure' not in self.force.columns:
            # Add pressure in kpa
            area = np.pi * (self.tip_diameter_mm / 1000)**2/4
            # Convert mN to kPa
            self.force['pressure'] = ((self.force['force']/1000) / area) / 1000
        return self.force[['depth', 'pressure']]

    @property
    def depth(self):
        raise NotImplemented("Must implement depth")

    @property
    def start(self):
        """ Return start event """
        raise NotImplemented("Must implement start event")

    @property
    def stop(self):
        """ Return stop event """
        raise NotImplemented("Must implement start event")

    @property
    def surface(self):
        """
        Return surface events for the nir and force which are physically separated by a distance
        """
        raise NotImplemented("Must implement surface event")

    @property
    def ground(self):
        """Event for ground detection"""
        if self._ground is None:
            ground = get_ground_strike(self.raw['Sensor1'], self.stop.index)
            if ground is not None:
                self._ground = Event(name='ground', index=ground, depth=self.depth.iloc[ground], time=None)
                if 'time' in self.raw.columns:
                    self._ground.time = self.raw['time'].iloc[ground]
            else:
                self._ground = Event(name='ground', index=None, depth=None, time=None)

        return self._ground

    @property
    def error(self):
        """ Return error event """
        raise NotImplemented("Error event not implemented")

    @property
    def distance_traveled(self):
        if self._distance_traveled is None:
            # Call depth to ensure its populated
            self.depth
            self._distance_traveled = abs(self.start.depth - self.stop.depth)
        return self._distance_traveled

    @property
    def distance_through_snow(self):
        if self._distance_through_snow is None:
            self._distance_through_snow = abs(self.surface.nir.depth - self.stop.depth)
        return self._distance_through_snow

    @property
    def datetime(self):
        """Retrieves the datetime object the measurement was taken"""
        if self._datetime is None:
            self._datetime = pd.to_datetime(self.metadata['RECORDED'])
        return self._datetime

    @property
    def resolution(self):
        """ Estimates the resolution of the profile"""
        if self._resolution is None:
            if type(self.nir) == pd.DataFrame:
                n_points = len(self.nir)
                self._resolution = n_points / self.distance_through_snow
            else:
                self._resolution = np.nan
        return self._resolution

    @property
    def events(self):
        """
        Return all the common events recorded
        """
        return [self.start, self.stop, self.surface.nir, self.surface.force,
                self.ground, self.error]

    @property
    def point(self):
        """Return custom gis point of the measurement location in EPSG 4326"""
        if self._point is None:
            if all([k in self.metadata.keys() for k in ['Latitude', 'Longitude']]):
                self._point = GISPoint(float(self.metadata['Longitude']), float(self.metadata['Latitude']))
            else:
                self._point = Sensor.UNAVAILABLE

        return self._point

    @property
    def has_upward_motion(self):
        """
        Bool indicating if upward motion was detected
        """
        if self._has_upward_motion is None:
            self._has_upward_motion = False
            # crop the depth data and down sample for speedy check
            n = get_points_from_fraction(len(self.depth), 0.005)
            coarse = self.depth.iloc[self.start.index:self.stop.index:n]
            # loop and find any values greater than the current value
            for i,v in coarse.items():
                upward = np.any(coarse.loc[i:] > v + 5)
                if upward:
                    self._has_upward_motion = True
                    break

        return self._has_upward_motion


class LyteProfileV6(GenericProfileV6):
    """
    Class for managing raw profiles pulled from the probe over USB. This class computes the
    depth profile from the raw data
    """
    def __init__(self, filename, depth_method='fused', **kwargs):
        super().__init__(filename, **kwargs)
        self.depth_method = depth_method
        # properties
        self._accelerometer = None
        self._barometer = None
        self._motion_detect_name = None  # column name containing accel data dir of travel
        self._acceleration_names = None  # All columns containing accel data
        self._moving_time = None  # time the probe was moving
        self._angle = None

    @staticmethod
    def process_df(df):
        """
        Migrate all baro depths to filtereddepth and remove ambient
        to add NIR column
        """
        df = df.rename(columns={'depth': 'filtereddepth'})
        df['nir'] = remove_ambient(df['Sensor3'], df['Sensor2'])
        return df

    @classmethod
    def from_dataframe(cls, df):
        profile = LyteProfileV6(None)
        profile._raw = cls.process_df(df)
        return profile

    @property
    def motion_detect_name(self):
        """Return all the names of acceleration columns"""
        if self._motion_detect_name is None:
            self._motion_detect_name = self.get_motion_name(self.raw.columns)
        return self._motion_detect_name

    @property
    def acceleration_names(self):
        """Return all the names of acceleration columns"""
        if self._acceleration_names is None:
            self._acceleration_names = self.get_acceleration_columns(self.raw.columns)
        return self._acceleration_names

    @property
    def acceleration(self):
        """
        Retrieve acceleration with gravity removed
        """
        # Assign the detection column if it is available
        if self._acceleration is None:
            if self.motion_detect_name != Sensor.UNAVAILABLE:
                # Remove gravity
                self._acceleration = get_neutral_bias_at_border(self.raw[self.motion_detect_name])
                # from study_lyte.plotting import plot_ts
                # ax = plot_ts(self._acceleration, show=False)
                # ax = plot_ts(self.raw[self.motion_detect_name], ax=ax, show=True)
            else:
                self._acceleration = Sensor.UNAVAILABLE
        return self._acceleration

    @property
    def accelerometer(self):
        """Returns a class holding timeseries of accelerometer based depth"""
        if self._accelerometer is None:
            if self.motion_detect_name == Sensor.UNAVAILABLE:
                self._accelerometer = Sensor.UNAVAILABLE
            else:
                data = pd.DataFrame.from_dict({'time':self.raw['time'], self.acceleration.name:self.acceleration.values})
                data = data.set_index('time')[self.acceleration.name]
                self._accelerometer = AccelerometerDepth(data, self.start.index, self.stop.index)
        return self._accelerometer

    @property
    def barometer(self):
        """Returns a class holding timeseries of barometer based depth"""
        if self._barometer is None:
            baro = self.raw[['time', 'filtereddepth']].set_index('time')['filtereddepth']
            if 'ZPFO' in self.metadata.keys():
                if self.metadata['ZPFO'] < 50:
                    LOG.info('Filtering barometer data...')
                    # TODO: make this more intelligent
                    baro = zfilter(self.raw['filtereddepth'].values, 0.4)
                    baro = pd.DataFrame.from_dict({'baro':baro, 'time': self.raw['time']})
                    baro = baro.set_index('time')['baro']

            if self.accelerometer != Sensor.UNAVAILABLE:
                # TODO: WHATS GOING ON HERE?
                idx = abs(self.accelerometer.depth - -1).argmin()
            else:
                idx = self.start.index

            angle = None if self.angle == Sensor.UNAVAILABLE else self.angle
            self._barometer = BarometerDepth(baro, idx, self.stop.index, angle=angle)

        return self._barometer

    @property
    def depth(self):
        if self._depth is None:
            if self.motion_detect_name != Sensor.UNAVAILABLE and self.depth_method != 'barometer':
                # User requested fused
                if self.depth_method == 'fused':
                    LOG.info("Using fused sensors to compute depth.")
                    depth = self.fuse_depths(self.accelerometer.depth.values.copy(),
                                                   self.barometer.depth.values.copy(),
                                                   error=self.error.index)

                    if depth.min() < -230 and self.accelerometer.depth.min() > -230:
                        LOG.warning('Fused depth result produced a profile > 230 cm. Defaulting to accelerometer')
                        self._depth = self.accelerometer.depth

                    elif depth.min() < -230 and self.barometer.depth.min() > -230:
                        LOG.warning('Fused and accelerometer depth resulted in a profile > 230 cm. Defaulting to barometer')
                        self._depth = self.barometer.depth

                    else:
                        self._depth = pd.Series(data=depth, index=self.raw['time'])

                # User requested accelerometer
                elif self.depth_method == 'accelerometer':
                    LOG.info("Using accelerometer alone to compute depth.")
                    self._depth = self.accelerometer.depth
            else:
                LOG.info("Using barometer alone to compute depth.")
                self._depth = self.barometer.depth

            # Assign positions of each event detected
            self.assign_event_depths()

        return self._depth

    @property
    def time(self):
        """Return the sample time data"""
        return self.raw['time']

    @property
    def start(self):
        """ Return start event """
        if self._start is None:
            if self.motion_detect_name != Sensor.UNAVAILABLE:
                idx = get_acceleration_start(self.acceleration)
            else:
                idx = 0

            self._start = Event(name='start', index=idx, depth=None, time=self.raw['time'].iloc[idx])
        return self._start

    @property
    def stop(self):
        """ Return stop event """
        if self._stop is None:
            if self.motion_detect_name != Sensor.UNAVAILABLE:
                backward_accel = get_neutral_bias_at_border(self.raw[self.motion_detect_name], direction='backward')
                idx = get_acceleration_stop(backward_accel)
            else:
                idx = get_nir_stop(self.raw['Sensor3'])
            if idx is not None:
                self._stop = Event(name='stop', index=idx, depth=None, time=self.raw['time'].iloc[idx])
            else:
                self._stop = Event(name='stop', index=len(self.raw) - 1, depth=None, time=self.raw['time'].iloc[0])

        return self._stop

    @property
    def surface(self):
        """
        Return surface events for the nir and force which are physically separated by a distance
        """
        if self._surface is None:
            # Call to populate nir in raw
            idx = get_nir_surface(self.raw['Sensor3'])
            if idx == 0:
                LOG.warning("Unable to find snow surface, defaulting to first data point")
            # Event according the NIR sensors
            depth = self.depth.iloc[idx]
            nir = Event(name='surface', index=idx, depth=depth, time=self.raw['time'].iloc[idx])

            # Event according to the force sensor
            force_surface_depth = depth + self.surface_detection_offset
            f_idx = abs(self.depth - force_surface_depth).argmin()
            # Retrieve force estimated start
            f_start = get_sensor_start(self.raw['Sensor1'], max_threshold=0.02, threshold=-0.02)
            f_start = f_start or f_idx

            # If the force start is before the NIR start then adjust
            if f_start < self.start.index:
                LOG.info(f'Choosing motion start ({self.start.index}) over force start ({f_start})...')
                f_idx = self.start.index
                force_surface_depth = self.depth.iloc[f_idx]

            elif f_start < f_idx:
                LOG.info(f'Choosing force start ({f_start}) over nir derived ({f_idx})...')
                f_idx = f_start
                force_surface_depth = self.depth.iloc[f_idx]

            force = Event(name='surface', index=f_idx, depth=force_surface_depth, time=self.raw['time'].iloc[f_idx])
            self._surface = SimpleNamespace(name='surface', nir=nir, force=force)

            # Allow surface detection to modify the start if there is conflict.
            if nir.time < self.start.time:
                self._start = nir
                self._start.name = 'start'

        return self._surface

    @property
    def ground(self):
        """Event for ground detection"""
        if self._ground is None:
            ground = get_ground_strike(self.raw['Sensor1'], self.stop.index)
            if ground is not None:
                self._ground = Event(name='ground', index=ground, depth=self.depth.iloc[ground], time=self.raw['time'].iloc[ground])
            else:
                self._ground = Event(name='ground', index=None, depth=None, time=None)

        return self._ground

    @property
    def error(self):
        """ Return error event """
        if self._error is None:
            if self.motion_detect_name != Sensor.UNAVAILABLE:
                idx = self.get_error(self.raw[self.motion_detect_name], self.metadata['ACC. Range'])
                depth = None
                if idx is None:
                    t = None
                else:
                    t = self.raw['time'].iloc[idx]

            else:
                idx = None
                depth = None
                t = None
            self._error = Event(name='error', index=idx, depth=depth, time=t)

        return self._error

    @property
    def moving_time(self):
        """Amount of time the probe was in motion"""
        if self._moving_time is None:
            self._moving_time = self.stop.time - self.start.time
        return self._moving_time

    @property
    def avg_velocity(self):
        if self._avg_velocity is None:
            self._avg_velocity = self.distance_traveled / self.moving_time
        return self._avg_velocity

    @staticmethod
    def get_motion_name(columns):
        """
        Find a column containing acceleration data sometimes called
        acceleration or Y-Axis to handle variations in formatting of file
        """
        candidates = [c for c in columns if c.lower() in ['acceleration', 'y-axis']]
        if candidates:
            return candidates[0]
        else:
            return Sensor.UNAVAILABLE

    @staticmethod
    def get_acceleration_columns(columns):
        """
        Find a columns containing acceleration data sometimes called
        acceleration or X,Y,Z-Axis to handle variations in formatting of file
        """
        candidates = [c for c in ['acceleration', 'X-Axis', 'Y-Axis', 'Z-Axis'] if c in columns]
        if candidates:
            return candidates
        else:
            return Sensor.UNAVAILABLE

    def report_card(self):
        """
        Return a useful string to print about metrics
        """
        msg = '| {:<15} {:<20} |\n'
        n_chars = int((39 - len(self.filename.name)) / 2)
        s =  '-'* n_chars
        header = f'\n{s} {self.filename.name} {s}\n'
        profile_string = header
        profile_string += msg.format('Recorded', f'{self.datetime.isoformat()}')
        profile_string += msg.format('Points', f'{len(self.raw.index):,}')
        profile_string += msg.format('Moving Time', f'{self.moving_time:0.1f} s')
        profile_string += msg.format('Avg. Speed', f'{self.avg_velocity:0.0f} cm/s')
        profile_string += msg.format('Resolution', f'{self.resolution:0.1f} pts/cm')
        profile_string += msg.format('Total Travel', f'{self.distance_traveled:0.1f} cm')
        profile_string += msg.format('Snow Depth', f'{self.distance_through_snow:0.1f} cm')
        profile_string += msg.format('Ground Strike:', 'True' if self.ground.time is not None else 'False')
        profile_string += msg.format('Upward Motion:', "True" if self.has_upward_motion else "False")
        if self.angle != Sensor.UNAVAILABLE:
            profile_string += msg.format('Angle:', int(self.angle))
        profile_string += msg.format('Errors:', f'@ {self.error.time:0.1f} s' if self.error.time is not None else 'None')

        profile_string += '-' * (len(header)-2) + '\n'
        return profile_string

    @classmethod
    def fuse_depths(cls, acc_depth, baro_depth, error=None):
        """
        Function to intelligently fuse together depth timeseries

        """
        # Accelerometer is always solid in the beginning, unknown as we move on in time
        weights_acc = np.ones_like(acc_depth) * 100
        weights_baro = np.ones_like(baro_depth)
        avg = np.average(np.array([acc_depth, baro_depth]).T, axis=1,
                         weights=np.array([weights_acc, weights_baro]).T)
        scaled_baro = baro_depth.copy()

        if error is not None:
            LOG.info("Blending depth timeseries...")
            minimum = 0.01
            # Ensure the same starting place
            scaled_baro[error:] = scaled_baro[error:] - (scaled_baro[error] - avg[error])

            # Full reliance on the constrained baro
            weights_acc[error:] = minimum

            avg = np.average(np.array([acc_depth, scaled_baro]).T, axis=1,
                             weights=np.array([weights_acc, weights_baro]).T)

        # The deeper we go the more the baro constrains
        baro_bottom = baro_depth.min()
        acc_bottom = acc_depth.min()
        avg_bottom = avg.min()

        # Scale total
        sensor_diff = abs(acc_bottom) - abs(baro_bottom)
        delta = 0.572 * abs(acc_bottom) + 0.308 * abs(baro_bottom) + 0.264 * sensor_diff + 8.916
        # delta = (acc_bottom * (5 - scale) + baro_bottom * scale) / 5
        avg = (avg / avg_bottom) * -1 * delta
        # from study_lyte.plotting import plot_ts
        # ax = plot_ts(avg, show=True)

        return avg

    @property
    def angle(self):
        """
        float indicating the angle at the start of a measurement
        """
        if self._angle is None and self.acceleration_names != Sensor.UNAVAILABLE:
            if 'Y-Axis' in self.acceleration_names:
                data = self.raw[self.acceleration_names].iloc[0:self.start.index + 1].mean(axis=0)
                magn = data.pow(2).sum()**0.5
                self._angle = np.arccos(abs(data['Y-Axis']) / magn) * 180 / np.pi
            else:
                self._angle = Sensor.UNAVAILABLE

        return self._angle

    @classmethod
    def get_error(cls, acc, acc_range, threshold=0.95):
        """Find a likely ACC error"""
        idx = acc.abs() >= (threshold * acc_range)
        error = None
        if np.any(idx):
            error = np.argwhere(idx.values)[0][0]
        return error

    def __repr__(self):
        profile_str = f"LyteProfile (Recorded {len(self.raw):,} points, {self.datetime.isoformat()})"
        return profile_str


class ProcessedProfileV6(GenericProfileV6):
    """ Class for managing profiles that have been depth processed already """
    def __init__(self, filename, **kwargs):
        super().__init__(filename, **kwargs)

    @staticmethod
    def process_df(df):
        """
        Migrate all baro depths to filtereddepth and remove ambient
        to add NIR column
        """
        df['nir'] = remove_ambient(df['Sensor3'], df['Sensor2'])
        return df

    @property
    def depth(self):
        return self.raw['depth']* -1

    @property
    def start(self):
        """ Return start event """
        if self._start is None:
            # TODO: PLACEHOLDER
            idx = 0
            self._start = Event(name='start', index=idx, depth=self.raw['depth'].iloc[idx], time=None)
        return self._start

    @property
    def stop(self):
        """ Return stop event """
        if self._stop is None:
            idx = self.raw.index[-1]
            self._stop = Event(name='stop', index=idx, depth=self.raw['depth'].iloc[idx], time=None)
        return self._stop

    @property
    def surface(self):
        """
        Return surface events for the nir and force which are physically separated by a distance
        """
        if self._surface is None:
            idx = 0
            force = Event(name='force', index=idx, depth=self.raw['depth'].iloc[0], time=None)
            nir = Event(name='nir', index=idx, depth=self.raw['depth'].iloc[0], time=None)
            self._surface = SimpleNamespace(name='surface', nir=nir, force=force)

        return self._surface