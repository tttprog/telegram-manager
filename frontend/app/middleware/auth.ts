import { useAuthStore } from "~/stores/auth"

export default defineNuxtRouteMiddleware((to, from) => {
    const authStor = useAuthStore()
    if (authStor.isAuthenticated) return
    if (!authStor.isAuthenticated) {
        abortNavigation()
        return navigateTo('/')
    }
})
