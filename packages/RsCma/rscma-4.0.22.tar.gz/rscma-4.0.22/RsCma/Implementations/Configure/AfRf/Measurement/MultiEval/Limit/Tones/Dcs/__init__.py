from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DcsCls:
	"""Dcs commands group definition. 3 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dcs", core, parent)

	@property
	def fskDeviation(self):
		"""fskDeviation commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fskDeviation'):
			from .FskDeviation import FskDeviationCls
			self._fskDeviation = FskDeviationCls(self._core, self._cmd_group)
		return self._fskDeviation

	@property
	def tocLength(self):
		"""tocLength commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tocLength'):
			from .TocLength import TocLengthCls
			self._tocLength = TocLengthCls(self._core, self._cmd_group)
		return self._tocLength

	@property
	def tofDeviation(self):
		"""tofDeviation commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tofDeviation'):
			from .TofDeviation import TofDeviationCls
			self._tofDeviation = TofDeviationCls(self._core, self._cmd_group)
		return self._tofDeviation

	def clone(self) -> 'DcsCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = DcsCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
