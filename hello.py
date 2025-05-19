from preswald import get_df, connect, plotly
import plotly.express as px

connect()
df = get_df("ml_jobs_usa")

# Clean and drop missing values
df_cleaned = df[['job_title', 'company_address_locality']].dropna()
df_cleaned['job_title'] = df_cleaned['job_title'].str.strip()
df_cleaned['company_address_locality'] = df_cleaned['company_address_locality'].str.strip()

# Filter for one specific job title
focus_title = "Machine Learning Engineer"
single_title_df = df_cleaned[df_cleaned['job_title'] == focus_title]

# Group by city for that job title
fig = px.histogram(
    single_title_df,
    x="company_address_locality",
    title=f"'{focus_title}' Job Count by City",
    color="company_address_locality",
    height=600,
    width=1000
)

# Enhance plot appearance
fig.update_layout(
    xaxis_title="City",
    yaxis_title="Job Count",
    xaxis_tickangle=30,
    showlegend=False,
    font=dict(size=14),
    title_font_size=20
)

plotly(fig)