import pandas as pd

# Read the file
data_source = "https://raw.githubusercontent.com/HackBio-Internship/2025_project_collection/refs/heads/main/Python/Dataset/Pesticide_treatment_data.txt"
df = pd.read_csv(data_source, sep = "\t")
df = df.T
print(df)
print(df.info)
df.columns = df.iloc[0]  # Set first row as column names
df = df[1:].reset_index(drop=True)  # Remove the old header and reset index
#Calculate the difference in metabolic response (ΔM) between the DMSO treatment from the 24 hours treatment for the wild type and mutants
#For Wild Type
df["ΔM_Wild_Type"] = df["WT_pesticide_24h_1"] - df["WT_DMSO_1"]
df["ΔM_Mutant"] = df["mutant_pesticide_24h_1"] - df["mutant_DMSO_1"]
print(df[["ΔM_Wild_Type", "ΔM_Mutant"]])
print(df)

#To Generate a scatter plot showing the difference for ΔM for WT and Mutants
import seaborn as sns
import matplotlib.pyplot as plt
sns.scatterplot(df, x = "ΔM_Wild_Type", y = "ΔM_Mutant")
# Fit a line that satisfies a y-intercept of 0 and a slope of 1
plt.title("Scatter plot of ΔM for Wild Type and Mutants")
plt.xlabel("ΔM_Wild_Type")
plt.ylabel("ΔM_Mutant")
plt.plot(df["ΔM_Wild_Type"], df["ΔM_Wild_Type"], color='red', linestyle='--', label='y=x')
plt.legend()
plt.show()
'''
Using a residual cut off of your choice
(calculated a the difference between the fitted line and each point) calculate the residual of each point on the scatter plot
'''
# Calculate the residuals
df["residuals"] = df["ΔM_Mutant"] - df["ΔM_Wild_Type"]
print(df["residuals"])
plt.title("Scatter plot of ΔM for Wild Type and Mutants with Residuals")
plt.xlabel("ΔM_Wild_Type")
plt.ylabel("ΔM_Mutant")
plt.plot(df["ΔM_Wild_Type"], df["residuals"], color='green', linestyle='--', label='Residuals')
plt.show()
'''
Color metabolites that fall within +/- n of your residual grey.
For example, if you have a cut-off of 0.3, color residual values that are within -0.3 and +0.3 grey
'''
# Define the cut-off
cut_off = 0.3
# Color the residuals
df["color"] = df["residuals"].apply(lambda x: "grey" if -cut_off <= x <= cut_off else "black")
# Plot the scatter plot
sns.scatterplot(data=df, x="ΔM_Wild_Type", y="ΔM_Mutant", hue="color")
plt.plot(df["ΔM_Wild_Type"], df["ΔM_Wild_Type"], color='red', linestyle='--', label='y=x')

#Color metabolites that fall outside this range salmon.
df["color"] = df["residuals"].apply(lambda x: "salmon" if x < -cut_off or x > cut_off else "grey")
# Plot the scatter plot
sns.scatterplot(data=df, x="ΔM_Wild_Type", y="ΔM_Mutant", hue="color")
plt.plot(df["ΔM_Wild_Type"], df["ΔM_Wild_Type"], color='red', label='y=x')
plt.show()

#What are these metabolites. How do you explain the trends you see on either direction of the plot?
df["Metabolites"] = df.index
print(df)
#Pick any 6 metabolites that fall outside this range and generate a line plot that spans from their 0h treatment to their 8h and 24hr.
# Select 6 metabolites
metabolites = df[df["color"] == "salmon"].sample(6).index

# Plot the line plot
for metabolite in metabolites:
    plt.plot(["0h", "8h", "24h"], df.loc[metabolite, ["WT_DMSO_1", "WT_pesticide_8h_1", "WT_pesticide_24h_1"]], label=metabolite)
plt.legend()
plt.show()
#What can you say about the plots you see?
'''
The plots show the trend of the metabolites over time. Specifically:
1. The metabolites that fall outside the residual cut-off range (colored in salmon) exhibit significant changes in metabolic response compared to the wild type.
2. The line plots for these metabolites indicate how their metabolic response changes from 0h to 8h and 24h treatments.
3. Metabolites with a positive residual indicate a higher metabolic response in mutants compared to the wild type, while those with a negative residual indicate a lower response.
4. The trends observed can help identify which metabolites are most affected by the pesticide treatment and may provide insights into the underlying biological mechanisms.
'''
