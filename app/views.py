from flask import render_template
from flask.ext.appbuilder import BaseView, expose, has_access
from app import appbuilder,db
from .models import Terminal
from flask_appbuilder import ModelView
from flask_appbuilder.fieldwidgets import Select2Widget
from flask.ext.appbuilder.models.sqla.interface import SQLAInterface
from wtforms import Form, StringField
from wtforms.validators import DataRequired
from flask.ext.appbuilder.fieldwidgets import BS3TextFieldWidget , DatePickerWidget
from flask.ext.appbuilder.forms import DynamicForm
from wtforms import BooleanField, TextField, TextAreaField, PasswordField, validators, HiddenField, DateField, SelectField
from flask_appbuilder import SimpleFormView
from flask.ext.babelpkg import lazy_gettext as _



def department_query():
    return db.session.query(Terminal)



class DepartmentView(ModelView):
    datamodel = SQLAInterface(Terminal)
    list_columns = ['name', 'serialNo', 'simNo']




class MyForm(DynamicForm):
    field1 = StringField(('First Name'),
        description=('Your field number one!'),
        validators = [DataRequired()], widget=BS3TextFieldWidget())
    field2 = StringField(('Last Name'),
        description=('Your field number two!'), widget=BS3TextFieldWidget())
    field3 = DateField (('Date'), format='%m/%d/%Y' ,widget =DatePickerWidget() )

class MyFormView(SimpleFormView):
    form = MyForm
    form_title = 'This is my first form view'
    message = 'My form submitted'

    def form_get(self, form):
        form.field1 = 'This was prefilled'

    def form_post(self, form):
        # post process form
        flash(self.message, 'info')

appbuilder.add_view(MyFormView, "My form View", icon="fa-group", label=_('My form View'),
                     category="My Forms", category_icon="fa-cogs")

db.create_all()



#appbuilder.add_view(MyView(), "Method2", href='/myview/method2/jonh', category='My View')
# Use add link instead there is no need to create MyView twice.
appbuilder.add_link("View Terminals", href='/Terminals/View Terminals/jonh', category='Terminals')
#appbuilder.add_link("Method3", href='/Terminals/method3/jonh', category='Terminals')
appbuilder.add_view(DepartmentView, "Create Terminals", icon="fa-folder-open-o", category="Terminals")