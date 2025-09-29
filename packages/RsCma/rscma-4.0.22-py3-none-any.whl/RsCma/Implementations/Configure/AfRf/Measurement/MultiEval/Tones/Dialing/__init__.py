from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DialingCls:
	"""Dialing commands group definition. 3 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dialing", core, parent)

	@property
	def timeout(self):
		"""timeout commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_timeout'):
			from .Timeout import TimeoutCls
			self._timeout = TimeoutCls(self._core, self._cmd_group)
		return self._timeout

	@property
	def toStart(self):
		"""toStart commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_toStart'):
			from .ToStart import ToStartCls
			self._toStart = ToStartCls(self._core, self._cmd_group)
		return self._toStart

	@property
	def toEnd(self):
		"""toEnd commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_toEnd'):
			from .ToEnd import ToEndCls
			self._toEnd = ToEndCls(self._core, self._cmd_group)
		return self._toEnd

	def clone(self) -> 'DialingCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = DialingCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
