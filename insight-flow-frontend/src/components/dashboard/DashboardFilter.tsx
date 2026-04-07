"use client";

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
}: Props) => (
    <div className="glass-card rounded-2xl bg-white p-4">
        <div className="grid grid-cols-1 gap-4 md:grid-cols-2 xl:grid-cols-5">
            <div className="space-y-1">
                <label className="text-xs font-medium text-[#9ca3af]">From</label>
                <input
                    type="date"
                    value={dateRange[0]}
                    onChange={e => setDateRange([e.target.value, dateRange[1]])}
                    className="h-11 w-full rounded-xl border border-[#e5e7eb] bg-white px-3 text-sm outline-none focus:border-[#f97316]"
                />
            </div>
            <div className="space-y-1">
                <label className="text-xs font-medium text-[#9ca3af]">To</label>
                <input
                    type="date"
                    value={dateRange[1]}
                    onChange={e => setDateRange([dateRange[0], e.target.value])}
                    className="h-11 w-full rounded-xl border border-[#e5e7eb] bg-white px-3 text-sm outline-none focus:border-[#f97316]"
                />
            </div>
            <div className="space-y-1">
                <label className="text-xs font-medium text-[#9ca3af]">Zone</label>
                <select
                    value={selectedZone}
                    onChange={(e) => setSelectedZone(e.target.value)}
                    className="h-11 w-full rounded-xl border border-[#e5e7eb] bg-white px-3 text-sm outline-none focus:border-[#f97316]"
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
                <label className="text-xs font-medium text-[#9ca3af]">Time of Day</label>
                <select
                    value={selectedTimeOfDay}
                    onChange={(e) => setSelectedTimeOfDay(e.target.value)}
                    className="h-11 w-full rounded-xl border border-[#e5e7eb] bg-white px-3 text-sm outline-none focus:border-[#f97316]"
                >
                    <option value="all">All Times</option>
                    <option value="morning">Morning (6-12)</option>
                    <option value="afternoon">Afternoon (12-17)</option>
                    <option value="evening">Evening (17-21)</option>
                    <option value="night">Night (21-6)</option>
                </select>
            </div>
            <div className="space-y-1">
                <label className="text-xs font-medium text-[#9ca3af]">Status</label>
                <select
                    value={selectedStatus}
                    onChange={(e) => setSelectedStatus(e.target.value)}
                    className="h-11 w-full rounded-xl border border-[#e5e7eb] bg-white px-3 text-sm outline-none focus:border-[#f97316]"
                >
                    <option value="all">All Orders</option>
                    <option value="on-time">On-Time</option>
                    <option value="delayed">Delayed</option>
                </select>
            </div>
        </div>
    </div>
);

export default DashboardFilters;
