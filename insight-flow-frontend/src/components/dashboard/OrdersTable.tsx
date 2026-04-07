import { useMemo } from "react";
import { motion } from "framer-motion";
import {
    Table,
    TableBody,
    TableCell,
    TableHead,
    TableHeader,
    TableRow,
} from "@/components/ui/table";
import { Badge } from "@/components/ui/badge";
import type { DeliveryOrder } from "@/lib/mockData";
import { useState } from "react";
import { Input } from "@/components/ui/input";
import { Search, ChevronLeft, ChevronRight, ClipboardList } from "lucide-react";
import { Button } from "@/components/ui/button";

interface Props {
    orders: DeliveryOrder[];
}

const PAGE_SIZE = 15;

const OrdersTable = ({ orders }: Props) => {
    const [search, setSearch] = useState("");
    const [page, setPage] = useState(0);
    const [sortCol, setSortCol] = useState<"deliveryDuration" | "orderTime">("orderTime");
    const [sortDir, setSortDir] = useState<"asc" | "desc">("desc");

    const filtered = useMemo(() => {
        let result = orders;
        if (search) {
            const q = search.toLowerCase();
            result = result.filter(
                o => o.id.toLowerCase().includes(q) || o.location.toLowerCase().includes(q) || o.zone.toLowerCase().includes(q)
            );
        }
        result = [...result].sort((a, b) => {
            const aVal = sortCol === "deliveryDuration" ? a.deliveryDuration : new Date(a.orderTime).getTime();
            const bVal = sortCol === "deliveryDuration" ? b.deliveryDuration : new Date(b.orderTime).getTime();
            return sortDir === "asc" ? aVal - bVal : bVal - aVal;
        });
        return result;
    }, [orders, search, sortCol, sortDir]);

    const totalPages = Math.ceil(filtered.length / PAGE_SIZE);
    const paged = filtered.slice(page * PAGE_SIZE, (page + 1) * PAGE_SIZE);

    const toggleSort = (col: "deliveryDuration" | "orderTime") => {
        if (sortCol === col) setSortDir(d => d === "asc" ? "desc" : "asc");
        else { setSortCol(col); setSortDir("desc"); }
    };

    return (
        <div className="glass-card rounded-2xl bg-white p-6">
            <div className="mb-4 flex flex-wrap items-center justify-between gap-3">
                <h3 className="flex items-center gap-2 text-3xl font-semibold text-[#1f1f1f]">
                    <ClipboardList className="h-5 w-5" />
                    <span>Orders Table</span>
                </h3>
                <div className="relative">
                    <Search className="absolute left-3 top-2.5 h-4 w-4 text-[#a1a1aa]" />
                    <Input
                        placeholder="Search orders..."
                        className="h-10 w-56 rounded-xl border-[#ece7e3] pl-9 text-sm placeholder:text-[#a8a29e] sm:w-64"
                        value={search}
                        onChange={e => { setSearch(e.target.value); setPage(0); }}
                    />
                </div>
            </div>

            <div className="overflow-x-auto">
                <Table>
                    <TableHeader>
                        <TableRow>
                            <TableHead>Order ID</TableHead>
                            <TableHead className="cursor-pointer select-none" onClick={() => toggleSort("orderTime")}>
                                Order Time {sortCol === "orderTime" ? (sortDir === "asc" ? "↑" : "↓") : ""}
                            </TableHead>
                            <TableHead>Location</TableHead>
                            <TableHead>Zone</TableHead>
                            <TableHead className="cursor-pointer select-none" onClick={() => toggleSort("deliveryDuration")}>
                                Duration {sortCol === "deliveryDuration" ? (sortDir === "asc" ? "↑" : "↓") : ""}
                            </TableHead>
                            <TableHead>Status</TableHead>
                        </TableRow>
                    </TableHeader>
                    <TableBody>
                        {paged.map((order, i) => (
                            <motion.tr
                                key={order.id}
                                initial={{ opacity: 0, x: -10 }}
                                animate={{ opacity: 1, x: 0 }}
                                transition={{ delay: i * 0.02 }}
                                className="border-b border-border/50"
                            >
                                <TableCell className="font-mono text-sm">{order.id}</TableCell>
                                <TableCell className="text-sm">
                                    {new Date(order.orderTime).toLocaleString("en-US", {
                                        month: "short", day: "numeric", hour: "2-digit", minute: "2-digit",
                                    })}
                                </TableCell>
                                <TableCell className="text-sm">{order.location}</TableCell>
                                <TableCell className="text-sm">{order.zone}</TableCell>
                                <TableCell className="text-sm font-medium">{order.deliveryDuration} min</TableCell>
                                <TableCell>
                                    <Badge
                                        variant={order.status === "on-time" ? "default" : "destructive"}
                                        className={
                                            order.status === "on-time"
                                                ? "border-green-200 bg-green-100 text-green-700"
                                                : "border-red-500 bg-red-500 text-white"
                                        }
                                    >
                                        {order.status}
                                    </Badge>
                                </TableCell>
                            </motion.tr>
                        ))}
                    </TableBody>
                </Table>
            </div>

            <div className="flex items-center justify-between mt-4 text-sm text-muted-foreground">
                <span>Showing {page * PAGE_SIZE + 1}–{Math.min((page + 1) * PAGE_SIZE, filtered.length)} of {filtered.length}</span>
                <div className="flex gap-2">
                    <Button variant="outline" size="sm" onClick={() => setPage(p => p - 1)} disabled={page === 0}>
                        <ChevronLeft className="h-4 w-4" />
                    </Button>
                    <Button variant="outline" size="sm" onClick={() => setPage(p => p + 1)} disabled={page >= totalPages - 1}>
                        <ChevronRight className="h-4 w-4" />
                    </Button>
                </div>
            </div>
        </div>
    );
};

export default OrdersTable;
