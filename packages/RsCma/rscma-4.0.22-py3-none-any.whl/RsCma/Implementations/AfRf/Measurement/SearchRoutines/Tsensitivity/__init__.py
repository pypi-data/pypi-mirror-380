from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TsensitivityCls:
	"""Tsensitivity commands group definition. 25 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tsensitivity", core, parent)

	@property
	def voip(self):
		"""voip commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_voip'):
			from .Voip import VoipCls
			self._voip = VoipCls(self._core, self._cmd_group)
		return self._voip

	@property
	def audioOutput(self):
		"""audioOutput commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_audioOutput'):
			from .AudioOutput import AudioOutputCls
			self._audioOutput = AudioOutputCls(self._core, self._cmd_group)
		return self._audioOutput

	@property
	def fdeviation(self):
		"""fdeviation commands group. 1 Sub-classes, 3 commands."""
		if not hasattr(self, '_fdeviation'):
			from .Fdeviation import FdeviationCls
			self._fdeviation = FdeviationCls(self._core, self._cmd_group)
		return self._fdeviation

	@property
	def pdeviation(self):
		"""pdeviation commands group. 1 Sub-classes, 3 commands."""
		if not hasattr(self, '_pdeviation'):
			from .Pdeviation import PdeviationCls
			self._pdeviation = PdeviationCls(self._core, self._cmd_group)
		return self._pdeviation

	@property
	def modDepth(self):
		"""modDepth commands group. 1 Sub-classes, 3 commands."""
		if not hasattr(self, '_modDepth'):
			from .ModDepth import ModDepthCls
			self._modDepth = ModDepthCls(self._core, self._cmd_group)
		return self._modDepth

	def clone(self) -> 'TsensitivityCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = TsensitivityCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
