from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LevelsCls:
	"""Levels commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("levels", core, parent)

	def set(self, level_1: float, level_2: float) -> None:
		"""SOURce:AFRF:GENerator<instance>:ADELay:VOIP:LEVels \n
		Snippet: driver.source.afRf.generator.adelay.voip.levels.set(level_1 = 1.0, level_2 = 1.0) \n
		No command help available \n
			:param level_1: No help available
			:param level_2: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('level_1', level_1, DataType.Float), ArgSingle('level_2', level_2, DataType.Float))
		self._core.io.write(f'SOURce:AFRF:GENerator<Instance>:ADELay:VOIP:LEVels {param}'.rstrip())

	# noinspection PyTypeChecker
	class LevelsStruct(StructBase):
		"""Response structure. Fields: \n
			- 1 Level_1: float: No parameter help available
			- 2 Level_2: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_float('Level_1'),
			ArgStruct.scalar_float('Level_2')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Level_1: float = None
			self.Level_2: float = None

	def get(self) -> LevelsStruct:
		"""SOURce:AFRF:GENerator<instance>:ADELay:VOIP:LEVels \n
		Snippet: value: LevelsStruct = driver.source.afRf.generator.adelay.voip.levels.get() \n
		No command help available \n
			:return: structure: for return value, see the help for LevelsStruct structure arguments."""
		return self._core.io.query_struct(f'SOURce:AFRF:GENerator<Instance>:ADELay:VOIP:LEVels?', self.__class__.LevelsStruct())
