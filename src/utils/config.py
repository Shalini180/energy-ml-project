# config/production.yaml
database:
  # Path to your production database
  path: "/path/to/production.db"  # Change this!
  # Or connection string for existing DB
  connection_string: null

carbon_api:
  # Get free API key from electricitymap.org
  api_key: "YOUR_API_KEY_HERE"  # Change this!
  zone: "US-CAL-CISO"  # Your region
  cache_minutes: 5
  fallback_to_historical: true

energy_profiling:
  enabled: true
  use_rapl: true  # Intel RAPL
  fallback_to_estimation: true

thresholds:
  low_carbon: 250   # gCO2/kWh
  high_carbon: 500  # gCO2/kWh

logging:
  level: "INFO"
  file: "logs/engine.log"
  max_bytes: 10485760  # 10MB
  backup_count: 5

metrics:
  output_dir: "data/results"
  auto_save: true
  save_interval_minutes: 60