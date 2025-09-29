from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.Types import DataType
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IlevelCls:
	"""Ilevel commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ilevel", core, parent)

	def set(self, ilevel_1: float, ilevel_2: float) -> None:
		"""SOURce:AFRF:GENerator<Instance>:IGENerator:SECond:DTONe:ILEVel \n
		Snippet: driver.source.afRf.generator.internalGenerator.second.dtone.ilevel.set(ilevel_1 = 1.0, ilevel_2 = 1.0) \n
		No command help available \n
			:param ilevel_1: No help available
			:param ilevel_2: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('ilevel_1', ilevel_1, DataType.Float), ArgSingle('ilevel_2', ilevel_2, DataType.Float))
		self._core.io.write(f'SOURce:AFRF:GENerator<Instance>:IGENerator:SECond:DTONe:ILEVel {param}'.rstrip())

	# noinspection PyTypeChecker
	class IlevelStruct(StructBase):
		"""Response structure. Fields: \n
			- 1 Ilevel_1: float: No parameter help available
			- 2 Ilevel_2: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_float('Ilevel_1'),
			ArgStruct.scalar_float('Ilevel_2')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Ilevel_1: float = None
			self.Ilevel_2: float = None

	def get(self) -> IlevelStruct:
		"""SOURce:AFRF:GENerator<Instance>:IGENerator:SECond:DTONe:ILEVel \n
		Snippet: value: IlevelStruct = driver.source.afRf.generator.internalGenerator.second.dtone.ilevel.get() \n
		No command help available \n
			:return: structure: for return value, see the help for IlevelStruct structure arguments."""
		return self._core.io.query_struct(f'SOURce:AFRF:GENerator<Instance>:IGENerator:SECond:DTONe:ILEVel?', self.__class__.IlevelStruct())
