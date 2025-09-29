from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TaDelayCls:
	"""TaDelay commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("taDelay", core, parent)

	def set(self, enable: bool, upper: float) -> None:
		"""CONFigure:AFRF:MEASurement<Instance>:SROutines:LIMit:TADelay \n
		Snippet: driver.configure.afRf.measurement.searchRoutines.limit.taDelay.set(enable = False, upper = 1.0) \n
		No command help available \n
			:param enable: No help available
			:param upper: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('enable', enable, DataType.Boolean), ArgSingle('upper', upper, DataType.Float))
		self._core.io.write(f'CONFigure:AFRF:MEASurement<Instance>:SROutines:LIMit:TADelay {param}'.rstrip())

	# noinspection PyTypeChecker
	class TaDelayStruct(StructBase):
		"""Response structure. Fields: \n
			- 1 Enable: bool: No parameter help available
			- 2 Upper: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_float('Upper')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Upper: float = None

	def get(self) -> TaDelayStruct:
		"""CONFigure:AFRF:MEASurement<Instance>:SROutines:LIMit:TADelay \n
		Snippet: value: TaDelayStruct = driver.configure.afRf.measurement.searchRoutines.limit.taDelay.get() \n
		No command help available \n
			:return: structure: for return value, see the help for TaDelayStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:AFRF:MEASurement<Instance>:SROutines:LIMit:TADelay?', self.__class__.TaDelayStruct())
