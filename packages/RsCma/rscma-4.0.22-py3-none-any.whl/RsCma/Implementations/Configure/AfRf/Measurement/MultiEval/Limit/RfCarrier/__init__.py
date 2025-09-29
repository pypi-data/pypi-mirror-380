from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RfCarrierCls:
	"""RfCarrier commands group definition. 3 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rfCarrier", core, parent)

	@property
	def power(self):
		"""power commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_power'):
			from .Power import PowerCls
			self._power = PowerCls(self._core, self._cmd_group)
		return self._power

	@property
	def freqError(self):
		"""freqError commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_freqError'):
			from .FreqError import FreqErrorCls
			self._freqError = FreqErrorCls(self._core, self._cmd_group)
		return self._freqError

	@property
	def pePower(self):
		"""pePower commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pePower'):
			from .PePower import PePowerCls
			self._pePower = PePowerCls(self._core, self._cmd_group)
		return self._pePower

	def clone(self) -> 'RfCarrierCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RfCarrierCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
