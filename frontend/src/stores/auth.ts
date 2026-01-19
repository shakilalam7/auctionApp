import { defineStore } from "pinia"
import router from "../router"

export interface User {
  id: number
  username: string
  email: string
  date_of_birth: string | null
  profile_image_url?: string | null
}

interface AuthState {
  user: User | null
  isAuthenticated: boolean
  token: string | null
  authChecked: boolean
}

export const useAuthStore = defineStore("auth", {
  state: (): AuthState => ({
    user: null,
    isAuthenticated: false,
    token: null,
    authChecked: false,
  }),

  actions: {
    setUser(user: User) {
      this.user = user
      this.isAuthenticated = true
      this.authChecked = true
    },

    setToken(token: string) {
      this.token = token
    },

    clearAuth() {
      this.user = null
      this.isAuthenticated = false
      this.token = null
      this.authChecked = true  // Mark as checked even when clearing
    },

    async logout() {
      try {
        await fetch("/api/logout/", {
          method: "POST",
          credentials: "include",
        })

        this.clearAuth()
        router.push("/signup")
        return true
      } catch (error) {
        console.error("Failed to logout:", error)
        this.clearAuth()
        router.push("/signup")
        return false
      }
    },

    async fetchUser() {
      try {
        const response = await fetch("/api/me/", {
          credentials: "include",
        })


        if (!response.ok) {
          this.clearAuth()
          return
        }

        const data = await response.json()
        if (data.ok && data.user) {
          this.setUser(data.user)
        } else {
          this.clearAuth()
        }
      } catch (error) {
        console.error("Failed to fetch user:", error)
        this.clearAuth()
      }
    },
  },
})
