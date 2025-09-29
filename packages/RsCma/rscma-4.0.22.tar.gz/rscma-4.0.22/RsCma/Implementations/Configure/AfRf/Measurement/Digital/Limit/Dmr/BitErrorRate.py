from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.Types import DataType
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BitErrorRateCls:
	"""BitErrorRate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bitErrorRate", core, parent)

	def set(self, enable_limit: bool, upper: float) -> None:
		"""CONFigure:AFRF:MEASurement<Instance>:DIGital:LIMit:DMR:BERate \n
		Snippet: driver.configure.afRf.measurement.digital.limit.dmr.bitErrorRate.set(enable_limit = False, upper = 1.0) \n
		Configures the upper limit of the bit error rate for standard DMR. \n
			:param enable_limit: OFF | ON Enables or disables the limit check
			:param upper: Upper limit Range: 0.1 % to 100 %, Unit: %
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('enable_limit', enable_limit, DataType.Boolean), ArgSingle('upper', upper, DataType.Float))
		self._core.io.write(f'CONFigure:AFRF:MEASurement<Instance>:DIGital:LIMit:DMR:BERate {param}'.rstrip())

	# noinspection PyTypeChecker
	class BitErrorRateStruct(StructBase):
		"""Response structure. Fields: \n
			- 1 Enable_Limit: bool: OFF | ON Enables or disables the limit check
			- 2 Upper: float: Upper limit Range: 0.1 % to 100 %, Unit: %"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable_Limit'),
			ArgStruct.scalar_float('Upper')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable_Limit: bool = None
			self.Upper: float = None

	def get(self) -> BitErrorRateStruct:
		"""CONFigure:AFRF:MEASurement<Instance>:DIGital:LIMit:DMR:BERate \n
		Snippet: value: BitErrorRateStruct = driver.configure.afRf.measurement.digital.limit.dmr.bitErrorRate.get() \n
		Configures the upper limit of the bit error rate for standard DMR. \n
			:return: structure: for return value, see the help for BitErrorRateStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:AFRF:MEASurement<Instance>:DIGital:LIMit:DMR:BERate?', self.__class__.BitErrorRateStruct())
