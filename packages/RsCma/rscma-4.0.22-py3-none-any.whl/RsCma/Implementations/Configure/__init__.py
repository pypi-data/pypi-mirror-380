from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ConfigureCls:
	"""Configure commands group definition. 631 total commands, 6 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("configure", core, parent)

	@property
	def afRf(self):
		"""afRf commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_afRf'):
			from .AfRf import AfRfCls
			self._afRf = AfRfCls(self._core, self._cmd_group)
		return self._afRf

	@property
	def base(self):
		"""base commands group. 11 Sub-classes, 2 commands."""
		if not hasattr(self, '_base'):
			from .Base import BaseCls
			self._base = BaseCls(self._core, self._cmd_group)
		return self._base

	@property
	def sequencer(self):
		"""sequencer commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_sequencer'):
			from .Sequencer import SequencerCls
			self._sequencer = SequencerCls(self._core, self._cmd_group)
		return self._sequencer

	@property
	def gprfMeasurement(self):
		"""gprfMeasurement commands group. 8 Sub-classes, 1 commands."""
		if not hasattr(self, '_gprfMeasurement'):
			from .GprfMeasurement import GprfMeasurementCls
			self._gprfMeasurement = GprfMeasurementCls(self._core, self._cmd_group)
		return self._gprfMeasurement

	@property
	def display(self):
		"""display commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_display'):
			from .Display import DisplayCls
			self._display = DisplayCls(self._core, self._cmd_group)
		return self._display

	@property
	def vse(self):
		"""vse commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_vse'):
			from .Vse import VseCls
			self._vse = VseCls(self._core, self._cmd_group)
		return self._vse

	def clone(self) -> 'ConfigureCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ConfigureCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
