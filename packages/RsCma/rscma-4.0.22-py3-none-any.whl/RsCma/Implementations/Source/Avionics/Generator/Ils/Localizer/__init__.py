from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LocalizerCls:
	"""Localizer commands group definition. 19 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("localizer", core, parent)

	@property
	def afSettings(self):
		"""afSettings commands group. 4 Sub-classes, 5 commands."""
		if not hasattr(self, '_afSettings'):
			from .AfSettings import AfSettingsCls
			self._afSettings = AfSettingsCls(self._core, self._cmd_group)
		return self._afSettings

	@property
	def rfSettings(self):
		"""rfSettings commands group. 2 Sub-classes, 2 commands."""
		if not hasattr(self, '_rfSettings'):
			from .RfSettings import RfSettingsCls
			self._rfSettings = RfSettingsCls(self._core, self._cmd_group)
		return self._rfSettings

	@property
	def idSignal(self):
		"""idSignal commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_idSignal'):
			from .IdSignal import IdSignalCls
			self._idSignal = IdSignalCls(self._core, self._cmd_group)
		return self._idSignal

	def clone(self) -> 'LocalizerCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = LocalizerCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
