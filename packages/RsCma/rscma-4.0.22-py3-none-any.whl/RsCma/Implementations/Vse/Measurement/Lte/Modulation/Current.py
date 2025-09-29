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
			- 3 Pusch_16_Qam: float: Unit: %
			- 4 Pusch_64_Qam: float: Unit: %
			- 5 Pusch_256_Qam: float: Unit: %
			- 6 Dmrs_Pusch_Qpsk: float: Unit: %
			- 7 Dmrs_Pusch_16_Qam: float: Unit: %
			- 8 Dmrs_Pusch_64_Qam: float: Unit: %
			- 9 Dmrs_Pusch_256_Qam: float: Unit: %
			- 10 Pucch: float: Unit: %
			- 11 Dmrs_Pucch: float: Unit: %
			- 12 Power: float: Unit: dBm
			- 13 Crest_Factor: float: Unit: dB
			- 14 Evm_All: float: Unit: %
			- 15 Phys_Channel: float: Unit: %
			- 16 Phys_Signal: float: Unit: %
			- 17 Frequency_Error: float: Unit: Hz
			- 18 Sampling_Error: float: No parameter help available
			- 19 Iq_Offset: float: Unit: dB
			- 20 Iq_Gain_Imbalance: float: Unit: dB
			- 21 Iq_Quadrature_Error: float: Unit: deg"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Pusch_Qpsk'),
			ArgStruct.scalar_float('Pusch_16_Qam'),
			ArgStruct.scalar_float('Pusch_64_Qam'),
			ArgStruct.scalar_float('Pusch_256_Qam'),
			ArgStruct.scalar_float('Dmrs_Pusch_Qpsk'),
			ArgStruct.scalar_float('Dmrs_Pusch_16_Qam'),
			ArgStruct.scalar_float('Dmrs_Pusch_64_Qam'),
			ArgStruct.scalar_float('Dmrs_Pusch_256_Qam'),
			ArgStruct.scalar_float('Pucch'),
			ArgStruct.scalar_float('Dmrs_Pucch'),
			ArgStruct.scalar_float('Power'),
			ArgStruct.scalar_float('Crest_Factor'),
			ArgStruct.scalar_float('Evm_All'),
			ArgStruct.scalar_float('Phys_Channel'),
			ArgStruct.scalar_float('Phys_Signal'),
			ArgStruct.scalar_float('Frequency_Error'),
			ArgStruct.scalar_float('Sampling_Error'),
			ArgStruct.scalar_float('Iq_Offset'),
			ArgStruct.scalar_float('Iq_Gain_Imbalance'),
			ArgStruct.scalar_float('Iq_Quadrature_Error')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Pusch_Qpsk: float = None
			self.Pusch_16_Qam: float = None
			self.Pusch_64_Qam: float = None
			self.Pusch_256_Qam: float = None
			self.Dmrs_Pusch_Qpsk: float = None
			self.Dmrs_Pusch_16_Qam: float = None
			self.Dmrs_Pusch_64_Qam: float = None
			self.Dmrs_Pusch_256_Qam: float = None
			self.Pucch: float = None
			self.Dmrs_Pucch: float = None
			self.Power: float = None
			self.Crest_Factor: float = None
			self.Evm_All: float = None
			self.Phys_Channel: float = None
			self.Phys_Signal: float = None
			self.Frequency_Error: float = None
			self.Sampling_Error: float = None
			self.Iq_Offset: float = None
			self.Iq_Gain_Imbalance: float = None
			self.Iq_Quadrature_Error: float = None

	def fetch(self) -> ResultData:
		"""FETCh:VSE:MEASurement<Instance>:LTE:MODulation:CURRent \n
		Snippet: value: ResultData = driver.vse.measurement.lte.modulation.current.fetch() \n
		Query LTE demodulation results. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:VSE:MEASurement<Instance>:LTE:MODulation:CURRent?', self.__class__.ResultData())

	def read(self) -> ResultData:
		"""READ:VSE:MEASurement<Instance>:LTE:MODulation:CURRent \n
		Snippet: value: ResultData = driver.vse.measurement.lte.modulation.current.read() \n
		Query LTE demodulation results. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:VSE:MEASurement<Instance>:LTE:MODulation:CURRent?', self.__class__.ResultData())
