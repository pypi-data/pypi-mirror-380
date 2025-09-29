from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class GprfMeasurementCls:
	"""GprfMeasurement commands group definition. 198 total commands, 7 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("gprfMeasurement", core, parent)

	@property
	def spectrum(self):
		"""spectrum commands group. 11 Sub-classes, 3 commands."""
		if not hasattr(self, '_spectrum'):
			from .Spectrum import SpectrumCls
			self._spectrum = SpectrumCls(self._core, self._cmd_group)
		return self._spectrum

	@property
	def extPwrSensor(self):
		"""extPwrSensor commands group. 1 Sub-classes, 6 commands."""
		if not hasattr(self, '_extPwrSensor'):
			from .ExtPwrSensor import ExtPwrSensorCls
			self._extPwrSensor = ExtPwrSensorCls(self._core, self._cmd_group)
		return self._extPwrSensor

	@property
	def nrt(self):
		"""nrt commands group. 3 Sub-classes, 4 commands."""
		if not hasattr(self, '_nrt'):
			from .Nrt import NrtCls
			self._nrt = NrtCls(self._core, self._cmd_group)
		return self._nrt

	@property
	def power(self):
		"""power commands group. 8 Sub-classes, 3 commands."""
		if not hasattr(self, '_power'):
			from .Power import PowerCls
			self._power = PowerCls(self._core, self._cmd_group)
		return self._power

	@property
	def fftSpecAn(self):
		"""fftSpecAn commands group. 7 Sub-classes, 3 commands."""
		if not hasattr(self, '_fftSpecAn'):
			from .FftSpecAn import FftSpecAnCls
			self._fftSpecAn = FftSpecAnCls(self._core, self._cmd_group)
		return self._fftSpecAn

	@property
	def acp(self):
		"""acp commands group. 4 Sub-classes, 3 commands."""
		if not hasattr(self, '_acp'):
			from .Acp import AcpCls
			self._acp = AcpCls(self._core, self._cmd_group)
		return self._acp

	@property
	def iqRecorder(self):
		"""iqRecorder commands group. 5 Sub-classes, 5 commands."""
		if not hasattr(self, '_iqRecorder'):
			from .IqRecorder import IqRecorderCls
			self._iqRecorder = IqRecorderCls(self._core, self._cmd_group)
		return self._iqRecorder

	def clone(self) -> 'GprfMeasurementCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = GprfMeasurementCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
