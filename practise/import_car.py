from car_class import Electric

new_car = Electric()
new_car.battery.describe_battery()

frozen_set = frozenset([1, 2, 3, 4, 5])
print(frozen_set)
# This will raise an AttributeError since frozen sets are immutable

