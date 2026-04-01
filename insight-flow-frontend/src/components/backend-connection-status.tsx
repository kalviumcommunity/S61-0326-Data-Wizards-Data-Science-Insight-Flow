"use client";

import { useState } from "react";
import {
  checkBackendHealth,
  getApiBaseUrl,
  type BackendHealthResult,
} from "@/lib/flask-api";

const statusStyles = {
  idle: "bg-slate-200 text-slate-700",
  loading: "bg-amber-100 text-amber-800",
  connected: "bg-emerald-100 text-emerald-800",
  error: "bg-rose-100 text-rose-800",
};

export function BackendConnectionStatus() {
  const [result, setResult] = useState<BackendHealthResult | null>(null);
  const [status, setStatus] = useState<keyof typeof statusStyles>("idle");

  const runCheck = async (showLoadingState = true) => {
    if (showLoadingState) {
      setStatus("loading");
    }

    const healthResult = await checkBackendHealth();
    setResult(healthResult);
    setStatus(healthResult.ok ? "connected" : "error");
  };

  return (
    <aside className="rounded-3xl border border-slate-200 bg-white p-7 shadow-lg shadow-slate-900/5">
      <h2 className="text-lg font-semibold text-slate-900">Backend Connection</h2>
      <p className="mt-2 text-sm text-slate-600">Flask API base URL</p>
      <p className="mt-1 break-all rounded-lg bg-slate-100 px-3 py-2 text-sm font-medium text-slate-800">
        {getApiBaseUrl()}
      </p>

      <span
        className={`mt-4 inline-flex rounded-full px-3 py-1 text-xs font-semibold uppercase tracking-wider ${statusStyles[status]}`}
      >
        {status === "loading"
          ? "Checking"
          : status === "connected"
            ? "Connected"
            : status === "error"
              ? "Connection Error"
              : "Idle"}
      </span>

      <div className="mt-4 space-y-2 text-sm text-slate-700">
        {result?.ok && <p>Backend responded successfully.</p>}
        {!result?.ok && result?.error && <p>{result.error}</p>}
        {!result && <p>Run a health check once the Flask server is online.</p>}
      </div>

      <button
        type="button"
        className="mt-5 rounded-xl bg-slate-900 px-4 py-2 text-sm font-semibold text-white transition hover:bg-slate-700"
        onClick={() => {
          void runCheck();
        }}
      >
        Retry Connection
      </button>
    </aside>
  );
}