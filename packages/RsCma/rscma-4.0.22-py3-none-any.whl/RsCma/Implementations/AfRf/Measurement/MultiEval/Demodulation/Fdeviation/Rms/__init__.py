from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RmsCls:
	"""Rms commands group definition. 8 total commands, 1 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rms", core, parent)

	@property
	def delta(self):
		"""delta commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_delta'):
			from .Delta import DeltaCls
			self._delta = DeltaCls(self._core, self._cmd_group)
		return self._delta

	def clone(self) -> 'RmsCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RmsCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
