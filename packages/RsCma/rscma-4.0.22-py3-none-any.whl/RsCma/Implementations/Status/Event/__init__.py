from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EventCls:
	"""Event commands group definition. 4 total commands, 1 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("event", core, parent)

	@property
	def bits(self):
		"""bits commands group. 3 Sub-classes, 1 commands."""
		if not hasattr(self, '_bits'):
			from .Bits import BitsCls
			self._bits = BitsCls(self._core, self._cmd_group)
		return self._bits

	def clone(self) -> 'EventCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = EventCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
