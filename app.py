from flask_bootstrap import Bootstrap
from flask import Flask, render_template

app = Flask(__name__)

bootstrap = Bootstrap(app)

# Homepage route
@app.route('/')
def index():
    return render_template('index.html')

# About page route
@app.route('/charter')
def about():
    return render_template('Project_charter.html')

# Services page route
@app.route('/services')
def services():
    return render_template('services.html')

# Contact page route
@app.route('/team_profile')
def contact():
    return render_template('team_profile.html')

# Charter page route
@app.route('/charter')
def charter():
    return render_template('charter.html')

# WBS page route
@app.route('/WBS')
def wbs():
    return render_template('WBS.html')

# GanttChart page route
@app.route('/GanttChart')
def ganttchart():
    return render_template('GanttChart.html')


# Cost Estimator page route
@app.route('/CostEstimator')
def costestimators():
    return render_template('CostEstimator.html')

# ProgressReport page route
@app.route('/ProgressReport')
def progressreport():
    return render_template('ProgressReport.html')

# StatusReport page route
@app.route('/StatusReport')
def statusreport():
    return render_template('StatusReport.html')

# RiskManagementPlan page route
@app.route('/RiskManagementPlan')
def riskmanagementplan():
    return render_template('RiskManagementPlan.html')

# AOA Diagrem page route
@app.route('/AOA')
def aoa():
    return render_template('AOA.html')

if __name__ == "__main__":
    app.run(debug=True)
# NEED TO CHANGE FILE NAMES STILL
