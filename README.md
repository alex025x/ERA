# Employee Retention Analyzer - A Predictive Classification Model for Employee Attrition

[Employee Retention Analyzer] is a machine-learning (ML) project that uses HR analytics data to predict the likelihood of employee attrition. The model achieves this through a classification task, using the 'left' attribute from the dataset as the target and employee characteristics as features. The project provides HR teams with actionable insights for improving retention strategies.

## Table of Contents
- [Dataset Content](#dataset-content)
- [Business Requirements](#business-requirements)
- [Hypothesis](#hypothesis-and-how-to-validate)
- [Mapping Business Requirements to Data Visualisation and ML Tasks](#the-rationale-to-map-the-business-requirements-to-the-data-visualizations-and-ml-tasks)
- [ML Business Case](#ml-business-case)
- [Epics and User Stories](#epics-and-user-stories)
- [Dashboard Design](#dashboard-design)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
- [Issues](#issues)
- [Unfixed Bugs](#unfixed-bugs)
- [Deployment](#deployment)
- [Credits](#credits)
- [Acknowledgements](#acknowledgements)

## Dataset Content
* The dataset is sourced from [XXXX]. Each row represents an employee and each column contains employee attributes. The dataset includes information about:
    - Employee satisfaction levels
    - Performance evaluation scores
    - Number of projects
    - Average monthly hours
    - Time at company
    - Work accidents
    - Promotions
    - Department and salary level
    - Whether they left the company

| Attribute | Information | Type/Units |
|-----------|-------------|------------|
| satisfaction_level | Employee's satisfaction rating | Float (0-1) |
| last_evaluation | Last performance evaluation score | Float (0-1) |
| number_project | Number of projects assigned | Integer |
| average_monthly_hours | Average monthly work hours | Integer |
| time_spend_company | Years at the company | Integer |
| Work_accident | Whether they had a work accident | Binary (0/1) |
| promotion_last_5years | Whether promoted in last 5 years | Binary (0/1) |
| Departments | Department employee works in | Categorical |
| salary | Salary level | Categorical (low/medium/high) |
| left | Whether the employee left | Binary (0/1) |

[Back to top](#table-of-contents)

## Business Requirements
* Employee turnover is a significant challenge for organizations, with replacement costs estimated at 1.5-2x the departing employee's salary. Early identification of attrition risks can enable proactive retention strategies.

* Business Requirement 1 - The client wants to identify which factors contribute most significantly to employee turnover, focusing on key predictors of departure.
* Business Requirement 2 - The client needs a tool to predict whether current employees are at risk of leaving based on their characteristics and behavior patterns.
* Business Requirement 3 - The client needs actionable insights and clear intervention triggers for HR to develop targeted retention strategies.

[Back to top](#table-of-contents)

## Hypothesis and how to validate?
* Hypothesis 1:
    - We suspect that satisfaction level and workload (project count/monthly hours) are the strongest predictors of turnover.
    - **Validation**: A correlation analysis that shows relationship strength between these features and the target 'left'.

* Hypothesis 2:
    - We suspect that employees with high workload and low satisfaction have the highest departure risk.
    - **Validation**: Analysis of feature importance and interaction effects through ML model evaluation.

* Hypothesis 3:
    - We suspect that employees in years 1-3 with low salaries have higher attrition rates.
    - **Validation**: Statistical analysis and visualization of departure rates across tenure and salary bands.

[Back to top](#table-of-contents)

## The rationale to map the business requirements to the Data Visualizations and ML tasks
* **Business Requirement 1**: Data Visualization and Correlation Study
    - We need to perform a correlation study to identify key attrition factors
    - Pearson correlation for linear relationships in numerical variables
    - Spearman correlation for monotonic relationships
    - PPS (Predictive Power Score) analysis for categorical variables
    - Feature importance analysis from ML model
    - This will be done in the Data Visualization and Preparation Epic

* **Business Requirement 2**: Classification Model
    - We need to predict binary outcome (stay/leave)
    - Build supervised classification model
    - Implement ML pipeline with preprocessing and prediction
    - Optimize hyperparameters for best performance
    - This will be executed in Model Training Epic

* **Business Requirement 3**: Actionable Insights
    - Identify critical thresholds for key metrics
    - Develop clear intervention triggers
    - Create visualization dashboard for HR
    - This spans both Analysis and Dashboard Development Epics

[Back to top](#table-of-contents)

## ML Business Case
* We want an ML model to predict whether an employee is likely to leave based on their current attributes and behavior patterns. The target variable 'left' is binary (0: stayed, 1: left).
* We will build a **classification model**, a supervised model with two-class, single-label output matching the target.
* The model success metrics are:
   - At least 95% F1 score on both train and test sets
   - High precision to minimize false alarms
   - High recall to catch actual flight risks
* The model will be considered a failure if:
   - The model fails to achieve 90% F1 score
   - False positive rate exceeds 15% (too many false alarms)
   - Features aren't interpretable for HR use
* The model output is defined as a flag indicating if an employee is likely to leave and the associated probability.
* The training data contains:
   - 4,998 employee records with 9 attributes + target
   - Mix of numerical and categorical features
   - Data from past employee records including both retained and departed staff

## Epics and User Stories
The project was split into 5 Epics based on Data Analysis and ML tasks, with user stories enabling agile methodology.

### Epic - Information Gathering and Data Collection
* **User Story** - As a data analyst, I can load employee data from local directories to begin analysis.
* **User Story** - As a data analyst, I can examine data quality to determine necessary preprocessing steps.

### Epic - Data Visualization, Cleaning, and Preparation
* **User Story** - As a data scientist, I can analyze correlations between features and attrition (**Business Requirement 1**).
* **User Story** - As a data analyst, I can handle missing values and outliers to prepare data for modeling.
* **User Story** - As a data analyst, I can check class balance in the target variable.
* **User Story** - As a data scientist, I can engineer features to improve model performance.
* **User Story** - As a data scientist, I can prepare features for ML pipeline implementation.

### Epic - Model Training, Optimization and Validation
* **User Story** - As a data scientist, I can split data appropriately for model training.
* **User Story** - As a data engineer, I can build ML pipeline with preprocessing steps.
* **User Story** - As a data engineer, I can select and optimize algorithms for prediction (**Business Requirement 2**).
* **User Story** - As a data scientist, I can tune hyperparameters for optimal performance.
* **User Story** - As a data scientist, I can validate model performance on test data.
* **User Story** - As a data scientist, I can analyze feature importance for insights (**Business Requirement 1**).

### Epic - Dashboard Planning, Designing, and Development
* **User Story** - As a user, I can view project overview and business requirements.
* **User Story** - As a user, I can see hypothesis validation results.
* **User Story** - As a user, I can input employee data for predictions (**Business Requirement 2**).
* **User Story** - As a technical user, I can examine correlation analysis (**Business Requirement 1**).
* **User Story** - As a technical user, I can review model performance metrics.
* **User Story** - As an HR user, I can get clear retention recommendations (**Business Requirement 3**).

### Epic - Dashboard Deployment and Release
* **User Story** - As a user, I can access the dashboard through a web interface.
* **User Story** - As a developer, I can deploy the project following documentation.

[Back to top](#table-of-contents)

## Dashboard Design
### Page 1: Project Summary
* **Section 1 - Summary**
   * Introduction to project goals
   * Dataset description and source
   * Link to readme
* **Section 2 - Business Requirements**
   * Business context
   * Specific requirements
   * Expected outcomes

### Page 2: Project Hypotheses
* Present the three project hypotheses
* Show validation results
* Visualize key findings

### Page 3: Correlation Study
* Address Business Requirement 1
* Show dataset overview
* Present correlation analysis
* Display PPS heatmap
* Feature distribution analysis
* Key conclusions

### Page 4: Attrition Prediction
* Address Business Requirement 2
* Input widgets for employee data
* Prediction interface
* Risk assessment display

### Page 5: Model Performance
* Performance metrics summary
* Pipeline description
* Feature importance analysis
* Train/test results documentation

[Back to top](#table-of-contents)

## ML Business Case
* We want an ML model to predict whether an employee is likely to leave based on their current attributes and behavior patterns. The target variable 'left' is binary (0: stayed, 1: left).
* We will build a **classification model**, a supervised model with two-class, single-label output matching the target.
* The model success metrics are:
   - At least 95% F1 score on both train and test sets
   - High precision to minimize false alarms
   - High recall to catch actual flight risks
* The model will be considered a failure if:
   - The model fails to achieve 90% F1 score
   - False positive rate exceeds 15% (too many false alarms)
   - Features aren't interpretable for HR use
* The model output is defined as a flag indicating if an employee is likely to leave and the associated probability.
* The training data contains:
   - 4,998 employee records with 9 attributes + target
   - Mix of numerical and categorical features
   - Data from past employee records including both retained and departed staff

## Epics and User Stories
The project was split into 5 Epics based on Data Analysis and ML tasks, with user stories enabling agile methodology.

### Epic - Information Gathering and Data Collection
* **User Story** - As a data analyst, I can load employee data from local directories to begin analysis.
* **User Story** - As a data analyst, I can examine data quality to determine necessary preprocessing steps.

### Epic - Data Visualization, Cleaning, and Preparation
* **User Story** - As a data scientist, I can analyze correlations between features and attrition (**Business Requirement 1**).
* **User Story** - As a data analyst, I can handle missing values and outliers to prepare data for modeling.
* **User Story** - As a data analyst, I can check class balance in the target variable.
* **User Story** - As a data scientist, I can engineer features to improve model performance.
* **User Story** - As a data scientist, I can prepare features for ML pipeline implementation.

### Epic - Model Training, Optimization and Validation
* **User Story** - As a data scientist, I can split data appropriately for model training.
* **User Story** - As a data engineer, I can build ML pipeline with preprocessing steps.
* **User Story** - As a data engineer, I can select and optimize algorithms for prediction (**Business Requirement 2**).
* **User Story** - As a data scientist, I can tune hyperparameters for optimal performance.
* **User Story** - As a data scientist, I can validate model performance on test data.
* **User Story** - As a data scientist, I can analyze feature importance for insights (**Business Requirement 1**).

### Epic - Dashboard Planning, Designing, and Development
* **User Story** - As a user, I can view project overview and business requirements.
* **User Story** - As a user, I can see hypothesis validation results.
* **User Story** - As a user, I can input employee data for predictions (**Business Requirement 2**).
* **User Story** - As a technical user, I can examine correlation analysis (**Business Requirement 1**).
* **User Story** - As a technical user, I can review model performance metrics.
* **User Story** - As an HR user, I can get clear retention recommendations (**Business Requirement 3**).

### Epic - Dashboard Deployment and Release
* **User Story** - As a user, I can access the dashboard through a web interface.
* **User Story** - As a developer, I can deploy the project following documentation.

[Back to top](#table-of-contents)

## Dashboard Design
### Page 1: Project Summary
* **Section 1 - Summary**
   * Introduction to project goals
   * Dataset description and source
   * Link to readme
* **Section 2 - Business Requirements**
   * Business context
   * Specific requirements
   * Expected outcomes

### Page 2: Project Hypotheses
* Present the three project hypotheses
* Show validation results
* Visualize key findings

### Page 3: Correlation Study
* Address Business Requirement 1
* Show dataset overview
* Present correlation analysis
* Display PPS heatmap
* Feature distribution analysis
* Key conclusions

### Page 4: Attrition Prediction
* Address Business Requirement 2
* Input widgets for employee data
* Prediction interface
* Risk assessment display

### Page 5: Model Performance
* Performance metrics summary
* Pipeline description
* Feature importance analysis
* Train/test results documentation

[Back to top](#table-of-contents)

[Previous sections above...]

## Technologies Used

The technologies used throughout the development are listed below:

### Languages
* [Python](https://www.python.org/)

### Python Packages
* [Pandas](https://pandas.pydata.org/docs/index.html) - Data manipulation and analysis
* [Numpy](https://numpy.org/doc/stable/index.html) - Numerical computing and array operations
* [Matplotlib](https://matplotlib.org/) - Data visualization and plotting
* [Seaborn](https://seaborn.pydata.org/) - Statistical data visualization
* [Scikit-learn](https://scikit-learn.org/stable/) - Machine learning algorithms and tools
* [Feature-engine](https://feature-engine.trainindata.com/en/latest/) - Feature engineering and selection
* [XGBoost](https://xgboost.readthedocs.io/en/stable/) - Gradient boosting framework
* [Streamlit](https://streamlit.io/) - Web application framework
* [Plotly](https://plotly.com/) - Interactive visualizations
* [ppscore](https://pypi.org/project/ppscore/) - Predictive power score calculations
* [Joblib](https://joblib.readthedocs.io/en/stable/) - Pipeline persistence

### Other Technologies
* [Git](https://git-scm.com/) - Version control
* [GitHub](https://github.com/) - Code repository and project management
* [VS Code](https://code.visualstudio.com/) - IDE for development
* [Heroku](https://heroku.com) - Application deployment platform

[Back to top](#table-of-contents)

## Testing

### Manual Testing

#### User Story Testing
* Dashboard was manually tested against user stories
* Each feature verified for functionality and usability

*As a non-technical user, I can view a project summary that describes the project, dataset and business requirements.*

| Feature | Action | Expected Result | Actual Result |
|---------|---------|-----------------|---------------|
| Project summary page | View landing page | Clear project overview displayed | Works as expected |
| Navigation | Click through sections | Smooth section transitions | Works as expected |
| Business requirements | View requirements section | Requirements clearly listed | Works as expected |

*As a technical user, I can access the correlation analysis and model performance metrics.*

| Feature | Action | Expected Result | Actual Result |
|---------|---------|-----------------|---------------|
| Correlation page | Navigate to analysis | Display correlation heatmaps | Works as expected |
| Feature importance | View importance plots | Show feature rankings | Works as expected |
| Performance metrics | Check model metrics | Display accuracy scores | Works as expected |

*As an HR user, I can input employee data and receive attrition predictions.*

| Feature | Action | Expected Result | Actual Result |
|---------|---------|-----------------|---------------|
| Prediction interface | Enter employee data | All inputs accept values | Works as expected |
| Run prediction | Click predict button | Show prediction result | Works as expected |
| Risk assessment | View prediction details | Display risk factors | Works as expected |

### Validation
* All Python code validated with PEP8
* Frontend validated for responsiveness
* Data pipeline tested for consistency

[Back to top](#table-of-contents)

## Issues
### Deployment Challenges
[Describe any significant issues encountered during development]
* Issue 1 description and resolution
* Issue 2 description and resolution

[Screenshot placeholder for any relevant issue documentation]

### Model Performance Optimization
[Describe any challenges in achieving desired model performance]
* Challenge 1 description and solution
* Challenge 2 description and solution

[Screenshot placeholder for performance metrics]

[Back to top](#table-of-contents)

## Unfixed Bugs
* No known bugs at time of deployment
* All identified issues have been resolved

[Back to top](#table-of-contents)

## Deployment
### Local Deployment
1. Clone the repository:
```bash
git clone [repository-url]
