import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from "recharts";

interface Props {
    data: { date: string; avgTime: number }[];
}

const DeliveryTrendChart = ({ data }: Props) => (
    <div className="glass-card rounded-xl p-6">
        <h3 className="text-lg font-semibold mb-4">📈 Delivery Time Trends</h3>
        <ResponsiveContainer width="100%" height={300}>
            <LineChart data={data}>
                <CartesianGrid strokeDasharray="3 3" stroke="hsl(30 15% 88%)" />
                <XAxis dataKey="date" tick={{ fontSize: 11 }} tickFormatter={(v) => v.slice(5)} />
                <YAxis tick={{ fontSize: 11 }} unit=" min" />
                <Tooltip
                    contentStyle={{
                        backgroundColor: "hsl(0 0% 100%)",
                        border: "1px solid hsl(30 15% 88%)",
                        borderRadius: "12px",
                    }}
                />
                <Line
                    type="monotone"
                    dataKey="avgTime"
                    stroke="hsl(18 90% 55%)"
                    strokeWidth={2.5}
                    dot={false}
                    name="Avg Delivery Time"
                />
            </LineChart>
        </ResponsiveContainer>
    </div>
);

export default DeliveryTrendChart;
