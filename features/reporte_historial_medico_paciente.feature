Feature: Generacion de historial medico de pacientes

  Scenario: Se requiere crear un reporte del historial medico de un paciente 
     Given Es atendido un pacientes
      When Cuando se pulse el boton generar historial medico
      Then Se visualiza el pdf generado del reporte general