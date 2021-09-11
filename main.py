from flask import Flask, render_template, request, url_for, redirect

import data_manager

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/mentors')
def mentors_list():
    mentor_name = request.args.get('mentor-last-name')
    city = request.args.get('city')
    if mentor_name:
        mentor_details = data_manager.get_mentors_by_last_name(mentor_name)
    elif city:
        mentor_details = data_manager.get_mentors_by_city(city)
    else:
        mentor_details = data_manager.get_mentors()
    return render_template('mentors.html', mentors=mentor_details)


@app.route("/applicants-phone")
def applicant_search():
    applicant_name = request.args.get('applicant_name')
    applicant_email = request.args.get('applicant_email')
    applicants_search = data_manager.applicant_search(applicant_name)
    applicant_search_by_email = data_manager.get_applicant_by_email(applicant_email)
    if applicant_name:
        return render_template("applicant_search_result.html", appl_s=applicants_search)
    elif applicant_email:
        return render_template("applicant_search_result.html", appl_s=applicant_search_by_email)


@app.route("/applicants")
def list_applicants():
    applicants_list = data_manager.read_all_applicant_info()
    return render_template("applicants_list.html", a_list=applicants_list)


@app.route("/applicants/<code>", methods=['GET', 'POST'])
def applicant_page(code):
    if request.method == 'GET':
        one_applicants_data = data_manager.read_one_applicants_data(code)
        return render_template("applicant_details.html", o_a_data=one_applicants_data, code=code)
    elif request.method == 'POST':
        updated_phone = request.form.get('update_phone')
        data_manager.update_applicant_info(updated_phone, code)
        return redirect(f"/applicants/{code}")


@app.route("/applicants/<code>/delete")
def delete_applicant(code):
    data_manager.delete_applicant(code)
    return redirect("/applicants")


@app.route("/delete-byemail", methods=['GET', 'POST'])
def delete_by_email():
    email = request.form.get('email_ending')
    data_manager.delete_applicant_by_email(email)
    return redirect("/applicants")


@app.route("/add-new-applicant", methods=['GET', 'POST'])
def add_new_applicant():
    if request.method == 'GET':
        return render_template("add_new_applicant.html")
    elif request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        phone_num = request.form.get('phone_number')
        email = request.form.get('email')
        application_code = request.form.get('application_code')
        a_data = [first_name, last_name, phone_num, email, application_code]
        data_manager.add_new_applicant(a_data)
        return redirect("/applicants")


if __name__ == '__main__':
    app.run(
        debug=True,
    )
