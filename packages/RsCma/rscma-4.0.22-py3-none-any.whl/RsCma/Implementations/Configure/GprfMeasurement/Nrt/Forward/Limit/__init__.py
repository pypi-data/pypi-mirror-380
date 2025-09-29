from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LimitCls:
	"""Limit commands group definition. 5 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("limit", core, parent)

	@property
	def enable(self):
		"""enable commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_enable'):
			from .Enable import EnableCls
			self._enable = EnableCls(self._core, self._cmd_group)
		return self._enable

	@property
	def power(self):
		"""power commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_power'):
			from .Power import PowerCls
			self._power = PowerCls(self._core, self._cmd_group)
		return self._power

	@property
	def pep(self):
		"""pep commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pep'):
			from .Pep import PepCls
			self._pep = PepCls(self._core, self._cmd_group)
		return self._pep

	@property
	def cfactor(self):
		"""cfactor commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cfactor'):
			from .Cfactor import CfactorCls
			self._cfactor = CfactorCls(self._core, self._cmd_group)
		return self._cfactor

	@property
	def cumulativeDistribFnc(self):
		"""cumulativeDistribFnc commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cumulativeDistribFnc'):
			from .CumulativeDistribFnc import CumulativeDistribFncCls
			self._cumulativeDistribFnc = CumulativeDistribFncCls(self._core, self._cmd_group)
		return self._cumulativeDistribFnc

	def clone(self) -> 'LimitCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = LimitCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
