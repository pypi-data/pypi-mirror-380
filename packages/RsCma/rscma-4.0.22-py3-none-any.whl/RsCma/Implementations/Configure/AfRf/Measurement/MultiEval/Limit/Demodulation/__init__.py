from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DemodulationCls:
	"""Demodulation commands group definition. 16 total commands, 9 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("demodulation", core, parent)

	@property
	def thDistortion(self):
		"""thDistortion commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_thDistortion'):
			from .ThDistortion import ThDistortionCls
			self._thDistortion = ThDistortionCls(self._core, self._cmd_group)
		return self._thDistortion

	@property
	def thdNoise(self):
		"""thdNoise commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_thdNoise'):
			from .ThdNoise import ThdNoiseCls
			self._thdNoise = ThdNoiseCls(self._core, self._cmd_group)
		return self._thdNoise

	@property
	def snRatio(self):
		"""snRatio commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_snRatio'):
			from .SnRatio import SnRatioCls
			self._snRatio = SnRatioCls(self._core, self._cmd_group)
		return self._snRatio

	@property
	def snnRatio(self):
		"""snnRatio commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_snnRatio'):
			from .SnnRatio import SnnRatioCls
			self._snnRatio = SnnRatioCls(self._core, self._cmd_group)
		return self._snnRatio

	@property
	def sinad(self):
		"""sinad commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sinad'):
			from .Sinad import SinadCls
			self._sinad = SinadCls(self._core, self._cmd_group)
		return self._sinad

	@property
	def sndRatio(self):
		"""sndRatio commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sndRatio'):
			from .SndRatio import SndRatioCls
			self._sndRatio = SndRatioCls(self._core, self._cmd_group)
		return self._sndRatio

	@property
	def fdeviation(self):
		"""fdeviation commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_fdeviation'):
			from .Fdeviation import FdeviationCls
			self._fdeviation = FdeviationCls(self._core, self._cmd_group)
		return self._fdeviation

	@property
	def pdeviation(self):
		"""pdeviation commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_pdeviation'):
			from .Pdeviation import PdeviationCls
			self._pdeviation = PdeviationCls(self._core, self._cmd_group)
		return self._pdeviation

	@property
	def fmStereo(self):
		"""fmStereo commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_fmStereo'):
			from .FmStereo import FmStereoCls
			self._fmStereo = FmStereoCls(self._core, self._cmd_group)
		return self._fmStereo

	def clone(self) -> 'DemodulationCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = DemodulationCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
