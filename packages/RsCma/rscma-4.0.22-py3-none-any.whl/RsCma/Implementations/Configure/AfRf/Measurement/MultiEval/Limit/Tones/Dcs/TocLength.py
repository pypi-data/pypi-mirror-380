from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal.Types import DataType
from .........Internal.StructBase import StructBase
from .........Internal.ArgStruct import ArgStruct
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TocLengthCls:
	"""TocLength commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tocLength", core, parent)

	def set(self, enable: bool, lower: float, upper: float) -> None:
		"""CONFigure:AFRF:MEASurement<Instance>:MEValuation:LIMit:TONes:DCS:TOCLength \n
		Snippet: driver.configure.afRf.measurement.multiEval.limit.tones.dcs.tocLength.set(enable = False, lower = 1.0, upper = 1.0) \n
		Configures limits for the duration of DCS turn-off code transmissions. \n
			:param enable: OFF | ON Enables or disables the limit check
			:param lower: Lower limit Range: 0 s to 0.15 s, Unit: s
			:param upper: Upper limit Range: 0.15 s to 1 s, Unit: s
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('enable', enable, DataType.Boolean), ArgSingle('lower', lower, DataType.Float), ArgSingle('upper', upper, DataType.Float))
		self._core.io.write(f'CONFigure:AFRF:MEASurement<Instance>:MEValuation:LIMit:TONes:DCS:TOCLength {param}'.rstrip())

	# noinspection PyTypeChecker
	class TocLengthStruct(StructBase):
		"""Response structure. Fields: \n
			- 1 Enable: bool: OFF | ON Enables or disables the limit check
			- 2 Lower: float: Lower limit Range: 0 s to 0.15 s, Unit: s
			- 3 Upper: float: Upper limit Range: 0.15 s to 1 s, Unit: s"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_float('Lower'),
			ArgStruct.scalar_float('Upper')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Lower: float = None
			self.Upper: float = None

	def get(self) -> TocLengthStruct:
		"""CONFigure:AFRF:MEASurement<Instance>:MEValuation:LIMit:TONes:DCS:TOCLength \n
		Snippet: value: TocLengthStruct = driver.configure.afRf.measurement.multiEval.limit.tones.dcs.tocLength.get() \n
		Configures limits for the duration of DCS turn-off code transmissions. \n
			:return: structure: for return value, see the help for TocLengthStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:AFRF:MEASurement<Instance>:MEValuation:LIMit:TONes:DCS:TOCLength?', self.__class__.TocLengthStruct())
