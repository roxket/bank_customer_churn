import matplotlib.pyplot as plt
import seaborn as sns

def plot_noise(df):
    fig = plt.figure(figsize = (30,10))
    viz_noise = df.drop('clientnum', axis=1).describe().transpose().reset_index()
    sns.barplot(data=viz_noise, x='index', y='std')
    plt.xlabel('Columns')
    plt.ylabel('Std.')
    plt.title('Viz of std')
    plt.xticks(rotation=45)
    plt.show()

def plot_outlayers(df):
    fig = plt.figure(figsize = (30,10))
    viz_outlayers = df.drop('clientnum', axis=1)
    sns.boxplot(data=viz_outlayers)
    plt.xlabel('Columns')
    plt.ylabel('Values')
    plt.title('Viz of IQR')
    plt.xticks(rotation=45)
    plt.show()

def plot_target_dist(df):
    sns.set(style = 'whitegrid')
    sns.set_context('paper', font_scale = 2)
    fig = plt.figure(figsize = (20, 10))
    plt.subplot(121)
    palette_color = sns.color_palette()[0:2]
    plt.pie(df.attrition_flag.value_counts(), labels = ['No Churn', 'Churn'], 
            autopct = '%.1f%%', 
            radius = 1, 
            textprops={'fontsize': 20, 'fontweight': 'bold'},
            colors=palette_color
            )
    plt.title('Churn Outcome Pie Chart', fontsize = 30, fontweight = 'bold')
    plt.subplot(122)

    order = df.attrition_flag.value_counts().sort_values(ascending=False).index
    t = sns.barplot(x=df.attrition_flag.value_counts().index, 
                    y=df.attrition_flag.value_counts().values, 
                    order=order)
    t.set_xlabel('Churn', fontweight = 'bold', fontsize = 20)
    t.set_ylabel('Count', fontweight = 'bold', fontsize = 20)
    plt.title('Churn Outcome Distributions', fontsize = 30, fontweight = 'bold')
    plt.tight_layout()

def plot_dis(df, feature):
    palette_color = reversed(sns.color_palette()[0:2])
    ax = sns.displot(data=df, 
                     x=feature, 
                     hue='attrition_flag', 
                     kde=True, 
                     bins=40, 
                     lw = 2, 
                     legend = True,
                     height=10, 
                     aspect=2,
                     palette=palette_color
                     ).set(title=f"KDE Plot: {feature}")
    ax.set_titles(f"Distribution Plot: {feature}", fontsize = 30, fontweight = 'bold')
    plt.xlabel(f"{feature}", fontsize = 20, fontweight = 'bold')
    plt.tight_layout()

def plot_cat_feature(df, feature):
    
    fig = plt.figure(figsize = (30,10))
    plt.subplot(131)
    plt.pie(df[feature].value_counts(), labels = df[feature].unique() , autopct = '%.1f%%', radius = 1, textprops = {'fontsize':20, 'fontweight':'bold'})
    plt.title(f"{feature} Composition of Overall Data", fontweight = 'bold', fontsize = 30)
        
    plt.subplot(132)
    palette_color = reversed(sns.color_palette()[0:2])
    g = df.copy()
    g = g.groupby(feature)['attrition_flag'].value_counts().to_frame()
    g = g.rename({'attrition_flag':'at_total'}, axis = 1).reset_index()
    t = sns.barplot(data = g, x = feature, y = 'at_total', hue = 'attrition_flag', palette=palette_color)
    t.set_title(f"Churn by {feature}", fontsize = 30, fontweight = 'bold')
    t.set_xlabel('')
    plt.xticks(rotation=45)
    t.set_ylabel('Num of Customers', fontsize = 20, fontweight = 'bold')
    t.set_xticklabels(labels = df[feature].unique(), fontweight = 'bold', fontsize = 20)
        
    plt.subplot(133)
    palette_color = reversed(sns.color_palette()[0:2])
    x = sns.violinplot(data = df, x = feature, y = 'total_trans_ct', hue = 'attrition_flag', split = True, palette=palette_color)
    x.set_title(f"Total Transactions by {feature}", fontsize = 30, fontweight = 'bold')
    x.set_xlabel(f"{feature}")
    plt.xticks(rotation=45)
    x.set_ylabel('Total Transactions', fontsize = 20, fontweight = 'bold')
    x.set_xticklabels(labels =df[feature].unique() , fontsize = 20, fontweight = 'bold')
        
    plt.tight_layout()