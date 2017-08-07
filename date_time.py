# -*- coding: utf-8 -*-

import datetime
from dateutil.relativedelta import relativedelta

# Obtener la fecha de hoy
date_now=datetime.date.today()
print(type(date_now))
print(date_now)


# Obtener la fecha junto con la hora de hoy
date_now=datetime.datetime.now()
print(type(date_now))
print(date_now)

# Obtener todas las funciones de: datetime.date
print(dir(datetime.date))

# Obtener todas las funciones de: datetime.datetime
print(dir(datetime.datetime))


hoy = datetime.date.today()
print("Día de la semana: {}".format(hoy.weekday()))
print("Día: {}".format(hoy.day))
print("Año: {}".format(hoy.year))
print("Mes: {}".format(hoy.month))

# Hacer uso de funciones de fecha relativa
# Obtener hoy en 6 meses:
print(hoy + relativedelta(months=+6))
# Obtener hoy en 60 dias:
print(hoy + relativedelta(days=+60))

# Sumar
six_months = datetime.date.today()+ relativedelta( months = +6)
print(six_months)



# Formatear Texto a Objeto fecha:
texto_fecha = 'March 7 2009 7:30pm EST'
texto_fecha = texto_fecha[:-3]
print(texto_fecha)
formatting = "%B %d %Y %I:%M%p "
fecha_formateada = datetime.datetime.strptime(texto_fecha, formatting)
print(fecha_formateada+ datetime.timedelta(hours=12))

# Fecha con isoformat
print(datetime.datetime.now().isoformat())

# Fecha formato UTC
print(datetime.datetime.utcnow())


# Formatear nueva Fecha
fecha_txt = '2017-07-25'
formatting_fecha = "%Y-%m-%d"
nueva_fecha=datetime.datetime.strptime(fecha_txt, formatting_fecha)
print('nueva fecha:')
print(nueva_fecha)



