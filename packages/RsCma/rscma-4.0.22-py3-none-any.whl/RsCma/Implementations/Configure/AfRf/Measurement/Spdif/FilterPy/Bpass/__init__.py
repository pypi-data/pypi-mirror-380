from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BpassCls:
	"""Bpass commands group definition. 3 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bpass", core, parent)

	@property
	def enable(self):
		"""enable commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_enable'):
			from .Enable import EnableCls
			self._enable = EnableCls(self._core, self._cmd_group)
		return self._enable

	@property
	def cfrequency(self):
		"""cfrequency commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cfrequency'):
			from .Cfrequency import CfrequencyCls
			self._cfrequency = CfrequencyCls(self._core, self._cmd_group)
		return self._cfrequency

	@property
	def bandwidth(self):
		"""bandwidth commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bandwidth'):
			from .Bandwidth import BandwidthCls
			self._bandwidth = BandwidthCls(self._core, self._cmd_group)
		return self._bandwidth

	def clone(self) -> 'BpassCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = BpassCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
