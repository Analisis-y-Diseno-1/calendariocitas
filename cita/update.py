from cita.models import Cita
from datetime import date, timedelta
from django.core.mail import send_mail

def update_somthing():
    tomorrow = date.today() + timedelta(days=1)
    appointments = Cita.objects.filter(fecha_cita=tomorrow)

    for cita in appointments:
        if cita.paciente.correo.find('@'):
            body = """¡Hola! 
                Te recordamos que la cita en CLINICA es mañana {0} a las {1} horas 
                has indicado que el motivo de la cita es ***{2}***. 
                Recuerda ser puntual en tu cita para no tener
                    inconvenientes con las citas siguientes a la tuya. 
                ¡Esperamos verte pronto!""".format( 
                    cita.fecha_cita,
                    cita.hora_cita,
                    cita.comentario
                )
            
            send_mail("Cita agendada",body,
            'medsistemnotify@gmail.com',[cita.paciente.correo],fail_silently=True)
        else:
            print("No es un email valido")
    print("Tarea hola")
    
