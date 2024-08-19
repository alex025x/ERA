import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from src.data_management import load_employee_data, load_pkl_file


def page_cluster_body():

    # Load cluster analysis files and pipeline
    version = 'v1'
    cluster_pipe = load_pkl_file(
        f"outputs/ml_pipeline/cluster_analysis/{version}/cluster_pipeline.pkl")
    cluster_silhouette = plt.imread(
        f"outputs/ml_pipeline/cluster_analysis/{version}/clusters_silhouette.png")
    features_to_cluster = plt.imread(
        f"outputs/ml_pipeline/cluster_analysis/{version}/features_define_cluster.png")
    cluster_profile = pd.read_csv(
        f"outputs/ml_pipeline/cluster_analysis/{version}/clusters_profile.csv")
    cluster_features = (pd.read_csv(f"outputs/ml_pipeline/cluster_analysis/{version}/TrainSet.csv")
                        .columns
                        .to_list()
                        )

    # Dataframe for cluster_distribution_per_variable()
    df_attrition_vs_clusters = load_employee_data().filter(['Attrition'], axis=1)
    df_attrition_vs_clusters['Clusters'] = cluster_pipe['model'].labels_

    st.write("### ML Pipeline: Cluster Analysis")
    # Display pipeline training summary conclusions
    st.info(
        f"* We refitted the cluster pipeline using fewer variables, and it delivered equivalent "
        f"performance to the pipeline fitted using all variables.\n"
        f"* The pipeline average silhouette score is 0.68"
    )
    st.write("---")

    st.write("#### Cluster ML Pipeline steps")
    st.write(cluster_pipe)

    st.write("#### The features the model was trained with")
    st.write(cluster_features)

    st.write("#### Clusters Silhouette Plot")
    st.image(cluster_silhouette)

    cluster_distribution_per_variable(df=df_attrition_vs_clusters, target='Attrition')

    st.write("#### Most important features to define a cluster")
    st.image(features_to_cluster)

    # Text based on the cluster analysis notebook conclusions
    st.write("#### Cluster Profile")
    statement = (
        f"* Historically, **employees in Cluster 0 do not tend to leave**, "
        f"whereas in **Cluster 1 a significant portion of employees left**, "
        f"and in **Cluster 2 a moderate portion of employees left**. \n"
        f"* From the Predict Attrition study, we noticed that Job Role and Monthly Income "
        f"are key predictor variables in determining whether an employee will leave or stay.\n"
        f"* **One potential action** when you detect that a given employee is expected to leave and "
        f"belongs to cluster 1 or 2 is to focus on improving job satisfaction or offering better incentives, "
        f"as learned from the attrition study."
    )
    st.info(statement)

    # Additional cluster profile interpretation
    statement = (
        f"* The cluster profile interpretation allowed us to label the clusters in the following way:\n"
        f"* Cluster 0 consists of employees with stable job roles and satisfaction.\n"
        f"* Cluster 1 includes employees with high workload and moderate satisfaction.\n"
        f"* Cluster 2 includes employees with lower income and lower satisfaction."
    )
    st.success(statement)

    # Hack to not display the index in st.table() or st.write()
    cluster_profile.index = [" "] * len(cluster_profile)
    st.table(cluster_profile)


# Function for visualizing cluster distribution per variable
def cluster_distribution_per_variable(df, target):

    df_bar_plot = df.value_counts(["Clusters", target]).reset_index()
    df_bar_plot.columns = ['Clusters', target, 'Count']
    df_bar_plot[target] = df_bar_plot[target].astype('object')

    st.write(f"#### Clusters distribution across {target} levels")
    fig = px.bar(df_bar_plot, x='Clusters', y='Count',
                 color=target, width=800, height=350)
    fig.update_layout(xaxis=dict(tickmode='array',
                      tickvals=df['Clusters'].unique()))
    st.plotly_chart(fig)

    df_relative = (df
                   .groupby(["Clusters", target])
                   .size()
                   .groupby(level=0)
                   .apply(lambda x:  100*x / x.sum())
                   .reset_index()
                   .sort_values(by=['Clusters'])
                   )
    df_relative.columns = ['Clusters', target, 'Relative Percentage (%)']

    st.write(f"#### Relative Percentage (%) of {target} in each cluster")
    fig = px.line(df_relative, x='Clusters', y='Relative Percentage (%)',
                  color=target, width=800, height=350)
    fig.update_layout(xaxis=dict(tickmode='array',
                      tickvals=df['Clusters'].unique()))
    fig.update_traces(mode='markers+lines')
    st.plotly_chart(fig)