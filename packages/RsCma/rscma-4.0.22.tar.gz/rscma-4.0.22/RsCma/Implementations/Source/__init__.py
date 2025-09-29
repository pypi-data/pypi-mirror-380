from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SourceCls:
	"""Source commands group definition. 347 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("source", core, parent)

	@property
	def afRf(self):
		"""afRf commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_afRf'):
			from .AfRf import AfRfCls
			self._afRf = AfRfCls(self._core, self._cmd_group)
		return self._afRf

	@property
	def xrt(self):
		"""xrt commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_xrt'):
			from .Xrt import XrtCls
			self._xrt = XrtCls(self._core, self._cmd_group)
		return self._xrt

	@property
	def avionics(self):
		"""avionics commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_avionics'):
			from .Avionics import AvionicsCls
			self._avionics = AvionicsCls(self._core, self._cmd_group)
		return self._avionics

	@property
	def base(self):
		"""base commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_base'):
			from .Base import BaseCls
			self._base = BaseCls(self._core, self._cmd_group)
		return self._base

	def clone(self) -> 'SourceCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SourceCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
