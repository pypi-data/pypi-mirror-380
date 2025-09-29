from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SfactorCls:
	"""Sfactor commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sfactor", core, parent)

	def set(self, factor: float, audioInput=repcap.AudioInput.Default) -> None:
		"""CONFigure:AFRF:MEASurement<Instance>:AIN<nr>:FILTer:DWIDth:SFACtor \n
		Snippet: driver.configure.afRf.measurement.audioInput.filterPy.dwidth.sfactor.set(factor = 1.0, audioInput = repcap.AudioInput.Default) \n
		Sets the distortion filter width factor for a user-defined distortion filter width. CONF:AFRF:MEAS:AIN1:FILT:DWID UDEF \n
			:param factor: Range: 0.001 to 0.005
			:param audioInput: optional repeated capability selector. Default value: Nr1 (settable in the interface 'AudioInput')
		"""
		param = Conversions.decimal_value_to_str(factor)
		audioInput_cmd_val = self._cmd_group.get_repcap_cmd_value(audioInput, repcap.AudioInput)
		self._core.io.write(f'CONFigure:AFRF:MEASurement<Instance>:AIN{audioInput_cmd_val}:FILTer:DWIDth:SFACtor {param}')

	def get(self, audioInput=repcap.AudioInput.Default) -> float:
		"""CONFigure:AFRF:MEASurement<Instance>:AIN<nr>:FILTer:DWIDth:SFACtor \n
		Snippet: value: float = driver.configure.afRf.measurement.audioInput.filterPy.dwidth.sfactor.get(audioInput = repcap.AudioInput.Default) \n
		Sets the distortion filter width factor for a user-defined distortion filter width. CONF:AFRF:MEAS:AIN1:FILT:DWID UDEF \n
			:param audioInput: optional repeated capability selector. Default value: Nr1 (settable in the interface 'AudioInput')
			:return: factor: Range: 0.001 to 0.005"""
		audioInput_cmd_val = self._cmd_group.get_repcap_cmd_value(audioInput, repcap.AudioInput)
		response = self._core.io.query_str(f'CONFigure:AFRF:MEASurement<Instance>:AIN{audioInput_cmd_val}:FILTer:DWIDth:SFACtor?')
		return Conversions.str_to_float(response)
