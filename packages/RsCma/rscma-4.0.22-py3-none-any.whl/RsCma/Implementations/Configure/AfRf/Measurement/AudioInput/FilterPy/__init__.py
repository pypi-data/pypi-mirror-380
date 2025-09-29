from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FilterPyCls:
	"""FilterPy commands group definition. 12 total commands, 8 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("filterPy", core, parent)

	@property
	def dwidth(self):
		"""dwidth commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_dwidth'):
			from .Dwidth import DwidthCls
			self._dwidth = DwidthCls(self._core, self._cmd_group)
		return self._dwidth

	@property
	def bpass(self):
		"""bpass commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_bpass'):
			from .Bpass import BpassCls
			self._bpass = BpassCls(self._core, self._cmd_group)
		return self._bpass

	@property
	def weighting(self):
		"""weighting commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_weighting'):
			from .Weighting import WeightingCls
			self._weighting = WeightingCls(self._core, self._cmd_group)
		return self._weighting

	@property
	def dfrequency(self):
		"""dfrequency commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dfrequency'):
			from .Dfrequency import DfrequencyCls
			self._dfrequency = DfrequencyCls(self._core, self._cmd_group)
		return self._dfrequency

	@property
	def robustAuto(self):
		"""robustAuto commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_robustAuto'):
			from .RobustAuto import RobustAutoCls
			self._robustAuto = RobustAutoCls(self._core, self._cmd_group)
		return self._robustAuto

	@property
	def notch(self):
		"""notch commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_notch'):
			from .Notch import NotchCls
			self._notch = NotchCls(self._core, self._cmd_group)
		return self._notch

	@property
	def lpass(self):
		"""lpass commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_lpass'):
			from .Lpass import LpassCls
			self._lpass = LpassCls(self._core, self._cmd_group)
		return self._lpass

	@property
	def hpass(self):
		"""hpass commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_hpass'):
			from .Hpass import HpassCls
			self._hpass = HpassCls(self._core, self._cmd_group)
		return self._hpass

	def clone(self) -> 'FilterPyCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = FilterPyCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
