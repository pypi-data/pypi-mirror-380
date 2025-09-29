"""Interactive globe plots and 2D world maps using Plotly and Matplotlib."""

import pandas as pd
import numpy as np
from typing import Dict, List, Optional, Tuple, Union, Any
from .base import ColorScheme
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.colors import LinearSegmentedColormap

try:
    import plotly.graph_objects as go
    import plotly.express as px
    HAS_PLOTLY = True
    PlotlyFig = go.Figure
except ImportError:
    HAS_PLOTLY = False
    go = None
    px = None
    PlotlyFig = type('Figure', (), {})

# ISO country code mappings for better data compatibility
COUNTRY_MAPPINGS = {
    'USA': 'United States', 'US': 'United States',
    'UK': 'United Kingdom', 'GBR': 'United Kingdom', 'GB': 'United Kingdom',
    'DEU': 'Germany', 'DE': 'Germany',
    'CHN': 'China', 'CN': 'China',
    'JPN': 'Japan', 'JP': 'Japan',
    'FRA': 'France', 'FR': 'France',
    'BRA': 'Brazil', 'BR': 'Brazil',
    'IND': 'India', 'IN': 'India',
    'RUS': 'Russia', 'RU': 'Russia',
    'ZAF': 'South Africa', 'ZA': 'South Africa',
    'CAN': 'Canada', 'CA': 'Canada',
    'AUS': 'Australia', 'AU': 'Australia',
    'ITA': 'Italy', 'IT': 'Italy',
    'ESP': 'Spain', 'ES': 'Spain',
    'MEX': 'Mexico', 'MX': 'Mexico',
    'KOR': 'South Korea', 'KR': 'South Korea',
    'IDN': 'Indonesia', 'ID': 'Indonesia',
    'TUR': 'Turkey', 'TR': 'Turkey',
    'SAU': 'Saudi Arabia', 'SA': 'Saudi Arabia',
    'NLD': 'Netherlands', 'NL': 'Netherlands',
    'CHE': 'Switzerland', 'CH': 'Switzerland',
    'TWN': 'Taiwan', 'TW': 'Taiwan',
    'BEL': 'Belgium', 'BE': 'Belgium',
    'IRL': 'Ireland', 'IE': 'Ireland',
    'ARG': 'Argentina', 'AR': 'Argentina',
    'ISR': 'Israel', 'IL': 'Israel',
    'ARE': 'United Arab Emirates', 'AE': 'United Arab Emirates',
    'THA': 'Thailand', 'TH': 'Thailand',
    'POL': 'Poland', 'PL': 'Poland',
    'EGY': 'Egypt', 'EG': 'Egypt',
    'VNM': 'Vietnam', 'VN': 'Vietnam',
    'BGD': 'Bangladesh', 'BD': 'Bangladesh',
    'PHL': 'Philippines', 'PH': 'Philippines',
    'CHL': 'Chile', 'CL': 'Chile',
    'FIN': 'Finland', 'FI': 'Finland',
    'ROU': 'Romania', 'RO': 'Romania',
    'CZE': 'Czech Republic', 'CZ': 'Czech Republic',
    'NZL': 'New Zealand', 'NZ': 'New Zealand',
    'PRT': 'Portugal', 'PT': 'Portugal',
    'PER': 'Peru', 'PE': 'Peru',
    'GRC': 'Greece', 'GR': 'Greece',
    'IRQ': 'Iraq', 'IQ': 'Iraq',
    'DZA': 'Algeria', 'DZ': 'Algeria',
    'QAT': 'Qatar', 'QA': 'Qatar',
    'KAZ': 'Kazakhstan', 'KZ': 'Kazakhstan',
    'HUN': 'Hungary', 'HU': 'Hungary',
    'KWT': 'Kuwait', 'KW': 'Kuwait',
    'MAR': 'Morocco', 'MA': 'Morocco',
    'UKR': 'Ukraine', 'UA': 'Ukraine',
    'ECU': 'Ecuador', 'EC': 'Ecuador',
    'SVK': 'Slovakia', 'SK': 'Slovakia',
    'DOM': 'Dominican Republic', 'DO': 'Dominican Republic',
    'ETH': 'Ethiopia', 'ET': 'Ethiopia',
    'AUT': 'Austria', 'AT': 'Austria',
    'KEN': 'Kenya', 'KE': 'Kenya',
    'LKA': 'Sri Lanka', 'LK': 'Sri Lanka',
    'AGO': 'Angola', 'AO': 'Angola',
}


class GlobeRiskPlot:
    """Interactive globe for geographic risk data."""

    def __init__(self):
        if not HAS_PLOTLY:
            raise ImportError("Plotly required. Install with: pip install plotly")
        self.fig = None

    def plot(self, data, country='country', value='value',
             risk=None, title='Global Risk Distribution',
             color_scale='RdYlGn_r', **kwargs):
        """Create globe visualization."""
        required = [country, value]
        missing = [col for col in required if col not in data.columns]
        if missing:
            raise ValueError(f"Missing columns: {missing}")

        # Create choropleth map
        fig = go.Figure(data=go.Choropleth(
            locations=data[country],
            z=data[value],
            locationmode='ISO-3',
            colorscale=color_scale,
            autocolorscale=False,
            text=data[country],
            marker_line_color='darkgray',
            marker_line_width=0.5,
            colorbar_title=kwargs.get('colorbar_title', value.title()),
        ))

        # Update layout for globe projection
        fig.update_layout(
            title=dict(
                text=title,
                x=0.5,
                font=dict(size=16)
            ),
            geo=dict(
                showframe=False,
                showcoastlines=True,
                projection_type='orthographic',
                projection_rotation=dict(
                    lon=kwargs.get('center_lon', 0),
                    lat=kwargs.get('center_lat', 0)
                ),
                bgcolor='rgba(0,0,0,0)',
                showlakes=True,
                lakecolor='lightblue',
                showocean=True,
                oceancolor='lightblue'
            ),
            width=kwargs.get('width', 800),
            height=kwargs.get('height', 600),
            margin=dict(l=0, r=0, t=50, b=0)
        )

        self.fig = fig
        return fig

    def plot_connections(self, data, src_country='source_country',
                        tgt_country='target_country', strength='strength',
                        src_lat='source_lat', src_lon='source_lon',
                        tgt_lat='target_lat', tgt_lon='target_lon',
                        title='Global Risk Connections', **kwargs):
        """Create globe with connections between countries."""
        fig = go.Figure()

        # Add connection lines
        for _, row in data.iterrows():
            fig.add_trace(go.Scattergeo(
                lon=[row[src_lon], row[tgt_lon]],
                lat=[row[src_lat], row[tgt_lat]],
                mode='lines',
                line=dict(
                    width=max(1, row[strength] * 5),
                    color='red' if row[strength] > 0.7 else 'orange' if row[strength] > 0.4 else 'green'
                ),
                opacity=0.6,
                showlegend=False,
                hoverinfo='text',
                text=f"{row[src_country]} → {row[tgt_country]}<br>Strength: {row[strength]:.2f}"
            ))

        # Add source points
        source_points = data[[src_country, src_lat, src_lon, strength]].drop_duplicates()
        fig.add_trace(go.Scattergeo(
            lon=source_points[src_lon],
            lat=source_points[src_lat],
            text=source_points[src_country],
            mode='markers',
            marker=dict(size=8, color='blue', sizemode='diameter'),
            name='Source Countries'
        ))

        # Update layout
        fig.update_layout(
            title=dict(
                text=title,
                x=0.5,
                font=dict(size=16)
            ),
            geo=dict(
                projection_type='orthographic',
                showland=True,
                landcolor='lightgray',
                showocean=True,
                oceancolor='lightblue',
                showlakes=True,
                lakecolor='lightblue',
                showframe=False,
                showcoastlines=True
            ),
            width=kwargs.get('width', 800),
            height=kwargs.get('height', 600),
            margin=dict(l=0, r=0, t=50, b=0)
        )

        self.fig = fig
        return fig

    def plot_time_series(self, data: pd.DataFrame,
                        country_col: str = 'country',
                        value_col: str = 'value',
                        time_col: str = 'date',
                        title: str = 'Global Risk Over Time',
                        **kwargs):
        """
        Create an animated globe showing risk evolution over time.

        Parameters
        ----------
        data : pd.DataFrame
            DataFrame containing time series data
        country_col : str
            Column name for countries
        value_col : str
            Column name for values
        time_col : str
            Column name for time periods
        title : str
            Plot title
        **kwargs
            Additional plotting parameters

        Returns
        -------
        fig : plotly.graph_objects.Figure
            Plotly figure object with animation
        """
        # Create animated choropleth
        fig = px.choropleth(
            data,
            locations=country_col,
            color=value_col,
            animation_frame=time_col,
            color_continuous_scale='RdYlGn_r',
            title=title,
            **kwargs
        )

        # Update layout for globe
        fig.update_layout(
            geo=dict(
                projection_type='orthographic',
                showframe=False,
                showcoastlines=True,
                showlakes=True,
                lakecolor='lightblue',
                showocean=True,
                oceancolor='lightblue'
            ),
            width=kwargs.get('width', 800),
            height=kwargs.get('height', 600)
        )

        self.fig = fig
        return fig

    def add_markers(self, locations: pd.DataFrame,
                   lat_col: str = 'latitude',
                   lon_col: str = 'longitude',
                   text_col: str = 'text',
                   size_col: Optional[str] = None,
                   color_col: Optional[str] = None) -> None:
        """
        Add markers to existing globe plot.

        Parameters
        ----------
        locations : pd.DataFrame
            DataFrame with location data
        lat_col : str
            Column name for latitude
        lon_col : str
            Column name for longitude
        text_col : str
            Column name for marker text
        size_col : str, optional
            Column name for marker sizes
        color_col : str, optional
            Column name for marker colors
        """
        if self.fig is None:
            raise ValueError("No figure available. Call plot() first.")

        marker_config = dict(
            size=locations[size_col] * 10 if size_col else 8,
            color=locations[color_col] if color_col else 'red',
            sizemode='diameter'
        )

        self.fig.add_trace(go.Scattergeo(
            lon=locations[lon_col],
            lat=locations[lat_col],
            text=locations[text_col],
            mode='markers',
            marker=marker_config,
            showlegend=True,
            name='Risk Markers'
        ))

    def save_html(self, filename: str) -> None:
        """Save the interactive plot as HTML."""
        if self.fig is None:
            raise ValueError("No figure to save. Call plot() first.")
        self.fig.write_html(filename)

    def show(self) -> None:
        """Display the interactive plot."""
        if self.fig is None:
            raise ValueError("No figure to show. Call plot() first.")
        self.fig.show()


def country_risk_globe(data, country='country', risk='risk_score',
                      title='Global Country Risk Distribution', **kwargs):
    """Country risk globe."""
    globe_plot = GlobeRiskPlot()
    return globe_plot.plot(data, country=country, value=risk,
                          title=title, color_scale='RdYlGn_r', **kwargs)


def trade_flow_globe(data, source='source_country', target='target_country',
                    volume='trade_volume', title='Global Trade Flow Risks',
                    **kwargs):
    """Trade flow globe."""
    globe_plot = GlobeRiskPlot()

    # Aggregate trade volumes by country
    source_agg = data.groupby(source)[volume].sum().reset_index()
    source_agg.columns = ['country', 'total_volume']

    target_agg = data.groupby(target)[volume].sum().reset_index()
    target_agg.columns = ['country', 'total_volume']

    # Combine and aggregate
    combined = pd.concat([source_agg, target_agg]).groupby('country')['total_volume'].sum().reset_index()

    return globe_plot.plot(combined, country='country', value='total_volume',
                          title=title, colorbar_title='Trade Volume', **kwargs)


class WorldMapPlot:
    """Professional 2D world map choropleth visualization for country data."""

    def __init__(self, backend='plotly'):
        """
        Initialize WorldMapPlot.

        Parameters
        ----------
        backend : str, default 'plotly'
            Visualization backend: 'plotly' for interactive, 'matplotlib' for static
        """
        self.backend = backend
        self.fig = None

        if backend == 'plotly' and not HAS_PLOTLY:
            raise ImportError("Plotly required for interactive maps. Install with: pip install plotly")

    def _normalize_country_codes(self, data, country_col):
        """Normalize country codes to standard format."""
        data = data.copy()
        data[country_col] = data[country_col].map(COUNTRY_MAPPINGS).fillna(data[country_col])
        return data

    def plot_choropleth(self, data, country_col='country', value_col='value',
                       title='Country Risk Map', color_scale='RdYlGn_r',
                       show_borders=True, ocean_color='lightblue',
                       missing_color='lightgray', **kwargs):
        """
        Create a professional 2D choropleth world map.

        Parameters
        ----------
        data : pd.DataFrame
            DataFrame containing country and value data
        country_col : str, default 'country'
            Column name containing country codes/names
        value_col : str, default 'value'
            Column name containing values to visualize
        title : str, default 'Country Risk Map'
            Map title
        color_scale : str, default 'RdYlGn_r'
            Color scale for the visualization
        show_borders : bool, default True
            Whether to show country borders
        ocean_color : str, default 'lightblue'
            Color of ocean areas
        missing_color : str, default 'lightgray'
            Color for countries with missing data
        **kwargs
            Additional plotting parameters

        Returns
        -------
        fig : Figure
            Plotly or matplotlib figure object
        """
        # Normalize country codes
        data = self._normalize_country_codes(data, country_col)

        if self.backend == 'plotly':
            return self._plot_plotly_choropleth(
                data, country_col, value_col, title, color_scale,
                show_borders, ocean_color, missing_color, **kwargs
            )
        else:
            return self._plot_matplotlib_choropleth(
                data, country_col, value_col, title, color_scale,
                show_borders, ocean_color, missing_color, **kwargs
            )

    def _plot_plotly_choropleth(self, data, country_col, value_col, title,
                               color_scale, show_borders, ocean_color,
                               missing_color, **kwargs):
        """Create plotly choropleth map."""
        # Create choropleth
        fig = go.Figure(data=go.Choropleth(
            locations=data[country_col],
            z=data[value_col],
            locationmode='country names',
            colorscale=color_scale,
            autocolorscale=False,
            text=data[country_col] + '<br>' + data[value_col].astype(str),
            hovertemplate='<b>%{text}</b><br>Value: %{z}<extra></extra>',
            marker_line_color='white' if show_borders else 'rgba(0,0,0,0)',
            marker_line_width=0.8 if show_borders else 0,
            colorbar_title=kwargs.get('colorbar_title', value_col.replace('_', ' ').title()),
        ))

        # Update layout for professional flat map
        fig.update_layout(
            title=dict(
                text=title,
                x=0.5,
                font=dict(size=18, family='Arial, sans-serif'),
                pad=dict(t=20)
            ),
            geo=dict(
                showframe=False,
                showcoastlines=True,
                coastlinecolor='darkgray',
                showland=True,
                landcolor=missing_color,
                showocean=True,
                oceancolor=ocean_color,
                showlakes=True,
                lakecolor=ocean_color,
                showrivers=False,
                projection_type='natural earth',
                bgcolor='white'
            ),
            width=kwargs.get('width', 1000),
            height=kwargs.get('height', 600),
            margin=dict(l=0, r=0, t=60, b=0),
            font=dict(family='Arial, sans-serif')
        )

        self.fig = fig
        return fig

    def _plot_matplotlib_choropleth(self, data, country_col, value_col, title,
                                   color_scale, show_borders, ocean_color,
                                   missing_color, **kwargs):
        """Create matplotlib choropleth map (simplified version)."""
        # For matplotlib, we'll create a simple bar chart representation
        # A full choropleth would require additional geographical data

        fig, ax = plt.subplots(figsize=kwargs.get('figsize', (12, 8)))

        # Sort data by value for better visualization
        data_sorted = data.sort_values(value_col, ascending=True)

        # Create horizontal bar chart
        bars = ax.barh(range(len(data_sorted)), data_sorted[value_col],
                       color=plt.cm.RdYlGn_r(
                           (data_sorted[value_col] - data_sorted[value_col].min()) /
                           (data_sorted[value_col].max() - data_sorted[value_col].min())
                       ),
                       edgecolor='white' if show_borders else None,
                       linewidth=0.5)

        # Customize appearance
        ax.set_yticks(range(len(data_sorted)))
        ax.set_yticklabels(data_sorted[country_col])
        ax.set_xlabel(value_col.replace('_', ' ').title())
        ax.set_title(title, fontsize=16, fontweight='bold', pad=20)

        # Add value labels
        for i, (bar, value) in enumerate(zip(bars, data_sorted[value_col])):
            ax.text(bar.get_width() + (data_sorted[value_col].max() * 0.01),
                   bar.get_y() + bar.get_height()/2,
                   f'{value:.2f}',
                   va='center', ha='left', fontsize=10)

        # Style
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.grid(axis='x', alpha=0.3)
        plt.tight_layout()

        self.fig = fig
        return fig, ax

    def add_annotations(self, annotations_data, lat_col='latitude',
                       lon_col='longitude', text_col='text',
                       marker_size=8, marker_color='red'):
        """
        Add annotations/markers to the map.

        Parameters
        ----------
        annotations_data : pd.DataFrame
            DataFrame with annotation data
        lat_col : str, default 'latitude'
            Column name for latitude
        lon_col : str, default 'longitude'
            Column name for longitude
        text_col : str, default 'text'
            Column name for annotation text
        marker_size : int, default 8
            Size of markers
        marker_color : str, default 'red'
            Color of markers
        """
        if self.fig is None:
            raise ValueError("No map created. Call plot_choropleth() first.")

        if self.backend == 'plotly':
            self.fig.add_trace(go.Scattergeo(
                lon=annotations_data[lon_col],
                lat=annotations_data[lat_col],
                text=annotations_data[text_col],
                mode='markers+text',
                marker=dict(size=marker_size, color=marker_color),
                textposition="top center",
                name='Annotations'
            ))

    def save(self, filename, **kwargs):
        """Save the map to file."""
        if self.fig is None:
            raise ValueError("No map to save. Call plot_choropleth() first.")

        if self.backend == 'plotly':
            if filename.endswith('.html'):
                self.fig.write_html(filename, **kwargs)
            elif filename.endswith('.png'):
                self.fig.write_image(filename, **kwargs)
            else:
                self.fig.write_html(filename + '.html', **kwargs)
        else:
            self.fig.savefig(filename, dpi=300, bbox_inches='tight', **kwargs)

    def show(self):
        """Display the map."""
        if self.fig is None:
            raise ValueError("No map to show. Call plot_choropleth() first.")

        if self.backend == 'plotly':
            self.fig.show()
        else:
            plt.show()


def country_choropleth_map(data, country_col='country', value_col='value',
                          title='Country Risk Distribution', backend='plotly',
                          color_scale='RdYlGn_r', **kwargs):
    """
    Create a professional 2D choropleth world map for country data.

    This function provides an easy way to visualize country-level data on a
    traditional flat world map, which is often more readable than 3D globe
    visualizations for risk analysis and reporting.

    Parameters
    ----------
    data : pd.DataFrame
        DataFrame containing country and value data
    country_col : str, default 'country'
        Column name containing country codes or names
    value_col : str, default 'value'
        Column name containing values to visualize
    title : str, default 'Country Risk Distribution'
        Map title
    backend : str, default 'plotly'
        Visualization backend: 'plotly' for interactive, 'matplotlib' for static
    color_scale : str, default 'RdYlGn_r'
        Color scale (red-yellow-green reversed for risk data)
    **kwargs
        Additional plotting parameters

    Returns
    -------
    fig : Figure
        Plotly or matplotlib figure object

    Examples
    --------
    >>> import riskplot
    >>> import pandas as pd
    >>>
    >>> # Create sample country risk data
    >>> data = pd.DataFrame({
    ...     'country': ['USA', 'Germany', 'China', 'Japan'],
    ...     'risk_score': [0.25, 0.18, 0.45, 0.22]
    ... })
    >>>
    >>> # Create interactive map
    >>> fig = riskplot.country_choropleth_map(
    ...     data, 'country', 'risk_score',
    ...     title='Global Country Risk Assessment'
    ... )
    >>> fig.show()
    """
    world_map = WorldMapPlot(backend=backend)
    return world_map.plot_choropleth(
        data, country_col, value_col, title, color_scale, **kwargs
    )


def regional_risk_heatmap(data, region_col='region', country_col='country',
                         value_col='value', title='Regional Risk Heatmap',
                         figsize=(12, 8)):
    """
    Create a regional risk heatmap showing countries grouped by region.

    Parameters
    ----------
    data : pd.DataFrame
        DataFrame with region, country, and value data
    region_col : str, default 'region'
        Column name for regions
    country_col : str, default 'country'
        Column name for countries
    value_col : str, default 'value'
        Column name for values
    title : str, default 'Regional Risk Heatmap'
        Plot title
    figsize : tuple, default (12, 8)
        Figure size

    Returns
    -------
    fig, ax : tuple
        Matplotlib figure and axis objects
    """
    fig, ax = plt.subplots(figsize=figsize)

    # Pivot data for heatmap
    pivot_data = data.pivot_table(
        index=region_col, columns=country_col, values=value_col, fill_value=0
    )

    # Create heatmap
    im = ax.imshow(pivot_data.values, cmap='RdYlGn_r', aspect='auto')

    # Set ticks and labels
    ax.set_xticks(range(len(pivot_data.columns)))
    ax.set_xticklabels(pivot_data.columns, rotation=45, ha='right')
    ax.set_yticks(range(len(pivot_data.index)))
    ax.set_yticklabels(pivot_data.index)

    # Add colorbar
    cbar = plt.colorbar(im, ax=ax)
    cbar.set_label(value_col.replace('_', ' ').title())

    # Add title and labels
    ax.set_title(title, fontsize=16, fontweight='bold', pad=20)
    ax.set_xlabel('Countries')
    ax.set_ylabel('Regions')

    # Add value annotations
    for i in range(len(pivot_data.index)):
        for j in range(len(pivot_data.columns)):
            value = pivot_data.iloc[i, j]
            if value != 0:
                ax.text(j, i, f'{value:.2f}', ha='center', va='center',
                       color='white' if value > pivot_data.values.mean() else 'black',
                       fontweight='bold')

    plt.tight_layout()
    return fig, ax