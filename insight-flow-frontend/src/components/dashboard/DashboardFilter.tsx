"use client";

import { X } from "lucide-react";
import { Button } from "@/components/ui/button";

interface Props {
    dateRange: [string, string];
    setDateRange: (r: [string, string]) => void;
    selectedZone: string;
    setSelectedZone: (z: string) => void;
    selectedTimeOfDay: string;
    setSelectedTimeOfDay: (t: string) => void;
    selectedStatus: string;
    setSelectedStatus: (s: string) => void;
    zones: string[];
}

const DashboardFilters = ({
    dateRange, setDateRange,
    selectedZone, setSelectedZone,
    selectedTimeOfDay, setSelectedTimeOfDay,
    selectedStatus, setSelectedStatus,
    zones,
}: Props) => {
  const hasActiveFilters = dateRange[0] || dateRange[1] || selectedZone !== "all" || selectedTimeOfDay !== "all" || selectedStatus !== "all";

  const handleClearFilters = () => {
    setDateRange(["", ""]);
    setSelectedZone("all");
    setSelectedTimeOfDay("all");
    setSelectedStatus("all");
  };

  return (
    <div className="rounded-2xl border border-[#e5e7eb] bg-gradient-to-br from-white via-[#fafafa] to-white p-6 shadow-sm">
        <div className="mb-6 flex items-center justify-between">
            <div>
                <h3 className="text-lg font-semibold text-[#1f1f1f]">Filters</h3>
                <p className="text-xs text-[#9ca3af]">Refine your delivery data</p>
            </div>
            {hasActiveFilters && (
                <Button
                    variant="outline"
                    size="sm"
                    onClick={handleClearFilters}
                    className="gap-2 rounded-lg border-[#fca5a5] text-[#dc2626] hover:bg-red-50"
                >
                    <X className="h-4 w-4" />
                    Clear All
                </Button>
            )}
        </div>

        <div className="grid grid-cols-1 gap-4 md:grid-cols-2 xl:grid-cols-5">
            <div className="space-y-1">
                <label className="flex items-center gap-1 text-xs font-semibold text-[#1f1f1f]">
                    📅 From
                    {dateRange[0] && <span className="inline-block h-2 w-2 rounded-full bg-violet-500"></span>}
                </label>
                <input
                    type="date"
                    value={dateRange[0]}
                    onChange={e => setDateRange([e.target.value, dateRange[1]])}
                    className="h-11 w-full rounded-lg border border-[#e5e7eb] bg-white px-3 text-sm transition-colors outline-none focus:border-violet-500 focus:ring-2 focus:ring-violet-100"
                />
            </div>
            <div className="space-y-1">
                <label className="flex items-center gap-1 text-xs font-semibold text-[#1f1f1f]">
                    📅 To
                    {dateRange[1] && <span className="inline-block h-2 w-2 rounded-full bg-violet-500"></span>}
                </label>
                <input
                    type="date"
                    value={dateRange[1]}
                    onChange={e => setDateRange([dateRange[0], e.target.value])}
                    className="h-11 w-full rounded-lg border border-[#e5e7eb] bg-white px-3 text-sm transition-colors outline-none focus:border-violet-500 focus:ring-2 focus:ring-violet-100"
                />
            </div>
            <div className="space-y-1">
                <label className="flex items-center gap-1 text-xs font-semibold text-[#1f1f1f]">
                    🗺️ Zone
                    {selectedZone !== "all" && <span className="inline-block h-2 w-2 rounded-full bg-emerald-500"></span>}
                </label>
                <select
                    value={selectedZone}
                    onChange={(e) => setSelectedZone(e.target.value)}
                    className="h-11 w-full rounded-lg border border-[#e5e7eb] bg-white px-3 text-sm transition-colors outline-none focus:border-emerald-500 focus:ring-2 focus:ring-emerald-100"
                >
                    <option value="all">All Zones</option>
                    {zones.map((z) => (
                        <option key={z} value={z}>
                            {z}
                        </option>
                    ))}
                </select>
            </div>
            <div className="space-y-1">
                <label className="flex items-center gap-1 text-xs font-semibold text-[#1f1f1f]">
                    ⏰ Time of Day
                    {selectedTimeOfDay !== "all" && <span className="inline-block h-2 w-2 rounded-full bg-blue-500"></span>}
                </label>
                <select
                    value={selectedTimeOfDay}
                    onChange={(e) => setSelectedTimeOfDay(e.target.value)}
                    className="h-11 w-full rounded-lg border border-[#e5e7eb] bg-white px-3 text-sm transition-colors outline-none focus:border-blue-500 focus:ring-2 focus:ring-blue-100"
                >
                    <option value="all">All Times</option>
                    <option value="morning">Morning (6-12)</option>
                    <option value="afternoon">Afternoon (12-17)</option>
                    <option value="evening">Evening (17-21)</option>
                    <option value="night">Night (21-6)</option>
                </select>
            </div>
            <div className="space-y-1">
                <label className="flex items-center gap-1 text-xs font-semibold text-[#1f1f1f]">
                    ✓ Status
                    {selectedStatus !== "all" && <span className="inline-block h-2 w-2 rounded-full bg-purple-500"></span>}
                </label>
                <select
                    value={selectedStatus}
                    onChange={(e) => setSelectedStatus(e.target.value)}
                    className="h-11 w-full rounded-lg border border-[#e5e7eb] bg-white px-3 text-sm transition-colors outline-none focus:border-purple-500 focus:ring-2 focus:ring-purple-100"
                >
                    <option value="all">All Orders</option>
                    <option value="on-time">On-Time</option>
                    <option value="delayed">Delayed</option>
                </select>
            </div>
        </div>
    </div>
  );
};

export default DashboardFilters;
