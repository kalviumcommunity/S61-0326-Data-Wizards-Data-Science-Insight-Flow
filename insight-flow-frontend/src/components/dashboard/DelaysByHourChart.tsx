interface Props {
    data: { hour: string; delays: number; total: number; delayRate: number }[];
}

import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from "recharts";

const DelaysByHourChart = ({ data }: Props) => (
    <div className="glass-card rounded-xl p-6">
        <h3 className="text-lg font-semibold mb-4">📊 Delays by Hour of Day</h3>
        <ResponsiveContainer width="100%" height={300}>
            <BarChart data={data}>
                <CartesianGrid strokeDasharray="3 3" stroke="hsl(30 15% 88%)" />
                <XAxis dataKey="hour" tick={{ fontSize: 11 }} />
                <YAxis tick={{ fontSize: 11 }} />
                <Tooltip
                    contentStyle={{
                        backgroundColor: "hsl(0 0% 100%)",
                        border: "1px solid hsl(30 15% 88%)",
                        borderRadius: "12px",
                    }}
                />
                <Bar dataKey="delays" fill="hsl(350 80% 55%)" radius={[6, 6, 0, 0]} name="Delayed Orders" />
                <Bar dataKey="total" fill="hsl(18 90% 55% / 0.3)" radius={[6, 6, 0, 0]} name="Total Orders" />
            </BarChart>
        </ResponsiveContainer>
    </div>
);

export default DelaysByHourChart;
