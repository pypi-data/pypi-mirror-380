from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LevelCls:
	"""Level commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("level", core, parent)

	def set(self, level_edit_mode: enums.LevelEditMode, internalGen=repcap.InternalGen.Default) -> None:
		"""SOURce:AFRF:GENerator<Instance>:IGENerator<nr>:DTONe:LEVel \n
		Snippet: driver.source.afRf.generator.internalGenerator.dtone.level.set(level_edit_mode = enums.LevelEditMode.INDividual, internalGen = repcap.InternalGen.Default) \n
		No command help available \n
			:param level_edit_mode: No help available
			:param internalGen: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InternalGenerator')
		"""
		param = Conversions.enum_scalar_to_str(level_edit_mode, enums.LevelEditMode)
		internalGen_cmd_val = self._cmd_group.get_repcap_cmd_value(internalGen, repcap.InternalGen)
		self._core.io.write(f'SOURce:AFRF:GENerator<Instance>:IGENerator{internalGen_cmd_val}:DTONe:LEVel {param}')

	# noinspection PyTypeChecker
	def get(self, internalGen=repcap.InternalGen.Default) -> enums.LevelEditMode:
		"""SOURce:AFRF:GENerator<Instance>:IGENerator<nr>:DTONe:LEVel \n
		Snippet: value: enums.LevelEditMode = driver.source.afRf.generator.internalGenerator.dtone.level.get(internalGen = repcap.InternalGen.Default) \n
		No command help available \n
			:param internalGen: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InternalGenerator')
			:return: level_edit_mode: No help available"""
		internalGen_cmd_val = self._cmd_group.get_repcap_cmd_value(internalGen, repcap.InternalGen)
		response = self._core.io.query_str(f'SOURce:AFRF:GENerator<Instance>:IGENerator{internalGen_cmd_val}:DTONe:LEVel?')
		return Conversions.str_to_scalar_enum(response, enums.LevelEditMode)
