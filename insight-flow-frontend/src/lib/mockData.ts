export interface DeliveryOrder {
    id: string;
    orderTime: string;
    deliveryTime: string;
    location: string;
    zone: string;
    status: "on-time" | "delayed";
    deliveryDuration: number; // minutes
    lat: number;
    lng: number;
}

const zones = ["Zone A", "Zone B", "Zone C", "Zone D", "Zone E"];
const locations = [
    "Downtown", "Uptown", "Midtown", "Suburbs", "Industrial Area",
    "University District", "Business Park", "Residential East", "Old Town", "Waterfront"
];

function randomBetween(min: number, max: number) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

function generateMockOrders(count: number): DeliveryOrder[] {
    const orders: DeliveryOrder[] = [];
    const startDate = new Date("2025-01-01");

    for (let i = 0; i < count; i++) {
        const dayOffset = randomBetween(0, 89);
        const hour = randomBetween(8, 23);
        const minute = randomBetween(0, 59);

        const orderDate = new Date(startDate);
        orderDate.setDate(orderDate.getDate() + dayOffset);
        orderDate.setHours(hour, minute, 0);

        // Delays are more likely during peak hours (19-22)
        const isPeakHour = hour >= 19 && hour <= 22;
        const zoneIndex = randomBetween(0, zones.length - 1);
        const isHighRiskZone = zoneIndex === 0; // Zone A is high risk

        let duration: number;
        if (isPeakHour && isHighRiskZone) {
            duration = randomBetween(40, 75);
        } else if (isPeakHour || isHighRiskZone) {
            duration = randomBetween(25, 55);
        } else {
            duration = randomBetween(15, 40);
        }

        const deliveryDate = new Date(orderDate.getTime() + duration * 60000);
        const isDelayed = duration > 35;

        orders.push({
            id: `ORD-${String(i + 1).padStart(5, "0")}`,
            orderTime: orderDate.toISOString(),
            deliveryTime: deliveryDate.toISOString(),
            location: locations[randomBetween(0, locations.length - 1)],
            zone: zones[zoneIndex],
            status: isDelayed ? "delayed" : "on-time",
            deliveryDuration: duration,
            lat: 28.6 + (Math.random() - 0.5) * 0.15,
            lng: 77.2 + (Math.random() - 0.5) * 0.15,
        });
    }

    return orders.sort((a, b) => new Date(a.orderTime).getTime() - new Date(b.orderTime).getTime());
}

export const mockOrders = generateMockOrders(500);

export function getMetrics(orders: DeliveryOrder[]) {
    const total = orders.length;
    const avgDelivery = orders.reduce((sum, o) => sum + o.deliveryDuration, 0) / total;
    const onTime = orders.filter(o => o.status === "on-time").length;
    const delayed = total - onTime;

    // Peak hours
    const hourCounts: Record<number, number> = {};
    orders.forEach(o => {
        const h = new Date(o.orderTime).getHours();
        hourCounts[h] = (hourCounts[h] || 0) + 1;
    });
    const peakHour = Object.entries(hourCounts).sort((a, b) => b[1] - a[1])[0]?.[0] || "12";

    return {
        avgDeliveryTime: Math.round(avgDelivery),
        onTimePercent: Math.round((onTime / total) * 100),
        delayedCount: delayed,
        peakHour: `${peakHour}:00`,
        totalOrders: total,
    };
}

export function getDeliveryTrends(orders: DeliveryOrder[]) {
    const dailyMap: Record<string, { total: number; count: number }> = {};
    orders.forEach(o => {
        const day = o.orderTime.slice(0, 10);
        if (!dailyMap[day]) dailyMap[day] = { total: 0, count: 0 };
        dailyMap[day].total += o.deliveryDuration;
        dailyMap[day].count++;
    });

    return Object.entries(dailyMap)
        .map(([date, { total, count }]) => ({
            date,
            avgTime: Math.round(total / count),
        }))
        .sort((a, b) => a.date.localeCompare(b.date));
}

export function getDelaysByHour(orders: DeliveryOrder[]) {
    const hourMap: Record<number, { delayed: number; total: number }> = {};
    for (let h = 8; h <= 23; h++) hourMap[h] = { delayed: 0, total: 0 };

    orders.forEach(o => {
        const h = new Date(o.orderTime).getHours();
        if (hourMap[h]) {
            hourMap[h].total++;
            if (o.status === "delayed") hourMap[h].delayed++;
        }
    });

    return Object.entries(hourMap).map(([hour, data]) => ({
        hour: `${hour}:00`,
        delays: data.delayed,
        total: data.total,
        delayRate: data.total > 0 ? Math.round((data.delayed / data.total) * 100) : 0,
    }));
}

export function getZonePerformance(orders: DeliveryOrder[]) {
    const zoneMap: Record<string, { totalDuration: number; delayed: number; count: number }> = {};
    orders.forEach(o => {
        if (!zoneMap[o.zone]) zoneMap[o.zone] = { totalDuration: 0, delayed: 0, count: 0 };
        zoneMap[o.zone].totalDuration += o.deliveryDuration;
        zoneMap[o.zone].count++;
        if (o.status === "delayed") zoneMap[o.zone].delayed++;
    });

    return Object.entries(zoneMap).map(([zone, data]) => ({
        zone,
        avgDeliveryTime: Math.round(data.totalDuration / data.count),
        delayRate: Math.round((data.delayed / data.count) * 100),
        totalOrders: data.count,
    }));
}

export function getStatusDistribution(orders: DeliveryOrder[]) {
    const onTime = orders.filter(o => o.status === "on-time").length;
    const delayed = orders.length - onTime;
    return [
        { name: "On-Time", value: onTime, fill: "hsl(160, 60%, 45%)" },
        { name: "Delayed", value: delayed, fill: "hsl(350, 80%, 55%)" },
    ];
}

export function generateInsights(orders: DeliveryOrder[]) {
    const hourData = getDelaysByHour(orders);
    const zoneData = getZonePerformance(orders);

    const peakDelayHours = hourData
        .sort((a, b) => b.delayRate - a.delayRate)
        .slice(0, 2);

    const worstZone = zoneData.sort((a, b) => b.avgDeliveryTime - a.avgDeliveryTime)[0];
    const bestZone = zoneData.sort((a, b) => a.avgDeliveryTime - b.avgDeliveryTime)[0];
    const metrics = getMetrics(orders);

    return [
        {
            icon: "⏰",
            title: "Peak Delay Window",
            text: `Delays are highest between ${peakDelayHours[0]?.hour} – ${peakDelayHours[1]?.hour} with up to ${peakDelayHours[0]?.delayRate}% delay rate.`,
            severity: "high" as const,
        },
        {
            icon: "📍",
            title: "High-Risk Zone",
            text: `${worstZone?.zone} has the highest average delivery time of ${worstZone?.avgDeliveryTime} minutes.`,
            severity: "high" as const,
        },
        {
            icon: "✅",
            title: "Best Performing Zone",
            text: `${bestZone?.zone} leads with an average delivery time of only ${bestZone?.avgDeliveryTime} minutes.`,
            severity: "low" as const,
        },
        {
            icon: "📊",
            title: "Overall Performance",
            text: `${metrics.onTimePercent}% of all deliveries arrive on time. ${metrics.delayedCount} orders experienced delays.`,
            severity: metrics.onTimePercent > 70 ? "low" as const : "medium" as const,
        },
        {
            icon: "🚀",
            title: "Recommendation",
            text: `Consider adding more delivery agents during ${peakDelayHours[0]?.hour} in ${worstZone?.zone} to reduce delays by up to 30%.`,
            severity: "medium" as const,
        },
    ];
}
