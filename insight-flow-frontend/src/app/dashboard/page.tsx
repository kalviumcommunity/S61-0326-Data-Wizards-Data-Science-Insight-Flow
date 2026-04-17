"use client";

import { useMemo, useState, useCallback, useEffect, type ChangeEvent } from "react";
import Link from "next/link";
import { motion } from "framer-motion";
import { ArrowLeft, Upload, LogOut, User } from "lucide-react";
import { Button } from "@/components/ui/button";
import { useAuth } from "@/hooks/useAuth";
import {
  mockOrders,
  getMetrics,
  getDeliveryTrends,
  getDelaysByHour,
  getZonePerformance,
  getStatusDistribution,
  generateInsights,
  type DeliveryOrder,
} from "@/lib/mockData";
import MetricCards from "@/components/dashboard/MetricCards";
import DeliveryTrendChart from "@/components/dashboard/DeliveryTreendChart";
import DelaysByHourChart from "@/components/dashboard/DelaysByHourChart";
import StatusPieChart from "@/components/dashboard/StatusPieChart";
import ZoneHeatmap from "@/components/dashboard/ZoneHeatmap";
import InsightsPanel from "@/components/dashboard/InsightsPanel";
import DashboardFilters from "@/components/dashboard/DashboardFilter";
import OrdersTable from "@/components/dashboard/OrdersTable";
import SavedReports from "@/components/dashboard/SavedReports";

type CsvParseResult = {
  rows: DeliveryOrder[];
  error?: string;
};

function splitCsvLine(line: string): string[] {
  const values: string[] = [];
  let current = "";
  let inQuotes = false;

  for (let i = 0; i < line.length; i++) {
    const char = line[i];

    if (char === '"') {
      if (inQuotes && line[i + 1] === '"') {
        current += '"';
        i++;
      } else {
        inQuotes = !inQuotes;
      }
      continue;
    }

    if (char === "," && !inQuotes) {
      values.push(current.trim());
      current = "";
      continue;
    }

    current += char;
  }

  values.push(current.trim());
  return values;
}

function normalizeHeader(value: string): string {
  return value.trim().toLowerCase().replace(/[^a-z0-9]/g, "");
}

function parseDateTime(value: string): Date | null {
  const raw = value.trim();
  if (!raw) {
    return null;
  }

  const direct = new Date(raw);
  if (!Number.isNaN(direct.getTime())) {
    return direct;
  }

  const normalized = raw.includes("T") ? raw : raw.replace(" ", "T");
  const retry = new Date(normalized);
  if (!Number.isNaN(retry.getTime())) {
    return retry;
  }

  return null;
}

function parseCsv(text: string): CsvParseResult {
  const lines = text
    .split(/\r?\n/)
    .map((line) => line.trim().replace(/^\uFEFF/, ""))
    .filter(Boolean);

  if (lines.length < 2) {
    return { rows: [], error: "The selected file appears empty or missing data rows." };
  }

  const headers = splitCsvLine(lines[0]).map(normalizeHeader);

  const indexOf = (keys: string[]) => headers.findIndex((h) => keys.includes(h));
  const idIdx = indexOf(["orderid", "id"]);
  const orderTimeIdx = indexOf(["ordertime", "orderts", "ordertimestamp", "orderdate", "orderedat"]);
  const deliveryTimeIdx = indexOf(["deliverytime", "deliveryts", "deliverytimestamp", "deliverydate", "deliveredat"]);
  const durationIdx = indexOf([
    "deliveryduration",
    "deliveryminutes",
    "deliverytimeminutes",
    "duration",
    "eta",
    "etaminutes",
  ]);
  const locationIdx = indexOf(["location", "city", "area", "address"]);
  const zoneIdx = indexOf(["zone", "region", "cluster"]);
  const statusIdx = indexOf(["status", "deliverystatus"]);

  if (orderTimeIdx === -1) {
    return {
      rows: [],
      error: "Missing required time column. Add an order time column like order_time or orderTime.",
    };
  }

  const rows = lines
    .slice(1)
    .map((line, i) => {
      const columns = splitCsvLine(line);
      const orderTime = columns[orderTimeIdx];
      const deliveryTime = deliveryTimeIdx >= 0 ? columns[deliveryTimeIdx] : "";
      const durationValue = durationIdx >= 0 ? columns[durationIdx] : "";

      if (!orderTime) {
        return null;
      }

      const orderDate = parseDateTime(orderTime);
      if (!orderDate) {
        return null;
      }

      let deliveryDate: Date | null = null;
      let duration: number | null = null;

      if (deliveryTime) {
        const parsedDeliveryDate = parseDateTime(deliveryTime);
        if (parsedDeliveryDate) {
          deliveryDate = parsedDeliveryDate;
          duration = Math.round((parsedDeliveryDate.getTime() - orderDate.getTime()) / 60000);
        }
      }

      if (duration === null && durationValue) {
        const parsedDuration = Number(durationValue);
        if (!Number.isNaN(parsedDuration)) {
          duration = Math.round(parsedDuration);
          deliveryDate = new Date(orderDate.getTime() + duration * 60000);
        }
      }

      if (duration === null || !deliveryDate) {
        return null;
      }

      const safeDuration = duration > 0 ? duration : 30;
      const statusFromCsv = statusIdx >= 0 ? (columns[statusIdx] || "").toLowerCase() : "";
      const normalizedStatus = statusFromCsv.includes("delay")
        ? "delayed"
        : statusFromCsv.includes("on")
          ? "on-time"
          : safeDuration > 35
            ? "delayed"
            : "on-time";

      return {
        id: idIdx >= 0 && columns[idIdx] ? String(columns[idIdx]) : `CSV-${i + 1}`,
        orderTime: orderDate.toISOString(),
        deliveryTime: deliveryDate.toISOString(),
        location: locationIdx >= 0 ? columns[locationIdx] || "Unknown" : "Unknown",
        zone: zoneIdx >= 0 ? columns[zoneIdx] || "Zone A" : "Zone A",
        status: normalizedStatus,
        deliveryDuration: safeDuration,
        lat: 28.6 + (Math.random() - 0.5) * 0.15,
        lng: 77.2 + (Math.random() - 0.5) * 0.15,
      } as DeliveryOrder;
    })
    .filter((row): row is DeliveryOrder => row !== null);

  if (rows.length === 0) {
    return {
      rows,
      error:
        "No valid rows were parsed. Check date/time formats and ensure required columns are present.",
    };
  }

  return { rows };
}

export default function DashboardPage() {
  const { user, signOut } = useAuth();
  const [orders, setOrders] = useState<DeliveryOrder[]>([]);
  const [dateRange, setDateRange] = useState<[string, string]>(["", ""]);
  const [selectedZone, setSelectedZone] = useState("all");
  const [selectedTimeOfDay, setSelectedTimeOfDay] = useState("all");
  const [selectedStatus, setSelectedStatus] = useState("all");
  const [uploadMessage, setUploadMessage] = useState<string>("");
  const [uploadMessageIsError, setUploadMessageIsError] = useState(false);

  useEffect(() => {
    setOrders(mockOrders);
  }, []);

  const filteredOrders = useMemo(() => {
    return orders.filter((o) => {
      if (dateRange[0] && o.orderTime.slice(0, 10) < dateRange[0]) return false;
      if (dateRange[1] && o.orderTime.slice(0, 10) > dateRange[1]) return false;
      if (selectedZone !== "all" && o.zone !== selectedZone) return false;
      if (selectedStatus !== "all" && o.status !== selectedStatus) return false;
      if (selectedTimeOfDay !== "all") {
        const h = new Date(o.orderTime).getHours();
        if (selectedTimeOfDay === "morning" && (h < 6 || h >= 12)) return false;
        if (selectedTimeOfDay === "afternoon" && (h < 12 || h >= 17)) return false;
        if (selectedTimeOfDay === "evening" && (h < 17 || h >= 21)) return false;
        if (selectedTimeOfDay === "night" && (h >= 6 && h < 21)) return false;
      }
      return true;
    });
  }, [orders, dateRange, selectedZone, selectedTimeOfDay, selectedStatus]);

  const metrics = useMemo(() => getMetrics(filteredOrders), [filteredOrders]);
  const trends = useMemo(() => getDeliveryTrends(filteredOrders), [filteredOrders]);
  const hourlyDelays = useMemo(() => getDelaysByHour(filteredOrders), [filteredOrders]);
  const zonePerf = useMemo(() => getZonePerformance(filteredOrders), [filteredOrders]);
  const statusDist = useMemo(() => getStatusDistribution(filteredOrders), [filteredOrders]);
  const insights = useMemo(() => generateInsights(filteredOrders), [filteredOrders]);

  const handleCSVUpload = useCallback((e: ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) {
      return;
    }

    setUploadMessage("");
    setUploadMessageIsError(false);

    const reader = new FileReader();
    reader.onload = () => {
      const text = typeof reader.result === "string" ? reader.result : "";
      const parsed = parseCsv(text);
      if (parsed.rows.length > 0) {
        setOrders(parsed.rows);
        setDateRange(["", ""]);
        setSelectedZone("all");
        setSelectedTimeOfDay("all");
        setSelectedStatus("all");
        setUploadMessage(`Uploaded ${parsed.rows.length} rows from ${file.name}.`);
        setUploadMessageIsError(false);
      } else {
        setUploadMessage(parsed.error ?? "CSV upload failed. No valid rows were found.");
        setUploadMessageIsError(true);
      }
    };

    reader.onerror = () => {
      setUploadMessage("Unable to read the selected file. Please try again.");
      setUploadMessageIsError(true);
    };

    reader.readAsText(file);
    e.target.value = "";
  }, []);

  const zones = useMemo(() => [...new Set(orders.map((o) => o.zone))].sort((a, b) => a.localeCompare(b)), [orders]);

  const currentFilters = { dateRange, selectedZone, selectedTimeOfDay, selectedStatus };

  const handleLoadReport = (filters: typeof currentFilters) => {
    if (filters.dateRange) setDateRange(filters.dateRange);
    if (filters.selectedZone) setSelectedZone(filters.selectedZone);
    if (filters.selectedTimeOfDay) setSelectedTimeOfDay(filters.selectedTimeOfDay);
    if (filters.selectedStatus) setSelectedStatus(filters.selectedStatus);
  };

  return (
    <div className="min-h-screen bg-gradient-to-b from-[#fafafa] to-white text-[#1f1f1f]">
      <header className="sticky top-0 z-50 border-b border-[#e5e7eb] bg-white/95 backdrop-blur-sm">
        <div className="mx-auto flex max-w-[1180px] items-center justify-between px-4 py-6 sm:px-6">
          <div className="flex items-center gap-4">
            <Link href="/">
              <Button variant="outline" size="sm" className="rounded-lg border-[#e5e7eb] text-[#4b5563] hover:bg-gray-50">
                <ArrowLeft className="h-4 w-4" />
              </Button>
            </Link>
            <div>
              <h1 className="text-3xl font-bold leading-tight tracking-tight">📊 Delivery Dashboard</h1>
              <p className="text-sm text-[#6b7280]">{filteredOrders.length} orders • Real-time insights</p>
            </div>
          </div>

          <div className="flex items-center gap-4">
            <div className="flex flex-col gap-2">
              <label className="cursor-pointer">
                <input type="file" accept=".csv" className="hidden" onChange={handleCSVUpload} />
                <div className="flex items-center gap-2 rounded-lg bg-gradient-to-r from-[#8b5cf6] to-[#6d28d9] px-5 py-2.5 text-sm font-semibold text-white shadow-lg transition-all hover:shadow-xl hover:scale-105 active:scale-95">
                  <Upload className="h-4 w-4" /> Upload CSV
                </div>
              </label>
              {uploadMessage && (
                <div className={`rounded-lg px-3 py-2 text-xs font-medium border ${
                  uploadMessageIsError 
                    ? "border-red-200 bg-red-50 text-red-700" 
                    : "border-emerald-200 bg-emerald-50 text-emerald-700"
                }`}>
                  {uploadMessageIsError ? "⚠️" : "✅"} {uploadMessage}
                </div>
              )}
            </div>

            <div className="flex items-center gap-2 rounded-lg border border-[#e5e7eb] bg-gradient-to-r from-[#f3f4f6] to-[#f9fafb] px-4 py-2.5 text-sm">
              <User className="h-4 w-4 text-[#6b7280]" />
              <span className="hidden max-w-[140px] truncate text-[#6b7280] sm:inline">{user?.email ?? "guest@example.com"}</span>
            </div>

            <Button variant="outline" size="sm" className="rounded-lg border-[#e5e7eb] text-[#6b7280] hover:bg-gray-50" onClick={signOut} title="Sign out">
              <LogOut className="h-4 w-4" />
            </Button>
          </div>
        </div>
      </header>

      <main className="mx-auto max-w-[1180px] space-y-8 px-4 py-12 sm:px-6">
        <DashboardFilters
          dateRange={dateRange}
          setDateRange={setDateRange}
          selectedZone={selectedZone}
          setSelectedZone={setSelectedZone}
          selectedTimeOfDay={selectedTimeOfDay}
          setSelectedTimeOfDay={setSelectedTimeOfDay}
          selectedStatus={selectedStatus}
          setSelectedStatus={setSelectedStatus}
          zones={zones}
        />

        <MetricCards metrics={metrics} />

        <div className="grid grid-cols-1 gap-6 lg:grid-cols-2">
          <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: 0.2 }}>
            <DeliveryTrendChart data={trends} />
          </motion.div>
          <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: 0.3 }}>
            <DelaysByHourChart data={hourlyDelays} />
          </motion.div>
        </div>

        <div className="grid grid-cols-1 gap-6 lg:grid-cols-3">
          <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: 0.4 }}>
            <StatusPieChart data={statusDist} />
          </motion.div>
          <motion.div className="lg:col-span-2" initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: 0.5 }}>
            <ZoneHeatmap data={zonePerf} />
          </motion.div>
        </div>

        <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: 0.55 }}>
          <OrdersTable orders={filteredOrders} />
        </motion.div>

        <div className="grid grid-cols-1 gap-6 lg:grid-cols-3">
          <motion.div className="lg:col-span-2" initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: 0.6 }}>
            <InsightsPanel insights={insights} />
          </motion.div>
          <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: 0.65 }}>
            <SavedReports
              currentFilters={currentFilters}
              currentMetrics={metrics}
              onLoadReport={handleLoadReport}
            />
          </motion.div>
        </div>
      </main>
    </div>
  );
}
