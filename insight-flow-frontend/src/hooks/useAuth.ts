"use client";

import { createElement, useEffect, useMemo, useState, createContext, useContext, type ReactNode } from "react";

type AuthUser = {
  id: string;
  email: string;
};

type AuthState = {
  user: AuthUser | null;
  signIn: (email: string) => void;
  signOut: () => void;
};

type AuthContextValue = AuthState;

const AuthContext = createContext<AuthContextValue | null>(null);
const AUTH_STORAGE_KEY = "insight-flow-auth-user";

export function AuthProvider({ children }: { children: ReactNode }) {
  const [user, setUser] = useState<AuthUser | null>(null);

  useEffect(() => {
    const storedUser = window.localStorage.getItem(AUTH_STORAGE_KEY);

    if (storedUser) {
      try {
        setUser(JSON.parse(storedUser) as AuthUser);
      } catch {
        window.localStorage.removeItem(AUTH_STORAGE_KEY);
      }
    }
  }, []);

  const value = useMemo<AuthState>(
    () => ({
      user,
      signIn: (email: string) => {
        const nextUser = { id: crypto.randomUUID(), email };
        setUser(nextUser);
        window.localStorage.setItem(AUTH_STORAGE_KEY, JSON.stringify(nextUser));
      },
      signOut: () => {
        setUser(null);
        window.localStorage.removeItem(AUTH_STORAGE_KEY);
      },
    }),
    [user],
  );

  return createElement(AuthContext.Provider, { value }, children);
}

export function useAuth(): AuthState {
  const context = useContext(AuthContext);

  if (!context) {
    throw new Error("useAuth must be used within an AuthProvider");
  }

  return context;
}