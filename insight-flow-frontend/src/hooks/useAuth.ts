type AuthUser = {
  id: string;
  email: string;
};

type AuthState = {
  user: AuthUser | null;
};

export function useAuth(): AuthState {
  return { user: null };
}