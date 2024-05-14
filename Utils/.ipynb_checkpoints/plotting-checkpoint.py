import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.metrics import confusion_matrix

def plot_feature_importance(df, x, y, ax, threshold=0.002, pad=5.0, title='Feature Importance', xlabel='Features', ylabel='Importance', palette=None):
    if palette is None:
        palette = ["blue", "red"]
    blue,red = palette
    color = [red if value >= threshold else blue for value in df[y]]
    sns.barplot(x=x, y=y, data=df, ax=ax, alpha=0.5, palette=colors)
    ax.set_xticklabels(df[x], rotation=70, fontsize=12)
    ax.set_ylabel(ylabel, fontsize=15)
    ax.set_xlabel(xlabel, fontsize=15) 
    ax.grid(axis='y')
    ax.set_title(title, fontsize=15)
    plt.tight_layout(pad=pad)

def plot_confusion_matrix(Y_true, Y_pred, title, ax, xy_legends):
    cm = confusion_matrix(Y_true,Y_pred)
    cm_norm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]

    sns.heatmap(cm_norm,annot=True,fmt='.2%', cmap='coolwarm',
                xticklabels= xy_legends, yticklabels= xy_legends,
                alpha=0.5, cbar=False,)

    ax.set_title(title)
    ax.set_ylabel('True labels')
    ax.set_xlabel('Predicted labels')


