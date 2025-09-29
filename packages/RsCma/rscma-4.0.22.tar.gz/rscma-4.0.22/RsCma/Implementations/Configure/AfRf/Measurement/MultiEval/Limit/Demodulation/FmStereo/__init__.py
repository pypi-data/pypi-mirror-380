from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FmStereoCls:
	"""FmStereo commands group definition. 6 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fmStereo", core, parent)

	@property
	def mdeviation(self):
		"""mdeviation commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_mdeviation'):
			from .Mdeviation import MdeviationCls
			self._mdeviation = MdeviationCls(self._core, self._cmd_group)
		return self._mdeviation

	@property
	def adeviation(self):
		"""adeviation commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_adeviation'):
			from .Adeviation import AdeviationCls
			self._adeviation = AdeviationCls(self._core, self._cmd_group)
		return self._adeviation

	@property
	def piDeviation(self):
		"""piDeviation commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_piDeviation'):
			from .PiDeviation import PiDeviationCls
			self._piDeviation = PiDeviationCls(self._core, self._cmd_group)
		return self._piDeviation

	@property
	def pfError(self):
		"""pfError commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pfError'):
			from .PfError import PfErrorCls
			self._pfError = PfErrorCls(self._core, self._cmd_group)
		return self._pfError

	@property
	def rdsDeviation(self):
		"""rdsDeviation commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rdsDeviation'):
			from .RdsDeviation import RdsDeviationCls
			self._rdsDeviation = RdsDeviationCls(self._core, self._cmd_group)
		return self._rdsDeviation

	def clone(self) -> 'FmStereoCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = FmStereoCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
