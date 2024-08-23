# Employee Retention Analyzer - Predictive Model for Employee Attrition

The Employee Retention Analyzer is a machine-learning (ML) project aimed at predicting whether an employee is at risk of leaving a company. Using a binary classification model, this project leverages a dataset to determine the factors that most contribute to employee attrition and to predict the likelihood of an employee leaving.

## Table of Contents

- [Dataset Content](#dataset-content)
- [Business Requirements](#business-requirements)
- [Hypothesis](#hypothesis-and-how-to-validate)
- [Mapping Business Requirements to Data Visualizations and ML Tasks](#mapping-business-requirements-to-data-visualizations-and-ml-tasks)
- [ML Business Case](#ml-business-case)
- [Epics and User Stories](#epics-and-user-stories)
- [Dashboard Design](#dashboard-design)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
- [Unfixed Bugs](#unfixed-bugs)
- [Deployment](#deployment)
- [Credits](#credits)
- [Acknowledgements](#acknowledgements)

## Dataset Content

The dataset is sourced from [Kaggle](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset) and contains records of employees from various departments. Each row represents an employee, and the columns provide various attributes related to demographics, job role, and satisfaction levels.

| Attribute                    | Information                                       | Units                    |
|------------------------------|---------------------------------------------------|--------------------------|
| Age                          | Age of the employee                               | years                    |
| BusinessTravel               | Frequency of travel                               | Travel_Rarely/Frequently |
| Department                   | Department of the employee                        | Sales/R&D/HR             |
| DistanceFromHome             | Distance from home to work                        | miles                    |
| Education                    | Level of education                                | 1-5                      |
| EnvironmentSatisfaction      | Work environment satisfaction                     | 1-4                      |
| JobRole                      | Role within the company                           | Job titles               |
| MonthlyIncome                | Monthly salary                                    | USD                      |
| YearsAtCompany               | Number of years with the company                  | years                    |
| Attrition                    | Target attribute (whether employee left the company) | Yes/No                   |

[Back to top](#table-of-contents)

## Business Requirements

Employee attrition is a critical issue for companies as it affects productivity and increases costs. A fictional HR department has requested a data practitioner to analyze employee data to determine the factors most associated with attrition and to predict the likelihood of an employee leaving.

* Business Requirement 1 - Identify the most influential factors that contribute to employee attrition.
* Business Requirement 2 - Develop a model to predict if an employee is at risk of leaving.

[Back to top](#table-of-contents)

## Hypothesis and how to validate?
* Hypothesis 1:
    - Employees with low job satisfaction and high distance from home are more likely to leave.
    - **Validation**: Correlation analysis to identify relationships between satisfaction levels, distance from home, and attrition.

* Hypothesis 2:
    - Employees who frequently travel for business are at a higher risk of leaving.
    - **Validation**: Correlation analysis and feature importance analysis in the ML model.

* Hypothesis 3:
    - Higher levels of education may correlate with lower attrition rates.
    - **Validation**: Analyzing attrition rates across different education levels using visualizations and ML models.

[Back to top](#table-of-contents)

## Mapping Business Requirements to Data Visualizations and ML Tasks

* **Business Requirement 1**: Data Visualization and Correlation Study
    - Perform correlation studies to identify key factors contributing to employee attrition.
    - Analyze relationships between job satisfaction, travel frequency, and attrition using Pearson and Spearman correlations.
    - Apply Predictive Power Score (PPS) to capture non-linear relationships.

* **Business Requirement 2**: Classification Model
    - Build a binary classification model to predict employee attrition.
    - Train the model on various features to assess their impact on prediction accuracy.
    - Optimize the model through hyperparameter tuning to achieve the best prediction performance.

[Back to top](#table-of-contents)

## ML Business Case

**Classification Model**
* The goal is to develop a predictive model to identify employees at risk of attrition using historical data.
* The target variable is 'Attrition', which indicates whether an employee has left the company.
* The model success metrics are:
    - At least 80% recall for predicting attrition on both training and test datasets.
    - At least 75% precision for predicting no attrition to minimize false positives.
* The model is trained on a dataset containing various attributes such as age, job role, department, and job satisfaction levels.

[Back to top](#table-of-contents)

## Epics and User Stories

### Epic - Data Collection and Preparation
* **User Story** - As a data analyst, I can download the dataset from Kaggle and load it into a DataFrame for analysis.
* **User Story** - As a data analyst, I can perform initial data cleaning to remove inconsistencies and prepare the dataset for modeling.

### Epic - Data Visualization and Correlation Study
* **User Story** - As a data scientist, I can visualize the relationship between various employee attributes and attrition to identify key factors.
* **User Story** - As a data analyst, I can calculate correlation coefficients to determine the strength of relationships between features and the target.

### Epic - Model Training, Optimization, and Validation
* **User Story** - As a data scientist, I can split the dataset into training and testing sets for model development.
* **User Story** - As a data engineer, I can build and optimize a classification model to predict employee attrition with high accuracy.
* **User Story** - As a data scientist, I can evaluate the model's performance and refine it to meet the specified success criteria.

### Epic - Dashboard Development and Deployment
* **User Story** - As a non-technical user, I can interact with a dashboard that predicts employee attrition based on input data.
* **User Story** - As a user, I can view the model's predictions and understand the key factors influencing attrition.

[Back to top](#table-of-contents)

## Dashboard Design

### Page 1: Project Overview
* **Section 1 - Introduction**
    * Overview of the project, objectives, and dataset description.
    * Links to relevant documentation and resources.
* **Section 2 - Business Requirements**
    * Detailed explanation of the business requirements and how the project aims to address them.

### Page 2: Data Exploration and Correlation Study
* Visual representation of the dataset's features and their relationship with attrition.
* Correlation heatmaps and PPS analysis to identify key factors influencing employee retention.

### Page 3: Attrition Prediction
* Interactive widgets for inputting employee data.
* Predictive model output indicating the risk of attrition for the given employee.

### Page 4: Model Performance
* Summary of the model's performance, including accuracy, recall, and precision metrics.
* Visualization of feature importance and how they contribute to the model's predictions.

[Back to top](#table-of-contents)

## Technologies Used

### Languages

* [Python](https://www.python.org/)

### Python Packages

* [Pandas](https://pandas.pydata.org/docs/) - Data manipulation and analysis.
* [NumPy](https://numpy.org/) - Support for large, multi-dimensional arrays and matrices.
* [Scikit-learn](https://scikit-learn.org/stable/) - Machine learning library for building models.
* [Matplotlib](https://matplotlib.org/) - Visualization library for creating static and interactive plots.
* [Seaborn](https://seaborn.pydata.org/) - Statistical data visualization.
* [Feature-engine](https://feature-engine.trainindata.com/en/latest/) - Tools for feature engineering and selection.
* [Joblib](https://joblib.readthedocs.io/en/stable/) - Pipeline processing and model persistence.

### Other Technologies

* [Streamlit](https://streamlit.io/) - Framework for building and deploying web apps.
* [Git](https://git-scm.com/) - Version control system.
* [GitHub](https://github.com/) - Hosting for software development and version control.
* [Heroku](https://www.heroku.com/) - Cloud platform for deploying apps.
* [VSCode](https://code.visualstudio.com/) - Integrated development environment.

[Back to top](#table-of-contents)

## Testing

### Manual Testing
#### User Story Testing
* Each dashboard page and feature was manually tested to ensure they function as expected based on the user stories.
* Input widgets were tested to ensure they accept and process user data correctly.

| Feature | Action | Expected Result | Actual Result |
|---------|--------|-----------------|---------------|
| Data Input | User inputs employee data | Data is accepted and processed | Functions as intended |
| Run Analysis | Click "Run Predictive Analysis" | Prediction is displayed on the page | Functions as intended |
| Visualization | Navigate through pages | All visualizations load correctly | Functions as intended |

### Validation
* Code was validated to conform to PEP8 standards.
* Manual checks were performed to ensure proper functionality across different parts of the app.

[Back to top](#table-of-contents)

## Unfixed Bugs
* No known bugs at the time of writing.

[Back to top](#table-of-contents)

## Deployment

### Heroku

* The App live link is: [Employee Retention Analyzer](#)


