from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PowerCls:
	"""Power commands group definition. 27 total commands, 8 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("power", core, parent)

	@property
	def state(self):
		"""state commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import StateCls
			self._state = StateCls(self._core, self._cmd_group)
		return self._state

	@property
	def elapsedStats(self):
		"""elapsedStats commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_elapsedStats'):
			from .ElapsedStats import ElapsedStatsCls
			self._elapsedStats = ElapsedStatsCls(self._core, self._cmd_group)
		return self._elapsedStats

	@property
	def current(self):
		"""current commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_current'):
			from .Current import CurrentCls
			self._current = CurrentCls(self._core, self._cmd_group)
		return self._current

	@property
	def minimum(self):
		"""minimum commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_minimum'):
			from .Minimum import MinimumCls
			self._minimum = MinimumCls(self._core, self._cmd_group)
		return self._minimum

	@property
	def maximum(self):
		"""maximum commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_maximum'):
			from .Maximum import MaximumCls
			self._maximum = MaximumCls(self._core, self._cmd_group)
		return self._maximum

	@property
	def average(self):
		"""average commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_average'):
			from .Average import AverageCls
			self._average = AverageCls(self._core, self._cmd_group)
		return self._average

	@property
	def peak(self):
		"""peak commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_peak'):
			from .Peak import PeakCls
			self._peak = PeakCls(self._core, self._cmd_group)
		return self._peak

	@property
	def standardDev(self):
		"""standardDev commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_standardDev'):
			from .StandardDev import StandardDevCls
			self._standardDev = StandardDevCls(self._core, self._cmd_group)
		return self._standardDev

	def initiate(self, opc_timeout_ms: int = -1) -> None:
		"""INITiate:GPRF:MEASurement<Instance>:POWer \n
		Snippet: driver.gprfMeasurement.power.initiate() \n
		Starts or continues the power measurement. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'INITiate:GPRF:MEASurement<Instance>:POWer', opc_timeout_ms)
		# OpcSyncAllowed = true

	def stop(self, opc_timeout_ms: int = -1) -> None:
		"""STOP:GPRF:MEASurement<Instance>:POWer \n
		Snippet: driver.gprfMeasurement.power.stop() \n
		Pauses the power measurement. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'STOP:GPRF:MEASurement<Instance>:POWer', opc_timeout_ms)
		# OpcSyncAllowed = true

	def abort(self, opc_timeout_ms: int = -1) -> None:
		"""ABORt:GPRF:MEASurement<Instance>:POWer \n
		Snippet: driver.gprfMeasurement.power.abort() \n
		Stops the power measurement. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'ABORt:GPRF:MEASurement<Instance>:POWer', opc_timeout_ms)
		# OpcSyncAllowed = true

	def clone(self) -> 'PowerCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PowerCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
