from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class VoipCls:
	"""Voip commands group definition. 26 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("voip", core, parent)

	@property
	def frequency(self):
		"""frequency commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import FrequencyCls
			self._frequency = FrequencyCls(self._core, self._cmd_group)
		return self._frequency

	@property
	def level(self):
		"""level commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_level'):
			from .Level import LevelCls
			self._level = LevelCls(self._core, self._cmd_group)
		return self._level

	@property
	def delay(self):
		"""delay commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_delay'):
			from .Delay import DelayCls
			self._delay = DelayCls(self._core, self._cmd_group)
		return self._delay

	@property
	def pctStamp(self):
		"""pctStamp commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pctStamp'):
			from .PctStamp import PctStampCls
			self._pctStamp = PctStampCls(self._core, self._cmd_group)
		return self._pctStamp

	@property
	def afSignal(self):
		"""afSignal commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_afSignal'):
			from .AfSignal import AfSignalCls
			self._afSignal = AfSignalCls(self._core, self._cmd_group)
		return self._afSignal

	def clone(self) -> 'VoipCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = VoipCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
