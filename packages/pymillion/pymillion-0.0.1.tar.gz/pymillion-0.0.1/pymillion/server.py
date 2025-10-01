from flask import Flask, request, render_template_string, jsonify
from .generator import generate_records
from .sender import send_batches
import threading, json, requests

app = Flask("million")

HTML_UI = """
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Million UI</title>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
<style>
body { background-color: #f8f9fa; color: #212529; }
.card { margin-top: 20px; padding: 20px; border-radius: 10px; box-shadow: 0 0 15px rgba(0,0,0,0.1); }
textarea { font-family: monospace; }
</style>
</head>
<body class="p-4">
<div class="container">
<h1 class="mb-4">Million UI</h1>

<div class="card">
<form method="POST">
<div class="mb-3">
<label class="form-label">URL</label>
<input class="form-control" name="url" required>
</div>
<div class="mb-3">
<label class="form-label">Método</label>
<select class="form-select" name="method" id="method-select">
<option>POST</option>
<option>PUT</option>
<option>GET</option>
</select>
</div>

<!-- Nav Tabs -->
<ul class="nav nav-tabs" id="modeTabs" role="tablist">
  <li class="nav-item" role="presentation">
    <button class="nav-link active" id="random-tab" data-bs-toggle="tab" data-bs-target="#random" type="button" role="tab">Random</button>
  </li>
  <li class="nav-item" role="presentation">
    <button class="nav-link" id="body-tab" data-bs-toggle="tab" data-bs-target="#body" type="button" role="tab">Body JSON</button>
  </li>
</ul>

<div class="tab-content mt-3">
  <!-- Random tab -->
  <div class="tab-pane fade show active" id="random" role="tabpanel">
    <div class="card mb-3" id="fields-card">
      <h5>Campos y tipos</h5>
      <div id="fields-container">
        <div class="input-group mb-2" id="field_group_0">
          <input type="text" class="form-control" name="field_name_0" placeholder="Nombre del campo" required>
          <select class="form-select" name="field_type_0">
            <option value="string">String</option>
            <option value="int">Int</option>
            <option value="float">Float</option>
            <option value="boolean">Boolean</option>
            <option value="date">Date</option>
            <option value="email">Email</option>
          </select>
          <button type="button" class="btn btn-danger" onclick="removeField(0)">Eliminar</button>
        </div>
      </div>
      <button type="button" class="btn btn-secondary mt-2" onclick="addField()">Agregar campo</button>
    </div>

    <div class="mb-3">
      <label class="form-label">Número de registros</label>
      <input class="form-control" name="number" type="number" value="1000" required>
    </div>

  </div>

  <!-- Body JSON tab -->
  <div class="tab-pane fade" id="body" role="tabpanel">
    <label class="form-label">JSON Body</label>
    <textarea class="form-control" name="json_body" rows="10" placeholder='{"key": "value"}'></textarea>
  </div>
</div>

<button class="btn btn-primary mt-3" type="submit">Enviar</button>
</form>
</div>

{% if response %}
<div class="card mt-4">
<h5>Respuesta</h5>
<textarea class="form-control" rows="10" readonly>{{ response }}</textarea>
</div>
{% endif %}

</div>

<script>
function addField() {
    const container = document.getElementById('fields-container');
    const index = container.children.length;
    container.insertAdjacentHTML('beforeend', `
    <div class="input-group mb-2" id="field_group_${index}">
        <input type="text" class="form-control" name="field_name_${index}" placeholder="Nombre del campo" required>
        <select class="form-select" name="field_type_${index}">
            <option value="string">String</option>
            <option value="int">Int</option>
            <option value="float">Float</option>
            <option value="boolean">Boolean</option>
            <option value="date">Date</option>
            <option value="email">Email</option>
        </select>
        <button type="button" class="btn btn-danger" onclick="removeField(${index})">Eliminar</button>
    </div>
    `);
}
function removeField(index) {
    const elem = document.getElementById('field_group_' + index);
    if(elem) elem.remove();
}
</script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
<footer class="text-center mt-4 p-3" style="background-color:#f1f1f1; position: fixed; bottom: 0; width: 100%;">
  <img src="{{ url_for('static', filename='gz.png') }}" alt="Logo" style="height:50px;">
</footer>
</html>
"""

@app.route("/", methods=["GET","POST"])
def index():
    response = None
    if request.method=="POST":
        url = request.form["url"]
        method = request.form["method"].upper()

        if method == "GET":
            try:
                r = requests.get(url)
                try:
                    response = json.dumps(r.json(), indent=2, ensure_ascii=False)
                except:
                    response = r.text
            except Exception as e:
                response = f"Error al realizar GET: {str(e)}"
        else:
            if "json_body" in request.form and request.form["json_body"].strip():
                try:
                    body = json.loads(request.form["json_body"])
                except:
                    body = {"error": "JSON inválido"}
                data_gen = [body]
            else:
                number = int(request.form["number"])
                country = request.form.get("country","")
                fields, types = [], []
                for key in request.form:
                    if key.startswith("field_name_"):
                        index = key.split("_")[-1]
                        fields.append(request.form[key])
                        types.append(request.form.get(f"field_type_{index}", "string"))
                data_gen = generate_records(fields, number, country, types)

            threading.Thread(target=send_batches, args=(url, method, data_gen)).start()
            response = json.dumps({"status":"Envio iniciado","method":method,"url":url}, indent=2)

    return render_template_string(HTML_UI, response=response)

def run_navigator():
    import webbrowser
    threading.Thread(target=lambda: webbrowser.open("http://127.0.0.1:5000")).start()
    app.run(port=5000)
