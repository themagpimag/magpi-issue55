from gpiozero import LED, Button
from gpiozero.tools import all_values, any_values, negated
from signal import pause

in_1 = Button(23)
in_2 = Button(15)

out_1 = LED(24)
out_2 = LED(18)
out_3 = LED(14)

out_1.source = all_values(in_1.values, in_2.values)
out_2.source = any_values(in_1.values, in_2.values)
out_3.source = negated(out_1.values)

pause()
