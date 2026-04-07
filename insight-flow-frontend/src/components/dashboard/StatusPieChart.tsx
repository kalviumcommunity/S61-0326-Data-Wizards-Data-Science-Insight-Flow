interface Props {
    data: { name: string; value: number; fill: string }[];
}

import { PieChart, Pie, Cell, Tooltip, ResponsiveContainer, Legend } from "recharts";

const StatusPieChart = ({ data }: Props) => (
    <div className="glass-card rounded-xl p-6">
        <h3 className="text-lg font-semibold mb-4">🥧 On-Time vs Delayed</h3>
        <ResponsiveContainer width="100%" height={300}>
            <PieChart>
                <Pie
                    data={data}
                    cx="50%"
                    cy="50%"
                    innerRadius={70}
                    outerRadius={110}
                    paddingAngle={4}
                    dataKey="value"
                    strokeWidth={0}
                >
                    {data.map((entry, i) => (
                        <Cell key={i} fill={entry.fill} />
                    ))}
                </Pie>
                <Tooltip
                    contentStyle={{
                        backgroundColor: "hsl(0 0% 100%)",
                        border: "1px solid hsl(30 15% 88%)",
                        borderRadius: "12px",
                    }}
                />
                <Legend />
            </PieChart>
        </ResponsiveContainer>
    </div>
);

export default StatusPieChart;
