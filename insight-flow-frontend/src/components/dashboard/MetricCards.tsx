import { motion } from "framer-motion";
import { Clock, CheckCircle, AlertTriangle, TrendingUp } from "lucide-react";

interface MetricCardsProps {
    metrics: {
        avgDeliveryTime: number;
        onTimePercent: number;
        delayedCount: number;
        peakHour: string;
    };
}

const MetricCards = ({ metrics }: MetricCardsProps) => {
    const cards = [
        { 
            icon: Clock, 
            label: "Avg Delivery Time", 
            value: `${metrics.avgDeliveryTime} min`, 
            bgGradient: "from-violet-50 to-violet-100",
            iconBg: "bg-gradient-to-br from-violet-400 to-violet-600"
        },
        { 
            icon: CheckCircle, 
            label: "On-Time Rate", 
            value: `${metrics.onTimePercent}%`, 
            bgGradient: "from-emerald-50 to-emerald-100",
            iconBg: "bg-gradient-to-br from-emerald-400 to-emerald-600"
        },
        { 
            icon: AlertTriangle, 
            label: "Delayed Orders", 
            value: metrics.delayedCount.toString(), 
            bgGradient: "from-red-50 to-red-100",
            iconBg: "bg-gradient-to-br from-red-400 to-red-600"
        },
        { 
            icon: TrendingUp, 
            label: "Peak Hour", 
            value: metrics.peakHour, 
            bgGradient: "from-purple-50 to-purple-100",
            iconBg: "bg-gradient-to-br from-purple-400 to-purple-600"
        },
    ];

    return (
        <div className="grid grid-cols-1 gap-5 sm:grid-cols-2 lg:grid-cols-4">
            {cards.map((card, i) => (
                <motion.div
                    key={card.label}
                    className={`rounded-xl border border-gray-200 bg-gradient-to-br ${card.bgGradient} p-5 shadow-sm transition-all hover:shadow-md hover:scale-105`}
                    initial={{ opacity: 0, y: 20 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ delay: i * 0.1 }}
                >
                    <div className="flex items-start justify-between">
                        <div className="flex-1">
                            <p className="text-xs font-semibold uppercase tracking-wide text-gray-600">{card.label}</p>
                            <p className="mt-3 text-2xl font-bold text-gray-900">{card.value}</p>
                        </div>
                        <div className={`flex h-11 w-11 items-center justify-center rounded-lg ${card.iconBg} shrink-0`}>
                            <card.icon className="h-5 w-5 text-white" />
                        </div>
                    </div>
                </motion.div>
            ))}
        </div>
    );
};

export default MetricCards;
