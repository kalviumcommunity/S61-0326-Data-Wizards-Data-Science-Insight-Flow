"use client";

import { useEffect } from "react";
import { useRouter } from "next/navigation";
import { ArrowLeft, BarChart3, Clock3, LogOut, MapPinned, TrendingUp, User } from "lucide-react";
import { useAuth } from "@/hooks/useAuth";

const metrics = [
  { label: "Orders Processed", value: "120K", icon: BarChart3 },
  { label: "Avg Delay", value: "28m", icon: Clock3 },
  { label: "Hot Zones", value: "14", icon: MapPinned },
  { label: "Trend Lift", value: "+18%", icon: TrendingUp },
];

export default function DashboardPage() {
  const router = useRouter();
  const { user, signOut } = useAuth();

  useEffect(() => {
    if (!user) {
      router.push("/auth");
    }
  }, [router, user]);

  if (!user) {
    return null;
  }

  return (
    <main className="min-h-screen bg-[radial-gradient(circle_at_top,_#542f1d_0%,_#231512_55%,_#140d0b_100%)] px-4 py-6 text-[#f7eee8]">
      <div className="mx-auto max-w-7xl">
        <button
          type="button"
          onClick={() => router.push("/")}
          className="inline-flex items-center gap-2 text-sm font-medium text-[#e7d9d2]/85 transition hover:text-white"
        >
          <ArrowLeft className="h-4 w-4" />
          Back to home
        </button>

        <section className="mt-8 rounded-[32px] border border-white/10 bg-white/8 p-6 shadow-[0_24px_80px_rgba(0,0,0,0.35)] backdrop-blur-2xl sm:p-8">
          <div className="flex flex-col gap-8 lg:flex-row lg:items-end lg:justify-between">
            <div>
              <p className="text-sm font-semibold uppercase tracking-[0.24em] text-[#f5b19c]">Insight Flow</p>
              <h1 className="mt-3 text-4xl font-black tracking-tight sm:text-5xl">Dashboard</h1>
              <p className="mt-3 max-w-2xl text-sm leading-6 text-[#f0ddd3]/80 sm:text-base">
                Track delivery performance, identify bottlenecks, and review operational trends in one place.
              </p>
            </div>
            <div className="flex items-center gap-3 rounded-2xl border border-white/10 bg-black/15 px-5 py-4 text-sm text-[#f0ddd3]/85">
              <div className="inline-flex h-10 w-10 items-center justify-center rounded-full bg-[linear-gradient(135deg,#ff6a2f_0%,#ff4d4f_100%)] text-white">
                <User className="h-5 w-5" />
              </div>
              <div>
                <p className="font-semibold text-white">Signed in as</p>
                <p className="text-[#f0ddd3]/80">{user.email}</p>
              </div>
              <button
                type="button"
                onClick={signOut}
                className="ml-2 inline-flex items-center gap-2 rounded-xl border border-white/10 bg-white/8 px-4 py-2 text-sm font-semibold text-white transition hover:bg-white/15"
              >
                <LogOut className="h-4 w-4" />
                Sign out
              </button>
            </div>
          </div>

          <div className="mt-8 grid gap-4 sm:grid-cols-2 xl:grid-cols-4">
            {metrics.map((metric) => {
              const Icon = metric.icon;

              return (
                <article
                  key={metric.label}
                  className="rounded-3xl border border-white/10 bg-white/8 p-5 shadow-lg shadow-black/15"
                >
                  <div className="flex items-center justify-between gap-4">
                    <div>
                      <p className="text-sm text-[#f0ddd3]/70">{metric.label}</p>
                      <p className="mt-2 text-3xl font-black tracking-tight">{metric.value}</p>
                    </div>
                    <div className="inline-flex h-12 w-12 items-center justify-center rounded-2xl bg-[linear-gradient(135deg,#ff6a2f_0%,#ff4d4f_100%)] text-white shadow-lg shadow-orange-500/30">
                      <Icon className="h-5 w-5" />
                    </div>
                  </div>
                </article>
              );
            })}
          </div>

          <div className="mt-8 grid gap-6 lg:grid-cols-[1.2fr_0.8fr]">
            <article className="rounded-3xl border border-white/10 bg-[#fffaf8] p-6 text-[#2c211d] shadow-xl shadow-black/10">
              <h2 className="text-xl font-bold">Today’s overview</h2>
              <div className="mt-5 h-64 rounded-2xl bg-[linear-gradient(135deg,#fff1ea_0%,#ffe0d3_50%,#ffd4ca_100%)] p-5">
                <div className="flex h-full flex-col justify-between">
                  <div className="flex items-center justify-between text-sm font-medium text-[#7a6256]">
                    <span>Delivery volume</span>
                    <span>Peak at 7 PM</span>
                  </div>
                  <div className="grid grid-cols-6 items-end gap-3">
                    {[32, 44, 58, 36, 66, 52].map((height, index) => (
                      <div key={index} className="flex flex-col items-center gap-2">
                        <div
                          className="w-full rounded-t-2xl bg-[linear-gradient(180deg,#ff6a2f_0%,#ff4d4f_100%)]"
                          style={{ height: `${height * 2}px` }}
                        />
                        <span className="text-xs font-semibold text-[#8d6d60]">{index + 1}</span>
                      </div>
                    ))}
                  </div>
                </div>
              </div>
            </article>

            <article className="rounded-3xl border border-white/10 bg-white/8 p-6 shadow-xl shadow-black/10">
              <h2 className="text-xl font-bold">Next actions</h2>
              <ul className="mt-5 space-y-4 text-sm text-[#f0ddd3]/82">
                <li className="rounded-2xl border border-white/10 bg-black/10 px-4 py-4">Review the top delay zones and address hotspots.</li>
                <li className="rounded-2xl border border-white/10 bg-black/10 px-4 py-4">Compare this week’s SLA against the previous week.</li>
                <li className="rounded-2xl border border-white/10 bg-black/10 px-4 py-4">Check driver load and route timing for peak hours.</li>
              </ul>
            </article>
          </div>
        </section>
      </div>
    </main>
  );
}