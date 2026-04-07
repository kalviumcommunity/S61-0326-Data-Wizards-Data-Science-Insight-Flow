interface ZoneData {
    zone: string;
    avgDeliveryTime: number;
    delayRate: number;
    totalOrders: number;
}

interface Props {
    data: ZoneData[];
}

const ZoneHeatmap = ({ data }: Props) => {
    const maxDelay = Math.max(...data.map(d => d.delayRate), 1);

    const getColor = (rate: number) => {
        const ratio = rate / maxDelay;
        if (ratio > 0.7) return "bg-red-50 border-red-200";
        if (ratio > 0.4) return "bg-amber-50 border-amber-200";
        return "bg-emerald-50 border-emerald-200";
    };

    const getTextColor = (rate: number) => {
        const ratio = rate / maxDelay;
        if (ratio > 0.7) return "text-red-600";
        if (ratio > 0.4) return "text-amber-600";
        return "text-emerald-600";
    };

    return (
        <div className="glass-card rounded-2xl bg-white p-6">
            <h3 className="mb-4 text-lg font-semibold">Zone Performance Heatmap</h3>
            <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-4">
                {data.map(zone => (
                    <div
                        key={zone.zone}
                        className={`rounded-xl border p-4 text-center transition-all ${getColor(zone.delayRate)}`}
                    >
                        <p className="font-semibold text-sm mb-2">{zone.zone}</p>
                        <p className={`text-2xl font-bold ${getTextColor(zone.delayRate)}`}>
                            {zone.delayRate}%
                        </p>
                        <p className="text-xs text-muted-foreground mt-1">delay rate</p>
                        <p className="text-xs text-muted-foreground">{zone.avgDeliveryTime} min avg</p>
                        <p className="text-xs text-muted-foreground">{zone.totalOrders} orders</p>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default ZoneHeatmap;
