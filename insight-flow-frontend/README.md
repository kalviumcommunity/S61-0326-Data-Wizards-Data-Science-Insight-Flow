# Insight Flow Frontend

Next.js + Tailwind CSS frontend for the Insight Flow food delivery analytics platform.

## Stack

- Next.js (App Router)
- React + TypeScript
- Tailwind CSS

## Local Setup

1. Install dependencies:

```bash
npm install
```

2. Create a local environment file:

```bash
cp .env.example .env.local
```

3. Start the frontend:

```bash
npm run dev
```

4. Open [http://localhost:3000](http://localhost:3000).

## Flask Backend Connection

The frontend expects a Flask backend URL in `.env.local`:

```env
NEXT_PUBLIC_FLASK_API_URL=http://127.0.0.1:5000
```

The starter UI checks backend health at:

`GET {NEXT_PUBLIC_FLASK_API_URL}/health`

If your backend uses a different endpoint shape, update [src/lib/flask-api.ts](src/lib/flask-api.ts).

## Scripts

- `npm run dev` starts the development server.
- `npm run build` creates a production build.
- `npm run start` runs the production server.
- `npm run lint` runs ESLint.
