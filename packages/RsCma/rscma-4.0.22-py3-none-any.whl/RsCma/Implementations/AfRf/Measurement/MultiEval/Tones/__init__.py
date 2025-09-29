from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TonesCls:
	"""Tones commands group definition. 54 total commands, 6 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tones", core, parent)

	@property
	def voip(self):
		"""voip commands group. 2 Sub-classes, 2 commands."""
		if not hasattr(self, '_voip'):
			from .Voip import VoipCls
			self._voip = VoipCls(self._core, self._cmd_group)
		return self._voip

	@property
	def dcs(self):
		"""dcs commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_dcs'):
			from .Dcs import DcsCls
			self._dcs = DcsCls(self._core, self._cmd_group)
		return self._dcs

	@property
	def audioInput(self):
		"""audioInput commands group. 2 Sub-classes, 2 commands."""
		if not hasattr(self, '_audioInput'):
			from .AudioInput import AudioInputCls
			self._audioInput = AudioInputCls(self._core, self._cmd_group)
		return self._audioInput

	@property
	def spdifLeft(self):
		"""spdifLeft commands group. 2 Sub-classes, 2 commands."""
		if not hasattr(self, '_spdifLeft'):
			from .SpdifLeft import SpdifLeftCls
			self._spdifLeft = SpdifLeftCls(self._core, self._cmd_group)
		return self._spdifLeft

	@property
	def spdifRight(self):
		"""spdifRight commands group. 2 Sub-classes, 2 commands."""
		if not hasattr(self, '_spdifRight'):
			from .SpdifRight import SpdifRightCls
			self._spdifRight = SpdifRightCls(self._core, self._cmd_group)
		return self._spdifRight

	@property
	def demodulation(self):
		"""demodulation commands group. 2 Sub-classes, 2 commands."""
		if not hasattr(self, '_demodulation'):
			from .Demodulation import DemodulationCls
			self._demodulation = DemodulationCls(self._core, self._cmd_group)
		return self._demodulation

	def clone(self) -> 'TonesCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = TonesCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
