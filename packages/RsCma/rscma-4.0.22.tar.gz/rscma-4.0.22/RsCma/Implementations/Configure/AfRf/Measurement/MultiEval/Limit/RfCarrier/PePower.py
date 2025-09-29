from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.Types import DataType
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PePowerCls:
	"""PePower commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pePower", core, parent)

	def set(self, enable_limit: bool, lower: float, upper: float) -> None:
		"""CONFigure:AFRF:MEASurement<Instance>:MEValuation:LIMit:RFCarrier:PEPower \n
		Snippet: driver.configure.afRf.measurement.multiEval.limit.rfCarrier.pePower.set(enable_limit = False, lower = 1.0, upper = 1.0) \n
		Configures limits for the measured RF signal power (PEP value) . \n
			:param enable_limit: OFF | ON Enables or disables the limit check
			:param lower: Lower power limit Range: -130 dBm to 55 dBm, Unit: dBm
			:param upper: Upper power limit Range: -130 dBm to 55 dBm, Unit: dBm
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('enable_limit', enable_limit, DataType.Boolean), ArgSingle('lower', lower, DataType.Float), ArgSingle('upper', upper, DataType.Float))
		self._core.io.write(f'CONFigure:AFRF:MEASurement<Instance>:MEValuation:LIMit:RFCarrier:PEPower {param}'.rstrip())

	# noinspection PyTypeChecker
	class PePowerStruct(StructBase):
		"""Response structure. Fields: \n
			- 1 Enable_Limit: bool: OFF | ON Enables or disables the limit check
			- 2 Lower: float: Lower power limit Range: -130 dBm to 55 dBm, Unit: dBm
			- 3 Upper: float: Upper power limit Range: -130 dBm to 55 dBm, Unit: dBm"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable_Limit'),
			ArgStruct.scalar_float('Lower'),
			ArgStruct.scalar_float('Upper')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable_Limit: bool = None
			self.Lower: float = None
			self.Upper: float = None

	def get(self) -> PePowerStruct:
		"""CONFigure:AFRF:MEASurement<Instance>:MEValuation:LIMit:RFCarrier:PEPower \n
		Snippet: value: PePowerStruct = driver.configure.afRf.measurement.multiEval.limit.rfCarrier.pePower.get() \n
		Configures limits for the measured RF signal power (PEP value) . \n
			:return: structure: for return value, see the help for PePowerStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:AFRF:MEASurement<Instance>:MEValuation:LIMit:RFCarrier:PEPower?', self.__class__.PePowerStruct())
