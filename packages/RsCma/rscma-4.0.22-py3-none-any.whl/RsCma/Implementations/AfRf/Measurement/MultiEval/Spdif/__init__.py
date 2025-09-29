from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SpdifCls:
	"""Spdif commands group definition. 1 total commands, 1 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("spdif", core, parent)

	@property
	def delay(self):
		"""delay commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_delay'):
			from .Delay import DelayCls
			self._delay = DelayCls(self._core, self._cmd_group)
		return self._delay

	def clone(self) -> 'SpdifCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SpdifCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
