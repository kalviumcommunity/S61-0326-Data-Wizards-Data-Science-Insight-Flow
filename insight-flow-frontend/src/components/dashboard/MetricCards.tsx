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
        { icon: Clock, label: "Avg Delivery Time", value: `${metrics.avgDeliveryTime} min`, gradient: "gradient-primary" },
        { icon: CheckCircle, label: "On-Time Rate", value: `${metrics.onTimePercent}%`, gradient: "gradient-primary" },
        { icon: AlertTriangle, label: "Delayed Orders", value: metrics.delayedCount.toString(), gradient: "gradient-primary" },
        { icon: TrendingUp, label: "Peak Hour", value: metrics.peakHour, gradient: "gradient-primary" },
    ];

    return (
        <div className="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-4">
            {cards.map((card, i) => (
                <motion.div
                    key={card.label}
                    className="metric-card flex items-center gap-4"
                    initial={{ opacity: 0, y: 20 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ delay: i * 0.1 }}
                >
                    <div className={`h-12 w-12 rounded-xl ${card.gradient} flex shrink-0 items-center justify-center`}>
                        <card.icon className="h-5 w-5 text-primary-foreground" />
                    </div>
                    <div>
                        <p className="text-sm text-[#9ca3af]">{card.label}</p>
                        <p className="text-[36px] leading-9 font-bold tracking-tight text-[#1f2937]">{card.value}</p>
                    </div>
                </motion.div>
            ))}
        </div>
    );
};

export default MetricCards;
