#IMPORTS:
import logging


"""
Objetos:
Logger es un registrador:
"logger" -> Registrador

Handler es 

Existen niveles de log, por ejemplo:
NOTSET:  0  (No hay)
DEBUG:  10 -> debug
INFO:  20  -> info
WARNING:  30 -> warning
WARN:  30 -> warn ###### DEPRECATED usar WARNING ######
ERROR:  40 -> error
CRITICAL:  50 -> critical
FATAL:  50 -> fatal      ### FATAL == CRITICAL & fatal == critical ###
"""


# Print cada nivel (Es como un Enum):
print("NIVELES:"
    "\n  NOTSET: ", logging.NOTSET,
    "\n  DEBUG: ", logging.DEBUG, 
    "\n  INFO: ", logging.INFO,
    "\n  WARN: ", logging.WARN, 
    "\n  WARNING: ", logging.WARNING, 
    "\n  ERROR: ", logging.ERROR,
    "\n  CRITICAL: ", logging.CRITICAL,
    "\n  FATAL: ",logging.FATAL
    ) 


# NIVELES:

# Warning siempre salen al ejecutar 
# el programa por 1ª vez: 
logging.warning("root -> WARNING")

# Crear loggers
logger1 = logging.getLogger('viko')
logger2 = logging.getLogger("\v")

# Set levels
logger1.setLevel(logging.DEBUG) # Este nivel permanece
logger2.setLevel(logging.CRITICAL)
logger2.setLevel(logging.ERROR)
logger1.setLevel(20)

# Si el main se está ejecutando:
if __name__ == "__main__":
    logger1.info("logger 1 -> INFO")

logging.info("root -> INFO")
logger1.debug("Logger 1 DEBUG")
logger1.warning("Logger 1 WARNING")
logger2.critical("hola critical log 2")
logger2.error("logger 1 -> ERROR")
logger2.fatal("logger 2 -> FATAL")


# HANDLER:

# Crear Handler:
manejador = logging.Handler(level = 1)

# Cracterísticas Handler:
# Añadir nombre
manejador.name = "manejador"
print("Nombre del manejador:", manejador.get_name(), manejador.name)

filtro = filter(logging.warning("filtro warning"), range(0, 5))
manejador.addFilter(filtro)
#manejador.filter(record = True)
print("Filtros del manejador:", manejador.filters)

#Añadirlo:
logger2.addHandler(manejador)

logger2.warning("filtro warning")
logger2.warning("filtro2 warning")
logger2.debug("hgf")
#Extras:
#logging.LoggerAdapter()
logging.captureWarnings(True)