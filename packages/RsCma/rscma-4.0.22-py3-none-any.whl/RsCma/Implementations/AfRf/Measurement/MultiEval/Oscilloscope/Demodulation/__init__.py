from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DemodulationCls:
	"""Demodulation commands group definition. 8 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("demodulation", core, parent)

	@property
	def pdeviation(self):
		"""pdeviation commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_pdeviation'):
			from .Pdeviation import PdeviationCls
			self._pdeviation = PdeviationCls(self._core, self._cmd_group)
		return self._pdeviation

	@property
	def modDepth(self):
		"""modDepth commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_modDepth'):
			from .ModDepth import ModDepthCls
			self._modDepth = ModDepthCls(self._core, self._cmd_group)
		return self._modDepth

	@property
	def lsbLevel(self):
		"""lsbLevel commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_lsbLevel'):
			from .LsbLevel import LsbLevelCls
			self._lsbLevel = LsbLevelCls(self._core, self._cmd_group)
		return self._lsbLevel

	@property
	def usbLevel(self):
		"""usbLevel commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_usbLevel'):
			from .UsbLevel import UsbLevelCls
			self._usbLevel = UsbLevelCls(self._core, self._cmd_group)
		return self._usbLevel

	def clone(self) -> 'DemodulationCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = DemodulationCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
