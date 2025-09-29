from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LimitCls:
	"""Limit commands group definition. 26 total commands, 6 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("limit", core, parent)

	@property
	def dmr(self):
		"""dmr commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_dmr'):
			from .Dmr import DmrCls
			self._dmr = DmrCls(self._core, self._cmd_group)
		return self._dmr

	@property
	def dpmr(self):
		"""dpmr commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_dpmr'):
			from .Dpmr import DpmrCls
			self._dpmr = DpmrCls(self._core, self._cmd_group)
		return self._dpmr

	@property
	def nxdn(self):
		"""nxdn commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_nxdn'):
			from .Nxdn import NxdnCls
			self._nxdn = NxdnCls(self._core, self._cmd_group)
		return self._nxdn

	@property
	def tetra(self):
		"""tetra commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_tetra'):
			from .Tetra import TetraCls
			self._tetra = TetraCls(self._core, self._cmd_group)
		return self._tetra

	@property
	def ptFive(self):
		"""ptFive commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_ptFive'):
			from .PtFive import PtFiveCls
			self._ptFive = PtFiveCls(self._core, self._cmd_group)
		return self._ptFive

	@property
	def rfCarrier(self):
		"""rfCarrier commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_rfCarrier'):
			from .RfCarrier import RfCarrierCls
			self._rfCarrier = RfCarrierCls(self._core, self._cmd_group)
		return self._rfCarrier

	def clone(self) -> 'LimitCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = LimitCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
