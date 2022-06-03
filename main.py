from flask import Flask, render_template, request, redirect

app = Flask('app')

partidas = []

@app.route('/')
def index():
  return render_template(
    'index.html',
    partidas=partidas
  )
  
@app.route('/store', methods=['POST'])
def create():
  timeCASA = request.form.get('timeCASA')
  timeVISITANTE = request.form.get('timeVISITANTE')
  golsCasa = request.form.get('golsCasa')
  golsVISITANTE = request.form.get('golsVISITANTE')
  partidas.append({
    'timeCASA': timeCASA,
    'timeVISITANTE': timeVISITANTE,
    'golsCasa': golsCasa,
    'golsVISITANTE': golsVISITANTE
  })
  return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)