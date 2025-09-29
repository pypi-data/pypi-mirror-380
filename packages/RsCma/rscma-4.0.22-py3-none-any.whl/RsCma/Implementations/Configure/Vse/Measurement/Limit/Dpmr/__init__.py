from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DpmrCls:
	"""Dpmr commands group definition. 5 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dpmr", core, parent)

	@property
	def ffError(self):
		"""ffError commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ffError'):
			from .FfError import FfErrorCls
			self._ffError = FfErrorCls(self._core, self._cmd_group)
		return self._ffError

	@property
	def fdError(self):
		"""fdError commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fdError'):
			from .FdError import FdErrorCls
			self._fdError = FdErrorCls(self._core, self._cmd_group)
		return self._fdError

	@property
	def merror(self):
		"""merror commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_merror'):
			from .Merror import MerrorCls
			self._merror = MerrorCls(self._core, self._cmd_group)
		return self._merror

	def clone(self) -> 'DpmrCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = DpmrCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
