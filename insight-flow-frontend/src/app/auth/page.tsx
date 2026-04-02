"use client";

import { useState, type FormEvent } from "react";
import { useRouter } from "next/navigation";
import {
  ArrowLeft,
  CircleUserRound,
  Eye,
  EyeOff,
  LockKeyhole,
  Mail,
} from "lucide-react";
import { motion } from "framer-motion";
import { useAuth } from "@/hooks/useAuth";

type Mode = "signin" | "signup";

export default function AuthPage() {
  const router = useRouter();
  const { signIn } = useAuth();
  const [mode, setMode] = useState<Mode>("signin");
  const [showPassword, setShowPassword] = useState(false);
  const [email, setEmail] = useState("you@example.com");
  const [fullName, setFullName] = useState("");
  const [password, setPassword] = useState("");

  function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    signIn(email);
    router.push("/dashboard");
  }

  return (
    <main className="min-h-screen bg-[radial-gradient(circle_at_top,_#5b2f1d_0%,_#341d14_42%,_#1b120f_100%)] px-4 py-6 text-[#2f231f]">
      <div className="mx-auto flex min-h-[calc(100vh-3rem)] max-w-6xl flex-col">
        <button
          type="button"
          onClick={() => router.push("/")}
          className="inline-flex w-fit items-center gap-2 text-sm font-medium text-[#e7d9d2]/85 transition hover:text-white"
        >
          <ArrowLeft className="h-4 w-4" />
          Back to home
        </button>

        <div className="flex flex-1 items-center justify-center py-10">
          <motion.section
            initial={{ opacity: 0, y: 18, scale: 0.98 }}
            animate={{ opacity: 1, y: 0, scale: 1 }}
            transition={{ duration: 0.45, ease: "easeOut" }}
            className="w-full max-w-[520px] rounded-[28px] border border-[#f0e6df] bg-[#fbf7f4] px-6 py-8 shadow-[0_24px_80px_rgba(0,0,0,0.35)] sm:px-10 sm:py-10"
          >
            <div className="text-center">
              <h1 className="text-3xl font-bold tracking-tight text-[#2f241f] sm:text-[2.15rem]">
                Welcome to Insight Flow
              </h1>
              <p className="mt-2 text-sm text-[#8e786d] sm:text-base">
                Sign in to access your analytics dashboard
              </p>
            </div>

            <button
              type="button"
              className="mt-8 flex w-full items-center justify-center gap-3 rounded-2xl border border-[#ece1da] bg-white px-5 py-3.5 text-base font-medium text-[#3a2f2b] shadow-sm transition hover:bg-[#fffaf7]"
            >
              <span className="inline-flex h-5 w-5 items-center justify-center rounded-full bg-white text-sm font-black text-[#4285f4] shadow-[0_0_0_1px_rgba(0,0,0,0.06)]">
                G
              </span>
              Continue with Google
            </button>

            <div className="relative my-8 flex items-center justify-center">
              <div className="h-px w-full bg-[#e8ddd6]" />
              <span className="absolute bg-[#fbf7f4] px-3 text-sm text-[#a48f85]">
                or continue with email
              </span>
            </div>

            <div className="grid grid-cols-2 rounded-2xl bg-[#f0ebe7] p-1">
              <button
                type="button"
                onClick={() => setMode("signin")}
                className={`rounded-xl px-4 py-3 text-base font-semibold transition ${
                  mode === "signin"
                    ? "bg-white text-[#433530] shadow-sm"
                    : "text-[#9a867d]"
                }`}
              >
                Sign In
              </button>
              <button
                type="button"
                onClick={() => setMode("signup")}
                className={`rounded-xl px-4 py-3 text-base font-semibold transition ${
                  mode === "signup"
                    ? "bg-white text-[#433530] shadow-sm"
                    : "text-[#9a867d]"
                }`}
              >
                Sign Up
              </button>
            </div>

            <form className="mt-8 space-y-5" onSubmit={handleSubmit}>
              {mode === "signup" && (
                <label className="block space-y-2">
                  <span className="text-base font-semibold text-[#3a2f2b]">Full Name</span>
                  <div className="flex items-center gap-3 rounded-2xl border border-[#ece1da] bg-white px-4 py-3.5 shadow-sm focus-within:border-[#ff7b4a]">
                    <CircleUserRound className="h-5 w-5 text-[#b39b8f]" />
                    <input
                      type="text"
                      placeholder="Your name"
                      value={fullName}
                      onChange={(event) => setFullName(event.target.value)}
                      className="w-full bg-transparent text-base outline-none placeholder:text-[#b8a9a0]"
                    />
                  </div>
                </label>
              )}

              <label className="block space-y-2">
                <span className="text-base font-semibold text-[#3a2f2b]">Email</span>
                <div className="flex items-center gap-3 rounded-2xl border border-[#ece1da] bg-white px-4 py-3.5 shadow-sm focus-within:border-[#ff7b4a]">
                  <Mail className="h-5 w-5 text-[#b39b8f]" />
                  <input
                    type="email"
                    placeholder="you@example.com"
                    value={email}
                    onChange={(event) => setEmail(event.target.value)}
                    className="w-full bg-transparent text-base outline-none placeholder:text-[#b8a9a0]"
                  />
                </div>
              </label>

              <label className="block space-y-2">
                <span className="text-base font-semibold text-[#3a2f2b]">Password</span>
                <div className="flex items-center gap-3 rounded-2xl border border-[#ece1da] bg-white px-4 py-3.5 shadow-sm focus-within:border-[#ff7b4a]">
                  <LockKeyhole className="h-5 w-5 text-[#b39b8f]" />
                  <input
                    type={showPassword ? "text" : "password"}
                    placeholder="••••••••"
                    value={password}
                    onChange={(event) => setPassword(event.target.value)}
                    className="w-full bg-transparent text-base outline-none placeholder:text-[#b8a9a0]"
                  />
                  <button
                    type="button"
                    onClick={() => setShowPassword((value) => !value)}
                    className="text-[#b39b8f] transition hover:text-[#7a675f]"
                    aria-label={showPassword ? "Hide password" : "Show password"}
                  >
                    {showPassword ? <EyeOff className="h-5 w-5" /> : <Eye className="h-5 w-5" />}
                  </button>
                </div>
              </label>

              <button
                type="submit"
                className="w-full rounded-2xl bg-[linear-gradient(90deg,#ff6a2f_0%,#ff4d4f_100%)] px-5 py-4 text-lg font-semibold text-white shadow-[0_18px_40px_rgba(255,93,64,0.35)] transition hover:brightness-105"
              >
                {mode === "signin" ? "Sign In" : "Create Account"}
              </button>
            </form>

            <button
              type="button"
              className="mx-auto mt-6 block text-sm font-semibold text-[#9b8479] transition hover:text-[#6f5b53]"
            >
              Send me a magic link instead
            </button>
          </motion.section>
        </div>
      </div>
    </main>
  );
}