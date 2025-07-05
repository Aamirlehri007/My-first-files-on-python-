# steps involved in the data visualization
# step1-import libraries
import seaborn as sns
import matplotlib.pyplot as plt

# step2- set a theme
sns.set_theme(style= "ticks", color_codes=True)

# step3- import dataset
kashti= sns.load_dataset("titanic")
#print(kashti)

# step4- plot basic graph with 1 variable
#p1= sns.countplot(x="sex", data=kashti)
#plt.show()


# step5- plot basic graph with 2 variable
p1= sns.countplot(x="sex", hue="class", data=kashti)
p1.set_title("Plot for Count") 
plt.show()
