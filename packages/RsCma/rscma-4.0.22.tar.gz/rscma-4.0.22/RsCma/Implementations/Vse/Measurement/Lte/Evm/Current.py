from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CurrentCls:
	"""Current commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("current", core, parent)

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- 1 Reliability: int: See 'Reliability indicator values'
			- 2 Pusch_Qpsk: float: Unit: %
			- 3 Dmrs_Pusch_Qpsk: float: Unit: %
			- 4 Pucch: float: Unit: %
			- 5 Dmrs_Pucch: float: Unit: %"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Pusch_Qpsk'),
			ArgStruct.scalar_float('Dmrs_Pusch_Qpsk'),
			ArgStruct.scalar_float('Pucch'),
			ArgStruct.scalar_float('Dmrs_Pucch')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Pusch_Qpsk: float = None
			self.Dmrs_Pusch_Qpsk: float = None
			self.Pucch: float = None
			self.Dmrs_Pucch: float = None

	def read(self) -> ResultData:
		"""READ:VSE:MEASurement<Instance>:LTE:EVM:CURRent \n
		Snippet: value: ResultData = driver.vse.measurement.lte.evm.current.read() \n
		Query LTE EVM results. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:VSE:MEASurement<Instance>:LTE:EVM:CURRent?', self.__class__.ResultData())

	def fetch(self) -> ResultData:
		"""FETCh:VSE:MEASurement<Instance>:LTE:EVM:CURRent \n
		Snippet: value: ResultData = driver.vse.measurement.lte.evm.current.fetch() \n
		Query LTE EVM results. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:VSE:MEASurement<Instance>:LTE:EVM:CURRent?', self.__class__.ResultData())
