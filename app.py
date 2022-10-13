# from Calculator.infrastructure import userEmissionMixedWaste
# from Calculator.infrastructure import userEmissionEnergy
from flask import Flask, render_template, redirect, request

from flask_login import LoginManager, login_required, login_user, logout_user, current_user

from static.python.conn_functions import *
from static.python.classes import Accounts
from static.python.functions import *

from Calculator.infrastructure import *
from Calculator.food import *
from Calculator.transport import *

app = Flask(__name__)
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
    val1 = float(request.form.get('val1'))
    val2 = float(request.form.get('val2'))
    val3 = float(request.form.get('val3'))
    val4 = float(request.form.get('val4'))
    val5 = float(request.form.get('val5'))
    val6 = float(request.form.get('val6'))
    val7 = float(request.form.get('val7'))
    val8 = float(request.form.get('val8'))
    val9 = float(request.form.get('val9'))

    final = userEmissionEnergy(val1, val2, val3, val4, val5, val6)
    final += userEmissionMixedWaste(val7, val8, val9)

    update_infra(current_user.school_id, final)
    return redirect('/dashboard')


@app.route('/trans_form_handler', methods=['POST'])
def trans_form_handle():
    Passengers = float(request.form.get('Passengers'))
    FuelUsed = request.form.get('FuelUsed')
    ShortFlightsAnswer = float(request.form.get('ShortFlightsAnswer'))
    LongFlightsHomelandAnswer = float(request.form.get('LongFlightsHomelandAnswer'))
    LongFlightsAbroadAnswer = float(request.form.get('LongFlightsAbroadAnswer'))
    LongFlightsOver3700Answer = float(request.form.get('LongFlightsOver3700Answer'))
    ShortDistanceBus = float(request.form.get('ShortDistanceBus'))
    LongDistanceBus = float(request.form.get('LongDistanceBus'))
    LongDistanceTrain = float(request.form.get('LongDistanceTrain'))
    ShortDistanceTrain = float(request.form.get('ShortDistanceTrain'))
    MetroInput = float(request.form.get('MetroInput'))
    TramInput = float(request.form.get('TramInput'))
    TrainAbroadInput = float(request.form.get('TrainAbroadInput'))
    BusAbroadInput = float(request.form.get('BusAbroadInput'))
    UnknownFuelInput = float(request.form.get('UnknownFuelInput'))
    DieselInput = float(request.form.get('DieselInput'))
    PetrolInput = float(request.form.get('PetrolInput'))
    NaturalGasInput = float(request.form.get('NaturalGasInput'))
    BioGasInput = float(request.form.get('BioGasInput'))
    ElectricCarInput = float(request.form.get('ElectricCarInput'))
    HybridInput = float(request.form.get('HybridInput'))
    ChargingHybridInput = float(request.form.get('ChargingHybridInput'))
    RentalBusInput = float(request.form.get('RentalBusInput'))
    HotelStaysInput = float(request.form.get('HotelStaysInput'))
    TaxiInput = float(request.form.get('TaxiInput'))
    MopedInput = float(request.form.get('MopedInput'))
    MopedCarInput = float(request.form.get('MopedCarInput'))
    MotorcycleInput = float(request.form.get('MotorcycleInput'))
    ATVInput = float(request.form.get('ATVInput'))
    TractorInput = float(request.form.get('TractorInput'))
    SnowmobileInput = float(request.form.get('SnowmobileInput'))
    ElectricKickboardRentalInput = float(request.form.get('ElectricKickboardRentalInput'))
    ElectricBycycleInput = float(request.form.get('ElectricBycycleInput'))
    BycycleInput = float(request.form.get('BycycleInput'))
    KickboardInput = float(request.form.get('KickboardInput'))

    final = carEmissions(Passengers, FuelUsed)
    final = userEmissionsFlights(ShortFlightsAnswer, LongFlightsHomelandAnswer, LongFlightsAbroadAnswer, LongFlightsOver3700Answer)
    final = userEmissionsPublicTransport(ShortDistanceBus, LongDistanceBus, LongDistanceTrain, ShortDistanceTrain, MetroInput, TramInput)
    final = userEmissionsPublicTransportAbroad(TrainAbroadInput, BusAbroadInput)
    final = userEmissionsCarTraffic(UnknownFuelInput, DieselInput, PetrolInput, NaturalGasInput, BioGasInput, ElectricCarInput, HybridInput, ChargingHybridInput)
    final = userEmissionsBusinessAndClassTrips(RentalBusInput, HotelStaysInput, TaxiInput)
    final = userEmissionsOtherVehicles(MopedInput, MopedCarInput, MotorcycleInput, ATVInput, TractorInput, SnowmobileInput)
    final = otherEmissions(ElectricKickboardRentalInput, ElectricBycycleInput, BycycleInput, KickboardInput)

    update_infra(current_user.school_id, final)
    return redirect('/dashboard')



@app.route('/food_form_handler', methods=['POST'])
def food_form_handle():
    num_students = get_school_students(current_user.school_id)

    side_dish = mealSide(request.form.get('sides'))

    m1 = meatMealProtein(request.form.get('meatProtein'))
    m2 = mealEgg(request.form.get('meatEgg'))
    m3 = mealDairy(request.form.get('meatDairy'))

    ve1 = vegMealProtein(request.form.get('veggieProtein'))
    ve3 = mealEgg(request.form.get('veggieEgg'))
    ve4 = mealDairy(request.form.get('veggieDairy'))

    vg1 = vegMealProtein(request.form.get('veganProtein'))

    meat_meal = co2OfMeatMeal(num_students, m1, side_dish, m2, m3)
    veggie_meal = co2ofVeggieMeal(num_students, ve1, side_dish, ve3, ve4)
    vegan_meal = co2OfVeganMeal(num_students, side_dish, vg1)
    final = (meat_meal + veggie_meal + vegan_meal)/3

    update_food(current_user.school_id, final)
    return redirect('/dashboard')


@app.route('/')
def introduction():
    return render_template('introduction.html')


@app.route('/currentstate')
def currentstate():
    return render_template('currentstate.html')


@app.route('/create')
def generate_db():
    create_table()
    create_school('sup', 'hello', 222)
    create_school_account('name@test', 'hello', 'password', 'sup', 654)
    create_account('test@feu', 'user1', 'edu', 'Bassani', 1, 'pass')
    return 'created'


@app.route('/login')
def login():
    return render_template('loginPage.html')


@app.route('/food')
def food():
    return render_template('food.html')


@app.route('/attitude')
def attitude():
    return render_template('attitude.html')


@app.route('/motion')
def motion():
    return render_template('motion.html')


@app.route('/infrastructure')
def infrastructure():
    return render_template('infrastructure.html')


@app.route('/transport_form')
def transport_form():
    return render_template('transport_form.html')


@app.route('/login-authentication', methods=['POST'])
def verifies_login():
    username = request.form.get('username')
    password = request.form.get('password')
    try:
        user = finds_user(username, password)

        if len(user) != 1:
            return redirect('/login')
        user_id = int(user[0][0])

        login_user(load_user(user_id), remember=True)

        return redirect('/dashboard')
    except Exception:
        return redirect('/login')


@app.route('/register')
def register_page():
    return render_template('registrationPage.html', schools=get_schools())


@app.route('/register_school')
def school_register_page():
    return render_template('newSchool.html')


@app.route('/food_form')
def food_form():
    return render_template('food_form.html')


@app.route('/create_account', methods=['POST'])
def create_user_account():
    email = request.form.get('email')
    username = request.form.get('username')
    forename = request.form.get('forename')
    surname = request.form.get('surname')
    school_id = request.form.get('school')
    password = request.form.get('password')
    create_account(email, username, forename, surname, school_id, password)
    return verifies_login()


@app.route('/create_school_account', methods=['POST'])
def new_school():
    email = request.form.get('email')
    name = request.form.get('username')
    city = request.form.get('city')
    num_student = request.form.get('num_student')
    password = request.form.get('password')
    create_school_account(email, name, password, city, num_student)
    return verifies_login()


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
