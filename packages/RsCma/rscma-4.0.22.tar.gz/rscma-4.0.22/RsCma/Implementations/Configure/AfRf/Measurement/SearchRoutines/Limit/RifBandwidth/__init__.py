from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RifBandwidthCls:
	"""RifBandwidth commands group definition. 2 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rifBandwidth", core, parent)

	@property
	def bwDisplace(self):
		"""bwDisplace commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bwDisplace'):
			from .BwDisplace import BwDisplaceCls
			self._bwDisplace = BwDisplaceCls(self._core, self._cmd_group)
		return self._bwDisplace

	@property
	def foffset(self):
		"""foffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_foffset'):
			from .Foffset import FoffsetCls
			self._foffset = FoffsetCls(self._core, self._cmd_group)
		return self._foffset

	def clone(self) -> 'RifBandwidthCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RifBandwidthCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
