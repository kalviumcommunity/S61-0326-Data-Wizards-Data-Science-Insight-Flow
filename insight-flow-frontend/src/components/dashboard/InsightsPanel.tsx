import { motion } from "framer-motion";

interface Insight {
  icon: string;
  title: string;
  text: string;
  severity: "high" | "medium" | "low";
}

interface Props {
  insights: Insight[];
}

const severityStyles = {
  high: "border-l-red-500",
  medium: "border-l-orange-400",
  low: "border-l-green-500",
};

const InsightsPanel = ({ insights }: Props) => (
  <div className="glass-card rounded-2xl border border-[#f3ded2] bg-white p-6 shadow-[0_12px_30px_rgba(60,20,8,0.08)]">
    <h3 className="mb-4 text-xl font-bold text-[#2b211b]">Auto-Generated Insights</h3>
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
      {insights.map((insight, i) => (
        <motion.div
          key={i}
          className={`rounded-xl border border-[#f3ded2] border-l-4 bg-[#fff9f6] p-4 shadow-sm ${severityStyles[insight.severity]}`}
          initial={{ opacity: 0, x: -20 }}
          animate={{ opacity: 1, x: 0 }}
          transition={{ delay: i * 0.1 }}
        >
          <div className="flex items-center gap-2 mb-2">
            <span className="text-xl">{insight.icon}</span>
            <h4 className="font-semibold text-sm">{insight.title}</h4>
          </div>
          <p className="text-sm text-muted-foreground">{insight.text}</p>
        </motion.div>
      ))}
    </div>
  </div>
);

export default InsightsPanel;
