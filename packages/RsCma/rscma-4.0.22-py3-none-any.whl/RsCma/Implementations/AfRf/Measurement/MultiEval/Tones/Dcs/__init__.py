from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DcsCls:
	"""Dcs commands group definition. 24 total commands, 6 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dcs", core, parent)

	@property
	def cword(self):
		"""cword commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_cword'):
			from .Cword import CwordCls
			self._cword = CwordCls(self._core, self._cmd_group)
		return self._cword

	@property
	def lcWord(self):
		"""lcWord commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_lcWord'):
			from .LcWord import LcWordCls
			self._lcWord = LcWordCls(self._core, self._cmd_group)
		return self._lcWord

	@property
	def fskDeviation(self):
		"""fskDeviation commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_fskDeviation'):
			from .FskDeviation import FskDeviationCls
			self._fskDeviation = FskDeviationCls(self._core, self._cmd_group)
		return self._fskDeviation

	@property
	def bitErrorRate(self):
		"""bitErrorRate commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_bitErrorRate'):
			from .BitErrorRate import BitErrorRateCls
			self._bitErrorRate = BitErrorRateCls(self._core, self._cmd_group)
		return self._bitErrorRate

	@property
	def tocLength(self):
		"""tocLength commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_tocLength'):
			from .TocLength import TocLengthCls
			self._tocLength = TocLengthCls(self._core, self._cmd_group)
		return self._tocLength

	@property
	def dmatches(self):
		"""dmatches commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_dmatches'):
			from .Dmatches import DmatchesCls
			self._dmatches = DmatchesCls(self._core, self._cmd_group)
		return self._dmatches

	def clone(self) -> 'DcsCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = DcsCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
