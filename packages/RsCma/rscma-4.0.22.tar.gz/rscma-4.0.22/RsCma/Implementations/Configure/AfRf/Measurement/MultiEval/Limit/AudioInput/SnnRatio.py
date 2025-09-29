from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.Types import DataType
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SnnRatioCls:
	"""SnnRatio commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("snnRatio", core, parent)

	def set(self, enable: bool, lower: float, upper: float=None, audioInput=repcap.AudioInput.Default) -> None:
		"""CONFigure:AFRF:MEASurement<Instance>:MEValuation:LIMit:AIN<Nr>:SNNRatio \n
		Snippet: driver.configure.afRf.measurement.multiEval.limit.audioInput.snnRatio.set(enable = False, lower = 1.0, upper = 1.0, audioInput = repcap.AudioInput.Default) \n
		Configures limits for all SNR results, measured via an AF input path. SNR results (signal/noise) include S/N, (S+N) /N
		and (S+N+D) /N. \n
			:param enable: OFF | ON Enables or disables the limit check.
			:param lower: Lower limit Range: 0.00 dB to 140.00 dB, Unit: dB
			:param upper: Upper limit Range: 0.00 dB to 140.00 dB, Unit: dB
			:param audioInput: optional repeated capability selector. Default value: Nr1 (settable in the interface 'AudioInput')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('enable', enable, DataType.Boolean), ArgSingle('lower', lower, DataType.Float), ArgSingle('upper', upper, DataType.Float, None, is_optional=True))
		audioInput_cmd_val = self._cmd_group.get_repcap_cmd_value(audioInput, repcap.AudioInput)
		self._core.io.write(f'CONFigure:AFRF:MEASurement<Instance>:MEValuation:LIMit:AIN{audioInput_cmd_val}:SNNRatio {param}'.rstrip())

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

	def get(self, audioInput=repcap.AudioInput.Default) -> SnnRatioStruct:
		"""CONFigure:AFRF:MEASurement<Instance>:MEValuation:LIMit:AIN<Nr>:SNNRatio \n
		Snippet: value: SnnRatioStruct = driver.configure.afRf.measurement.multiEval.limit.audioInput.snnRatio.get(audioInput = repcap.AudioInput.Default) \n
		Configures limits for all SNR results, measured via an AF input path. SNR results (signal/noise) include S/N, (S+N) /N
		and (S+N+D) /N. \n
			:param audioInput: optional repeated capability selector. Default value: Nr1 (settable in the interface 'AudioInput')
			:return: structure: for return value, see the help for SnnRatioStruct structure arguments."""
		audioInput_cmd_val = self._cmd_group.get_repcap_cmd_value(audioInput, repcap.AudioInput)
		return self._core.io.query_struct(f'CONFigure:AFRF:MEASurement<Instance>:MEValuation:LIMit:AIN{audioInput_cmd_val}:SNNRatio?', self.__class__.SnnRatioStruct())
