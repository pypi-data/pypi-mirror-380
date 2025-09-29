from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UserDefinedCls:
	"""UserDefined commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("userDefined", core, parent)

	def get_enable(self) -> bool:
		"""SOURce:AFRF:GENerator<Instance>:DIALing:SCAL:UDEFined:ENABle \n
		Snippet: value: bool = driver.source.afRf.generator.dialing.scal.userDefined.get_enable() \n
		No command help available \n
			:return: user_defined: No help available
		"""
		response = self._core.io.query_str('SOURce:AFRF:GENerator<Instance>:DIALing:SCAL:UDEFined:ENABle?')
		return Conversions.str_to_bool(response)

	def set_enable(self, user_defined: bool) -> None:
		"""SOURce:AFRF:GENerator<Instance>:DIALing:SCAL:UDEFined:ENABle \n
		Snippet: driver.source.afRf.generator.dialing.scal.userDefined.set_enable(user_defined = False) \n
		No command help available \n
			:param user_defined: No help available
		"""
		param = Conversions.bool_to_str(user_defined)
		self._core.io.write(f'SOURce:AFRF:GENerator<Instance>:DIALing:SCAL:UDEFined:ENABle {param}')
