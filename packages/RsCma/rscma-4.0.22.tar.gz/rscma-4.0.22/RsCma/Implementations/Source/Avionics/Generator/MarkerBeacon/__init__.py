from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MarkerBeaconCls:
	"""MarkerBeacon commands group definition. 14 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("markerBeacon", core, parent)

	@property
	def afSettings(self):
		"""afSettings commands group. 1 Sub-classes, 4 commands."""
		if not hasattr(self, '_afSettings'):
			from .AfSettings import AfSettingsCls
			self._afSettings = AfSettingsCls(self._core, self._cmd_group)
		return self._afSettings

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_state'):
			from .State import StateCls
			self._state = StateCls(self._core, self._cmd_group)
		return self._state

	@property
	def rfSettings(self):
		"""rfSettings commands group. 1 Sub-classes, 2 commands."""
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

	def clone(self) -> 'MarkerBeaconCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = MarkerBeaconCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
