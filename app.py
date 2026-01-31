import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Title
st.title("IPL Data Analysis")

# Load data
scorecard = pd.read_csv("matches.csv")

# Show data
st.subheader("Dataset Preview")
st.dataframe(scorecard.head())

# Plot 1
fig1 = plt.figure(figsize=(10,5))
sns.countplot(data=scorecard, x='toss_decision', palette='Dark2')
plt.title('Toss Decision Distribution')
plt.xlabel('Toss Decision')
plt.ylabel('Number of Matches')
st.pyplot(fig1)

# Plot 2
fig2 = plt.figure(figsize=(10,5))
sns.countplot(data=scorecard, x='dl_applied', palette='Dark2')
plt.title('D/L Method Applied')
plt.xlabel('D/L Applied')
plt.ylabel('Number of Matches')
st.pyplot(fig2)

# Plot 3
fig3 = plt.figure(figsize=(10,5))
sns.countplot(data=scorecard, x='winner', palette='Dark2')
plt.title('Matches Won by Each Team')
plt.xticks(rotation=45)
st.pyplot(fig3)

# Plot 4
fig4 = plt.figure(figsize=(10,5))
sns.countplot(data=scorecard, x='venue', palette='Dark2')
plt.title('Matches Played at Each Venue')
plt.xticks(rotation=45)
st.pyplot(fig4)

# Plot 5
fig5 = plt.figure(figsize=(10,5))
sns.countplot(data=scorecard, x='city', palette='Dark2')
plt.title('Matches Played in Each City')
plt.xticks(rotation=45)
st.pyplot(fig5)

# Plot 6
fig6 = plt.figure(figsize=(10,5))
sns.countplot(data=scorecard, x='result', palette='Dark2')
plt.title('Match Results Distribution')
plt.xlabel('Result')
plt.ylabel('Number of Matches')
st.pyplot(fig6)

# Plot 7
fig7 = plt.figure(figsize=(10,5))
sns.countplot(data=scorecard, x='toss_winner', palette='Dark2')
plt.title('Toss Winners Distribution')
plt.xlabel('Toss Winner')
plt.ylabel('Number of Matches')
st.pyplot(fig7)


# Additional value counts
st.subheader("Additional Value Counts")
st.write("Toss Winners:")
st.write(scorecard['toss_winner'].value_counts())
st.write("Match Results:")
st.write(scorecard['result'].value_counts())
st.write("Venues:")
st.write(scorecard['venue'].value_counts())
st.write("Cities:")
st.write(scorecard['city'].value_counts())
st.write("Toss Decisions:")
st.write(scorecard['toss_decision'].value_counts())
st.write("D/L Method Applied:")
st.write(scorecard['dl_applied'].value_counts())
st.write("Match Winners:")
st.write(scorecard['winner'].value_counts())
