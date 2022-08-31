from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
import wtforms.validators
from flask_ckeditor import CKEditorField
from wtforms import validators

##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[wtforms.validators.DataRequired()])
    subtitle = StringField("Subtitle", validators=[wtforms.validators.DataRequired()])
    img_url = StringField("Blog Image URL", validators=[wtforms.validators.DataRequired(), wtforms.validators.URL()])
    body = CKEditorField("Blog Content", validators=[wtforms.validators.DataRequired()])
    submit = SubmitField("Submit Post")

class RegisterForm(FlaskForm):
    email = StringField(label='Email address', validators=[validators.DataRequired()])
    password = PasswordField(label='Password', validators=[validators.DataRequired()])
    name = StringField("Name", validators=[wtforms.validators.DataRequired()])
    submit = SubmitField("SIGN ME UP!")

class LoginForm(FlaskForm):
    email = StringField(label='Email address', validators=[validators.DataRequired()])
    password = PasswordField(label='Password', validators=[validators.DataRequired()])
    submit = SubmitField("SIGN IN")

class CommentForm(FlaskForm):
    comment = CKEditorField("Comment", validators=[wtforms.validators.DataRequired()])
    submit = SubmitField("SUBMIT COMMENT")