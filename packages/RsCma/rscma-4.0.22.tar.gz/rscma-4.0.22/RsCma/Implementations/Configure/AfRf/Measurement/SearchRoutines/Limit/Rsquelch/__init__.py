from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RsquelchCls:
	"""Rsquelch commands group definition. 2 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rsquelch", core, parent)

	@property
	def tsensitivity(self):
		"""tsensitivity commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tsensitivity'):
			from .Tsensitivity import TsensitivityCls
			self._tsensitivity = TsensitivityCls(self._core, self._cmd_group)
		return self._tsensitivity

	@property
	def thysteresis(self):
		"""thysteresis commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_thysteresis'):
			from .Thysteresis import ThysteresisCls
			self._thysteresis = ThysteresisCls(self._core, self._cmd_group)
		return self._thysteresis

	def clone(self) -> 'RsquelchCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RsquelchCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
