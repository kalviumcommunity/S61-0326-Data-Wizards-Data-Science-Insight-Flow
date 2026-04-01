const DEFAULT_API_BASE_URL = "http://127.0.0.1:5000";

export type BackendHealthResult = {
  ok: boolean;
  error?: string;
};

export function getApiBaseUrl() {
  return process.env.NEXT_PUBLIC_FLASK_API_URL ?? DEFAULT_API_BASE_URL;
}

export async function checkBackendHealth(): Promise<BackendHealthResult> {
  try {
    const response = await fetch(`${getApiBaseUrl()}/health`, {
      cache: "no-store",
    });

    if (!response.ok) {
      return {
        ok: false,
        error: `Received HTTP ${response.status} from Flask backend.`,
      };
    }

    return { ok: true };
  } catch {
    return {
      ok: false,
      error:
        "Could not reach Flask backend. Start the server and confirm CORS is enabled for this frontend origin.",
    };
  }
}