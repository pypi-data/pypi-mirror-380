from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ZboxCls:
	"""Zbox commands group definition. 2 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("zbox", core, parent)

	@property
	def impedance(self):
		"""impedance commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_impedance'):
			from .Impedance import ImpedanceCls
			self._impedance = ImpedanceCls(self._core, self._cmd_group)
		return self._impedance

	@property
	def attenuator(self):
		"""attenuator commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_attenuator'):
			from .Attenuator import AttenuatorCls
			self._attenuator = AttenuatorCls(self._core, self._cmd_group)
		return self._attenuator

	def clone(self) -> 'ZboxCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ZboxCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
