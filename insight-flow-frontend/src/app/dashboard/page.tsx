"use client";

import { useMemo, useState, useCallback, type ChangeEvent } from "react";
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

function parseCsv(text: string): DeliveryOrder[] {
  const lines = text
    .split(/\r?\n/)
    .map((line) => line.trim())
    .filter(Boolean);

  if (lines.length < 2) {
    return [];
  }

  const headers = lines[0].split(",").map((h) => h.trim().toLowerCase());

  const indexOf = (keys: string[]) => headers.findIndex((h) => keys.includes(h));
  const orderTimeIdx = indexOf(["order time", "ordertime", "order_time"]);
  const deliveryTimeIdx = indexOf(["delivery time", "deliverytime", "delivery_time"]);
  const locationIdx = indexOf(["location"]);
  const zoneIdx = indexOf(["zone"]);

  if (orderTimeIdx === -1 || deliveryTimeIdx === -1) {
    return [];
  }

  return lines
    .slice(1)
    .map((line, i) => {
      const columns = line.split(",").map((c) => c.trim());
      const orderTime = columns[orderTimeIdx];
      const deliveryTime = columns[deliveryTimeIdx];

      if (!orderTime || !deliveryTime) {
        return null;
      }

      const orderDate = new Date(orderTime);
      const deliveryDate = new Date(deliveryTime);

      if (Number.isNaN(orderDate.getTime()) || Number.isNaN(deliveryDate.getTime())) {
        return null;
      }

      const duration = Math.round((deliveryDate.getTime() - orderDate.getTime()) / 60000);

      return {
        id: `CSV-${i + 1}`,
        orderTime: orderDate.toISOString(),
        deliveryTime: deliveryDate.toISOString(),
        location: locationIdx >= 0 ? columns[locationIdx] || "Unknown" : "Unknown",
        zone: zoneIdx >= 0 ? columns[zoneIdx] || "Zone A" : "Zone A",
        status: duration > 35 ? "delayed" : "on-time",
        deliveryDuration: duration > 0 ? duration : 30,
        lat: 28.6 + (Math.random() - 0.5) * 0.15,
        lng: 77.2 + (Math.random() - 0.5) * 0.15,
      } as DeliveryOrder;
    })
    .filter((row): row is DeliveryOrder => row !== null);
}

export default function DashboardPage() {
  const { user, signOut } = useAuth();
  const [orders, setOrders] = useState<DeliveryOrder[]>(mockOrders);
  const [dateRange, setDateRange] = useState<[string, string]>(["", ""]);
  const [selectedZone, setSelectedZone] = useState("all");
  const [selectedTimeOfDay, setSelectedTimeOfDay] = useState("all");
  const [selectedStatus, setSelectedStatus] = useState("all");

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

    const reader = new FileReader();
    reader.onload = () => {
      const text = typeof reader.result === "string" ? reader.result : "";
      const parsed = parseCsv(text);
      if (parsed.length > 0) {
        setOrders(parsed);
      }
    };
    reader.readAsText(file);
  }, []);

  const zones = useMemo(() => [...new Set(orders.map((o) => o.zone))], [orders]);

  const currentFilters = { dateRange, selectedZone, selectedTimeOfDay, selectedStatus };

  const handleLoadReport = (filters: typeof currentFilters) => {
    if (filters.dateRange) setDateRange(filters.dateRange);
    if (filters.selectedZone) setSelectedZone(filters.selectedZone);
    if (filters.selectedTimeOfDay) setSelectedTimeOfDay(filters.selectedTimeOfDay);
    if (filters.selectedStatus) setSelectedStatus(filters.selectedStatus);
  };

  return (
    <div className="min-h-screen bg-[#fafafa] text-[#1f1f1f]">
      <header className="sticky top-0 z-50 border-b border-[#ececec] bg-white">
        <div className="mx-auto flex max-w-[1180px] items-center justify-between px-4 py-4 sm:px-6">
          <div className="flex items-center gap-4">
            <Link href="/">
              <Button variant="outline" size="sm" className="rounded-xl border-[#e5e7eb] text-[#4b5563]">
                <ArrowLeft className="h-4 w-4" />
              </Button>
            </Link>
            <div>
              <h1 className="text-[34px] font-bold leading-tight tracking-tight">Delivery Dashboard</h1>
              <p className="text-sm text-[#9ca3af]">{filteredOrders.length} orders analyzed</p>
            </div>
          </div>

          <div className="flex items-center gap-3">
            <label className="cursor-pointer">
              <input type="file" accept=".csv" className="hidden" onChange={handleCSVUpload} />
              <div className="gradient-primary flex items-center gap-2 rounded-xl px-4 py-2 text-sm font-semibold text-white shadow-[0_6px_18px_rgba(244,67,54,0.28)]">
                <Upload className="h-4 w-4" /> Upload CSV
              </div>
            </label>

            <div className="flex items-center gap-2 rounded-xl border border-[#ededed] bg-[#f8f8f8] px-3 py-2 text-sm">
              <User className="h-4 w-4 text-[#9ca3af]" />
              <span className="hidden max-w-[140px] truncate text-[#9ca3af] sm:inline">{user?.email ?? "guest@example.com"}</span>
            </div>

            <Button variant="outline" size="sm" className="rounded-xl border-[#e5e7eb] text-[#6b7280]" onClick={signOut} title="Sign out">
              <LogOut className="h-4 w-4" />
            </Button>
          </div>
        </div>
      </header>

      <main className="mx-auto max-w-[1180px] space-y-8 px-4 py-8 sm:px-6">
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
