from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TetraCls:
	"""Tetra commands group definition. 2 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tetra", core, parent)

	@property
	def bitErrorRate(self):
		"""bitErrorRate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bitErrorRate'):
			from .BitErrorRate import BitErrorRateCls
			self._bitErrorRate = BitErrorRateCls(self._core, self._cmd_group)
		return self._bitErrorRate

	@property
	def freqError(self):
		"""freqError commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_freqError'):
			from .FreqError import FreqErrorCls
			self._freqError = FreqErrorCls(self._core, self._cmd_group)
		return self._freqError

	def clone(self) -> 'TetraCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = TetraCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
