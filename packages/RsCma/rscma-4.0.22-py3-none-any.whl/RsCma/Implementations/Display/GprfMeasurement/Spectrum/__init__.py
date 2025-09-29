from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SpectrumCls:
	"""Spectrum commands group definition. 2 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("spectrum", core, parent)

	@property
	def application(self):
		"""application commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_application'):
			from .Application import ApplicationCls
			self._application = ApplicationCls(self._core, self._cmd_group)
		return self._application

	@property
	def trace(self):
		"""trace commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_trace'):
			from .Trace import TraceCls
			self._trace = TraceCls(self._core, self._cmd_group)
		return self._trace

	def clone(self) -> 'SpectrumCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SpectrumCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
