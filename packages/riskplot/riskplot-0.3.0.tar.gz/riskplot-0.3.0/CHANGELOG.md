# Changelog

All notable changes to RiskPlot will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.3.0] - 2024-09-28

### Added
- **Major Enhancement: Professional 2D World Maps**
  - New `country_choropleth_map()` function for traditional flat world maps
  - Professional choropleth visualization perfect for reports and presentations
  - Support for multiple country code formats (ISO-2, ISO-3, country names)
  - Automatic country code normalization and mapping
  - Customizable color scales, borders, and ocean colors
  - Export capabilities (HTML, PNG, PDF)

- **Enhanced Geographic Analysis**
  - New `WorldMapPlot` class for advanced 2D map customization
  - `regional_risk_heatmap()` function for regional country comparisons
  - Improved country code support with comprehensive mapping dictionary
  - Multiple backend support (Plotly for interactive, Matplotlib for static)

- **Comprehensive Examples and Documentation**
  - New `comprehensive_country_mapping.py` example showcasing all geographic features
  - Enhanced API documentation with complete geographic module reference
  - Updated feature documentation with best practices and use cases
  - Professional documentation website with geographic analysis guide

### Enhanced
- **Improved 3D Globe Functionality**
  - Enhanced `country_risk_globe()` with better parameter consistency
  - Fixed parameter naming issues in existing examples
  - Improved error handling and user experience

- **Documentation and Examples**
  - Significantly expanded documentation with professional styling
  - Added comprehensive API reference for geographic functions
  - Updated examples gallery with new geographic capabilities
  - Enhanced README with clear feature descriptions

### Fixed
- Fixed parameter name inconsistencies in `country_risk_example.py`
- Improved error messaging for missing dependencies
- Enhanced country code handling and validation

### Technical
- Updated package description and keywords for better discoverability
- Enhanced module exports and __all__ lists
- Improved import structure for geographic modules
- Added comprehensive type hints and documentation strings

## [0.2.0] - Previous Release

### Added
- Core visualization functions (ridge plots, heatmaps, waterfall charts)
- Time series analysis capabilities
- Basic globe visualization
- Network analysis functionality
- Surface plotting capabilities

### Features
- Ridge plots for distribution analysis
- Correlation heatmaps and risk matrices
- Waterfall charts for attribution analysis
- VaR tracking and drawdown analysis
- Interactive 3D globe visualizations
- Financial network analysis
- 3D surface plots and risk landscapes

## [0.1.0] - Initial Release

### Added
- Basic visualization framework
- Core plotting utilities
- Initial documentation structure