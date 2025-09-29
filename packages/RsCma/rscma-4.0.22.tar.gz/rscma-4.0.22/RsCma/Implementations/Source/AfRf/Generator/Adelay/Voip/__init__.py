from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class VoipCls:
	"""Voip commands group definition. 4 total commands, 2 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("voip", core, parent)

	@property
	def frequencies(self):
		"""frequencies commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_frequencies'):
			from .Frequencies import FrequenciesCls
			self._frequencies = FrequenciesCls(self._core, self._cmd_group)
		return self._frequencies

	@property
	def levels(self):
		"""levels commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_levels'):
			from .Levels import LevelsCls
			self._levels = LevelsCls(self._core, self._cmd_group)
		return self._levels

	def get_enable(self) -> bool:
		"""SOURce:AFRF:GENerator<Instance>:ADELay:VOIP:ENABle \n
		Snippet: value: bool = driver.source.afRf.generator.adelay.voip.get_enable() \n
		No command help available \n
			:return: enable: No help available
		"""
		response = self._core.io.query_str('SOURce:AFRF:GENerator<Instance>:ADELay:VOIP:ENABle?')
		return Conversions.str_to_bool(response)

	def set_enable(self, enable: bool) -> None:
		"""SOURce:AFRF:GENerator<Instance>:ADELay:VOIP:ENABle \n
		Snippet: driver.source.afRf.generator.adelay.voip.set_enable(enable = False) \n
		No command help available \n
			:param enable: No help available
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'SOURce:AFRF:GENerator<Instance>:ADELay:VOIP:ENABle {param}')

	def get_packets(self) -> int:
		"""SOURce:AFRF:GENerator<Instance>:ADELay:VOIP:PACKets \n
		Snippet: value: int = driver.source.afRf.generator.adelay.voip.get_packets() \n
		No command help available \n
			:return: count: No help available
		"""
		response = self._core.io.query_str('SOURce:AFRF:GENerator<Instance>:ADELay:VOIP:PACKets?')
		return Conversions.str_to_int(response)

	def set_packets(self, count: int) -> None:
		"""SOURce:AFRF:GENerator<Instance>:ADELay:VOIP:PACKets \n
		Snippet: driver.source.afRf.generator.adelay.voip.set_packets(count = 1) \n
		No command help available \n
			:param count: No help available
		"""
		param = Conversions.decimal_value_to_str(count)
		self._core.io.write(f'SOURce:AFRF:GENerator<Instance>:ADELay:VOIP:PACKets {param}')

	def clone(self) -> 'VoipCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = VoipCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
