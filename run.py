from flask import Flask, render_template, flash, redirect, url_for
from System.code import process
from forms import UserForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'e6b6d4067cecbf154d448a9616da183f'

@app.route('/', methods=['GET','POST'])
def home():
    form = UserForm()
    if form.validate_on_submit():
        movList = process(form.fav_movie_name.data)
        if not movList:
            flash('No related movies found!', 'danger')
        else:
            return render_template('displayList.html', movList=movList)
        return redirect(url_for('home'))
    return render_template('forms.html',  title='User_Input', form=form)

if __name__ == "__main__":
    app.run(debug=True)