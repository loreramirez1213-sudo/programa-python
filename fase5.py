def procesar_jornada_laboral(matriz_empleados):
    UMBRAL_HORAS = 40
    print("\n" + "="*65)
    print(f"{'RECURSO':<15} | {'HORAS TOTALES':<15} | {'CLASIFICACIÓN JORNADA'}")
    print("="*65)
    
    for empleado in matriz_empleados:
        nombre = empleado[0]
        horas_semanales = sum(empleado[1:])
        
        if horas_semanales > UMBRAL_HORAS:
            clasificacion = "⚠️ Sobretiempo"
        else:
            clasificacion = "✅ Horario Estándar"
            
        print(f"{nombre:<15} | {horas_semanales:<15.1f} | {clasificacion}")
    print("="*65 + "\n")

def main():
    horas_equipo = [
        ["Ana Gómez",    8.0, 8.5, 9.0, 8.0, 8.0],
        ["Carlos Ruiz",  8.0, 8.0, 8.0, 8.0, 8.0],
        ["María López",  6.0, 7.0, 8.0, 6.5, 7.0],
        ["Jorge Diaz",   9.0, 9.0, 8.5, 9.0, 9.5]
    ]
    print("Sistema de Control de Asistencia y Tiempos - Fase 5")
    procesar_jornada_laboral(horas_equipo)

if __name__ == "__main__":
    main()