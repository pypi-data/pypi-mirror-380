from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ReferenceMarkerCls:
	"""ReferenceMarker commands group definition. 2 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("referenceMarker", core, parent)

	@property
	def speak(self):
		"""speak commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_speak'):
			from .Speak import SpeakCls
			self._speak = SpeakCls(self._core, self._cmd_group)
		return self._speak

	@property
	def npeak(self):
		"""npeak commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_npeak'):
			from .Npeak import NpeakCls
			self._npeak = NpeakCls(self._core, self._cmd_group)
		return self._npeak

	def clone(self) -> 'ReferenceMarkerCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ReferenceMarkerCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
