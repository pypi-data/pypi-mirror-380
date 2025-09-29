from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.Types import DataType
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ThDistortionCls:
	"""ThDistortion commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("thDistortion", core, parent)

	def set(self, enable: bool, upper: float) -> None:
		"""CONFigure:AFRF:MEASurement<Instance>:MEValuation:LIMit:DEModulation:THDistortion \n
		Snippet: driver.configure.afRf.measurement.multiEval.limit.demodulation.thDistortion.set(enable = False, upper = 1.0) \n
		Configures a limit for the THD results, measured via the RF input path. \n
			:param enable: OFF | ON Enables or disables the limit check
			:param upper: Upper THD limit Range: 0.001 % to 100 %, Unit: %
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('enable', enable, DataType.Boolean), ArgSingle('upper', upper, DataType.Float))
		self._core.io.write(f'CONFigure:AFRF:MEASurement<Instance>:MEValuation:LIMit:DEModulation:THDistortion {param}'.rstrip())

	# noinspection PyTypeChecker
	class ThDistortionStruct(StructBase):
		"""Response structure. Fields: \n
			- 1 Enable: bool: OFF | ON Enables or disables the limit check
			- 2 Upper: float: Upper THD limit Range: 0.001 % to 100 %, Unit: %"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_float('Upper')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Upper: float = None

	def get(self) -> ThDistortionStruct:
		"""CONFigure:AFRF:MEASurement<Instance>:MEValuation:LIMit:DEModulation:THDistortion \n
		Snippet: value: ThDistortionStruct = driver.configure.afRf.measurement.multiEval.limit.demodulation.thDistortion.get() \n
		Configures a limit for the THD results, measured via the RF input path. \n
			:return: structure: for return value, see the help for ThDistortionStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:AFRF:MEASurement<Instance>:MEValuation:LIMit:DEModulation:THDistortion?', self.__class__.ThDistortionStruct())
