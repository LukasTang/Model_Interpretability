from plotnine import ggplot, aes, geom_bar, geom_histogram, theme_minimal, labs, theme, element_text
import pandas as pd
class FeaturePlot:
    def __init__(self, df):
        self.df = df

    def apply_base_theme(self, plot):
        return (
            plot +
            theme_minimal() +
            theme(axis_text_x=element_text(rotation=45, hjust=1))
        )

    def create_plot(self, x, fill, title,plot_type = 'bar'):
        plot = ggplot(self.df, aes(x=x, fill=fill))
        if plot_type == 'bar':
            plot += geom_bar(position='dodge')
        elif plot_type == 'histogram':
            plot += geom_histogram(position='dodge')
        else:
            raise ValueError(f"Unsupported plot type: {plot_type}")

        plot = self.apply_base_theme(plot)
        plot += labs(title=title, y='Count')
        return plot
    