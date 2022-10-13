from flask import Flask, render_template, url_for

from static.python.functions import *
from static.python.conn_functions import *

app = Flask(__name__)
<<<<<<< Updated upstream
=======
app.config['SECRET_KEY'] = 'password'

login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.session_protection = "strong"


@login_manager.user_loader
def load_user(user_id):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute("SELECT * from accounts where id = (?)", (user_id,))
    info = cur.fetchone()
    if info is None:
        return None
    else:
        return Accounts(int(info[0]), info[1], info[2], info[3], info[4], info[5], info[6],
                        info[7], info[8], info[9], info[10], info[11])


@app.route('/dashboard')
@login_required
def index():  # put application's code here
    update_carbon()
    top3 = False
    topSchools = get_top_schools()[:3]
    currentSchool = ()
    currentSchoolAccount = ()

    for i in get_school_accounts():
        if i[5] == current_user.school_id:
            currentSchoolAccount = i

    for i in get_schools():
        if i[0] == current_user.school_id:
            currentSchool = i

    for i in topSchools:
        if i[0] == currentSchool[1]:
            top3 = True
            break

    if top3:
        return render_template('dashboard.html', schools=topSchools, school=currentSchool,
                               schoolAccount=currentSchoolAccount)

    topSchools.append(currentSchool)
    return render_template('dashboard.html', schools=topSchools, school=currentSchool,
                           schoolAccount=currentSchoolAccount)


@app.route('/infrastructure_form')
def infrastructure_form():
    return render_template('infrastructureform.html')


@app.route('/infrastructure_form_handler', methods=['POST'])
def infra_form_handle():
    avgCons= request.form.get('val1')

    update_infra(current_user.school_id, 55)
    return redirect('/dasboard')


@app.route('/trans_form_handler', methods=['POST'])
def trans_form_handle():
    float(request.form.get('Passengers'))
    request.form.get('FuelUsed')
    float(request.form.get('ShortFlightsAnswer'))
    float(request.form.get('LongFlightsHomelandAnswer'))
    float(request.form.get('LongFlightsAbroadAnswer'))
    float(request.form.get('LongFlightsOver3700Answer'))
    float(request.form.get('ShortDistanceBus'))
    float(request.form.get('LongDistanceBus'))
    float(request.form.get('LongDistanceTrain'))
    float(request.form.get('ShortDistanceTrain'))
    float(request.form.get('MetroInput'))
    float(request.form.get('TramInput'))
    float(request.form.get('TrainAbroadInput'))
    float(request.form.get('BusAbroadInput'))
    float(request.form.get('UnknownFuelInput'))
    float(request.form.get('DieselInput'))
    float(request.form.get('PetrolInput'))
    float(request.form.get('NaturalGasInput'))
    float(request.form.get('BioGasInput'))
    float(request.form.get('ElectricCarInput'))
    float(request.form.get('HybridInput'))
    float(request.form.get('ChargingHybridInput'))
    float(request.form.get('RentalBusInput'))
    float(request.form.get('HotelStaysInput'))
    float(request.form.get('TaxiInput'))
    float(request.form.get('MopedInput'))
    float(request.form.get('MopedCarInput'))
    float(request.form.get('MotorcycleInput'))
    float(request.form.get('ATVInput'))
    float(request.form.get('TractorInput'))
    float(request.form.get('SnowmobileInput'))
    float(request.form.get('ElectricKickboardRentalInput'))
    float(request.form.get('ElectricBycycleInput'))
    float(request.form.get('BycycleInput'))
    float(request.form.get('KickboardInput'))



    update_infra(current_user.school_id, 55)
    return redirect('/dasboard')




@app.route('/food_form_handler', methods=['POST'])
def food_form_handle():
    avgCons= request.form.get('val1')
    food()

    update_food(current_user.school_id, 55)
    return redirect('/dasboard')

>>>>>>> Stashed changes


@app.route('/')
def index():  # put application's code here
    return render_template('index.html')


@app.route('/create')
def generate_db():
    create_table()
    create_school('sup', 'hello', 222)
    create_school_account('name@test', 'hello', 2, 200, 'sup')
    return 'created'


if __name__ == '__main__':
    app.run(debug=True)
