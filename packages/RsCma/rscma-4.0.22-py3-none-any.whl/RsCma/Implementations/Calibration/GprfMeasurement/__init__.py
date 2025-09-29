from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class GprfMeasurementCls:
	"""GprfMeasurement commands group definition. 3 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("gprfMeasurement", core, parent)

	@property
	def spectrum(self):
		"""spectrum commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_spectrum'):
			from .Spectrum import SpectrumCls
			self._spectrum = SpectrumCls(self._core, self._cmd_group)
		return self._spectrum

	@property
	def extPwrSensor(self):
		"""extPwrSensor commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_extPwrSensor'):
			from .ExtPwrSensor import ExtPwrSensorCls
			self._extPwrSensor = ExtPwrSensorCls(self._core, self._cmd_group)
		return self._extPwrSensor

	@property
	def nrt(self):
		"""nrt commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_nrt'):
			from .Nrt import NrtCls
			self._nrt = NrtCls(self._core, self._cmd_group)
		return self._nrt

	def clone(self) -> 'GprfMeasurementCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = GprfMeasurementCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
