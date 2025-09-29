from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DmrCls:
	"""Dmr commands group definition. 12 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dmr", core, parent)

	@property
	def poOff(self):
		"""poOff commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_poOff'):
			from .PoOff import PoOffCls
			self._poOff = PoOffCls(self._core, self._cmd_group)
		return self._poOff

	@property
	def sinfo(self):
		"""sinfo commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_sinfo'):
			from .Sinfo import SinfoCls
			self._sinfo = SinfoCls(self._core, self._cmd_group)
		return self._sinfo

	@property
	def power(self):
		"""power commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_power'):
			from .Power import PowerCls
			self._power = PowerCls(self._core, self._cmd_group)
		return self._power

	@property
	def bitErrorRate(self):
		"""bitErrorRate commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_bitErrorRate'):
			from .BitErrorRate import BitErrorRateCls
			self._bitErrorRate = BitErrorRateCls(self._core, self._cmd_group)
		return self._bitErrorRate

	def clone(self) -> 'DmrCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = DmrCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
