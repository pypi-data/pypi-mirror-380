from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SecondCls:
	"""Second commands group definition. 2 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("second", core, parent)

	@property
	def dtone(self):
		"""dtone commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_dtone'):
			from .Dtone import DtoneCls
			self._dtone = DtoneCls(self._core, self._cmd_group)
		return self._dtone

	@property
	def multiTone(self):
		"""multiTone commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_multiTone'):
			from .MultiTone import MultiToneCls
			self._multiTone = MultiToneCls(self._core, self._cmd_group)
		return self._multiTone

	def clone(self) -> 'SecondCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SecondCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
