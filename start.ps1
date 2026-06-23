# Pink Lightning Set List Generator - Quick Start Script

Write-Host "========================================" -ForegroundColor Magenta
Write-Host "Pink Lightning Set List Generator" -ForegroundColor Magenta
Write-Host "========================================" -ForegroundColor Magenta
Write-Host ""

# Check if virtual environment exists
if (-not (Test-Path "venv")) {
	Write-Host "Creating virtual environment..." -ForegroundColor Yellow
	python -m venv venv
	Write-Host ""
}

# Activate virtual environment
Write-Host "Activating virtual environment..." -ForegroundColor Yellow
& ".\venv\Scripts\Activate.ps1"

# Install requirements
if (-not (Test-Path "venv\Lib\site-packages\flask")) {
	Write-Host "Installing dependencies..." -ForegroundColor Yellow
	pip install -r requirements.txt
	Write-Host ""
}

# Initialize database
if (-not (Test-Path "pinklightning.db")) {
	Write-Host "Initializing database..." -ForegroundColor Yellow
	python init_db.py
	Write-Host ""
}

# Start the app
Write-Host "Starting Pink Lightning Set List Generator..." -ForegroundColor Green
Write-Host ""
Write-Host "Open your browser to: " -NoNewline
Write-Host "http://localhost:5000" -ForegroundColor Cyan
Write-Host "Login: " -NoNewline
Write-Host "pinklightning / gottohave100" -ForegroundColor Yellow
Write-Host ""
Write-Host "Press CTRL+C to stop the server" -ForegroundColor Red
Write-Host ""

python app.py
