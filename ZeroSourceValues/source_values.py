from gpiozero import LED, Button
from gpiozero.tools import all_values, any_values, negated
from signal import pause

in_1 = Button(0)
in_2 = Button(1)

out_1 = LED(2)
out_2 = LED(3)
out_3 = LED(4)

out_1.source = all_values(in_1.values, in_2.values)
out_2.source = any_values(in_1.values, in_2.values)
out_3.source = negated(out_1.values)

pause()