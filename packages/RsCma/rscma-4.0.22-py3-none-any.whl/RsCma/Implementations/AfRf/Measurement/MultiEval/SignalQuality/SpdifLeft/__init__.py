from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SpdifLeftCls:
	"""SpdifLeft commands group definition. 12 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("spdifLeft", core, parent)

	@property
	def current(self):
		"""current commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_current'):
			from .Current import CurrentCls
			self._current = CurrentCls(self._core, self._cmd_group)
		return self._current

	@property
	def average(self):
		"""average commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_average'):
			from .Average import AverageCls
			self._average = AverageCls(self._core, self._cmd_group)
		return self._average

	@property
	def deviation(self):
		"""deviation commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_deviation'):
			from .Deviation import DeviationCls
			self._deviation = DeviationCls(self._core, self._cmd_group)
		return self._deviation

	@property
	def extreme(self):
		"""extreme commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_extreme'):
			from .Extreme import ExtremeCls
			self._extreme = ExtremeCls(self._core, self._cmd_group)
		return self._extreme

	def clone(self) -> 'SpdifLeftCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SpdifLeftCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
