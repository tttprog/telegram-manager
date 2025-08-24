// https://nuxt.com/docs/api/configuration/nuxt-config
import tailwindcss from "@tailwindcss/vite";

export default defineNuxtConfig({
  compatibilityDate: '2025-07-15',
  devtools: { enabled: false },
  modules: [
    '@nuxt/ui',
    '@nuxtjs/color-mode',
    '@nuxt/icon',
    '@pinia/nuxt',
    '@nuxtjs/device',
  ],
  vite: {
    plugins: [
      tailwindcss(),
    ],
  },
  css: ['~/assets/css/main.css'],
  pinia: {
    storesDirs: ['~/app/stores/**',],
  },
  runtimeConfig: {
    api_v1: "http://127.0.0.1:8000/api/v1",
  }
})