from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.Types import DataType
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SnnRatioCls:
	"""SnnRatio commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("snnRatio", core, parent)

	def set(self, enable: bool, lower: float, upper: float=None) -> None:
		"""CONFigure:AFRF:MEASurement<Instance>:MEValuation:LIMit:DEModulation:SNNRatio \n
		Snippet: driver.configure.afRf.measurement.multiEval.limit.demodulation.snnRatio.set(enable = False, lower = 1.0, upper = 1.0) \n
		Configures limits for all SNR results, measured via the RF input path. SNR results include S/N, (S+N) /N and (S+N+D) /N. \n
			:param enable: OFF | ON Enables or disables the limit check.
			:param lower: Lower limit Range: 0.00 dB to 140.00 dB, Unit: dB
			:param upper: Upper limit Range: 0.00 dB to 140.00 dB, Unit: dB
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('enable', enable, DataType.Boolean), ArgSingle('lower', lower, DataType.Float), ArgSingle('upper', upper, DataType.Float, None, is_optional=True))
		self._core.io.write(f'CONFigure:AFRF:MEASurement<Instance>:MEValuation:LIMit:DEModulation:SNNRatio {param}'.rstrip())

	# noinspection PyTypeChecker
	class SnnRatioStruct(StructBase):
		"""Response structure. Fields: \n
			- 1 Enable: bool: OFF | ON Enables or disables the limit check.
			- 2 Lower: float: Lower limit Range: 0.00 dB to 140.00 dB, Unit: dB
			- 3 Upper: float: Upper limit Range: 0.00 dB to 140.00 dB, Unit: dB"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_float('Lower'),
			ArgStruct.scalar_float('Upper')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Lower: float = None
			self.Upper: float = None

	def get(self) -> SnnRatioStruct:
		"""CONFigure:AFRF:MEASurement<Instance>:MEValuation:LIMit:DEModulation:SNNRatio \n
		Snippet: value: SnnRatioStruct = driver.configure.afRf.measurement.multiEval.limit.demodulation.snnRatio.get() \n
		Configures limits for all SNR results, measured via the RF input path. SNR results include S/N, (S+N) /N and (S+N+D) /N. \n
			:return: structure: for return value, see the help for SnnRatioStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:AFRF:MEASurement<Instance>:MEValuation:LIMit:DEModulation:SNNRatio?', self.__class__.SnnRatioStruct())
