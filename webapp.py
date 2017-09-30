from flask import Flask
from flask import render_template, flash, request, redirect
import os
from werkzeug.utils import secure_filename
import tempfile
from funding_earnings_stats import FundingEarningsCalculator

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ['csv']


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
        if not (allowed_file(file.filename)):
            flash("Unsupported filetype")
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            target_path = os.path.join(os.path.join(tempfile.gettempdir(), filename))
            file.save(target_path)
            calc = FundingEarningsCalculator(target_path)
            currency_stats_tables = []
            for currency, dataframe in calc.get_currency_stats().items():
                currency_stats_tables.append((
                    currency,
                    dataframe.to_html(classes=['table table-striped']).replace('border="1"', 'border="0"').replace(
                        'border="1"', 'border="0"')))
            monthly_earnings_table = calc.get_monthly_earnings().to_html(
                classes=['table table-striped']).replace('border="1"', 'border="0"')
            return render_template('show_stats.html', monthly_earnings=monthly_earnings_table,currency_stats=currency_stats_tables)
    return render_template('choose_file.html')
