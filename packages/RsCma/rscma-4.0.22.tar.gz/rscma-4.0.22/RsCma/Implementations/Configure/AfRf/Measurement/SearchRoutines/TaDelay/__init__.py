from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TaDelayCls:
	"""TaDelay commands group definition. 4 total commands, 1 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("taDelay", core, parent)

	@property
	def voip(self):
		"""voip commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_voip'):
			from .Voip import VoipCls
			self._voip = VoipCls(self._core, self._cmd_group)
		return self._voip

	def get_scount(self) -> int:
		"""CONFigure:AFRF:MEASurement<Instance>:SROutines:TADelay:SCOunt \n
		Snippet: value: int = driver.configure.afRf.measurement.searchRoutines.taDelay.get_scount() \n
		No command help available \n
			:return: count: No help available
		"""
		response = self._core.io.query_str('CONFigure:AFRF:MEASurement<Instance>:SROutines:TADelay:SCOunt?')
		return Conversions.str_to_int(response)

	def set_scount(self, count: int) -> None:
		"""CONFigure:AFRF:MEASurement<Instance>:SROutines:TADelay:SCOunt \n
		Snippet: driver.configure.afRf.measurement.searchRoutines.taDelay.set_scount(count = 1) \n
		No command help available \n
			:param count: No help available
		"""
		param = Conversions.decimal_value_to_str(count)
		self._core.io.write(f'CONFigure:AFRF:MEASurement<Instance>:SROutines:TADelay:SCOunt {param}')

	def get_pkg_count(self) -> int:
		"""CONFigure:AFRF:MEASurement<Instance>:SROutines:TADelay:PKGCount \n
		Snippet: value: int = driver.configure.afRf.measurement.searchRoutines.taDelay.get_pkg_count() \n
		No command help available \n
			:return: package_count: No help available
		"""
		response = self._core.io.query_str('CONFigure:AFRF:MEASurement<Instance>:SROutines:TADelay:PKGCount?')
		return Conversions.str_to_int(response)

	def set_pkg_count(self, package_count: int) -> None:
		"""CONFigure:AFRF:MEASurement<Instance>:SROutines:TADelay:PKGCount \n
		Snippet: driver.configure.afRf.measurement.searchRoutines.taDelay.set_pkg_count(package_count = 1) \n
		No command help available \n
			:param package_count: No help available
		"""
		param = Conversions.decimal_value_to_str(package_count)
		self._core.io.write(f'CONFigure:AFRF:MEASurement<Instance>:SROutines:TADelay:PKGCount {param}')

	def clone(self) -> 'TaDelayCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = TaDelayCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
