from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DemodulationCls:
	"""Demodulation commands group definition. 76 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("demodulation", core, parent)

	@property
	def frequency(self):
		"""frequency commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import FrequencyCls
			self._frequency = FrequencyCls(self._core, self._cmd_group)
		return self._frequency

	@property
	def modDepth(self):
		"""modDepth commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_modDepth'):
			from .ModDepth import ModDepthCls
			self._modDepth = ModDepthCls(self._core, self._cmd_group)
		return self._modDepth

	@property
	def fdeviation(self):
		"""fdeviation commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_fdeviation'):
			from .Fdeviation import FdeviationCls
			self._fdeviation = FdeviationCls(self._core, self._cmd_group)
		return self._fdeviation

	@property
	def fmStereo(self):
		"""fmStereo commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_fmStereo'):
			from .FmStereo import FmStereoCls
			self._fmStereo = FmStereoCls(self._core, self._cmd_group)
		return self._fmStereo

	@property
	def pdeviation(self):
		"""pdeviation commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_pdeviation'):
			from .Pdeviation import PdeviationCls
			self._pdeviation = PdeviationCls(self._core, self._cmd_group)
		return self._pdeviation

	def clone(self) -> 'DemodulationCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = DemodulationCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
