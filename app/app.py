import os
from flask import Flask, render_template_string, request

base_dir = os.path.dirname(os.path.abspath(__file__))
html_file_path = os.path.join(base_dir, 'index.html')

app = Flask(__name__)

@app.route('/')
def home():
    try:
        with open(html_file_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
        return render_template_string(html_content)
    except FileNotFoundError:
        return "<h1>Error: No se encuentra index.html en la carpeta principal.</h1>", 404

@app.route('/enviar', methods=['POST'])
def recibir_mensaje():
    tipo_usuario = request.form.get('tipo_usuario')
    usuario = request.form.get('nombre')
    identificacion = request.form.get('identificacion')
    ubicacion = request.form.get('ubicacion')
    urgencia = request.form.get('urgencia')
    texto_falla = request.form.get('falla')
    
    # Esto se imprimirá en los Logs de Render en tiempo real
    print("\n" + "╔" + "═"*45 + "╗")
    if tipo_usuario == 'Profesor':
        print(f"║ [SERVIDOR] ¡NUEVO REPORTE DE PROFESOR!      ║")
        print(f"╠" + "═"*45 + "╣")
        print(f"• Nombre del Profesor: {usuario}")
        print(f"• Número de Empleado:  {identificacion}")
    else:
        print(f"║ [SERVIDOR] ¡NUEVO REPORTE DE ALUMNO!        ║")
        print(f"╠" + "═"*45 + "╣")
        print(f"• Nombre del Alumno:   {usuario}")
        print(f"• Número de Boleta:    {identificacion}")
        
    print(f"• Ubicación:           {ubicacion}")
    print(f"• Urgencia:            {urgencia}")
    print(f"• Detalle de falla:    {texto_falla}")
    print("╚" + "═"*45 + "╝\n")
    
    return f"""
    <div style="font-family: Arial, sans-serif; text-align: center; margin-top: 50px;">
        <h1 style="color: #673ab7;">¡Muchas gracias, {usuario}!</h1>
        <p style="font-size: 18px;">Tu reporte como <strong>{tipo_usuario}</strong> ha sido recibido con éxito.</p>
        <a href="/" style="color: #512da8; text-decoration: none; font-weight: bold;">← Enviar otro reporte</a>
    </div>
    """

if __name__ == '__main__':
    # Configuración local de pruebas
    app.run(debug=True, port=8080)
