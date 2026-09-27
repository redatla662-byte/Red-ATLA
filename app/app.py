import os
from flask import Flask, render_template_string, request

base_dir = os.path.dirname(os.path.abspath(__file__))
html_file_path = os.path.join(base_dir, 'index.html')

# Render busca obligatoriamente esta palabra 'app' exacta y en minúsculas
app = Flask(__name__)

@app.route('/')
def home():
    try:
        with open(html_file_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
        return render_template_string(html_content)
    except FileNotFoundError:
        return "<h1>Error: No se encuentra index.html en el servidor.</h1>", 404

@app.route('/enviar', methods=['POST'])
def recibir_mensaje():
    tipo_usuario = request.form.get('tipo_usuario')
    usuario = request.form.get('nombre')
    identificacion = request.form.get('identificacion')
    ubicacion = request.form.get('ubicacion')
    urgencia = request.form.get('urgencia')
    texto_falla = request.form.get('falla')
    
    print("\n" + "="*45)
    print(f"[SERVIDOR] ¡NUEVO REPORTE DE {str(tipo_usuario).upper()}!")
    print(f"• Nombre:        {usuario}")
    print(f"• Identificación:{identificacion}")
    print(f"• Ubicación:     {ubicacion}")
    print(f"• Urgencia:      {urgencia}")
    print(f"• Falla:         {texto_falla}")
    print("="*45 + "\n")
    
    return f"""
    <div style="font-family: Arial, sans-serif; text-align: center; margin-top: 50px;">
        <h1 style="color: #673ab7;">¡Muchas gracias, {usuario}!</h1>
        <p style="font-size: 18px;">Tu reporte como <strong>{tipo_usuario}</strong> ha sido recibido con éxito en el sistema.</p>
        <a href="/" style="color: #512da8; text-decoration: none; font-weight: bold;">← Enviar otro reporte</a>
    </div>
    """

if __name__ == '__main__':
    app.run(debug=True, port=8080)

