"use client";

import { motion } from "framer-motion";
import { useRouter } from "next/navigation";
import {
  ArrowRight,
  BarChart3,
  Building2,
  CheckCircle2,
  Clock,
  Gauge,
  LogIn,
  MapPin,
  Route,
  ShieldCheck,
  Sparkles,
  TrendingUp,
  Upload,
} from "lucide-react";
import { Button } from "@/components/ui/button";
import { useAuth } from "@/hooks/useAuth";

const features = [
  {
    icon: Clock,
    title: "Real-Time Tracking",
    desc: "Monitor delivery times and identify delays instantly",
  },
  {
    icon: MapPin,
    title: "Zone Analysis",
    desc: "Discover high-risk areas and optimize delivery routes",
  },
  {
    icon: BarChart3,
    title: "Smart Analytics",
    desc: "AI-powered insights to improve performance",
  },
  {
    icon: TrendingUp,
    title: "Trend Detection",
    desc: "Spot patterns and predict future bottlenecks",
  },
  {
    icon: Gauge,
    title: "Performance Score",
    desc: "Track SLA health with one clear reliability index",
  },
  {
    icon: ShieldCheck,
    title: "Risk Alerts",
    desc: "Get early warning signals for surge and failure zones",
  },
];

const quickMetrics = [
  { label: "Orders Processed / Day", value: "120K+" },
  { label: "Average Delay Reduction", value: "-23%" },
  { label: "ETA Accuracy Improvement", value: "+18%" },
  { label: "Actionable Insights / Week", value: "3.4K" },
];

const steps = [
  {
    icon: Upload,
    title: "Ingest",
    desc: "Upload delivery logs or connect your order data pipeline.",
  },
  {
    icon: BarChart3,
    title: "Analyze",
    desc: "Detect bottlenecks by zone, shift, restaurant, and rider cohort.",
  },
  {
    icon: Route,
    title: "Optimize",
    desc: "Apply route and staffing recommendations with confidence.",
  },
];

const partners = ["SwiftBite", "UrbanEats", "DashCart", "QuickBasket", "MetroMeals"];

const testimonials = [
  {
    quote:
      "Insight Flow helped us reduce peak-hour delays by 26% within six weeks across three cities.",
    name: "Nadia Singh",
    role: "Head of Logistics, SwiftBite",
  },
  {
    quote:
      "The zone risk intelligence is excellent. We can spot service pressure before SLA drops.",
    name: "Arun Patel",
    role: "Ops Director, UrbanEats",
  },
  {
    quote:
      "We finally have a single source of truth for route efficiency, order velocity, and delivery confidence.",
    name: "Mina Joseph",
    role: "VP Operations, DashCart",
  },
];

const container = {
  hidden: { opacity: 0 },
  show: { opacity: 1, transition: { staggerChildren: 0.1 } },
};

const item = {
  hidden: { opacity: 0, y: 18 },
  show: { opacity: 1, y: 0 },
};

export default function LandingPage() {
  const router = useRouter();
  const { user } = useAuth();

  return (
    <div className="min-h-screen relative overflow-x-clip">
      <div className="bg-grid-overlay" />

      <nav className="fixed top-0 left-0 right-0 z-30 px-4 md:px-6 py-4 backdrop-blur-2xl bg-slate-950/45 border-b border-white/10">
        <div className="mx-auto flex w-full max-w-7xl items-center justify-between">
          <span className="text-primary-foreground font-bold text-xl tracking-wide inline-flex items-center gap-3">
            <span className="inline-flex h-8 w-8 items-center justify-center rounded-lg gradient-primary text-xs font-black text-[#061018] shadow-lg shadow-orange-500/30">
              IF
            </span>
            Insight Flow
          </span>
          <div className="flex gap-3">
            {user ? (
              <Button
                size="sm"
                className="gradient-primary text-primary-foreground rounded-lg border-0 font-semibold shadow-lg px-4"
                onClick={() => router.push("/dashboard")}
              >
                Dashboard <ArrowRight className="ml-2 h-4 w-4" />
              </Button>
            ) : (
              <Button
                size="sm"
                variant="outline"
                className="border-primary-foreground/35 text-primary-foreground hover:bg-primary-foreground/12 rounded-lg font-semibold px-4"
                onClick={() => router.push("/auth")}
              >
                <LogIn className="mr-2 h-4 w-4" /> Sign In
              </Button>
            )}
          </div>
        </div>
      </nav>

      <section className="gradient-hero relative overflow-hidden min-h-screen flex items-center justify-center pt-24 pb-16">
        <div className="absolute inset-0 opacity-35">
          {[...Array(5)].map((_, i) => (
            <div
              key={i}
              className="absolute rounded-full gradient-primary"
              style={{
                width: `${240 + i * 110}px`,
                height: `${240 + i * 110}px`,
                top: `${8 + i * 15}%`,
                left: `${-8 + i * 20}%`,
                filter: "blur(96px)",
              }}
            />
          ))}
        </div>

        <div className="container mx-auto px-6 md:px-8 relative z-10 grid gap-10 lg:gap-16 lg:grid-cols-[1.05fr_0.95fr] items-center max-w-7xl">
          <div className="max-w-3xl">
            <motion.div
              initial={{ opacity: 0, y: 40 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.7 }}
            >
              <span className="inline-flex items-center gap-2.5 px-5 py-2 rounded-full text-sm font-semibold bg-gradient-to-r from-orange-500/95 to-orange-600/95 text-white mb-5 shadow-lg shadow-orange-500/50 hover:shadow-xl transition-all border border-orange-400/40 backdrop-blur-sm">
                <Sparkles className="h-4 w-4" /> Enterprise Delivery Intelligence
              </span>
            </motion.div>

            <motion.h1
              className="text-4xl md:text-6xl font-black leading-[0.98] tracking-tight mb-6"
              initial={{ opacity: 0, y: 40 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.7, delay: 0.15 }}
            >
              <span className="text-primary-foreground block">Smart Food</span>
              <span className="text-gradient block">Delivery Analytics</span>
            </motion.h1>

            <motion.p
              className="text-lg md:text-xl text-primary-foreground/80 mb-10 max-w-2xl leading-relaxed font-medium"
              initial={{ opacity: 0, y: 30 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.7, delay: 0.3 }}
            >
              Analyze delays, optimize driver routing, and improve customer satisfaction with real-time, decision-ready performance insights.
            </motion.p>

            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.7, delay: 0.45 }}
              className="flex flex-col sm:flex-row sm:items-center gap-4"
            >
              <Button
                size="lg"
                className="gradient-primary text-primary-foreground px-8 py-5 text-base font-bold rounded-xl shadow-lg shadow-orange-950/50 hover:shadow-2xl hover:scale-105 transition-all duration-300 group"
                onClick={() => router.push(user ? "/dashboard" : "/auth")}
              >
                {user ? "View Dashboard" : "Sign In to Continue"}
                <ArrowRight className="ml-3 h-5 w-5 group-hover:translate-x-1 transition-transform" />
              </Button>
              <p className="text-sm text-primary-foreground/70 font-medium max-w-[18rem]">
                Trusted by operations teams across 40+ delivery zones.
              </p>
            </motion.div>

            <motion.div
              initial={{ opacity: 0, y: 18 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.7, delay: 0.55 }}
              className="mt-9 grid gap-2 text-sm text-primary-foreground/78 font-medium"
            >
              {[
                "Real-time SLA visibility",
                "Predictive bottleneck alerts",
                "City-level route optimization",
              ].map((point) => (
                <div key={point} className="inline-flex items-center gap-3 hover:text-primary-foreground transition-colors">
                  <CheckCircle2 className="h-5 w-5 text-emerald-400 flex-shrink-0" />
                  <span>{point}</span>
                </div>
              ))}
            </motion.div>
          </div>

          <motion.div
            className="glass-card rounded-3xl p-6 bg-card/60 backdrop-blur-2xl border border-white/12 animate-float w-full max-w-[340px] mx-auto lg:mx-0 lg:justify-self-end lg:mt-10 shadow-lg shadow-orange-950/25"
            initial={{ opacity: 0, x: 60, y: 20 }}
            animate={{ opacity: 1, x: 0, y: 0 }}
            transition={{ duration: 0.8, delay: 0.6 }}
          >
            <div className="space-y-3.5">
              {[
                { label: "Avg Delivery", value: "28 min", tone: "text-green-400" },
                { label: "On-Time Rate", value: "91%", tone: "text-orange-300" },
                { label: "Orders Today", value: "1,247", tone: "text-yellow-300" },
              ].map((stat) => (
                <div
                  key={stat.label}
                  className="flex items-center gap-3.5 rounded-2xl border border-white/12 bg-white/8 px-4 py-3"
                >
                  <div className="h-11 w-11 rounded-xl gradient-primary flex items-center justify-center shadow-md shadow-orange-500/30 flex-shrink-0">
                    <BarChart3 className="h-4.5 w-4.5 text-primary-foreground" />
                  </div>
                  <div className="flex-1 min-w-0">
                    <p className="text-xs leading-snug text-primary-foreground/58 font-bold uppercase tracking-[0.08em]">
                      {stat.label}
                    </p>
                    <p className={`text-[2.15rem] leading-none font-black mt-1 ${stat.tone}`}>
                      {stat.value}
                    </p>
                  </div>
                </div>
              ))}
            </div>
          </motion.div>
        </div>
      </section>

      <section className="px-6 py-10 -mt-6 relative z-20">
        <motion.div
          variants={container}
          initial="hidden"
          whileInView="show"
          viewport={{ once: true }}
          className="container mx-auto grid grid-cols-2 lg:grid-cols-4 gap-5 md:gap-7 max-w-7xl"
        >
          {quickMetrics.map((metric) => (
            <motion.div
              variants={item}
              key={metric.label}
              className="surface-panel rounded-3xl p-7 md:p-8 text-center shadow-xl hover:shadow-2xl transition-shadow"
            >
              <p className="text-2xl md:text-3xl xl:text-4xl font-black text-slate-900 leading-tight">{metric.value}</p>
              <p className="mt-2 text-xs text-slate-600 font-bold uppercase tracking-wide">{metric.label}</p>
            </motion.div>
          ))}
        </motion.div>
      </section>

      <section className="px-6 py-8">
        <div className="container mx-auto max-w-7xl">
          <div className="rounded-3xl border border-white/12 bg-gradient-to-br from-white/[0.06] to-white/[0.02] backdrop-blur-lg p-8 md:p-10 text-center hover:border-white/20 transition-all duration-300 group">
            <p className="text-xs uppercase tracking-[0.32em] text-slate-400 mb-6 font-bold group-hover:text-slate-500 transition-colors">
              Trusted By High-Volume Delivery Teams
            </p>
            <div className="flex flex-wrap items-center justify-center gap-4 md:gap-6">
              {partners.map((partner) => (
                <span
                  key={partner}
                  className="inline-flex items-center gap-2 rounded-full border-2 border-orange-200 bg-gradient-to-r from-white to-orange-50 px-5 py-2.5 text-xs font-bold text-slate-700 hover:shadow-lg hover:border-orange-400 hover:scale-110 transition-all duration-300 group"
                >
                  <Building2 className="h-5 w-5 text-orange-500 flex-shrink-0 group-hover:scale-125 transition-transform" />
                  {partner}
                </span>
              ))}
            </div>
          </div>
        </div>
      </section>

      <section className="py-16 px-6 bg-[#fffaf6]">
        <div className="container mx-auto max-w-7xl">
          <motion.div
            className="text-center mb-14"
            initial={{ opacity: 0, y: 30 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
          >
            <h2 className="text-4xl md:text-5xl lg:text-6xl font-black mb-6 text-slate-900 leading-tight bg-gradient-to-r from-slate-900 to-orange-700 bg-clip-text text-transparent">
              More Than A Dashboard
            </h2>
            <p className="text-slate-600 text-base md:text-lg max-w-3xl mx-auto leading-relaxed font-medium">
              Built for city-scale delivery teams that need decisions, not just charts.
            </p>
          </motion.div>

          <motion.div
            variants={container}
            initial="hidden"
            whileInView="show"
            viewport={{ once: true }}
            className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-7 md:gap-10"
          >
            {features.map((feature) => (
              <motion.div
                variants={item}
                key={feature.title}
                className="metric-card group cursor-pointer h-full hover:shadow-2xl transition-all duration-300"
              >
                <div className="h-16 w-16 rounded-2xl gradient-primary flex items-center justify-center mb-7 group-hover:scale-110 transition-transform duration-300 shadow-lg shadow-orange-500/25 group-hover:shadow-orange-500/50">
                  <feature.icon className="h-9 w-9 text-primary-foreground" />
                </div>
                <h3 className="text-lg font-bold mb-4 text-slate-900 group-hover:text-orange-600 transition-colors">{feature.title}</h3>
                <p className="text-slate-600 text-sm leading-7 group-hover:text-slate-700 transition-colors">{feature.desc}</p>
              </motion.div>
            ))}
          </motion.div>
        </div>
      </section>

      <section className="py-28 px-6 bg-[#fff7f2]">
        <div className="container mx-auto max-w-7xl">
          <motion.div
            className="rounded-3xl border-2 border-orange-200/80 bg-gradient-to-br from-white to-orange-50 p-12 md:p-16 lg:p-20 shadow-3xl hover:shadow-orange-950/30 transition-shadow group"
            initial={{ opacity: 0, y: 24 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
          >
            <h3 className="text-4xl md:text-5xl font-black text-slate-900 mb-4 bg-gradient-to-r from-slate-900 to-orange-700 bg-clip-text text-transparent">
              How Insight Flow Works
            </h3>
            <p className="text-slate-600 mb-12 text-base font-medium">Three simple steps to operationalize your delivery intelligence.</p>
            <div className="grid gap-7 md:grid-cols-3">
              {steps.map((step, index) => (
                <div
                  key={step.title}
                  className="rounded-2xl border-2 border-orange-100 bg-gradient-to-br from-[#fffbf8] to-[#fff8f5] p-8 md:p-10 hover:shadow-lg hover:border-orange-200 transition-all group duration-300"
                >
                  <span className="inline-flex h-14 w-14 items-center justify-center rounded-xl gradient-primary text-primary-foreground font-bold shadow-lg shadow-orange-500/25 group-hover:shadow-orange-500/50 group-hover:scale-110 transition-transform duration-300">
                    <step.icon className="h-7 w-7" />
                  </span>
                  <p className="mt-5 text-xs font-bold tracking-[0.28em] text-slate-500 uppercase group-hover:text-orange-600 transition-colors">
                    STEP {index + 1}
                  </p>
                  <h4 className="mt-3 text-lg font-bold text-slate-900 group-hover:text-orange-700 transition-colors">{step.title}</h4>
                  <p className="mt-4 text-slate-600 text-sm leading-7 group-hover:text-slate-700 transition-colors">{step.desc}</p>
                </div>
              ))}
            </div>
          </motion.div>
        </div>
      </section>

      <section className="py-28 px-6 bg-[#fffaf6]">
        <div className="container mx-auto max-w-7xl">
          <motion.div
            className="text-center mb-20"
            initial={{ opacity: 0, y: 24 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
          >
            <h3 className="text-4xl md:text-5xl font-black text-slate-900 mb-6 bg-gradient-to-r from-slate-900 to-orange-700 bg-clip-text text-transparent">
              What Operations Leaders Say
            </h3>
            <p className="mt-2 text-slate-600 max-w-3xl mx-auto text-base font-medium">
              Teams use Insight Flow to increase on-time delivery confidence and act faster on operational risk.
            </p>
          </motion.div>

          <motion.div
            variants={container}
            initial="hidden"
            whileInView="show"
            viewport={{ once: true }}
            className="grid gap-8 md:grid-cols-3"
          >
            {testimonials.map((testimonial) => (
              <motion.blockquote
                variants={item}
                key={testimonial.name}
                className="surface-panel rounded-2xl p-10 flex flex-col hover:shadow-2xl transition-all duration-300 group"
              >
                <div className="flex items-start gap-3 mb-4">
                  {[...Array(5)].map((_, i) => (
                    <span key={i} className="text-yellow-400 text-sm">★</span>
                  ))}
                </div>
                <p className="text-slate-700 leading-8 flex-1 text-base group-hover:text-slate-900 transition-colors italic">
                  &ldquo;{testimonial.quote}&rdquo;
                </p>
                <footer className="mt-8 pt-8 border-t-2 border-slate-200 group-hover:border-orange-200 transition-colors">
                  <p className="font-bold text-slate-900 text-base group-hover:text-orange-700 transition-colors">{testimonial.name}</p>
                  <p className="text-sm text-slate-500 mt-1 group-hover:text-slate-600 transition-colors">{testimonial.role}</p>
                </footer>
              </motion.blockquote>
            ))}
          </motion.div>
        </div>
      </section>

      <section className="py-24 px-6">
        <div className="container mx-auto max-w-7xl">
          <motion.div
            className="gradient-hero rounded-3xl p-14 md:p-16 lg:p-20 text-center relative overflow-hidden shadow-2xl shadow-orange-950/45 hover:shadow-orange-950/60 transition-all duration-300 group"
            initial={{ opacity: 0, scale: 0.95 }}
            whileInView={{ opacity: 1, scale: 1 }}
            viewport={{ once: true }}
          >
            <h2 className="text-4xl md:text-5xl lg:text-6xl font-black text-primary-foreground mb-8 leading-tight relative z-10">
              Ready to optimize your deliveries?
            </h2>
            <p className="text-primary-foreground/80 text-lg md:text-xl mb-10 max-w-3xl mx-auto leading-relaxed font-medium relative z-10">
              Upload your data and get instant insights to reduce delays and boost efficiency.
            </p>
            <Button
              size="lg"
              className="gradient-primary text-primary-foreground px-10 py-7 text-lg font-bold rounded-xl hover:scale-105 transition-all shadow-lg shadow-orange-950/50 hover:shadow-2xl relative z-10"
              onClick={() => router.push("/dashboard")}
            >
              Get Started <ArrowRight className="ml-3 h-6 w-6" />
            </Button>
          </motion.div>
        </div>
      </section>
    </div>
  );
}
