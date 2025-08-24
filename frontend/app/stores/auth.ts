import { defineStore } from 'pinia'

export const useAuthStore = defineStore('authStore', {
  state: () => ({
    isAuthenticated: false
  }),
  actions: {
    async login(body: object) {
      const { data, status } = await useFetch("/api/login", {
        body: body
      })
      if (data.value && status.value === "success") {
        const token = useCookie("token")
        token.value = data?.value?.access ?? ''
        this.isAuthenticated = true
        return true
      } else {
        const token = useCookie("token")
        token.value = ""
        this.isAuthenticated = false
        return false
      }
    },
    async logout() {
      const token = useCookie("token")
      token.value = ""
      this.isAuthenticated = false
    },
  }
})
