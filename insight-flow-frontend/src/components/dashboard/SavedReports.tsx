"use client";

import { useEffect, useMemo, useState } from "react";
import { Save, Trash2 } from "lucide-react";
import { Button } from "@/components/ui/button";

type SavedReport = {
  id: string;
  title: string;
  filters: {
    dateRange: [string, string];
    selectedZone: string;
    selectedTimeOfDay: string;
    selectedStatus: string;
  };
  metrics: {
    avgDeliveryTime: number;
    onTimePercent: number;
    delayedCount: number;
    peakHour: string;
  };
  createdAt: string;
};

type Props = {
  currentFilters: SavedReport["filters"];
  currentMetrics: SavedReport["metrics"];
  onLoadReport: (filters: SavedReport["filters"]) => void;
};

const STORAGE_KEY = "insight-flow-saved-reports";

export default function SavedReports({ currentFilters, currentMetrics, onLoadReport }: Props) {
  const [title, setTitle] = useState("");
  const [reports, setReports] = useState<SavedReport[]>([]);

  useEffect(() => {
    const raw = window.localStorage.getItem(STORAGE_KEY);
    if (!raw) {
      return;
    }
    try {
      const parsed = JSON.parse(raw) as SavedReport[];
      setReports(parsed);
    } catch {
      window.localStorage.removeItem(STORAGE_KEY);
    }
  }, []);

  const sortedReports = useMemo(
    () => [...reports].sort((a, b) => b.createdAt.localeCompare(a.createdAt)),
    [reports],
  );

  function persist(nextReports: SavedReport[]) {
    setReports(nextReports);
    window.localStorage.setItem(STORAGE_KEY, JSON.stringify(nextReports));
  }

  function saveCurrentReport() {
    const newReport: SavedReport = {
      id: crypto.randomUUID(),
      title: title.trim() || `Report ${new Date().toLocaleDateString()}`,
      filters: currentFilters,
      metrics: currentMetrics,
      createdAt: new Date().toISOString(),
    };

    persist([newReport, ...reports]);
    setTitle("");
  }

  function deleteReport(id: string) {
    persist(reports.filter((report) => report.id !== id));
  }

  return (
    <div className="glass-card rounded-2xl border border-[#f3ded2] bg-white p-6 shadow-[0_12px_30px_rgba(60,20,8,0.08)]">
      <h3 className="mb-4 text-lg font-semibold text-[#2b211b]">Saved Reports</h3>

      <div className="mb-4 flex gap-2">
        <input
          placeholder="Report name..."
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          className="flex-1 rounded-xl border border-[#ead8ce] bg-white px-3 py-2 text-sm outline-none focus:border-[#ff6a2f]"
        />
        <Button onClick={saveCurrentReport} className="gradient-primary text-primary-foreground">
          <Save className="mr-1 h-4 w-4" /> Save
        </Button>
      </div>

      {sortedReports.length === 0 ? (
        <p className="py-4 text-center text-sm text-[#8b7769]">No saved reports yet</p>
      ) : (
        <div className="max-h-64 space-y-2 overflow-y-auto">
          {sortedReports.map((report) => (
            <div
              key={report.id}
              className="flex items-center justify-between rounded-lg border border-[#f3ded2] bg-[#fff9f6] p-3"
            >
              <button className="flex-1 text-left" onClick={() => onLoadReport(report.filters)}>
                <p className="text-sm font-medium text-[#3b2d26]">{report.title}</p>
                <p className="text-xs text-[#8b7769]">{new Date(report.createdAt).toLocaleDateString()}</p>
              </button>
              <Button
                variant="outline"
                size="sm"
                className="border-[#f1ddd1] text-[#8b7769]"
                onClick={() => deleteReport(report.id)}
              >
                <Trash2 className="h-4 w-4" />
              </Button>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
