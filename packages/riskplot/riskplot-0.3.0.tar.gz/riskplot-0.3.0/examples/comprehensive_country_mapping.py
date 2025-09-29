#!/usr/bin/env python3
"""
Comprehensive Country Mapping Example - 2D and 3D Geographic Visualizations

This example demonstrates the full range of country plotting capabilities in RiskPlot,
including both traditional 2D flat world maps and interactive 3D globe visualizations.
Perfect for risk analysis, economic data visualization, and geopolitical assessments.
"""

import pandas as pd
import numpy as np
import riskplot
import matplotlib.pyplot as plt


def generate_comprehensive_country_data():
    """Generate realistic sample country data for demonstration."""

    # Major economies with realistic risk metrics
    countries_data = {
        'Country': [
            'United States', 'China', 'Japan', 'Germany', 'United Kingdom',
            'France', 'India', 'Italy', 'Brazil', 'Canada',
            'Russia', 'South Korea', 'Australia', 'Mexico', 'Spain',
            'Indonesia', 'Netherlands', 'Saudi Arabia', 'Turkey', 'Taiwan',
            'Switzerland', 'Belgium', 'Ireland', 'Israel', 'Argentina',
            'Thailand', 'Nigeria', 'Egypt', 'Philippines', 'South Africa',
            'Bangladesh', 'Vietnam', 'Chile', 'Finland', 'Malaysia',
            'Norway', 'New Zealand', 'Singapore', 'Portugal', 'Peru'
        ],
        'ISO_Code': [
            'USA', 'CHN', 'JPN', 'DEU', 'GBR',
            'FRA', 'IND', 'ITA', 'BRA', 'CAN',
            'RUS', 'KOR', 'AUS', 'MEX', 'ESP',
            'IDN', 'NLD', 'SAU', 'TUR', 'TWN',
            'CHE', 'BEL', 'IRL', 'ISR', 'ARG',
            'THA', 'NGA', 'EGY', 'PHL', 'ZAF',
            'BGD', 'VNM', 'CHL', 'FIN', 'MYS',
            'NOR', 'NZL', 'SGP', 'PRT', 'PER'
        ],
        'Region': [
            'North America', 'Asia Pacific', 'Asia Pacific', 'Europe', 'Europe',
            'Europe', 'Asia Pacific', 'Europe', 'Latin America', 'North America',
            'Europe', 'Asia Pacific', 'Asia Pacific', 'Latin America', 'Europe',
            'Asia Pacific', 'Europe', 'Middle East', 'Europe', 'Asia Pacific',
            'Europe', 'Europe', 'Europe', 'Middle East', 'Latin America',
            'Asia Pacific', 'Africa', 'Africa', 'Asia Pacific', 'Africa',
            'Asia Pacific', 'Asia Pacific', 'Latin America', 'Europe', 'Asia Pacific',
            'Europe', 'Asia Pacific', 'Asia Pacific', 'Europe', 'Latin America'
        ]
    }

    df = pd.DataFrame(countries_data)

    # Generate realistic risk metrics
    np.random.seed(42)  # For reproducible results

    # Political risk (0-100, higher = riskier)
    df['Political_Risk'] = np.random.beta(2, 5, len(df)) * 100

    # Economic risk (0-100, higher = riskier)
    df['Economic_Risk'] = np.random.beta(2.5, 4, len(df)) * 100

    # Credit rating (AAA=1, AA=2, A=3, BBB=4, BB=5, B=6, CCC=7)
    df['Credit_Rating_Score'] = np.random.randint(1, 8, len(df))

    # GDP Growth Rate (-5% to 10%)
    df['GDP_Growth'] = np.random.normal(2.5, 2.5, len(df))

    # Composite Risk Score (weighted average)
    df['Composite_Risk'] = (
        0.4 * df['Political_Risk'] +
        0.4 * df['Economic_Risk'] +
        0.2 * (df['Credit_Rating_Score'] - 1) * 16.67  # Normalize to 0-100
    )

    # ESG Score (0-100, higher = better)
    df['ESG_Score'] = 100 - (df['Composite_Risk'] * 0.7 + np.random.normal(0, 10, len(df)))
    df['ESG_Score'] = np.clip(df['ESG_Score'], 0, 100)

    return df


def demonstrate_2d_world_maps(data):
    """Demonstrate 2D flat world map capabilities."""
    print("\n" + "="*60)
    print("2D WORLD MAP DEMONSTRATIONS")
    print("="*60)

    # 1. Basic 2D Choropleth Map
    print("\n1. Creating basic 2D choropleth world map...")
    try:
        fig = riskplot.country_choropleth_map(
            data,
            country_col='Country',
            value_col='Composite_Risk',
            title='Global Risk Assessment - 2D World Map',
            color_scale='RdYlGn_r',  # Red-Yellow-Green reversed (red = high risk)
            width=1200,
            height=700
        )

        # Save both HTML and PNG
        if hasattr(fig, 'write_html'):
            fig.write_html('world_map_2d_risk.html')
            print("   ✓ Saved interactive map as 'world_map_2d_risk.html'")

        fig.show()
        print("   ✓ Basic 2D world map created successfully")

    except Exception as e:
        print(f"   ✗ Error creating 2D map: {e}")

    # 2. ESG Score Visualization
    print("\n2. Creating ESG score visualization...")
    try:
        fig = riskplot.country_choropleth_map(
            data,
            country_col='Country',
            value_col='ESG_Score',
            title='Global ESG Performance Assessment',
            color_scale='RdYlGn',  # Regular scale (green = high ESG)
            colorbar_title='ESG Score (0-100)',
            width=1200,
            height=700
        )

        if hasattr(fig, 'write_html'):
            fig.write_html('world_map_esg_scores.html')
            print("   ✓ Saved ESG map as 'world_map_esg_scores.html'")

        fig.show()
        print("   ✓ ESG score map created successfully")

    except Exception as e:
        print(f"   ✗ Error creating ESG map: {e}")

    # 3. Regional Risk Heatmap
    print("\n3. Creating regional risk heatmap...")
    try:
        # Prepare data for regional analysis
        regional_data = data[['Region', 'Country', 'Composite_Risk']].copy()

        fig, ax = riskplot.regional_risk_heatmap(
            regional_data,
            region_col='Region',
            country_col='Country',
            value_col='Composite_Risk',
            title='Risk Assessment by Region and Country',
            figsize=(14, 8)
        )

        plt.savefig('regional_risk_heatmap.png', dpi=300, bbox_inches='tight')
        plt.show()
        print("   ✓ Regional heatmap created and saved as 'regional_risk_heatmap.png'")

    except Exception as e:
        print(f"   ✗ Error creating regional heatmap: {e}")


def demonstrate_3d_globe_maps(data):
    """Demonstrate 3D globe visualization capabilities."""
    print("\n" + "="*60)
    print("3D GLOBE DEMONSTRATIONS")
    print("="*60)

    # 1. Interactive 3D Globe
    print("\n1. Creating interactive 3D globe...")
    try:
        fig = riskplot.country_risk_globe(
            data,
            country='ISO_Code',
            risk='Composite_Risk',
            title='Global Risk Assessment - 3D Globe View',
            center_lon=0,
            center_lat=30,
            width=800,
            height=600
        )

        if hasattr(fig, 'write_html'):
            fig.write_html('globe_3d_risk.html')
            print("   ✓ Saved 3D globe as 'globe_3d_risk.html'")

        fig.show()
        print("   ✓ 3D globe visualization created successfully")

    except Exception as e:
        print(f"   ✗ Error creating 3D globe: {e}")


def demonstrate_advanced_features(data):
    """Demonstrate advanced country mapping features."""
    print("\n" + "="*60)
    print("ADVANCED FEATURES DEMONSTRATION")
    print("="*60)

    # 1. Multiple Risk Dimensions
    print("\n1. Creating multi-dimensional risk analysis...")

    # Create subplots for different risk types
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    fig.suptitle('Multi-Dimensional Country Risk Analysis', fontsize=16, fontweight='bold')

    risk_types = ['Political_Risk', 'Economic_Risk', 'Credit_Rating_Score', 'GDP_Growth']
    titles = ['Political Risk', 'Economic Risk', 'Credit Rating Risk', 'GDP Growth Rate']

    for i, (risk_type, title) in enumerate(zip(risk_types, titles)):
        ax = axes[i//2, i%2]

        # Sort data for better visualization
        data_sorted = data.sort_values(risk_type, ascending=True)

        # Color mapping
        if risk_type == 'GDP_Growth':
            # For GDP growth, green = positive, red = negative
            colors = ['red' if x < 0 else 'orange' if x < 2 else 'green' for x in data_sorted[risk_type]]
        else:
            # For risk metrics, green = low risk, red = high risk
            colors = plt.cm.RdYlGn_r((data_sorted[risk_type] - data_sorted[risk_type].min()) /
                                   (data_sorted[risk_type].max() - data_sorted[risk_type].min()))

        bars = ax.barh(range(len(data_sorted)), data_sorted[risk_type],
                      color=colors, alpha=0.8, edgecolor='white', linewidth=0.5)

        # Customize
        ax.set_yticks(range(0, len(data_sorted), 5))  # Show every 5th country
        ax.set_yticklabels(data_sorted['Country'].iloc[::5], fontsize=8)
        ax.set_xlabel(f'{title} Score')
        ax.set_title(title, fontweight='bold')
        ax.grid(axis='x', alpha=0.3)

        # Add top 5 labels
        top_5_indices = [-5, -4, -3, -2, -1]  # Last 5 (highest values)
        for idx in top_5_indices:
            value = data_sorted[risk_type].iloc[idx]
            country = data_sorted['Country'].iloc[idx]
            ax.text(value + (data_sorted[risk_type].max() * 0.02),
                   len(data_sorted) + idx,
                   f'{country}: {value:.1f}',
                   va='center', ha='left', fontsize=8, fontweight='bold')

    plt.tight_layout()
    plt.savefig('multi_dimensional_risk_analysis.png', dpi=300, bbox_inches='tight')
    plt.show()
    print("   ✓ Multi-dimensional analysis saved as 'multi_dimensional_risk_analysis.png'")

    # 2. Statistical Summary
    print("\n2. Generating statistical summary...")

    summary_stats = data[['Political_Risk', 'Economic_Risk', 'Composite_Risk', 'ESG_Score', 'GDP_Growth']].describe()
    print("\nRisk Metrics Summary Statistics:")
    print(summary_stats.round(2))

    # 3. Top/Bottom Performers
    print("\n3. Identifying top and bottom performers...")

    print("\nLOWEST RISK COUNTRIES (Top 5):")
    top_performers = data.nsmallest(5, 'Composite_Risk')[['Country', 'Composite_Risk', 'Region']]
    for i, row in top_performers.iterrows():
        print(f"   {row['Country']:20} | Risk: {row['Composite_Risk']:5.1f} | {row['Region']}")

    print("\nHIGHEST RISK COUNTRIES (Bottom 5):")
    bottom_performers = data.nlargest(5, 'Composite_Risk')[['Country', 'Composite_Risk', 'Region']]
    for i, row in bottom_performers.iterrows():
        print(f"   {row['Country']:20} | Risk: {row['Composite_Risk']:5.1f} | {row['Region']}")


def main():
    """Main demonstration function."""
    print("="*80)
    print("RISKPLOT COMPREHENSIVE COUNTRY MAPPING DEMONSTRATION")
    print("="*80)
    print("This example showcases the full range of country plotting capabilities")
    print("including 2D flat world maps, 3D interactive globes, and advanced analytics.")
    print("="*80)

    # Generate comprehensive dataset
    print("\n📊 Generating comprehensive country dataset...")
    data = generate_comprehensive_country_data()
    print(f"   ✓ Created dataset with {len(data)} countries across {data['Region'].nunique()} regions")
    print(f"   ✓ Risk metrics: Political, Economic, Credit, ESG, GDP Growth")

    # Save the dataset for reference
    data.to_csv('country_risk_dataset.csv', index=False)
    print("   ✓ Dataset saved as 'country_risk_dataset.csv'")

    # Demonstrate 2D capabilities
    demonstrate_2d_world_maps(data)

    # Demonstrate 3D capabilities
    demonstrate_3d_globe_maps(data)

    # Demonstrate advanced features
    demonstrate_advanced_features(data)

    print("\n" + "="*80)
    print("DEMONSTRATION COMPLETE")
    print("="*80)
    print("Files generated:")
    print("   • world_map_2d_risk.html - Interactive 2D risk map")
    print("   • world_map_esg_scores.html - Interactive ESG map")
    print("   • globe_3d_risk.html - Interactive 3D globe")
    print("   • regional_risk_heatmap.png - Regional analysis")
    print("   • multi_dimensional_risk_analysis.png - Multi-dimensional charts")
    print("   • country_risk_dataset.csv - Source data")
    print("\nOpen the HTML files in your browser for interactive exploration!")
    print("="*80)


if __name__ == "__main__":
    main()