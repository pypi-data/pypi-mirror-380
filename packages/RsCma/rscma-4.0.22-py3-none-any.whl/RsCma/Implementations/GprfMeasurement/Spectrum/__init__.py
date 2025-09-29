from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SpectrumCls:
	"""Spectrum commands group definition. 56 total commands, 11 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("spectrum", core, parent)

	@property
	def tgenerator(self):
		"""tgenerator commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_tgenerator'):
			from .Tgenerator import TgeneratorCls
			self._tgenerator = TgeneratorCls(self._core, self._cmd_group)
		return self._tgenerator

	@property
	def state(self):
		"""state commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import StateCls
			self._state = StateCls(self._core, self._cmd_group)
		return self._state

	@property
	def frequency(self):
		"""frequency commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import FrequencyCls
			self._frequency = FrequencyCls(self._core, self._cmd_group)
		return self._frequency

	@property
	def zeroSpan(self):
		"""zeroSpan commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_zeroSpan'):
			from .ZeroSpan import ZeroSpanCls
			self._zeroSpan = ZeroSpanCls(self._core, self._cmd_group)
		return self._zeroSpan

	@property
	def referenceMarker(self):
		"""referenceMarker commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_referenceMarker'):
			from .ReferenceMarker import ReferenceMarkerCls
			self._referenceMarker = ReferenceMarkerCls(self._core, self._cmd_group)
		return self._referenceMarker

	@property
	def sample(self):
		"""sample commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_sample'):
			from .Sample import SampleCls
			self._sample = SampleCls(self._core, self._cmd_group)
		return self._sample

	@property
	def rms(self):
		"""rms commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_rms'):
			from .Rms import RmsCls
			self._rms = RmsCls(self._core, self._cmd_group)
		return self._rms

	@property
	def maximum(self):
		"""maximum commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_maximum'):
			from .Maximum import MaximumCls
			self._maximum = MaximumCls(self._core, self._cmd_group)
		return self._maximum

	@property
	def minimum(self):
		"""minimum commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_minimum'):
			from .Minimum import MinimumCls
			self._minimum = MinimumCls(self._core, self._cmd_group)
		return self._minimum

	@property
	def average(self):
		"""average commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_average'):
			from .Average import AverageCls
			self._average = AverageCls(self._core, self._cmd_group)
		return self._average

	@property
	def freqSweep(self):
		"""freqSweep commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_freqSweep'):
			from .FreqSweep import FreqSweepCls
			self._freqSweep = FreqSweepCls(self._core, self._cmd_group)
		return self._freqSweep

	def initiate(self, opc_timeout_ms: int = -1) -> None:
		"""INITiate:GPRF:MEASurement<Instance>:SPECtrum \n
		Snippet: driver.gprfMeasurement.spectrum.initiate() \n
		Starts or continues the spectrum analyzer. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'INITiate:GPRF:MEASurement<Instance>:SPECtrum', opc_timeout_ms)
		# OpcSyncAllowed = true

	def stop(self, opc_timeout_ms: int = -1) -> None:
		"""STOP:GPRF:MEASurement<Instance>:SPECtrum \n
		Snippet: driver.gprfMeasurement.spectrum.stop() \n
		Pauses the spectrum analyzer. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'STOP:GPRF:MEASurement<Instance>:SPECtrum', opc_timeout_ms)
		# OpcSyncAllowed = true

	def abort(self, opc_timeout_ms: int = -1) -> None:
		"""ABORt:GPRF:MEASurement<Instance>:SPECtrum \n
		Snippet: driver.gprfMeasurement.spectrum.abort() \n
		Stops the spectrum analyzer. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'ABORt:GPRF:MEASurement<Instance>:SPECtrum', opc_timeout_ms)
		# OpcSyncAllowed = true

	def clone(self) -> 'SpectrumCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SpectrumCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
