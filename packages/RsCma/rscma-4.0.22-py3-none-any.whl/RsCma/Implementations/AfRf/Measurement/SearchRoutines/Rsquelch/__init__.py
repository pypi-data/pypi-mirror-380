from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RsquelchCls:
	"""Rsquelch commands group definition. 18 total commands, 8 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rsquelch", core, parent)

	@property
	def ofLevel(self):
		"""ofLevel commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_ofLevel'):
			from .OfLevel import OfLevelCls
			self._ofLevel = OfLevelCls(self._core, self._cmd_group)
		return self._ofLevel

	@property
	def onLevel(self):
		"""onLevel commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_onLevel'):
			from .OnLevel import OnLevelCls
			self._onLevel = OnLevelCls(self._core, self._cmd_group)
		return self._onLevel

	@property
	def ofsQuality(self):
		"""ofsQuality commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_ofsQuality'):
			from .OfsQuality import OfsQualityCls
			self._ofsQuality = OfsQualityCls(self._core, self._cmd_group)
		return self._ofsQuality

	@property
	def onsQuality(self):
		"""onsQuality commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_onsQuality'):
			from .OnsQuality import OnsQualityCls
			self._onsQuality = OnsQualityCls(self._core, self._cmd_group)
		return self._onsQuality

	@property
	def hysteresis(self):
		"""hysteresis commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_hysteresis'):
			from .Hysteresis import HysteresisCls
			self._hysteresis = HysteresisCls(self._core, self._cmd_group)
		return self._hysteresis

	@property
	def tlevel(self):
		"""tlevel commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_tlevel'):
			from .Tlevel import TlevelCls
			self._tlevel = TlevelCls(self._core, self._cmd_group)
		return self._tlevel

	@property
	def signalQuality(self):
		"""signalQuality commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_signalQuality'):
			from .SignalQuality import SignalQualityCls
			self._signalQuality = SignalQualityCls(self._core, self._cmd_group)
		return self._signalQuality

	@property
	def llist(self):
		"""llist commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_llist'):
			from .Llist import LlistCls
			self._llist = LlistCls(self._core, self._cmd_group)
		return self._llist

	def clone(self) -> 'RsquelchCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RsquelchCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
