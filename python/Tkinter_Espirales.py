import tkinter as tk
from tkinter import font
import math

# --- CONSTANTES Y CONFIGURACIÓN ---
ANCHO_CANVAS = 600
ALTO_CANVAS = 550
ANCHO_VENTANA = 600
ALTO_VENTANA = 720 # Aumentamos el alto para los controles
COLOR_FONDO = "black"
COLOR_PUNTO = "gold"
TAMANO_PUNTO = 2

# --- CREACIÓN DE LA VENTANA PRINCIPAL ---
ventana = tk.Tk()
ventana.title("Geometría Viva")
ventana.geometry(f"{ANCHO_VENTANA}x{ALTO_VENTANA}")
ventana.resizable(False, False) # Evita que se pueda cambiar el tamaño de la ventana

# --- FUNCIÓN PRINCIPAL PARA DIBUJAR ---
def actualizar_espiral():
    """
    Lee los valores de los inputs, calcula el ángulo y dibuja la espiral.
    (Versión corregida)
    """
    # 1. Limpiar el lienzo
    lienzo.delete("all")

    # 2. Obtener y validar valores
    try:
        num = int(entry_numerador.get())
        den = int(entry_denominador.get())

        if den == 0:
            label_angulo_resultado.config(text="Error: Denominador no puede ser 0")
            return

        angulo_objetivo = (num / den) * 360
        label_angulo_resultado.config(text=f"{angulo_objetivo:.2f}°")

    except ValueError:
        label_angulo_resultado.config(text="Error: Ingrese solo números enteros")
        return

    # 4. Dibujar la nueva espiral (LÓGICA CORREGIDA)
    centro_x = ANCHO_CANVAS / 2
    centro_y = ALTO_CANVAS / 2
    a = 0
    b = 4
    
    # Usaremos un bucle while para permitir incrementos decimales
    angulo_actual_grados = 0.0
    paso_angulo = 2.0  # Grados a incrementar en cada iteración. Un valor más pequeño = más suave.

    while angulo_actual_grados <= angulo_objetivo:
        angulo_rad = math.radians(angulo_actual_grados)
        radio = a + b * angulo_rad
        
        x = centro_x + radio * math.cos(angulo_rad)
        y = centro_y + radio * math.sin(angulo_rad)
        
        x1, y1 = (x - TAMANO_PUNTO), (y - TAMANO_PUNTO)
        x2, y2 = (x + TAMANO_PUNTO), (y + TAMANO_PUNTO)
        
        lienzo.create_oval(x1, y1, x2, y2, fill=COLOR_PUNTO, outline="")
        
        # Incrementar el ángulo para la siguiente iteración
        angulo_actual_grados += paso_angulo
        
    # --- Pequeña mejora: dibujar un punto final exactamente en el ángulo objetivo ---
    # Esto asegura que el final de la espiral siempre sea visible, incluso si el 'paso' se lo salta.
    if angulo_objetivo > 0:
        angulo_rad_final = math.radians(angulo_objetivo)
        radio_final = a + b * angulo_rad_final
        x_final = centro_x + radio_final * math.cos(angulo_rad_final)
        y_final = centro_y + radio_final * math.sin(angulo_rad_final)
        x1, y1 = (x_final - TAMANO_PUNTO), (y_final - TAMANO_PUNTO)
        x2, y2 = (x_final + TAMANO_PUNTO), (y_final + TAMANO_PUNTO)
        lienzo.create_oval(x1, y1, x2, y2, fill="red", outline="") # Punto final rojo para destacarlo


# --- CREACIÓN DE LA INTERFAZ GRÁFICA (WIDGETS) ---

# 1. Lienzo para dibujar la espiral
lienzo = tk.Canvas(ventana, width=ANCHO_CANVAS, height=ALTO_CANVAS, bg=COLOR_FONDO)
lienzo.pack(pady=10) # pack lo añade a la ventana con un poco de espacio vertical

# 2. Marco (Frame) para agrupar los controles
frame_controles = tk.Frame(ventana)
frame_controles.pack(padx=20, pady=5, fill=tk.X)

# Definir una fuente para las etiquetas
fuente_label = font.Font(family="Helvetica", size=10)
fuente_resultado = font.Font(family="Helvetica", size=12, weight="bold")

# 3. Widgets para el Numerador
label_numerador = tk.Label(frame_controles, text="Numerador:", font=fuente_label)
label_numerador.grid(row=0, column=0, sticky="w", padx=5) # sticky="w" alinea a la izquierda (West)

entry_numerador = tk.Entry(frame_controles, width=10, font=fuente_label)
entry_numerador.grid(row=0, column=1, pady=5)

# 4. Widgets para el Denominador
label_denominador = tk.Label(frame_controles, text="Denominador:", font=fuente_label)
label_denominador.grid(row=1, column=0, sticky="w", padx=5)

entry_denominador = tk.Entry(frame_controles, width=10, font=fuente_label)
entry_denominador.grid(row=1, column=1, pady=5)

# 5. Botón para dibujar
boton_dibujar = tk.Button(frame_controles, text="Dibujar Espiral", command=actualizar_espiral)
boton_dibujar.grid(row=0, column=2, rowspan=2, padx=20, ipady=5) # Ocupa 2 filas de alto

# 6. Etiqueta para mostrar el ángulo
label_angulo_info = tk.Label(frame_controles, text="Ángulo formado:", font=fuente_label)
label_angulo_info.grid(row=2, column=0, columnspan=2, pady=(10, 0), sticky="w")

label_angulo_resultado = tk.Label(frame_controles, text="0°", font=fuente_resultado, fg="blue")
label_angulo_resultado.grid(row=2, column=2, pady=(10, 0))

# 7. Botón para cerrar (en la parte inferior derecha)
# Usamos un frame separado para controlar su posición fácilmente
frame_cierre = tk.Frame(ventana)
frame_cierre.pack(fill=tk.X, side=tk.BOTTOM, padx=10, pady=10)

boton_cerrar = tk.Button(frame_cierre, text="Cerrar", command=ventana.quit)
boton_cerrar.pack(side=tk.RIGHT) # pack(side=RIGHT) lo empuja a la derecha de su contenedor

# --- INICIALIZACIÓN DE LA APLICACIÓN ---

# Poner valores iniciales para que el usuario vea un ejemplo al abrir
entry_numerador.insert(0, "1")
entry_denominador.insert(0, "4")
# Dibujar la espiral inicial
actualizar_espiral()

# Iniciar el bucle principal de la aplicación
ventana.mainloop()
