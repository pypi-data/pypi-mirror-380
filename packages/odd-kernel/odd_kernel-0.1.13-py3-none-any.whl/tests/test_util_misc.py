from odd_kernel.util.misc import ding
from odd_kernel.util.general import wait_some_time
from odd_kernel.util.charts import get_colors

wait_some_time(1, 5)

for i in range(3):
    ding(2000)

print(get_colors(100))