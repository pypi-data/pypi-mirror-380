from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LimitCls:
	"""Limit commands group definition. 46 total commands, 6 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("limit", core, parent)

	@property
	def tones(self):
		"""tones commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_tones'):
			from .Tones import TonesCls
			self._tones = TonesCls(self._core, self._cmd_group)
		return self._tones

	@property
	def spdif(self):
		"""spdif commands group. 2 Sub-classes, 4 commands."""
		if not hasattr(self, '_spdif'):
			from .Spdif import SpdifCls
			self._spdif = SpdifCls(self._core, self._cmd_group)
		return self._spdif

	@property
	def demodulation(self):
		"""demodulation commands group. 9 Sub-classes, 0 commands."""
		if not hasattr(self, '_demodulation'):
			from .Demodulation import DemodulationCls
			self._demodulation = DemodulationCls(self._core, self._cmd_group)
		return self._demodulation

	@property
	def audioInput(self):
		"""audioInput commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_audioInput'):
			from .AudioInput import AudioInputCls
			self._audioInput = AudioInputCls(self._core, self._cmd_group)
		return self._audioInput

	@property
	def voip(self):
		"""voip commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_voip'):
			from .Voip import VoipCls
			self._voip = VoipCls(self._core, self._cmd_group)
		return self._voip

	@property
	def rfCarrier(self):
		"""rfCarrier commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_rfCarrier'):
			from .RfCarrier import RfCarrierCls
			self._rfCarrier = RfCarrierCls(self._core, self._cmd_group)
		return self._rfCarrier

	def clone(self) -> 'LimitCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = LimitCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
