from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PctStampCls:
	"""PctStamp commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pctStamp", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- 1 Reliability: int: No parameter help available
			- 2 Pc_Time_Stamp_Lo: int: No parameter help available
			- 3 Pc_Time_Stamp_Hi: int: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Pc_Time_Stamp_Lo'),
			ArgStruct.scalar_int('Pc_Time_Stamp_Hi')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Pc_Time_Stamp_Lo: int = None
			self.Pc_Time_Stamp_Hi: int = None

	def fetch(self, audioInput=repcap.AudioInput.Default) -> FetchStruct:
		"""FETCh:AFRF:MEASurement<instance>:MEValuation:AIN<Nr>:PCTStamp \n
		Snippet: value: FetchStruct = driver.afRf.measurement.multiEval.audioInput.pctStamp.fetch(audioInput = repcap.AudioInput.Default) \n
		No command help available \n
			:param audioInput: optional repeated capability selector. Default value: Nr1 (settable in the interface 'AudioInput')
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		audioInput_cmd_val = self._cmd_group.get_repcap_cmd_value(audioInput, repcap.AudioInput)
		return self._core.io.query_struct(f'FETCh:AFRF:MEASurement<Instance>:MEValuation:AIN{audioInput_cmd_val}:PCTStamp?', self.__class__.FetchStruct())
