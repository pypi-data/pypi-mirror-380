from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MultiToneCls:
	"""MultiTone commands group definition. 9 total commands, 7 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("multiTone", core, parent)

	@property
	def tone(self):
		"""tone commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_tone'):
			from .Tone import ToneCls
			self._tone = ToneCls(self._core, self._cmd_group)
		return self._tone

	@property
	def enable(self):
		"""enable commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_enable'):
			from .Enable import EnableCls
			self._enable = EnableCls(self._core, self._cmd_group)
		return self._enable

	@property
	def crest(self):
		"""crest commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_crest'):
			from .Crest import CrestCls
			self._crest = CrestCls(self._core, self._cmd_group)
		return self._crest

	@property
	def frequency(self):
		"""frequency commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import FrequencyCls
			self._frequency = FrequencyCls(self._core, self._cmd_group)
		return self._frequency

	@property
	def level(self):
		"""level commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_level'):
			from .Level import LevelCls
			self._level = LevelCls(self._core, self._cmd_group)
		return self._level

	@property
	def ilevel(self):
		"""ilevel commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ilevel'):
			from .Ilevel import IlevelCls
			self._ilevel = IlevelCls(self._core, self._cmd_group)
		return self._ilevel

	@property
	def tlevel(self):
		"""tlevel commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tlevel'):
			from .Tlevel import TlevelCls
			self._tlevel = TlevelCls(self._core, self._cmd_group)
		return self._tlevel

	def clone(self) -> 'MultiToneCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = MultiToneCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
