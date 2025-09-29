from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FftSpecAnCls:
	"""FftSpecAn commands group definition. 26 total commands, 7 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fftSpecAn", core, parent)

	@property
	def state(self):
		"""state commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import StateCls
			self._state = StateCls(self._core, self._cmd_group)
		return self._state

	@property
	def marker(self):
		"""marker commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_marker'):
			from .Marker import MarkerCls
			self._marker = MarkerCls(self._core, self._cmd_group)
		return self._marker

	@property
	def peaks(self):
		"""peaks commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_peaks'):
			from .Peaks import PeaksCls
			self._peaks = PeaksCls(self._core, self._cmd_group)
		return self._peaks

	@property
	def power(self):
		"""power commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_power'):
			from .Power import PowerCls
			self._power = PowerCls(self._core, self._cmd_group)
		return self._power

	@property
	def qcomponent(self):
		"""qcomponent commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_qcomponent'):
			from .Qcomponent import QcomponentCls
			self._qcomponent = QcomponentCls(self._core, self._cmd_group)
		return self._qcomponent

	@property
	def icomponent(self):
		"""icomponent commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_icomponent'):
			from .Icomponent import IcomponentCls
			self._icomponent = IcomponentCls(self._core, self._cmd_group)
		return self._icomponent

	@property
	def tdomain(self):
		"""tdomain commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_tdomain'):
			from .Tdomain import TdomainCls
			self._tdomain = TdomainCls(self._core, self._cmd_group)
		return self._tdomain

	def initiate(self, opc_timeout_ms: int = -1) -> None:
		"""INITiate:GPRF:MEASurement<Instance>:FFTSanalyzer \n
		Snippet: driver.gprfMeasurement.fftSpecAn.initiate() \n
		Starts or continues the FFT spectrum analyzer. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'INITiate:GPRF:MEASurement<Instance>:FFTSanalyzer', opc_timeout_ms)
		# OpcSyncAllowed = true

	def stop(self, opc_timeout_ms: int = -1) -> None:
		"""STOP:GPRF:MEASurement<Instance>:FFTSanalyzer \n
		Snippet: driver.gprfMeasurement.fftSpecAn.stop() \n
		Pauses the FFT spectrum analyzer. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'STOP:GPRF:MEASurement<Instance>:FFTSanalyzer', opc_timeout_ms)
		# OpcSyncAllowed = true

	def abort(self, opc_timeout_ms: int = -1) -> None:
		"""ABORt:GPRF:MEASurement<Instance>:FFTSanalyzer \n
		Snippet: driver.gprfMeasurement.fftSpecAn.abort() \n
		Stops the FFT spectrum analyzer. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'ABORt:GPRF:MEASurement<Instance>:FFTSanalyzer', opc_timeout_ms)
		# OpcSyncAllowed = true

	def clone(self) -> 'FftSpecAnCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = FftSpecAnCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
