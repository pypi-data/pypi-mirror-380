from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FftCls:
	"""Fft commands group definition. 92 total commands, 8 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fft", core, parent)

	@property
	def demodulation(self):
		"""demodulation commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_demodulation'):
			from .Demodulation import DemodulationCls
			self._demodulation = DemodulationCls(self._core, self._cmd_group)
		return self._demodulation

	@property
	def audioInput(self):
		"""audioInput commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_audioInput'):
			from .AudioInput import AudioInputCls
			self._audioInput = AudioInputCls(self._core, self._cmd_group)
		return self._audioInput

	@property
	def spdif(self):
		"""spdif commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_spdif'):
			from .Spdif import SpdifCls
			self._spdif = SpdifCls(self._core, self._cmd_group)
		return self._spdif

	@property
	def voip(self):
		"""voip commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_voip'):
			from .Voip import VoipCls
			self._voip = VoipCls(self._core, self._cmd_group)
		return self._voip

	@property
	def spdifRight(self):
		"""spdifRight commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_spdifRight'):
			from .SpdifRight import SpdifRightCls
			self._spdifRight = SpdifRightCls(self._core, self._cmd_group)
		return self._spdifRight

	@property
	def spdifLeft(self):
		"""spdifLeft commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_spdifLeft'):
			from .SpdifLeft import SpdifLeftCls
			self._spdifLeft = SpdifLeftCls(self._core, self._cmd_group)
		return self._spdifLeft

	@property
	def demodLeft(self):
		"""demodLeft commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_demodLeft'):
			from .DemodLeft import DemodLeftCls
			self._demodLeft = DemodLeftCls(self._core, self._cmd_group)
		return self._demodLeft

	@property
	def demodRight(self):
		"""demodRight commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_demodRight'):
			from .DemodRight import DemodRightCls
			self._demodRight = DemodRightCls(self._core, self._cmd_group)
		return self._demodRight

	def clone(self) -> 'FftCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = FftCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
