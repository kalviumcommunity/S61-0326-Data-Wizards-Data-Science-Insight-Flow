# Insight Flow

Food Delivery Performance Analytics Dashboard.

## Tech Stack

- Backend: Flask, SQLite, Pandas, NumPy, Matplotlib, Seaborn
- Frontend: Next.js, Tailwind CSS, Recharts, React Leaflet
- Optional ML dependency included: scikit-learn

## Project Structure

- `backend/` Flask API + SQLite storage
- `frontend/` Next.js dashboard UI

## Backend Setup

1. Open a terminal in `backend/`.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the API:

```bash
python app.py
```

Backend runs at `http://localhost:5000`.

### Backend Endpoints

- `GET /api/health`
- `POST /api/upload` (multipart form with key `file`)
- `POST /api/bootstrap-sample` (loads `backend/seed_sample.csv`)
- `GET /api/dashboard` with filters:
  - `start_date`
  - `end_date`
  - `location`
  - `time_of_day`
  - `status`

## Frontend Setup

1. Open another terminal in `frontend/`.
2. Install dependencies:

```bash
npm install
```

3. Create env file:

```bash
cp .env.local.example .env.local
```

On Windows PowerShell:

```powershell
Copy-Item .env.local.example .env.local
```

4. Run app:

```bash
npm run dev
```

Frontend runs at `http://localhost:3000`.

## How to Use

1. Open the landing page and click **View Dashboard**.
2. Click **Upload CSV** and upload your delivery dataset.
3. Or load sample dataset by calling:

```bash
curl -X POST http://localhost:5000/api/bootstrap-sample
```

4. Use filters (date, location, time of day, status).
5. Review metrics, charts, heatmap, map markers, and auto insights.

## CSV Columns

Required columns (aliases supported):

- `Order Time`
- `Delivery Time`
- `Location`

Optional columns:

- `Status`
- `Latitude`
- `Longitude`
