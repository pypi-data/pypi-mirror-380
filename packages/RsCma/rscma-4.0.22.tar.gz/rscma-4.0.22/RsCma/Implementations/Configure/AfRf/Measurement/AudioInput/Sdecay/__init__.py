from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SdecayCls:
	"""Sdecay commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sdecay", core, parent)

	@property
	def enable(self):
		"""enable commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_enable'):
			from .Enable import EnableCls
			self._enable = EnableCls(self._core, self._cmd_group)
		return self._enable

	def set(self, slow_decay: enums.SlowDecay, audioInput=repcap.AudioInput.Default) -> None:
		"""CONFigure:AFRF:MEASurement<Instance>:AIN<nr>:SDECay \n
		Snippet: driver.configure.afRf.measurement.audioInput.sdecay.set(slow_decay = enums.SlowDecay.OFF, audioInput = repcap.AudioInput.Default) \n
		Requires 'Auto Range' > 'ON', see method RsCma.Configure.AfRf.Measurement.AudioInput.Aranging.set. Sets longer decay
		times of the auto ranging procedure implying longer decay times of a digital automatic gain control (AGC) . You can set
		multiples of the standard decay time of the digital AGC. \n
			:param slow_decay: OFF | X2 | X3 | X4 | X10 OFF Standard decay of the digital AGC. X2 | X3 | X4 | X10 Sets for longer decay times using multiples of standard decay time of the digital AGC.
			:param audioInput: optional repeated capability selector. Default value: Nr1 (settable in the interface 'AudioInput')
		"""
		param = Conversions.enum_scalar_to_str(slow_decay, enums.SlowDecay)
		audioInput_cmd_val = self._cmd_group.get_repcap_cmd_value(audioInput, repcap.AudioInput)
		self._core.io.write(f'CONFigure:AFRF:MEASurement<Instance>:AIN{audioInput_cmd_val}:SDECay {param}')

	# noinspection PyTypeChecker
	def get(self, audioInput=repcap.AudioInput.Default) -> enums.SlowDecay:
		"""CONFigure:AFRF:MEASurement<Instance>:AIN<nr>:SDECay \n
		Snippet: value: enums.SlowDecay = driver.configure.afRf.measurement.audioInput.sdecay.get(audioInput = repcap.AudioInput.Default) \n
		Requires 'Auto Range' > 'ON', see method RsCma.Configure.AfRf.Measurement.AudioInput.Aranging.set. Sets longer decay
		times of the auto ranging procedure implying longer decay times of a digital automatic gain control (AGC) . You can set
		multiples of the standard decay time of the digital AGC. \n
			:param audioInput: optional repeated capability selector. Default value: Nr1 (settable in the interface 'AudioInput')
			:return: slow_decay: OFF | X2 | X3 | X4 | X10 OFF Standard decay of the digital AGC. X2 | X3 | X4 | X10 Sets for longer decay times using multiples of standard decay time of the digital AGC."""
		audioInput_cmd_val = self._cmd_group.get_repcap_cmd_value(audioInput, repcap.AudioInput)
		response = self._core.io.query_str(f'CONFigure:AFRF:MEASurement<Instance>:AIN{audioInput_cmd_val}:SDECay?')
		return Conversions.str_to_scalar_enum(response, enums.SlowDecay)

	def clone(self) -> 'SdecayCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SdecayCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
