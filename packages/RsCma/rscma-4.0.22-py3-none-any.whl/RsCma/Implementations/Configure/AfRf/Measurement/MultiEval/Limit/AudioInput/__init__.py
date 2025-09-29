from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.RepeatedCapability import RepeatedCapability
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AudioInputCls:
	"""AudioInput commands group definition. 6 total commands, 6 Subgroups, 0 group commands
	Repeated Capability: AudioInput, default value after init: AudioInput.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("audioInput", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_audioInput_get', 'repcap_audioInput_set', repcap.AudioInput.Nr1)

	def repcap_audioInput_set(self, audioInput: repcap.AudioInput) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to AudioInput.Default.
		Default value after init: AudioInput.Nr1"""
		self._cmd_group.set_repcap_enum_value(audioInput)

	def repcap_audioInput_get(self) -> repcap.AudioInput:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

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
	def sinad(self):
		"""sinad commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sinad'):
			from .Sinad import SinadCls
			self._sinad = SinadCls(self._core, self._cmd_group)
		return self._sinad

	@property
	def snnRatio(self):
		"""snnRatio commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_snnRatio'):
			from .SnnRatio import SnnRatioCls
			self._snnRatio = SnnRatioCls(self._core, self._cmd_group)
		return self._snnRatio

	@property
	def sndRatio(self):
		"""sndRatio commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sndRatio'):
			from .SndRatio import SndRatioCls
			self._sndRatio = SndRatioCls(self._core, self._cmd_group)
		return self._sndRatio

	def clone(self) -> 'AudioInputCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = AudioInputCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
