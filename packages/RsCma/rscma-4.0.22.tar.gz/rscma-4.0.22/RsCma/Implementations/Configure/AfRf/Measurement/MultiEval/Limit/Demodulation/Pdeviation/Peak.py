from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal.Types import DataType
from .........Internal.StructBase import StructBase
from .........Internal.ArgStruct import ArgStruct
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PeakCls:
	"""Peak commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("peak", core, parent)

	def set(self, enable: bool, lower: float=None, upper: float=None) -> None:
		"""CONFigure:AFRF:MEASurement<Instance>:MEValuation:LIMit:DEModulation:PDEViation:PEAK \n
		Snippet: driver.configure.afRf.measurement.multiEval.limit.demodulation.pdeviation.peak.set(enable = False, lower = 1.0, upper = 1.0) \n
		Configures limits for the phase deviation results '+Peak' and '-Peak', measured for PM. The upper and lower limits have
		the same absolute value but different signs. \n
			:param enable: OFF | ON Enables or disables the limit check
			:param lower: A query returns the lower limit. A setting applies the absolute value to the upper limit and the absolute value plus a negative sign to the lower limit. Range: -10 rad to 0 rad, Unit: rad
			:param upper: A query returns the upper limit. A setting ignores this parameter. Range: 0 rad to 10 rad, Unit: rad
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('enable', enable, DataType.Boolean), ArgSingle('lower', lower, DataType.Float, None, is_optional=True), ArgSingle('upper', upper, DataType.Float, None, is_optional=True))
		self._core.io.write(f'CONFigure:AFRF:MEASurement<Instance>:MEValuation:LIMit:DEModulation:PDEViation:PEAK {param}'.rstrip())

	# noinspection PyTypeChecker
	class PeakStruct(StructBase):
		"""Response structure. Fields: \n
			- 1 Enable: bool: OFF | ON Enables or disables the limit check
			- 2 Lower: float: A query returns the lower limit. A setting applies the absolute value to the upper limit and the absolute value plus a negative sign to the lower limit. Range: -10 rad to 0 rad, Unit: rad
			- 3 Upper: float: A query returns the upper limit. A setting ignores this parameter. Range: 0 rad to 10 rad, Unit: rad"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_float('Lower'),
			ArgStruct.scalar_float('Upper')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Lower: float = None
			self.Upper: float = None

	def get(self) -> PeakStruct:
		"""CONFigure:AFRF:MEASurement<Instance>:MEValuation:LIMit:DEModulation:PDEViation:PEAK \n
		Snippet: value: PeakStruct = driver.configure.afRf.measurement.multiEval.limit.demodulation.pdeviation.peak.get() \n
		Configures limits for the phase deviation results '+Peak' and '-Peak', measured for PM. The upper and lower limits have
		the same absolute value but different signs. \n
			:return: structure: for return value, see the help for PeakStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:AFRF:MEASurement<Instance>:MEValuation:LIMit:DEModulation:PDEViation:PEAK?', self.__class__.PeakStruct())
