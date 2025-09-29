from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SinfoCls:
	"""Sinfo commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sinfo", core, parent)

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- 1 Reliability: int: See 'Reliability indicator values'
			- 2 System_Code: int: System code
			- 3 Sharing_Mode: enums.SharingModeTetra: CONTinuous | CARRier | MMCH | TRAFfic Sharing mode
			- 4 Reserved_Frame: int: Reserved frame
			- 5 Dtx: enums.Allow: NA | ALLowed
			- 6 Frame_Ext: enums.Allow: NA | ALLowed
			- 7 Broadcast: enums.Allow: NA | ALLowed
			- 8 Cell_Service_Level: enums.Allow: NA | ALLowed
			- 9 Late_Entry: enums.Allow: NA | ALLowed
			- 10 Bcc: int: No parameter help available
			- 11 Mcc: int: No parameter help available
			- 12 Mnc: int: No parameter help available
			- 13 Time_Slot_Num: int: No parameter help available
			- 14 Frame_Num: int: No parameter help available
			- 15 Multiframe_Num: int: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('System_Code'),
			ArgStruct.scalar_enum('Sharing_Mode', enums.SharingModeTetra),
			ArgStruct.scalar_int('Reserved_Frame'),
			ArgStruct.scalar_enum('Dtx', enums.Allow),
			ArgStruct.scalar_enum('Frame_Ext', enums.Allow),
			ArgStruct.scalar_enum('Broadcast', enums.Allow),
			ArgStruct.scalar_enum('Cell_Service_Level', enums.Allow),
			ArgStruct.scalar_enum('Late_Entry', enums.Allow),
			ArgStruct.scalar_int('Bcc'),
			ArgStruct.scalar_int('Mcc'),
			ArgStruct.scalar_int('Mnc'),
			ArgStruct.scalar_int('Time_Slot_Num'),
			ArgStruct.scalar_int('Frame_Num'),
			ArgStruct.scalar_int('Multiframe_Num')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.System_Code: int = None
			self.Sharing_Mode: enums.SharingModeTetra = None
			self.Reserved_Frame: int = None
			self.Dtx: enums.Allow = None
			self.Frame_Ext: enums.Allow = None
			self.Broadcast: enums.Allow = None
			self.Cell_Service_Level: enums.Allow = None
			self.Late_Entry: enums.Allow = None
			self.Bcc: int = None
			self.Mcc: int = None
			self.Mnc: int = None
			self.Time_Slot_Num: int = None
			self.Frame_Num: int = None
			self.Multiframe_Num: int = None

	def fetch(self) -> ResultData:
		"""FETCh:AFRF:MEASurement<Instance>:DIGital:TETRa:SINFo \n
		Snippet: value: ResultData = driver.afRf.measurement.digital.tetra.sinfo.fetch() \n
		Queries signal information parameters for the TETRA standard when operating in downlink/forward direction:
		CONF:AFRF:MEAS:DIG:TETR:LDIR DLNK Signal information includes the system code, test modes, frame and service information. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:AFRF:MEASurement<Instance>:DIGital:TETRa:SINFo?', self.__class__.ResultData())

	def read(self) -> ResultData:
		"""READ:AFRF:MEASurement<Instance>:DIGital:TETRa:SINFo \n
		Snippet: value: ResultData = driver.afRf.measurement.digital.tetra.sinfo.read() \n
		Queries signal information parameters for the TETRA standard when operating in downlink/forward direction:
		CONF:AFRF:MEAS:DIG:TETR:LDIR DLNK Signal information includes the system code, test modes, frame and service information. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:AFRF:MEASurement<Instance>:DIGital:TETRa:SINFo?', self.__class__.ResultData())
