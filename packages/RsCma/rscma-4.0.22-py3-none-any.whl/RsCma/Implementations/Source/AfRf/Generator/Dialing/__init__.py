from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DialingCls:
	"""Dialing commands group definition. 38 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dialing", core, parent)

	@property
	def scal(self):
		"""scal commands group. 3 Sub-classes, 5 commands."""
		if not hasattr(self, '_scal'):
			from .Scal import ScalCls
			self._scal = ScalCls(self._core, self._cmd_group)
		return self._scal

	@property
	def dtmf(self):
		"""dtmf commands group. 2 Sub-classes, 5 commands."""
		if not hasattr(self, '_dtmf'):
			from .Dtmf import DtmfCls
			self._dtmf = DtmfCls(self._core, self._cmd_group)
		return self._dtmf

	@property
	def fdialing(self):
		"""fdialing commands group. 2 Sub-classes, 7 commands."""
		if not hasattr(self, '_fdialing'):
			from .Fdialing import FdialingCls
			self._fdialing = FdialingCls(self._core, self._cmd_group)
		return self._fdialing

	@property
	def selCall(self):
		"""selCall commands group. 2 Sub-classes, 7 commands."""
		if not hasattr(self, '_selCall'):
			from .SelCall import SelCallCls
			self._selCall = SelCallCls(self._core, self._cmd_group)
		return self._selCall

	def clone(self) -> 'DialingCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = DialingCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
